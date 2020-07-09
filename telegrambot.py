import telebot

bot = telebot.TeleBot('___')


bot.send_message(text = 'Какие продукты в фудшеринге Вам интересны?', chat_id = ___)

@bot.message_handler(content_types=['text'])
def start(message):
	bot.send_message(text = 'Теперь я буду отслеживать в фудшеринге {} и сообщать о предложениях'.format(message.text), chat_id = ___)


bot.polling(none_stop=True, interval=0)
