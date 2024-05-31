"""
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

    
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
    

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
"""

class Specie:
    def __init__(self, nome, popolazione, tasso_crescita) -> None:
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita
        self.popolazione_nuova = 0
    
    def cresci(self):
        self.popolazione_nuova = self.popolazione * (1 + self.tasso_crescita)
