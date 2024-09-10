from film import Film

class Azione(Film):
    def __init__(self, id: int, title: str, genre = "Azione") -> None:
        super().__init__(id, title)
        self.genre = genre
        self.__penale = 3
    
    def getGenere(self):
        return self.genre
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo):
        return self.__penale * giorniRitardo


class Commedia(Film):
    def __init__(self, id: int, title: str, genre = "Commedia") -> None:
        super().__init__(id, title)
        self.genre = genre
        self.__penale = 2.5
    
    def getgenre(self):
        return self.genre
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo):
        return self.__penale * giorniRitardo


class Drama(Film):
    def __init__(self, id: int, title: str, genre = "Drama") -> None:
        super().__init__(id, title)
        self.genre = genre
        self.__penale = 2
    
    def getgenre(self):
        return self.genre
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo):
        return self.__penale * giorniRitardo
