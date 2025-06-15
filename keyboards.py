from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

#клавиатура в зоне написания сообщений
reply = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='➕ Добавить задачу')],
                [KeyboardButton(text='📋 Мои задачи')],
                [KeyboardButton(text='✅ Выполнить задачу')]
            ],
                resize_keyboards = True,
                input_field_placeholder='Нажми на кнопку снизу....'
            )

#клавиатура внутри поле сообщения

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Обычная', callback_data='Button1')],
        [InlineKeyboardButton(text='Важная', callback_data='Button2')]
    ]
)

