class Pagamento:
    def __init__(self) -> None:
        self.__importo = 0.0
    
    def setPagamento(self, pagamento):
        self.__importo = pagamento
    
    def getPagamento(self):
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: ¢{self.getPagamento():.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self, importo) -> None:
        super().__init__()
        self.__importo = self.setPagamento(importo)
    
    def dettagliPagamento(self):
        print(f"Pagamento in contatni di: {self.getPagamento():.2f}")
    
    def inPezziDa(self):
        importo = self.getPagamento()
        banconote = [500, 200, 100, 50, 20, 10, 5]
        monete = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]

        for banconota in banconote:
            num_banconote = int(importo/banconota)
            if num_banconote > 0:
                print(f"{num_banconote} banconota/e da {banconota} euro")
                importo -= num_banconote * banconota
        for moneta in monete:
            num_monete = int(importo / moneta)
            if num_monete > 0:
                print(f"{num_monete} moneta/e da {moneta} euro")
                importo -= num_monete * moneta
        """
        appoggio = self.__importo
        banconota500 = 0
        banconota200 = 0
        banconota100 = 0
        banconota50 = 0
        banconota20 = 0
        banconota10 = 0
        banconota5 = 0
        moneta2 = 0
        moneta1 = 0
        moneta050 = 0
        moneta020 = 0
        moneta010 = 0
        moneta005 = 0
        moneta001 = 0
        while appoggio > 0:
            if appoggio - 500 >= 0:
                banconota500 += 1
                appoggio -= 500
            elif appoggio - 200 >= 0:
                banconota200 += 1
                appoggio -= 200
            elif appoggio - 100 >= 0:
                banconota100 += 1
                appoggio -= 100
            elif appoggio - 50 >= 0:
                banconota50 += 1
                appoggio -= 50
            elif appoggio - 20 >= 0:
                banconota20 += 1
                appoggio -= 20
            elif appoggio - 10 >= 0:
                banconota10 += 1
                appoggio -= 10
            elif appoggio - 5 >= 0:
                banconota5 += 1
                appoggio -= 5
            elif appoggio - 2 >= 0:
                moneta2 += 1
                appoggio -= 2
            elif appoggio - 1 >= 0:
                moneta1 += 1
                appoggio -= 1
            elif appoggio - 0.5 >= 0:
                moneta050 += 1
                appoggio -= 0.5
            elif appoggio - 0.2 >= 0:
                moneta020 += 1
                appoggio -= 0.2
            elif appoggio - 0.1 >= 0:
                moneta010 += 1
                appoggio -= 0.1
            elif appoggio - 0.05 >= 0:
                moneta005 += 1
                appoggio -= 0.05
            elif appoggio - 0.01 >= 0:
                moneta001 += 1
                appoggio -= 0.01
        print(f"Pagamento in contanti di: ¢{self.__importo}\n{self.__importo} euro da pagare in contanti con:")
        if banconota500 > 0:
            print(f"{banconota500} banconota/e da 500 euro")
        if banconota200 > 0:
            print(f"{banconota200} banconota/e da 200 euro")
        if banconota100 > 0:
            print(f"{banconota100} banconota/e da 100 euro")
        if banconota50 > 0:
            print(f"{banconota50} banconota/e da 50 euro")
        if banconota20 > 0:
            print(f"{banconota20} banconota/e da 20 euro")
        if banconota10 > 0:
            print(f"{banconota10} banconota/e da 10 euro")
        if banconota5 > 0:
            print(f"{banconota5} banconota/e da 5 euro")
        if moneta2 > 0:
            print(f"{moneta2} moneta/e da 2 euro")
        if moneta1 > 0:
            print(f"{moneta1} moneta/e da 1 euro")
        if moneta050 > 0:
            print(f"{moneta050} moneta/e da 0.50 euro")
        if moneta020 > 0:
            print(f"{moneta020} moneta/e da 0.20 euro")
        if moneta010 > 0:
            print(f"{moneta010} moneta/e da 0.10 euro")
        if moneta005 > 0:
            print(f"{moneta005} moneta/e da 0.05 euro")
        if moneta001 > 0:
            print(f"{moneta001} moneta/e da 0.01 euro")
    """
            
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome, scadenza, numero_carta) -> None:
        super().__init__()
        self.nome = nome
        self.scadenza = scadenza
        self.numero_carta = numero_carta

    
    def dettagliPagamento(self):
        super().dettagliPagamento()
        print(f"effettuato con la carta di credito\nNome sulla carta: {self.nome}\nData di scadenza: {self.scadenza}\nNumero della carta: {self.numero_carta}")
    

pagamento_contanti1 = PagamentoContanti(150)
pagamento_contanti2 = PagamentoContanti(92.25)
pagamento_carta1 = PagamentoCartaDiCredito("Daniele Fioravanti", "26/30", "987654321")
pagamento_carta2 = PagamentoCartaDiCredito("Leonardo Marianella", "12/24", "123456789")
pagamento_contanti1.setPagamento(150.00)
pagamento_contanti1.dettagliPagamento()
pagamento_contanti1.inPezziDa()
pagamento_contanti2.setPagamento(95.25)
pagamento_contanti2.dettagliPagamento()
pagamento_contanti2.inPezziDa()
pagamento_carta1.setPagamento(200.00)
pagamento_carta2.setPagamento(2000.00)
pagamento_carta1.dettagliPagamento()
pagamento_carta2.dettagliPagamento()