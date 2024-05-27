class Prodotto:
    def __init__(self, nome : str, quantita : int) -> None:
        self.nome = nome
        self.quantita = quantita
    
class Magazzino:
    def __init__(self) -> None:
        self.prodotti = []
        
    def aggiungi_prodotto(self, prodotto : Prodotto):
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome):
        for prodotto in self.prodotti:
            if nome == prodotto.nome:
                print(f"{prodotto.nome} e presente nella lista!")
                break
            else:
                print(f"{prodotto.nome} non e presente nella lista!")
                break
    
    def verifica_disponibilita(self, nome):
        for prodotto in self.prodotti:
            if nome == prodotto.nome and prodotto.quantita > 0:
                print(f"{prodotto.nome} e ancora disponibile!")
                break
                
            elif nome == prodotto.nome and prodotto.quantita <= 0:
                print(f"{prodotto.nome} non e piu disponibile")
                break

prodotto1 : Prodotto = Prodotto("mela", 20)
prodotto2 : Prodotto = Prodotto("pasta", 30)
prodotto3 : Prodotto = Prodotto("manzo", 0)
prodotto4 : Prodotto = Prodotto("patata", 50)

magazzino : Magazzino = Magazzino()

magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)
magazzino.aggiungi_prodotto(prodotto4)

magazzino.cerca_prodotto("mela")

magazzino.verifica_disponibilita("manzo")