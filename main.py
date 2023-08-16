from aiogram.utils import executor
from config import dp
from handlers import start, chat_action
from database import sql_commands


async def onstart_up(_):
    db = sql_commands.Database()
    db.sql_create_db()


start.register_start_handler(dp)
chat_action.register_chat_action_handler(dp)



if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True, on_startup = onstart_up)

