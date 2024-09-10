class Film:
    def __init__(self, titolo, durata) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, id, posti, film = Film()) -> None:
        self.id = id
        self.posti = posti
        self.film = film
        self.prenotati = 0
    
    def prenota_posti(self, num_posti):
        if self.posti - self.prenotati > 0:
            self.prenotati += num_posti
            print("posti prenotati correttamente!")
        else:
            print("la sala e piena non e possibile prenotare")
        return self.prenotati
    
    def posti_disponibili(self):
        if self.posti - self.prenotati > 0:
            print(f"la sala {self.id} ha ancora {self.posti - self.prenotati} posti liberi")
        else:
            print("la sala non ha posti disponibili")

class Cinema:
    def __init__(self) -> None:
        self.sale = []
    
    def aggiungi_sala(self, sala : Sala):
        self.sale.append(sala)
    
    def prenota_film(self, titolo_film, num_posti):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        else:
            print("il film selezionato non e in lista!")


film1 : Film = Film("rambo", 110)
film2 : Film = Film("terminator", 130)
film3 : Film = Film("matrix", 100)

sala1 : Sala = Sala(1, 50, 12, film1)
sala2 : Sala = Sala(2, 60, 40, film2)
sala3 : Sala = Sala(3, 100, 85, film3)

cinema1 : Cinema = Cinema(sala1, sala2, sala3)

