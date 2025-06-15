from tkinter import Button

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, callback_query
from aiogram.filters import Command
import asyncio
from keyboards import reply
from aiogram.fsm.context import FSMContext
from states import Registration
from keyboards import InlineKeyboardButton, menu

router_handlers = Router()

@router_handlers.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Привет!", reply_markup=reply)


#приоритет задачи - Обычная
@router_handlers.callback_query(F.data == 'Button1')
async def save(callback: CallbackQuery, message: Message, state: FSMContext):
    await state.update_data(importance = message.text)
    await callback.message.answer("Приоритет - Обычная")


