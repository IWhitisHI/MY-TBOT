import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=["start"])
def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("1")
	item2 = types.KeyboardButton("2")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привіт!!!\nЯкий зараз тиждень???",
		parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == "1":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='1')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='2')
			item3 = types.InlineKeyboardButton("Середа", callback_data='3')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='4')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='5')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='1ALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)
		elif message.text == "2":


			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='6')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='7')
			item3 = types.InlineKeyboardButton("Середа", callback_data='8')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='9')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='10')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='2ALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)
		else:
			bot.send_message(message.chat.id, '"Слова" ВВОДИТИ НЕЛЬЗЯ!!!')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:

		if call.message:
			if call.data == '1':
				a=time.strftime("%H:%M",time.localtime())
				bot.send_message(call.message.chat.id, a+'\n Понеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА:')
			elif call.data == '2':
				bot.send_message(call.message.chat.id, 'Вівторок:\n1 ПАРА:\n2 ПАРА: Історія--АУДИТОРІИЯ: 3.112\n3 ПАРА: Електромех-АУДИТОРІИЯ: 10.104\n4 ПАРА: Фіз-ра')
			elif call.data == '3':
				bot.send_message(call.message.chat.id, 'Середа:\n1 ПАРА:\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Прога--АУДИТОРІИЯ: 5.409\n4 ПАРА:')
			elif call.data == '4':
				bot.send_message(call.message.chat.id, 'Четверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429')
			elif call.data == '5':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА:")
			elif call.data == '6':
				bot.send_message(call.message.chat.id, 'Понеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА: ')
			elif call.data == '7':
				bot.send_message(call.message.chat.id, 'Вівторок:\n1 ПАРА:\n2 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Історія(Л)--АУДИТОРІИЯ: 4.201\n4 ПАРА: ')
			elif call.data == '8':
				bot.send_message(call.message.chat.id, 'Середа:\n1 ПАРА: Прога--АУДИТОРІИЯ: 5.409\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Англ--АУДИТОРІИЯ: 8.1110а\n4 ПАРА:')
			elif call.data == '9':
				bot.send_message(call.message.chat.id, 'Четверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429')
			elif call.data == '10':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА: Вишка--АУДИТОРІИЯ: 3.112")
			elif call.data == '1ALL':
				bot.send_message(call.message.chat.id, "------------------------1ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА:\nВівторок:\n1 ПАРА:\n2 ПАРА: Історія--АУДИТОРІИЯ: 3.112\n3 ПАРА: Електромех-АУДИТОРІИЯ: 10.104\n4 ПАРА: Фіз-ра\nСереда:\n1 ПАРА:\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Прога--АУДИТОРІИЯ: 5.409\n4 ПАРА:\nЧетверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\nП'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА:")
			elif call.data == '2ALL':
				bot.send_message(call.message.chat.id, "------------------------2ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА: \nВівторок:\n1 ПАРА:\n2 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Історія(Л)--АУДИТОРІИЯ: 4.201\n4 ПАРА: \nСереда:\n1 ПАРА:  Прога--АУДИТОРІИЯ: 5.409\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Англ--АУДИТОРІИЯ: 8.1110а\n4 ПАРА:\nЧетверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\nП'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА: Вишка--АУДИТОРІИЯ: 3.112")
	except Exception as e:
		print(repr(e))

bot.polling(none_stop=True)