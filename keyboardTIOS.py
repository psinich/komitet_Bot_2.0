from aiogram import types, \
	ReplyKeyboardMarkup, KeyboardButton, \
	InlineKeyboardMarkup, InlineKeyboardButton

kb1 = KeyboardButton('Информация')
kb2 = KeyboardButton('Достижения')
kb3 = KeyboardButton('Контакты')
kb4 = KeyboardButton('Назад')

menu_tios = ReplyKeyboardMarkup(resize_keyboard=True).row(kb1, kb2, kb3).row(kb4)
