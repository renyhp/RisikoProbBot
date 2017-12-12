import json
import numpy
import math

with open("data.json") as datafile:
    data = json.load(datafile)
    fav = numpy.array(data["sdadata"]["fav"])
    poss = numpy.array(data["sdadata"]["poss"])
    vittoria = numpy.array(data["vittoria"])
    matrice = numpy.array(data["matrice"])

    
def sdadata(chat, message, args):
    try:
        att = int(args[0])
        dif = int(args[1])
        if not ((0 < dif <= att < 4) and len(args) == 2):
            raise Exception
    except:
        result = "⚠ ️*Comando:* `/sdadata <att> <def>`\n`<att>` = numero di dadi dell'attaccante\n`<def>` = numero di dadi del difensore\n_L'attaccante non può tirare meno dadi del difensore._"
    else:
        result = "🎲 _Sdadata:_ *{} vs {}*\n".format(att, dif)
        for i in range(dif+1):
            result += "\n{}:`  {:>{w}}/{}` = {}".format(i, str(fav[att-1, dif-1, i]), str(poss[att-1, dif-1]), num_to_perc(fav[att-1, dif-1, i]/poss[att-1, dif-1]), w = max_ord_grandezza(fav[att-1, dif-1,:dif]))
    chat.send(result)



def max_ord_grandezza(arr):
    return max([math.log10(x)+1 for x in arr])

def num_to_perc(n):
    if not 0 <= n <= 1:
        raise Exception("Non è una percentuale!")
    if n == 1:
        return "100%"
    elif -int(math.log10(n))+1 in (1, 2):  # decine, o unità, di percento
        return "{:.{prec}f}%".format(n*100, prec=-int(math.log10(n))+1)
    else:
        return "{:.2E}%".format(n*100)
    
