def start(chat, message, args):
    chat.send("Ciao! Conosco da cima a fondo le probabilità dei dadi del _RisiKo!_. Chiedimi qualcosa ;)")

def aiuto(chat, message, args):
    if len(args) == 0:
        chat.send(
            """<b>Comandi</b>

<code>/sdadata &lt;att&gt; &lt;def&gt;</code>
<i>Elenca le probabilità di abbattere i possibili numeri di carri del difensore con una singola sdadata di</i> <code>&lt;att&gt;</code> <i>dadi contro</i> <code>&lt;def&gt;</code>
Ulteriori informazioni: /guida_sdadata
	        """
        )
    
def guida(chat, message, args):
    if len(args) > 0:
        return
    chat.send("Clicca su un comando per leggere la guida corrispondente.\n\n/guida_sdadata")


def guida_comandi(chat, message, matches):
    comando = matches[0]
    if comando == "sdadata":
        result = (
        "*Formato*: `/sdadata <att> <def>`\n\n"
        "Considera una situazione in cui l'attaccante tira `<att>` dadi e il difensore ne tira `<def>`. L'attaccante può abbattere 0, 1, 2 o 3 carri del difensore (o meno, se il difensore ne ha meno di 3). Per ognuno di questi numeri, vengono elencati il numero di esiti favorevoli e possibili, e la corrispondente probabilità.\n\n"
        "_Esempio_: `/sdadata 3 2` mostra la seguente tabella:\n"
        "0:`  2275/7776` = 29.3%\n"
        "1:`  2611/7776` = 33.6%\n"
        "2:`  2890/7776` = 37.2%\n"
        "Ciò significa che, se l'attaccante tira 3 dadi e il difensore tira 2 dadi, ci sono 7776 esiti possibili del lancio, e\n"
        "-- in 2275 casi (cioè con probabilità 29.3%) l'attaccante abbatte 0 carri del difensore;\n"
        "-- in 2611 casi (cioè con probabilità 33.6%) l'attaccante abbatte 1 carro del difensore;\n"
        "-- in 2890 casi (cioè con probabilità 37.2%) l'attaccante abbatte 2 carri del difensore."
        )
    else:
        return
    
    chat.send(result)
    
