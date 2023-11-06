from aiogram.fsm.state import StatesGroup, State


class WriteTheUserState(StatesGroup):
    GET_USER_ID = State()
    GET_MESSAGE_FOR_USER = State()


class UserMessagingState(StatesGroup):
    GET_MESSAGE_FOR_MESSAGING = State()


class AddNewAdminState(StatesGroup):
    GET_NEW_ADMIN_ID = State()


class DeleteAdminState(StatesGroup):
    GET_ADMIN_FOR_DELETE = State()
