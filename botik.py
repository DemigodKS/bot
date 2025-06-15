from aiogram import Bot, Dispatcher
import asyncio
from handlers import router_handlers
from states import router_state

#создание экземпляра бота
bot = Bot(token=" ")
dp = Dispatcher()
#запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # создание экземпляра бота
    bot = Bot(token="8140173668:AAG9kiA0f22gv_7p-Z4-Hk-y2GYykQ8EsXE")
    dp = Dispatcher()

    dp.include_router(router_handlers)
    dp.include_router(router_state)

    asyncio.run(main())
