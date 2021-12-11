from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def luo_kaksinpeli():
    return KPSPelaajaVsPelaaja()

def luo_yksinpeli():
    return KPSTekoaly()

def luo_haastava_yksinpeli():
    return KPSParempiTekoaly()