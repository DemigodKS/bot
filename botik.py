from aiogram import Bot, Dispatcher
import asyncio
from handlers import router_handlers
from states import router_state

#запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # создание экземпляра бота
    bot = Bot(token=" ")
    dp = Dispatcher()

    dp.include_router(router_handlers)
    dp.include_router(router_state)

    asyncio.run(main())
