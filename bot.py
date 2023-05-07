import os
import telebot
import ast

import utils
import db_interactions as db
import messages as msg

# VARIABLES/REFERENCES
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

conn = db.create_conn()




# BOT HANDLERS
# commands
@bot.message_handler(commands=['start'])
def start_bot(message):
    _, name, _ , lang = utils.parse_message(message)

    print(message)
    bot.send_message(message.chat.id, lang['welcome_message'].format(name, utils.pick_flower(name)), parse_mode='HTML')


@bot.message_handler(commands=['subscribe'])
def register_user(message):
    user, name, surname , lang = utils.parse_message(message)
    full_name = name + " " + surname

    if db.check_if_user_exists_and_valid(conn, user):
        # already exists
        bot.send_message(message.chat.id, lang['already_registered'], parse_mode='HTML')
    else:
        # go on with registration
        bot.send_message(message.chat.id, lang['subscribe_user'].format(name, full_name), reply_markup=utils.build_keyboard(lang['name_yes_no']), parse_mode='HTML')


@bot.message_handler(commands=['withdraw'])
def withdraw_user(message):
    user, name, _ , lang = utils.parse_message(message)
    if db.withdraw_user(conn, user):
        bot.send_message(message.chat.id, lang['withdrawn_user'].format(name), parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, lang['already_withdrawn'], parse_mode='HTML')



@bot.message_handler(commands=['status'])
def status_user(message):
    user, name, _ , lang = utils.parse_message(message)
    if db.check_if_user_exists_and_valid(conn, user):
        #registered
        bot.send_message(message.chat.id, lang['status_registered'].format(name, user), parse_mode='HTML')
    else:
        #not registered:
        bot.send_message(message.chat.id, lang['status_not_registered'].format(name, user), parse_mode='HTML')


@bot.message_handler(commands=['eating'])
def withdraw_user(message):
    bot.send_message(message.chat.id, 'not implemented', parse_mode='HTML')


# callback/message handlers
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    handler, value = call.data.split("_")

    if handler == 'name':
        name_handler(call, value)

    # edit the message sent to hide buttons, as the user already gave his answer
    bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id=call.message.message_id, parse_mode='HTML')


def name_handler(call: any, value: str):
    user, name, surname, lang = utils.parse_message(call)

    if value == 'yes':
        # store the user
        add_user(call.message.chat.id, lang, user, name + " " + surname)
    elif value == 'no':
        # start rename procedure
        db.wait_for_name_change(conn, user)
        bot.send_message(call.message.chat.id, lang['user_rename'], parse_mode='HTML')


@bot.message_handler(func=lambda message: True)
def handler_user_input(message):
    user,_ ,_ ,lang = utils.parse_message(message)
    waiting = db.waiting_user(conn, user)

    if waiting == 'name_change':
        db.stop_waiting(conn, user)
        add_user(message.chat.id, lang, user, message.text)
    elif waiting == 'food_allergies':
        pass
    elif waiting == 'notes':
        pass
    else: 
        bot.send_message(message.chat.id, lang["unknown_command"], parse_mode='HTML')




# SUPPORT FUNCTIONS
def add_user(answer_id: int, lang: any, user: str, full_name: str):
    if db.add_user(conn, user, full_name):
        bot.send_message(answer_id, lang['subscribe_user_success'].format(full_name), parse_mode='HTML')
    else:
        # let's hope it never reaches this point
        bot.send_message(answer_id, lang['subscribe_user_failure'], parse_mode='HTML')
        



if __name__ == '__main__':
    print("Starting good ol' Grill Valley bot")
    bot.infinity_polling()