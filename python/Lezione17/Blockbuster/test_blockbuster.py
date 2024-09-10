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
        self.lista_film = [self.film, self.film1, self.film2, self.film4, self.film5, self.film6, self.film7, self.film8, self.film9]
        self.noleggio = Noleggio(self.lista_film)
    
    def test_isAvaible(self):
        self.assertTrue(self.noleggio.isAvaible(self.film))
        self.assertTrue(self.noleggio.isAvaible(self.film3))
    
    def test_rentAMovie(self):
        self.noleggio.rentAMovie(self.film, 1)
        self.assertFalse(self.noleggio.isAvaible(self.film))
        self.noleggio.printRentMovies()

    def test_rentAMovieNotAvaible(self):
        self.noleggio.rentAMovie(self.film6, 2)
        self.noleggio.rentAMovie(self.film6, 3)
        self.assertNotIn(self.film6, self.noleggio.rented_film[3])
    
    def test_giveBack(self):
        self.noleggio.rentAMovie(self.film5, 4)
        self.noleggio.giveBack(self.film5, 4, 5)
        self.noleggio.printMovies()
        self.noleggio.printRentMovies(4)
    
    def test_calcolaPenaleRitardo(self):
        self.film.calcolaPenaleRitardo(2)
        self.film8.calcolaPenaleRitardo(2)
        self.film9.calcolaPenaleRitardo(2)
    
    def test_printRentMovies(self):
        self.noleggio.rentAMovie(self.film8, 10)
        self.noleggio.printRentMovies(10)

if __name__ == "__main__":
    unittest.main()