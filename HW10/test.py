from bot_creds import bot_token
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


bot = Bot(bot_token)
updater = Updater(bot_token, use_context = True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет " + str(update.effective_chat.id))

def message_func(update, context):
    if update.message.text == "Кодовое слово": context.bot.send_message(update.effective_chat.id, "Ты знаешь кодовое слово!!!")
    else: context.bot.send_message(update.effective_chat.id, "Моя твоя не понимай... Пиши команды, насяльника!")

def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, "Не знаю такой команды...")

def get_number(update, context):
    keyboard = [
        [InlineKeyboardButton("первая", callback_data = '1'), InlineKeyboardButton("вторая", callback_data = '2')],
        [InlineKeyboardButton("третья", callback_data = '3'), InlineKeyboardButton("четвертая", callback_data = '4')]
    ]
    update.message.reply_text("Выбери", reply_markup = InlineKeyboardMarkup(keyboard))

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1': context.bot.send_message(update.effective_chat.id, "один")
    elif query.data == '2': context.bot.send_message(update.effective_chat.id, "два")
    elif query.data == '3': context.bot.send_message(update.effective_chat.id, "три")
    elif query.data == '4': context.bot.send_message(update.effective_chat.id, "четыре")

button_handler = CallbackQueryHandler(button)
start_handler = CommandHandler('start', start)
get_number_handler = CommandHandler('getnumber', get_number)
message_handler = MessageHandler(Filters.text, message_func)
unknown_handler = MessageHandler(Filters.command, unknown)


dispatcher.add_handler(button_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_number_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()