import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.varasto_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.x = 1
        
        def viitegeneraattori_uusi():
            self.x += 1
            return self.x

        self.viitegeneraattori_mock.uusi.side_effect = viitegeneraattori_uusi
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "suola", 1)
            if tuote_id == 3:
                return Tuote(3, "villatakki", 30)
        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_tilisiirto_metodi_kutsutaan_oikeilla_parametreilla_kun_ostetaan_yksi_tuote(self):
        

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka","12345",)

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,5)

    def test_tilisiirto_metodi_kutsutaan_oikeilla_parametreilla_kun_ostetaan_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345",)
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,6)

    def test_tilisiirto_metodi_kutsutaan_oikeilla_parametreilla_kun_ostetaan_kaksi_samanlaista_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka","12345",)
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,10)
    
    def test_tilisiirto_metodi_kutsutaan_oikeilla_parametreilla_kun_ostetaan_yksi_tuote_jota_on_ja_toinen_joka_on_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka","12345",)
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,1)
    
    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("marja","54321",)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345",)
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,1)
        
    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("marja","54321",)
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2,ANY,ANY,ANY)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345",)
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 3,ANY,ANY,ANY)
    
    def test_ei_makseta_tuotteesta_joka_on_poistettu_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka","12345",)
        self.pankki_mock.tilisiirto.assert_called_with("pekka",ANY,"12345",ANY,1)