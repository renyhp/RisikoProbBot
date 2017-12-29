def start(chat, message, args):
    chat.send("Ciao! Conosco da cima a fondo le probabilità dei dadi del _RisiKo!_. Chiedimi qualcosa ;)")

def aiuto(chat, message, args):
    if len(args) == 0:
        chat.send(
            """ℹ️ <b>Comandi</b>

<code>/sdadata &lt;att&gt; &lt;def&gt;</code>
<i>Elenca le probabilità di abbattere i possibili numeri di carri del difensore con una singola sdadata di</i> <code>&lt;att&gt;</code> <i>dadi contro</i> <code>&lt;def&gt;</code>
Ulteriori informazioni: /guida_sdadata

<code>/vittoria [&lt;att&gt; &lt;def&gt;]</code>
<i>Se</i> <code>&lt;att&gt;</code> <i>e</i> <code>&lt;def&gt;</code> <i>sono specificati, restituisce le probabilità di vittoria dell'attaccante. Altrimenti, invia la tabella completa delle probabilità di vittoria dell'attaccante.</i>
Ulteriori informazioni: /guida_vittoria

<code>/passaggi &lt;att&gt; &lt;def&gt;</code>
<i>Invia la tabella delle probabilità di passaggio per ogni possibile situazione a partire dalla situazione in cui l'attaccante ha</i> <code>&lt;att&gt;</code> <i>carri e il difensore ha</i> <code>&lt;def&gt;</code> <i>carri.</i>
Ulteriori informazioni: /guida_passaggi

<code>/difesa &lt;def&gt;</code>
<i>Invia una tabella con le probabilità di vittoria dell'attaccante contro</i> <code>&lt;def&gt;</code> <i>carri, al variare del numero di carri iniziali e finali dell'attaccante.</i>
Ulteriori informazioni: /guida_difesa


✉️ Domande? Suggerimenti? Scrivi allo sviluppatore 👉 @renyhp
	        """, syntax = "HTML"
        )
    
def guida(chat, message, args):
    if len(args) > 0:
        return
    chat.send("Clicca su un comando per leggere la guida corrispondente.\n\n/guida_sdadata\n/guida_vittoria\n/guida_passaggi\n/guida_difesa", syntax = "plain")


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
    elif comando == "passaggi":
        result = (
        "*Formato*: `/passaggi <att> <def>`\n\n"
        "Considera che l'attaccante abbia inizialmente `<att>` carri e il difensore `<def>`, ed inizi ad attaccare, continuando finché non vince, o finché non perde.\n"
        "Il comando restituisce una tabella in cui, all'incrocio tra la riga `n` e la colonna `m`, è descritta la probabilità che, in un qualsiasi momento, ci si ritrovi con il numero di carri dell'attaccante ridotto ad `n` e il numero di carri del difensore ad `m`, _indipendentemente dal numero di attacchi effettuati_.\n"
        "Vengono inoltre fornite le probabilità totali di vittoria e di sconfitta, insieme con il numero finale medio di carri dell'attaccante in caso di vittoria, e il numero finale medio di carri del difensore in caso di sconfitta.\n"
        "Nota: il massimo numero di carri, sia per l'attaccante che per il difensore, è 40."
        )
    elif comando == "difesa":
        result = (
        "*Formato*: `/difesa <def>`\n\n"
        "Considera che il difensore abbia `<def>` carri sul suo territorio.\n"
        "- Nella colonna A (risp. _nella colonna B_), alla riga `n`, è descritta la probabilità che l'attaccante, partendo da `n` carri e attaccando senza sosta, vinca, rimanendo con solo 1 carro (risp. _con solo 2 carri_]. (Nota: si tratta di carri _utili_, ossia non viene contato il carro che deve sempre rimanere a difesa del territorio).\n"
        "- Nella colonna P, alla riga `n`, è descritta la probabilità che l'attaccante, attaccando senza sosta, vinca, perdendo `n` carri. Questa probabilità non dipende dal numero di carri iniziali, fermo restando che il numero di carri rimanenti deve essere almeno 3 (altrimenti bisogna leggere le colonne precedenti).\n"
        "- Nella colonna TOT, alla riga `n`, è descritta la probabilità totale che l'attaccante vinca partendo da `n` carri e attaccando senza sosta.\n"
        "- Viene inoltre fornito il numero medio di carri persi in caso di vittoria. Anche questo numero non dipende dal numero di carri iniziali dell'attaccante. Esso è calcolato considerando solo i casi in cui l'attaccante parte da un massimo di 40 carri, e dunque è frutto di un'approssimazione tanto più valida quanto più è probabile che con 40 carri l'attaccante vinca.\n"
        "Nota: il numero massimo per `<def>` è 40."
        )
    else:
        return
    
    chat.send("📖 " + result)
    
