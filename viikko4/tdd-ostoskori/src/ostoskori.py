from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self.kori:
            maara += self.kori[ostos].lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self.kori:
            hinta += self.kori[ostos].hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        if ostos.tuotteen_nimi() in self.kori:
            self.kori[ostos.tuotteen_nimi()].muuta_lukumaaraa(1)
        else:
            self.kori[ostos.tuotteen_nimi()] = ostos

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.kori[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self.kori[poistettava.nimi()].lukumaara() == 0:
            self.kori.pop(poistettava.nimi())

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset = []
        for ostos in self.kori:
            ostokset.append(self.kori[ostos])
        return ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
