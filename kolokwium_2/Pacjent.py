from User import User


class Pacjent(User):
    def __init__(self, imie: str, nazwisko: str, pesel: str, plec: str):
        super().__init__(imie, nazwisko)
        self.__plec = plec
        self.__pesel = pesel

    @property
    def get_plec(self):
        return self.__plec

    def get_pesel(self):
        return self.__pesel

    def __str__(self):
        return f'imie pacjenta: {self.get_imie} ;' \
               f'nazwisko pacjenta: {self.get_nazwisko()}; ' \
               f'pesel pacjenta: {self.get_pesel()}; ' \
               f'plec pacjenta: {self.get_plec}; '
