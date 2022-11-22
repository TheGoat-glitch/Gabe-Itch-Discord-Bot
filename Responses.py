import random
import discord


def handle_response(message):
    p_message = message

    def percent_gay():
        return "yi" + 'is ' + str(random.randrange(1, 100))

    if p_message == '$hello':
        return 'Hey Guys Gabe Itch Here!'

    if p_message == '$roll':
        return str(random.randint(1, 6))

    if p_message == '$percent':
        return str(random.randrange(1,100)) + '%'

    if p_message == '$help':
        return "`PLEASE KEEP LOWERCASE \n $hello -> Hey there! \n $roll -> rolls dice \n $help -> help menu \n " \
               "$percent -> decimal that can be coverted to percent \n Use ^ before your statement to have the bot DM" \
               " you` "

    if p_message == '$fbi':
        return "FBI OPEN UP!!!"

    if p_message == '$percent_gay':
        return percent_gay()

    if p_message == '$moan':
        return 'Enjoy this! ' + 'www.moanalisa.co.uk'



