import json
import numpy
import math

from helpers import num_to_perc, mat_to_img


with open("data.json") as datafile:
    data = json.load(datafile)
    fav = numpy.array(data["sdadata"]["fav"])
    poss = numpy.array(data["sdadata"]["poss"])
    vittoria = numpy.array(data["vittoria"])
    matrice = numpy.array(data["matrice"])

    
def sdadata(chat, message, args):
    try:
        # controlla che args abbia solo due argomenti, interi e che possano essere una sdadata
        att = int(args[0])
        dif = int(args[1])
        if not ((0 < dif <= att < 4) and len(args) == 2):
            raise Exception
    except:
        result = "⚠ ️*Comando:* `/sdadata <att> <def>`\n`<att>` = numero di dadi dell'attaccante\n`<def>` = numero di dadi del difensore\n_L'attaccante non può tirare meno dadi del difensore._"
    else:
        # ok gli argomenti sono giusti
        result = "🎲 _Sdadata:_ *{} vs {}*\n".format(att, dif)
        tot = poss[att-1, dif-1] # gli array sono 0-based
        dim = max((int(math.log10(x)) + 1 for x in fav[att-1, dif-1,:dif+1])) # max numero di cifre di fav
        for i in range(dif+1):
            result += "\n{}:`  {:{w}d}/{:d}` = {}".format(i, fav[att-1, dif-1, i], tot, num_to_perc(fav[att-1, dif-1, i]/tot), w = dim)
    chat.send(result)



