from tekoaly_parannettu import TekoalyParannettu
from kps import KPS


class KPSParempiTekoaly(KPS):
    def _aseta_tekoaly(self):
        return TekoalyParannettu()
    
    def _aseta_toinen_siirto(self, tekoaly, siirto=None):
        tekoaly.aseta_siirto(siirto)