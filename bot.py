import botogram
import botogram.defaults
import os

from help import start, aiuto, guida, guida_comandi
from helpers import file_id
from risiko import sdadata, vittoria, passaggi, difesa

botogram.defaults.DefaultComponent.no_commands_hook = lambda self: None #togli i msg di quando si sbaglia comandi
bot = botogram.create(os.environ.get("TELEGRAM_TOKEN"))

comandi = (start, aiuto, guida, sdadata, vittoria, passaggi, difesa, file_id)

component = botogram.Component()
component.add_command("help", lambda : "(:")
component.add_message_matches_hook("^/guida_([A-Za-z]+)$", guida_comandi, False)
for func in comandi:
    component.add_command(func.__name__, func)

bot.use(component)
bot.run()
