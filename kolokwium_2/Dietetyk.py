from User import User


class Dietetyk(User):
    def __init__(self, imie: str, nazwisko: str, regon: str, numer_poswiadczenia_zawodowego: str):
        super().__init__(imie, nazwisko)
        self.__numer_poswiadczenia_zawodowego = numer_poswiadczenia_zawodowego
        self.__regon = regon

    @property
    def get_numer_poswiadczenia_zawodowego(self):
        return self.__numer_poswiadczenia_zawodowego

    @property
    def get_regon(self):
        return self.__regon

    def __str__(self):
        return f'imie dietetyka: {self.get_imie} ;' \
               f'nazwisko dietetyka: {self.get_nazwisko()}; ' \
               f'regon dietetyka: {self.get_regon}; ' \
               f'numer poswiadczenia zawodowego dietetyka: {self.get_numer_poswiadczenia_zawodowego}; '
