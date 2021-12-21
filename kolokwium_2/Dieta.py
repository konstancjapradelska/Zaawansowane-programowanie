class Dieta:
    k = 0

    def __init__(self, nazwa: str, cena: int, ilosc_kalorii: int, czy_wegetarianska: str):
        self.__nazwa = nazwa
        self.__cena = cena
        self.__ilosc_kalorii = ilosc_kalorii
        self.__czy_wegetarianska = czy_wegetarianska
        Dieta.k += 1
        self.id = Dieta.k

    @property
    def get_nazwa(self):
        return self.__nazwa

    def get_cena(self):
        return self.__cena

    def get_ilosc_kalorii(self):
        return self.__ilosc_kalorii

    def get_czy_wegetarianska(self):
        return self.__czy_wegetarianska

    def __repr__(self):
        return '\n' + str(self.id) + f'.    Nazwa diety: {self.get_nazwa}| ' \
                                     f'cena diety: {self.get_cena()}| ' \
                                     f'ilosc kalorii: {self.get_ilosc_kalorii()}| ' \
                                     f'czy wegetarianska: {self.get_czy_wegetarianska()}|'
