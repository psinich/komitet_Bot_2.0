from aiogram import types, \
	ReplyKeyboardMarkup, KeyboardButton, \
	InlineKeyboardMarkup, InlineKeyboardButton

kb1 = KeyboardButton('Подписаться на все новости')
kb2 = KeyboardButton('Подписаться на внутренние новости')
kb3 = KeyboardButton('Подписаться на сторонние новости')
kb4 = KeyboardButton('Назад')

menu_sub_settings = ReplyKeyboardMarkup(resize_keyboard=True).row(kb1).row(kb2).row(kb3).row(kb4)