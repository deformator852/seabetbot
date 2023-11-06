from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

TOKEN = "6197552285:AAGCO_BOGXIWuwLpREaio4wMcSNtrsDXANc"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()
root_admins = [
    46629637,
]
