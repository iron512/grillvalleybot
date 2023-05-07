import telebot 
import messages as msg

def parse_message(message: telebot.types.Message):
    user = message.from_user.username
    name = message.from_user.first_name
    surname = message.from_user.last_name
    lang = msg.en

    language = message.from_user.language_code
    if language == 'it':
        lang = msg.it
    
    return user, name, surname, lang

def pick_flower(name: str):
    flowers = ['🌷','🌵','🏵️','🪷','🪻','🌺','🌹','🌸','🌻','🌼']
    index = 0
    mult = 2

    for chr in name.lower():
        index = index + ord(chr) * mult
        mult = mult * 2

    index = index % len(flowers)
    
    # Hardcoding the Tulips if the name is Sara.
    # My GF is named Sara and she literally loves them.
    # (Yes i could have inserted the Tulip in a position 
    # that matches the result of my function, but i like this)
    if name.lower() == 'sara':
        index = 0
    
    return flowers[index]

def build_keyboard(keys: dict):
    markup = telebot.types.InlineKeyboardMarkup()

    for key, value in keys.items():
        markup.add(telebot.types.InlineKeyboardButton(text=value,callback_data=key))

    return markup


if __name__ == '__main__':
    print(pick_flower("Ivan"))
