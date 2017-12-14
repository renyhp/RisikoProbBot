import numpy
import math
import datetime
from PIL import Image, ImageDraw, ImageFont

font, fontbold = (ImageFont.truetype("FreeSans"+x+".ttf", 50) for x in ("", "Bold")) # viva python & pigrizia
w, h = 350, 75 # dimensioni di una cella di tabella
wi = 150 # la colonna di intestazione la facciamo più piccola
offw, offh = 20, 12 # coordinate, rispetto all'angolo top-left, del top-left di ogni testo all'interno della propria cella
wl = 3 # spessore riga della griglia
wlb = 8 # spessore riga intestazione

def num_to_perc(n):
    if (not 0 <= n <= 1) and n != -1:
        raise Exception("Non è una percentuale!")
    if n == 1:
        return "100%"
    elif n == -1:
        return "---"
    elif -int(math.log10(n))+1 in (1, 2):  # decine, o unità, di percento
        return "{:.{prec}f}%".format(n*100, prec=-int(math.log10(n))+1)
    else:
        return "{:.2E}%".format(n*100)

def mat_to_img(mat, intestazione):
    r, c = (x+1 for x in mat.shape) # righe e colonne, + 1 riga e 1 colonna d'intestazione
    if len(intestazione) != c-1:
        raise Exception("Le intestazioni non matchano il n di colonne")
        
    ## robe fisse
    
    width, height = w*(c-1) + wi, h*r # dimensioni totali
    
    # crea l'immagine
    img = Image.new("L", (width, height), 255)
    d = ImageDraw.Draw(img)
    
    # crea una griglia
    d.line([(wi,0),(wi, height)], 0, wlb) # colonna dell'intestazione
    for i in range(1,c-1):
        d.line([(wi+i*w,0),(wi+i*w,height)], 0, wl)
    for i in range(1,r):
        d.line([(0,i*h),(width,i*h)], 0, wl if i != 1 else wlb) # la prima riga più spessa
        
    # adesso scrivi le intestazioni
    for i in range(c-1): # colonne
        d.text((wi+i*w+offw, offh), str(intestazione[i]), fill=0, font=fontbold)
    for i in range(r-1): # righe
        d.text((offw, (i+1)*h+offh), str(i), fill=0, font=fontbold)
    
    # scrivi le entrate nelle loro celle
    for i in range(r-1):
        for j in range(c-1):
            d.text((wi+j*w+offw,(i+1)*h+offh), num_to_perc(mat[i,j]), fill=0, font=font)
    
    # salva il file
    nome = datetime.datetime.now().strftime("%H%M%S%f") + ".png"
    img.save(nome)
    return nome

    
