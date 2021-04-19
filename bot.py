import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# логгирование бота
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')

def start_bot(update: Updater, context: CallbackContext):
	# функция ответа текстом в бот после ввода /start
	mytext = """Hello {}
	I have only /start command""".format(update.message.chat.first_name)
	update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
	# функция ответа текстом в бот на введенный текст
	text = update.message.text
	# добавление в лог введенного текста
	logging.info(text)

	update.message.reply_text(text)

def main():
	updtr = Updater(settings.TOKEN_TELEGRAMM)
	# возврат функции после ввода в боте /start
	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	# возврат функции после ввода в боте любого символа
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot starting')
	main()
