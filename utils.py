import messages as msg

def parse_message(message):
    name = message.from_user.first_name
    lang = msg.en

    language = message.from_user.language_code
    if language == 'it':
        lang = msg.it
    
    return name, lang

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

if __name__ == '__main__':
    print(pick_flower("Ivan"))
