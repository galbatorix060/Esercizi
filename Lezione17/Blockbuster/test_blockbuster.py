import unittest
from film import Film
from noleggio import Noleggio
from movie_genre import Drama, Commedia, Azione

class TestFilm(unittest.TestCase):
    def setUp(self) -> None:
        self.film = Azione(1, "Rambo")
        self.film1 = Azione(2, "john wick")
        self.film2 = Azione(3, "django")
        self.film3 = Azione(4, "deadpool")
        self.film4 = Azione(5, "pulp fiction")
        self.film5 = Commedia(6, "griffin")
        self.film6 = Commedia(7, "garfield")
        self.film7 = Commedia(8, "il dittatore")
        self.film8 = Commedia(9, "sausage party")
        self.film9 = Drama(10, "oppenheimer")
        lista_film = [self.film, self.film1, self.film2, self.film3, self.film4, self.film5, self.film6, self.film7, self.film8, self.film9]
        noleggio = Noleggio(lista_film)