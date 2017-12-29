import json
import numpy
import math
import os

from helpers import num_to_perc, mat_to_img, process_args

vittoria_id = os.environ.get("VITTORIA_ID")
# renyhpbot: BQADBAADdwIAAkZGsFHASj_FEEcLKAI
# risikoprobbot: BQADBAADwAMAAnzZqFH_EKEc-fUVEgI

with open("data.json") as datafile:
    data = json.load(datafile)
    fav = numpy.array(data["sdadata"]["fav"])
    poss = numpy.array(data["sdadata"]["poss"])
    vitt = numpy.array(data["vittoria"])
    matrice = numpy.array(data["matrice"])

    
def sdadata(chat, message, args):
    args = process_args(args)
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

def vittoria(bot, chat, message, args):    
    args = process_args(args)
    if len(args) == 0:
        bot.api.call("sendDocument", { "chat_id" : chat.id, "document" : vittoria_id })
        return
    
    try:
        # controlla che args abbia solo due argomenti, interi e del numero giusto
        att = int(args[0])
        dif = int(args[1])
        if not (0 < att < 41 and 0 < dif < 41 and not (att < 3 and att < dif)):
            raise Exception
    except:
        result = "⚠ ️*Comando:* `/vittoria [<att> <def>]`\n`<att>` = numero di carri dell'attaccante\n`<def>` = numero di carri del difensore\n\n_Note:_\n• L'attaccante non può tirare meno dadi del difensore.\n• Il numero massimo di carri è 40.\n• Senza argomenti, il comando restituisce la tabella completa."
    else:
        result = "🏆 _Vittoria:_ *{} vs {}*\n\n{}".format(att, dif, num_to_perc(vitt[att, dif]))
    chat.send(result)
    
    
def passaggi(bot, chat, message, args):
    args = process_args(args)
    
    try:
        # controlla che args abbia solo due argomenti, interi e che possano essere uno stato iniziale
        att = int(args[0])
        dif = int(args[1])
        if not (0 < att < 41 and 0 < dif < 41 and not (att < 3 and att < dif)):
            raise Exception
    except:
        chat.send("⚠ ️*Comando:* `/passaggi <att> <def>`\n`<att>` = numero di carri dell'attaccante\n`<def>` = numero di carri del difensore\n\n_Note:_\n• L'attaccante non può tirare meno dadi del difensore.\n• Il numero massimo di carri è 40.")
    else:
        result = matrice[att,dif,:(att+1),:(dif+1)]
        
        probvitt = numpy.sum(result[:,0])
        attmedi = numpy.average(range(att+1), weights=result[:,0]) #definizione di media!
        probsconf = tuple(numpy.sum(result[i,(i+1):]) for i in (0,1,2)) #probabilità di rimanere sconfitto con "i" carri
        #ora fai la media. non è così semplice! se M1 e M2 sono due medie pesate parziali su pesi totali W1 e W2, la media pesata è (M1W1+M2W2)/(W1+W2).
        medieparziali = tuple(numpy.average(range(i+1, dif+1), weights=result[i,(i+1):]) for i in (0,1,2))
        difmedi = numpy.average(medieparziali, weights=probsconf)
        probsconf = sum(probsconf)
        
        caption = "⚔️ Passaggi: {} vs {}\n\n• Vittoria: {} (mediamente con {:.2f} carri)\n• Sconfitta: {} (mediamente con {:.2f} carri)".format(att, dif, num_to_perc(probvitt), attmedi, num_to_perc(probsconf), difmedi)
        nomefile = mat_to_img(result, tuple(range(dif+1)))
        bot.api.call("sendDocument", { "chat_id" : chat.id, "caption" : caption }, {"document" : open(nomefile, "rb") })
        os.remove(nomefile)
