class User:
    def __init__(self, imie: str, nazwisko: str):
        self.__imie = imie
        self.__nazwisko = nazwisko

    @property
    def get_imie(self):
        return self.__imie

    def get_nazwisko(self):
        return self.__nazwisko

    def __str__(self):
        return f'imie usera: {self.get_imie} ;' \
               f'nazwisko usera: {self.get_nazwisko()}; ' \
