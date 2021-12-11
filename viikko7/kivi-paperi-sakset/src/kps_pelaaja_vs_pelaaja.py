from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, tekoaly=None):
        return input("Toisen pelaajan siirto: ")

    def _siirtoviesti(self, siirto=None):
        pass