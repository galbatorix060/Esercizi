import random
import time

lunghezza_lista = 70
percorso: list = ['-'] * lunghezza_lista
tartaruga: int = 1
lepre: int = 1
abilita:int = 0
condizioni_meteo : list = ["soleggiato", "pioggia"]
stamina_tartaruga : int = 100
stamina_lepre : int = 100
meteo_corrente = ""
ostacoli = {15 : -3, 30 : -5, 45 : -7}
bonus = {10 : 5, 25 : 3, 50 : 10}

def ostacoli_aggiuntivi(percorso, tipo):
    if tipo == 'ostacoli' and percorso in ostacoli:
        percorso += ostacoli[percorso]
        percorso = max(1, percorso)
    elif tipo == 'bonus' and percorso in bonus:
        percorso += bonus[percorso]
        percorso = min(lunghezza_lista, percorso)
    return percorso

def mossa_t(tartaruga,abilita_t, stamina_tartaruga):
    if abilita_t >= 1 and abilita_t <= 5 and stamina_tartaruga >= 5:
        tartaruga = tartaruga + 3
        stamina_tartaruga -= 5
    elif abilita_t >= 6 and abilita_t <= 7 and stamina_tartaruga >= 10:
        tartaruga = tartaruga - 6
        stamina_tartaruga -= 10
    elif abilita_t >= 8 and abilita_t <= 10 and stamina_tartaruga >= 3:
        tartaruga = tartaruga + 1
        stamina_tartaruga -= 3
    else:
        stamina_tartaruga += 10

    if meteo_corrente == "pioggia":
        tartaruga -= 1
    tartaruga = ostacoli_aggiuntivi(tartaruga, 'ostacoli')
    tartaruga = ostacoli_aggiuntivi(tartaruga, 'bonus')
    return tartaruga, stamina_tartaruga

def mossa_h(lepre,abilita_h, stamina_lepre):
    if abilita_h >= 1 and abilita_h <= 2:
        stamina_lepre = min(100, stamina_lepre + 10)
    elif abilita_h >= 3 and abilita_h <= 4 and stamina_lepre >= 15:
        lepre = lepre + 9
        stamina_lepre -= 15
    elif abilita_h == 5 and stamina_lepre >= 20:
        lepre = lepre - 12
        stamina_lepre -= 20
    elif abilita_h >= 6 and abilita_h <= 8 and stamina_lepre >= 5:
        lepre = lepre + 1
        stamina_lepre -= 5
    elif abilita_h >= 9 and abilita_h <= 10 and stamina_lepre >= 8:
        lepre = lepre - 2
        stamina_lepre -= 8
    else:
        stamina_lepre += 10

    if meteo_corrente == "pioggia":
        lepre -= 2
    lepre = ostacoli_aggiuntivi(lepre, 'ostacoli')
    lepre = ostacoli_aggiuntivi(lepre, 'bonus')
    return lepre, stamina_lepre

movimento_t = 0
movimento_h = 0

print("BANG!!! AND THEY'RE OFF!!!")
tick : int = 1

while True:
    tick += 1
    percorso[movimento_t] = '-'
    percorso[movimento_h] = '-'
    abilita_t = random.randint(1,10)
    abilita_h = random.randint(1,10)

    movimento_t = mossa_t(tartaruga,abilita_t, stamina_tartaruga)
    movimento_h = mossa_h(tartaruga,abilita_h, stamina_lepre)
    tartaruga = movimento_t
    lepre = movimento_h

    #time.sleep (0.5)

    if tick % 10 == 0:
        meteo_corrente = random.choice(condizioni_meteo)
        print("condizioni meteo cambiate: ", meteo_corrente)

    if lepre >= 70 - 1:
        print("HARE WINS || YUCH!!!")
        break
    elif tartaruga >= 70 - 1:
        print("TORTOISE WINS!||VAY!!!")
        break
    if movimento_t < 1:
        tartaruga = 1
    if movimento_h < 1:
        lepre = 1
    if percorso[movimento_t] == '-':
        percorso[movimento_t] = 'T'
    elif percorso[movimento_t] == 'H':
        percorso[movimento_t] == 'TH'
        print("OUCH!!!")

    if percorso[movimento_h] == '-':
        percorso[movimento_h] = 'H'
    elif percorso[movimento_h] == 'T':
        percorso[movimento_h] = 'HT'
        print("OUCH!!!")

    print(percorso)

