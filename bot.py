import os
import time
import telebot

import utils
import messages as msg

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_bot(message):
    name, lang = utils.parse_message(message)

    print(message)
    bot.send_message(message.chat.id, lang['welcome_message'].format(name, utils.pick_flower(name)), parse_mode='HTML')

if __name__ == '__main__':
    print("Starting good ol' Grill Valley bot")
    bot.infinity_polling()