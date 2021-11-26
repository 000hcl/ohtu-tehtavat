class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti

        self.kasvatuskoko = kasvatuskoko
            
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        n_lukumaara = 0

        for i in range(self.alkioiden_lkm):
            if n == self.lukujono[i]:
                n_lukumaara += 1

        if n_lukumaara > 0:
            return True

        return False

    def lisaa(self, uusi_luku):

        if not self.kuuluu(uusi_luku):
            self.lukujono[self.alkioiden_lkm] = uusi_luku
            self.alkioiden_lkm += 1

            if self.on_taynna():
                self.tee_taulukko_isommaksi()
            return True

        return False
    
    def on_taynna(self):
        return self.alkioiden_lkm % len(self.lukujono) == 0
    
    def tee_taulukko_isommaksi(self):
        taulukko_old = self.lukujono
        self.kopioi_taulukko(self.lukujono, taulukko_old)
        self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.lukujono)

    def poista(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.lukujono[i]:
                n_indeksi = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[n_indeksi] = 0
                self.siirra_taaksepain(n_indeksi)
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True

        return False

    def siirra_taaksepain(self, kohta):
        apu = 0
        for j in range(kohta, self.alkioiden_lkm - 1):
            apu = self.lukujono[j]
            self.lukujono[j] = self.lukujono[j + 1]
            self.lukujono[j + 1] = apu

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def max_pituus(a, b):
        return max(len(a), len(b))

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            for j in b_taulu:
                if i == j:
                    y.lisaa(i)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            if i not in b_taulu:
                z.lisaa(i)

        return z

    def __str__(self):
        tuotos = "{"
        for i in range(self.alkioiden_lkm):
            tuotos = tuotos + str(self.lukujono[i])
            if i < self.alkioiden_lkm-1:
                tuotos += ", "
        tuotos = tuotos + "}"
        return tuotos
