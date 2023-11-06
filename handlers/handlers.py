from create_bot import dp, root_admins, bot
from aiogram.filters.command import Command
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.methods.send_message import SendMessage
from datetime import datetime
from states import *
import sqlite3


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    start_message = f"Hello, {message.from_user.first_name}! Welcome to our bot.\nHere are some options for you:"  # pyright:ignore
    conn = sqlite3.connect("database/admins.db")
    cursor = conn.cursor()
    admin_btn = [
        types.InlineKeyboardButton(
            text="write the user", callback_data="write_the_user"
        ),
        types.InlineKeyboardButton(
            text="user messaging", callback_data="user_messaging"
        ),
    ]
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Live Agent", url="https://direct.lc.chat/16107516/"
            ),
            types.InlineKeyboardButton(text="Play Now", url="seabet.io"),
        ],
        [
            types.InlineKeyboardButton(text="Promotions", callback_data="https://www.seabet8.io/#/promo"),
            types.InlineKeyboardButton(
                text="Telegram channel", url="https://t.me/seabetcommunity"
            ),
        ],
    ]

    admins = cursor.execute(
        f"SELECT * FROM admins WHERE admin = {message.from_user.id}"  # pyright:ignore
    )

    if admins.fetchone():
        buttons.append(admin_btn)

    if message.from_user.id in root_admins:  # pyright:ignore
        root_admin_btn = [
            types.InlineKeyboardButton(
                text="add new admin", callback_data="add_new_admin"
            ),
            types.InlineKeyboardButton(
                text="delete admin", callback_data="delete_admin"
            ),
        ]

        buttons.append(root_admin_btn)
        buttons.append(admin_btn)

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    cursor.close()

    await message.answer(start_message, reply_markup=keyboard)


# ----------------------
# block with functions write the user
@dp.callback_query(F.data == "write_the_user")
async def write_the_user(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter the user_id:")  # pyright:ignore
    await state.set_state(WriteTheUserState.GET_USER_ID)


@dp.message(WriteTheUserState.GET_USER_ID)
async def get_id(message: types.Message, state: FSMContext):
    await message.answer("Enter the message: ")
    await state.update_data(user_id=message.text)
    await state.set_state(WriteTheUserState.GET_MESSAGE_FOR_USER)


@dp.message(WriteTheUserState.GET_MESSAGE_FOR_USER)
async def get_message(message: types.Message, state: FSMContext):
    context_data = await state.get_data()
    message_for_user = message.text
    user_id = context_data.get("user_id")
    await bot.send_message(
        chat_id=int(user_id), text=message_for_user  # pyright:ignore
    )
    await state.clear()


# -----------------------
# block with function user messaging
@dp.callback_query(F.data == "user_messaging")
async def user_messaging(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(  # pyright: ignore
        "Write the message for messaging: "
    )
    await state.set_state(UserMessagingState.GET_MESSAGE_FOR_MESSAGING)


@dp.message(UserMessagingState.GET_MESSAGE_FOR_MESSAGING)
async def get_message_for_messaging(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id, text=message.text)  # pyright:ignore
    await state.clear()


# ------------------------
# block with function add new admin
@dp.callback_query(F.data == "add_new_admin")
async def add_new_admin(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter the admin ID for add:  ")  # pyright:ignore
    await state.set_state(AddNewAdminState.GET_NEW_ADMIN_ID)


@dp.message(AddNewAdminState.GET_NEW_ADMIN_ID)
async def get_new_admin(message: types.Message, state: FSMContext):
    conn = sqlite3.connect("database/admins.db")
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO admins (admin) VALUES({int(message.text)});"  # pyright:ignore
    )
    conn.commit()
    conn.close()
    await message.answer("New admin was add!")
    await state.clear()


# -----------------------
# block with function delete new admin
@dp.callback_query(F.data == "delete_admin")
async def delete_admin(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter the admin id to delete: ")  # pyright:ignore
    await state.set_state(DeleteAdminState.GET_ADMIN_FOR_DELETE)


@dp.message(DeleteAdminState.GET_ADMIN_FOR_DELETE)
async def get_admin_for_delete(message: types.Message, state: FSMContext):
    conn = sqlite3.connect("database/admins.db")
    cursor = conn.cursor()
    cursor.execute(
        f"DELETE FROM admins WHERE admin = {int(message.text)};"  # pyright:ignore
    )
    conn.commit()
    conn.close()
    await message.answer("Admin was delete!")
    await bot.send_message(
        chat_id=message.text, text="You was delete from admins!"  # pyright:ignore
    )
    await state.clear()


# ------------------------
