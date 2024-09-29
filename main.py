import asyncio

import logging
from logger.logger import BotLogger
from Constants import BotConfig

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
logger = BotLogger().get_logger()

bot = Bot(BotConfig.TOKEN.value)

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"Started bot {message.chat.id}")
    await message.answer("Добро пожаловать в Бота пойзон для заказов!")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())