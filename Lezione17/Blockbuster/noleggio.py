from film import Film
from movie_genre import Drama, Commedia, Azione

class Noleggio:
    def __init__(self, film_list : list) -> None:
        self.film_list = film_list
        self.rented_film_list = []
        self.rented_film = {}

    def isAvaible(self, film):
        for i in self.film_list:
            if film.__id in i.__id:
                print(f"il film scelto è disponibile {film.__title}!")
                return True
            else:
                print(f"il film scelto non è disponibile {film.__title}!")
                return False
    
    def rentAMovie(self, film, clientID):
        for i in self.film_list:
            if film.__id in i.__id:
                self.film_list.remove(i)
                self.rented_film_list.append(i)
                self.rented_film[clientID] = self.rented_film_list
                print(f"Il cliente {clientID} ha noleggiato {film.__title}!")
            else:
                print(f"Non è possibile noleggiare il film {film.__title}!")
    
    def giveBack(self, film, clientID, days):
        self.rented_film[clientID].remove(film)
        self.film_list.append(film)
        penale_pagare = film.calcolaPenaleRitardo(days)
        print(f"Cliente: {clientID}! La penale da pagare per il film {film.__title} e' di {penale_pagare} euro!")

    def printMovies(self):
        for i in self.film_list:
            print(f"{i.__title} - {i.genre}")
    
    def printRentMovies(self, clientID):
        for k, v in self.rented_film:
            if k == clientID:
                print(f"{clientID} ha noleggiato: {v}")