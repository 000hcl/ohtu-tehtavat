from tuomari import Tuomari

class KPS:
    def pelaa(self):
        tekoaly = self._aseta_tekoaly()
        tuomari = Tuomari()
        ensimmainen_peli = True
        
        while True:
            if not ensimmainen_peli:
                tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(tuomari)
            
            ekan_siirto = self._ensimmainen_siirto()
            tokan_siirto = self._toisen_siirto(tekoaly)
            
            self._aseta_toinen_siirto(tekoaly, ekan_siirto)
            self._siirtoviesti(tokan_siirto)
            
            ensimmainen_peli = False
            
            if not self._siirrot_ok(ekan_siirto, tokan_siirto):
                break

        self._loppuviesti(tuomari)

    def _siirrot_ok(self, ekan_siirto, tokan_siirto):
        return self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto)

    def _aseta_tekoaly(self):
        return None

    def _siirtoviesti(self, siirto=None):
        print(f"Tietokone valitsi: {siirto}")

    def _loppuviesti(self, tuomari):
        print("Kiitos!")
        print(tuomari)

    def _aseta_toinen_siirto(self, tekoaly, siirto=None):
        pass

    def _ensimmainen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, tekoaly=None):
        return tekoaly.anna_siirto()

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"