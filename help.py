def start(chat, message, args):
    chat.send("Ciao! Conosco da cima a fondo le probabilità dei dadi del _RisiKo!_. Chiedimi qualcosa ;)")

def aiuto(chat, message, args):
    if len(args) == 0:
        chat.send(
            """<b>Comandi</b>

<code>/sdadata &lt;att&gt; &lt;def&gt;</code>
<i>Elenca le probabilità di abbattere i possibili numeri di carri del difensore con una singola sdadata di</i> <code>&lt;att&gt;</code> <i>dadi contro</i> <code>&lt;def&gt;</code>
Ulteriori informazioni: /guida_sdadata

<code>/vittoria [&lt;att&gt; &lt;def&gt;]</code>
<i>Se</i> <code>&lt;att&gt;</code> <i>e</i> <code>&lt;def&gt;</code> <i>sono specificati, restituisce le probabilità di vittoria dell'attaccante. Altrimenti, invia la tabella completa delle probabilità di vittoria dell'attaccante.</i>
Ulteriori informazioni: /guida_vittoria
	        """, syntax = "HTML"
        )
    
def guida(chat, message, args):
    if len(args) > 0:
        return
    chat.send("Clicca su un comando per leggere la guida corrispondente.\n\n/guida_sdadata\n/guida_vittoria", syntax = "plain")


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
    elif comando == "vittoria":
        result = (
        "*Formato*: `/vittoria [<att> <def>]`\n\n"
        "Considera che l'attaccante, durante l'attacco, continui ad attaccare finché non abbatte tutti i carri del difensore (nel qual caso vince) oppure è costretto a tirare meno dadi del difensore (nel qual caso perde).\n"
        "Il comando restituisce la probabilità di vincere attaccando con `<att>` carri contro `<def>`.\n"
        "Se `<att>` e `<def>` non sono specificati, il comando restituisce una tabella in cui, all'incrocio tra la riga `n` e la colonna `m`, è descritta la probabilità di vincere attaccando con `n` carri contro `m`.\n"
        "Nota: il massimo numero di carri, sia per l'attaccante che per il difensore, è 40."
        )
    else:
        return
    
    chat.send(result)
    
