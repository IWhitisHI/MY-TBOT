import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Українська")
	item2 = types.KeyboardButton("Русский")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "На якій мові будемо спілкуватись ?",
		parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def whoareyou(message):
	if message.chat.type == 'private':
		if message.text == "Українська":

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			markup.row('PrP', 'PoP', 'FTTB')

			bot.send_message(message.chat.id, "Який напрямок тебе цікавить ?", reply_markup=markup)
		if message.text == "Русский":

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			markup.row('PrP', 'PoP', 'FTTB')

			bot.send_message(message.chat.id, "Какое направление тебя интересует ?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		

bot.polling(none_stop=True)
