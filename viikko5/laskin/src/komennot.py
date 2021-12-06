

class Komento:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        

    def suorita(self):
        pass


class Summa(Komento):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self.sovelluslogiikka.plus(self.syote)

class Erotus(Komento):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self.sovelluslogiikka.miinus(self.syote)

class Nollaus(Komento):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa(Komento):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self.sovelluslogiikka.kumoa()