import random
import time

lunghezza_lista = 70
percorso: list = ['-'] * lunghezza_lista
tartaruga: int = 1
lepre: int = 1
abilita:int = 0

def mossa_t(tartaruga,abilita_t):
    if abilita_t >= 1 and abilita_t <= 5:
        tartaruga = tartaruga + 3
    elif abilita_t >= 6 and abilita_t <= 7:
        tartaruga = tartaruga - 6
    elif abilita_t >= 8 and abilita_t <= 10:
        tartaruga = tartaruga + 1
    return tartaruga

def mossa_h(lepre,abilita_h):
    if abilita_h >= 1 and abilita_h <= 2:
        pass
    elif abilita_h >= 3 and abilita_h <= 4:
        lepre = lepre + 9
    elif abilita_h == 5:
        lepre = lepre - 12
    elif abilita_h >= 6 and abilita_h <= 8:
        lepre = lepre + 1
    elif abilita_h >= 9 and abilita_h <= 10:
        lepre = lepre - 2
    return lepre

movimento_t = 0
movimento_h = 0

print("BANG!!! AND THEY'RE OFF!!!")

while True:
    percorso[movimento_t] = '-'
    percorso[movimento_h] = '-'
    abilita_t = random.randint(1,10)
    abilita_h = random.randint(1,10)

    movimento_t = mossa_t(tartaruga,abilita_t)
    movimento_h = mossa_h(tartaruga,abilita_h)
    tartaruga = movimento_t
    lepre = movimento_h

    time.sleep (0.5)

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

