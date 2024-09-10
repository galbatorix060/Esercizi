class Libro:
    def __init__(self, titolo, autore) -> None:
        self.stato_prestito = False
        self.titolo = titolo
        self.autore = autore

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo: list[Libro] = []
    
    def aggiungi_libro(self, libro : Libro):
        self.catalogo.append(libro)
        return "il libro e stato aggiunto"

    def presta_libro(self, titolo : str):
        for libro_prestare in self.catalogo:
            if libro_prestare.titolo == titolo:
                if libro_prestare.stato_prestito:
                    return "il libro non e disponibile"
                else:
                    libro_prestare.stato_prestito = True
                    return "il libro e disponibile"
    
    def restituisci_libro(self, titolo : str):
        for libro_restituire in self.catalogo:
            if libro_restituire.titolo == titolo:
                if libro_restituire.stato_prestito:
                    libro_restituire.stato_prestito = False
                    return "il libro e stato restituito"
                else:
                    return "libro prestato"
    
    def mostra_libri_disponibili(self):
        for libro in self.catalogo:
            if libro.stato_prestito == False:
                print(f"{libro.titolo} e disponibile")
            else:
                print(f"{libro.titolo} non e disponibile")
    
libro1 : Libro = Libro("harry potter", "JFK rowling")
libro2 : Libro = Libro("god", "peppe")
libro3 : Libro = Libro("aria", "gianni")

biblioteca1 : Biblioteca = Biblioteca()

print(biblioteca1.aggiungi_libro(libro1))
print(biblioteca1.aggiungi_libro(libro2))
print(biblioteca1.aggiungi_libro(libro3))

print(biblioteca1.presta_libro("harry potter"))
print(biblioteca1.presta_libro("god"))

print(biblioteca1.restituisci_libro("harry potter"))

print(biblioteca1.mostra_libri_disponibili())


