from telebot import TeleBot
from domains_search import domains_search

#name: Dominios registrados
#name bot: Dominiosregistrados_bot

api_key = "YOUR TOKEN"

bot = TeleBot(api_key)

@bot.message_handler(commands=["welcome"])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome stranger, tengo unos comandos que podrían interesarte. Escribe /help")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, """
    /info te dara un poco de información acerca del bot. \n/search (un dominio) buscará si tal dominio se encuentran activos. Por ejemplo: /search google
    """)

@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id, """
    Este bot utiliza la API de Domainsdb. Por defecto, la API se limita a buscar 50 dominios, pero el bot solo te mostrará 10. Para más información: https://domainsdb.info/
    """)

@bot.message_handler(commands=["search"])
def search(message):
    #controls that the command is invoked with a domain
    if (len(message.text.split()) <= 1):
        bot.send_message(message.chat.id, "Se necesita un dominio que buscar")
    else:
        bot.send_message(message.chat.id, domains_search(message.text.split()[1::]))

bot.infinity_polling()
 



