from aiogram import types, \
	ReplyKeyboardMarkup, KeyboardButton, \
	InlineKeyboardMarkup, InlineKeyboardButton

kb1 = KeyboardButton('ТИОС')
kb2 = KeyboardButton('БИС')
kb3 = KeyboardButton('Прочее')
kb4 = KeyboardButton('Назад')

menu_noci_nili = ReplyKeyboardMarkup(resize_keyboard=True).row(kb1, kb2, kb3).row(kb4)