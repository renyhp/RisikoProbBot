import botogram
import botogram.defaults
import os

from help import start, aiuto, guida, guida_comandi
from risiko import sdadata

botogram.defaults.DefaultComponent.no_commands_hook = lambda self: None
bot = botogram.create(os.environ.get("TELEGRAM_TOKEN"))

component = botogram.Component()
component.add_command("start", start)
component.add_command("help", lambda : "(:")
component.add_command("aiuto", aiuto)
component.add_command("sdadata", sdadata)
component.add_command("guida", guida)
component.add_message_matches_hook("^/guida_([A-Za-z]+)$", guida_comandi, False)

bot.use(component)
bot.run()
