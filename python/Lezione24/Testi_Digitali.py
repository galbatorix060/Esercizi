class Documento:
    def __init__(self) -> None:
        self.testo : str = ""
    
    def getText(self):
        return self.testo
    
    def setText(self, testo):
        self.testo = testo

    def isInText(self, key):
        if key in self.testo:
            return True
        else:
            return False

class Email(Documento):
    def __init__(self, testo) -> None:
        super().__init__()
        self.mittente = ""
        self.destinatario = ""
        self.titolo = ""
        self.setText(testo)
    
    def getMittente(self):
        return self.mittente
    
    def setMittente(self, mittente):
        self.mittente = mittente

    def getDestinatario(self):
        return self.destinatario
    
    def setDestinatario(self, destinatario):
        self.destinatario = destinatario
    
    def getTitolo(self):
        return self.titolo