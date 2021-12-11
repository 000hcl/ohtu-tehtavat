from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def _aseta_tekoaly(self):
        return Tekoaly()
