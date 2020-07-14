import telebot

bot = telebot.TeleBot('___')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, который будет подбирать для Вас интересующие продукты из тех, которыми готовы делиться участники фудшеринга. Какие продукты в фудшеринге Вам интересны?')


# bot.send_message(text = 'Какие продукты в фудшеринге Вам интересны?', chat_id = message.chat.id)

@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == '/find':
		bot.send_message(text = 'Теперь я буду отслеживать в фудшеринге {} и сообщать о предложениях'.format(message.text), chat_id = message.chat.id)
		# bot.register_next_step_handler(message, get_choice)
	if message.text == '/help':
		help(message)
	if message.text == '/choice':
		get_choice(message)


def get_choice(message):
	bot.send_message(text = 'В настоящее время предлагается: {}'.format('SELECT...'), chat_id = message.chat.id)

def help(message):
	if message.text == '/help':
		bot.send_message(message.chat.id, '/find команда для поиска продуктов\
			/choise команда для показа текущих вариантов')

bot.polling(none_stop=True, interval=0)
