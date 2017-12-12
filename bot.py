import botogram
import botogram.defaults
import os

from help import start, aiuto
from risiko import sdadata

botogram.defaults.DefaultComponent.no_commands_hook = lambda self: None
bot = botogram.create(os.environ.get("TELEGRAM_TOKEN"))

component = botogram.Component()
component.add_command("start", start)
component.add_command("help", lambda : "(:")
component.add_command("aiuto", aiuto)
component.add_command("sdadata", sdadata)

bot.use(component)
bot.run()
