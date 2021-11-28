import telebot
from telebot import types

token = '2112233757:AAE132fp7qWYJOZTlji0OqRwNBXCIVkU2rU'
bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['/help'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Привет!\nнажми /help чтобы увидеть список команд', reply_markup = keyboard)


@bot.message_handler(commands = ['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Мои команды:\n/mtuci -главная страница МТУСИ\n/mtucivk -страница МТУСИ ВКонтакте\n/memmtuci -мемы МТУСИ')
    bot.send_message(message.chat.id, 'Я умею разговаривать. Напиши мне:\n-Привет\n-Как дела?\n-Пока')


@bot.message_handler(commands = ['mtuci'])
def info(message):
    bot.send_message(message.chat.id, 'Ссылка на сайт: http://mtuci.ru')


@bot.message_handler(commands = ['mtucivk'])
def joke(message):
    bot.send_message(message.chat.id, 'МТУСИ ВКонтанке: https://vk.com/mtuci')


@bot.message_handler(commands = ['memmtuci'])
def weather(message):
    bot.send_message(message.chat.id, 'Мем МТУСИ: https://vk.com/memmtuci')


@bot.message_handler(content_types = ['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, 'Отлично!')
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, 'Ещё увидимся!')

bot.infinity_polling()