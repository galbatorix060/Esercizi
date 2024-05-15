nome_variabile : int = 10
nome_variabile : float = 10.0
nome_variabile : bool = False
nome_variabile : int = 10

nome_variabile = nome_variabile + 5
nome_variabile += 5 #scrivere cosi è la stessa cosa

import math
punto_di_mezzo : float = 3.2
print(math.ceil(punto_di_mezzo))
print(math.acosh(1))

var_1 : bool = True
var_2 : bool = False

print(var_1 and var_2)
print(var_2 or var_1)
print(not var_1)

if var_1 and var_2:
    print(f"{var_1 and var_2}")

if var_1 or var_2:
    print(f"{var_1 and var_2}")

lista : list = [1, 2, 3, 5]

i : int = 0

if lista[i] < lista[i+1]:
    temp : int = lista[i]
    lista[i] = lista[i+1]
    lista[i] = temp

x : int = 10000

if x > 0 or x < 20:
    print(f"x: {x}")

elif var_1 and var_2:
    pass

a : bool = False
b : bool = False

for i in lista:
    print("il quadrato è: ", i**2)

if a and b:
    print("sono nel primo if")

elif a or b:
    print("sono nell'elif")

elif not(a and b):
    print("Sono nell'else")


anagrafe : list = [{"nome" : "valerio", "voto" : 10}, {"nome" : "osvaldo", "voto" : 8}, {"nome" : "osvaldo", "voto" : 5}]
aggr : dict = {}

for dizionario in anagrafe:

    nome: str = dizionario["nome"]
    voto : int = dizionario["voto"]

    if nome in aggr:

        aggr[nome].append(voto)
    
    else:

        aggr[nome] = [voto]

    
aggr: dict = {"key1" : {"key1_1" : {"floor" : 10}}, "key2" : {"key2_1" : {"floor" : 1}}}

aggr["key1"]["key1_1"]["floor"]
aggr["key2"]["key2_1"]["floor"]