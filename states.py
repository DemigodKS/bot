from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import menu, reply

router_state = Router()

class Registration(StatesGroup):
    title = State()
    importance = State()

@router_state.message(F.text == '➕ Добавить задачу')
async def task(message:Message, state: FSMContext):
    await state.set_state(Registration.title)
    await message.reply("Укажите название задачи")

@router_state.message(Registration.title)
async def add_Tasktitle(message: Message, state: FSMContext):
    #сохраняем название задачи
    await state.update_data(title = message.text)
    await state.set_state(Registration.importance)
    await message.reply("Укажите приоритет задачи", reply_markup=menu)

@router_state.message(Registration.importance)
async def task_importance(message: Message, state: FSMContext):
    await state.update_data(importance=message.text)
    #сохраняем данные
    dat = await state.get_data()
    await message.answer(f"Задача зарегистрирована. Ваши данные:\nНазвание: {dat['title']}\nПриоритет: {dat['importance']}")

