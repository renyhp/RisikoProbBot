import json
import numpy

with open("data.json") as datafile:
    data = json.load(datafile)
    fav = data["sdadata"]["fav"]
    poss = data["sdadata"]["poss"]
    vittoria = numpy.array(data["vittoria"])
    matrice = numpy.array(data["matrice"])

def sdadata(chat, message, args):
    try:
        att = int(args[0])
        dif = int(args[1])
        if not ((0 < dif <= att < 4) and len(args) == 2):
            raise Exception
    except:
        chat.send("⚠️*Comando:* `/sdadata <att> <def>`\n`<att>` = numero di dadi dell'attaccante\n`<def>` = numero di dadi del difensore\n_L'attaccante non può tirare meno dadi del difensore._")
        return
    chat.send("🎲_Sdadata:_ *{} vs {}*".format(att, dif))
