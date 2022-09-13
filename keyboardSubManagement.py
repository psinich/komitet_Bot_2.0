from aiogram import types, \
	ReplyKeyboardMarkup, KeyboardButton, \
	InlineKeyboardMarkup, InlineKeyboardButton

kb1 = KeyboardButton('Управление подпиской')
kb2 = KeyboardButton('Мероприятия')
kb3 = KeyboardButton('Записаться на мероприятия')
kb4 = KeyboardButton('Назад')

menu_sub_management = ReplyKeyboardMarkup(resize_keyboard=True).row(kb1, kb2, kb3).row(kb4)