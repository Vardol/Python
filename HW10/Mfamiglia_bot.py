from bot_creds import bot_token
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
import rbc_bs_parser
import weather_parser

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


news = rbc_bs_parser
weather = weather_parser
bot = Bot(bot_token)
updater = Updater(bot_token, use_context = True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет!" + str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, "Список доступных команд:")
    help(update, context)

def message_func(update, context):
    if update.message.text == "Кодовое слово": context.bot.send_message(update.effective_chat.id, "Ты знаешь кодовое слово!!!")
    else: context.bot.send_message(update.effective_chat.id, "Моя твоя не понимай... Пиши команды, насяльника!")

def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, "Не знаю такой команды...")

def help(update, context):
    commands_list = ["/start - приветствие.","/menu - главное меню функций.","/help - список команд."]
    for text in commands_list:
        context.bot.send_message(update.effective_chat.id, str(text))

def menu(update, context):
    keyboard = [
        [InlineKeyboardButton("Сводка новостей (rbc)", callback_data = '1')],
        [InlineKeyboardButton("Погода сейчас в Казани", callback_data = '2'), InlineKeyboardButton("Погода в Казани Завтра", callback_data = '3')]
    ]
    update.message.reply_text("Меню:", reply_markup = InlineKeyboardMarkup(keyboard))

def print_news(update, context):
    for text in news.main():
        context.bot.send_message(update.effective_chat.id, str(text))

def weather_tod(update, context):
    context.bot.send_message(update.effective_chat.id, str(f"Погода сейчас в Казани: {weather.tod_weather()}"))

def weather_tom(update, context):
    context.bot.send_message(update.effective_chat.id, str(f"Завтра в Казани: {weather.tom_weather()}"))

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1': print_news(update, context)
    elif query.data == '2': weather_tod(update, context)
    elif query.data == '3': weather_tom(update, context)

button_handler = CallbackQueryHandler(button)
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
get_number_handler = CommandHandler('menu', menu)
message_handler = MessageHandler(Filters.text, message_func)
unknown_handler = MessageHandler(Filters.command, unknown)


dispatcher.add_handler(button_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(get_number_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()