import requests, json
from requests.auth import HTTPBasicAuth

base_api_url = "https://127.0.0.1:8080/"
username=""
password=""
nome=""
cognome=""
data_nascita=""
Cod_Fis=""


def Get_Comando():
    print("Digitare il numero corrispondete al comando:\n1) Crea cittadino\n2)Cancella cittadino\n3)Leggi cittadini\n4)Aggiorna cittadini\n5) Inserisci credenziali\n6) Exit")
    comando = str(input())
    return comando

comando = Get_Comando()


def inserisci_cittadino():
    global nome, cognome, data_nascita, Cod_Fis
    nome = input("inserisci il nome del cittadino: ")
    cognome = input("inserisci il cognome del cittadino: ")
    data_nascita = input("inserisci data di nascita del cittadino (gg/mm/aaaa): ")
    Cod_Fis = input("inserisci il codice fiscale del cittadino: ")

if comando == "1":
    api_url = "https://127.0.0.1:8085/post_create" 
    inserisci_cittadino()
    cittadino = {"nome": nome, "surname": cognome, "date": data_nascita, "CF": Cod_Fis} 
    response = requests.post(api_url,json=cittadino, verify=False,auth=HTTPBasicAuth(username,password)) 
    #print(response.json()) 
    print(response.status_code) 
    print(response.headers["Content-Type"])

def acquisisci_credenziali():
    global username, password
    username = input("inserisci username: ")
    password = input("inserisci password: ")

if comando == "5":
    acquisisci_credenziali()