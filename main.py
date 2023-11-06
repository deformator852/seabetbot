from create_bot import root_admins, bot, dp
import logging
import sys
import asyncio
from handlers import handlers


async def main() -> None:
    dp.message.register(handlers.cmd_start)
    dp.message.register(handlers.get_id)
    dp.message.register(handlers.get_message)
    dp.message.register(handlers.get_message_for_messaging)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
