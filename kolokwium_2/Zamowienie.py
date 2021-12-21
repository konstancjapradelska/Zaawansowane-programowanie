class Zamowienie:
    @property
    def get_data_zamowienia(self):
        return self.__data_zamowienia

    @property
    def get_dieta(self):
        return self.__dieta

    @property
    def get_pacjent(self):
        return self.__pacjent

    @property
    def get_dietetyk(self):
        return self.__dietetyk

    def set_dieta(self, dieta):
        self.__dieta = dieta

    def set_pacjent(self, pacjent):
        self.__pacjent = pacjent

    def set_dietetyk(self, dietetyk):
        self.__dietetyk = dietetyk

    def set_data_zamowienia(self, data_zamowienia):
        self.__data_zamowienia = data_zamowienia

    def wartosc_zamowienia(self) -> int:
        suma = 0
        for item in self.get_dieta:
            suma += item.get_cena()
        return round(suma, 2)

    def ilosc_kalorii(self) -> int:
        suma = 0
        for item in self.get_dieta:
            suma += item.get_ilosc_kalorii()
        return suma

    def __str__(self):
        return f'Zamowienie:\npacjenta: {self.get_pacjent} \n' \
               f'od dietetyka: {self.get_dietetyk} \n' \
               f'na diety: {self.get_dieta} \n' \
               f'data_zamowienia: {self.get_data_zamowienia} \n' \
               f'wartosc zamowienia: {self.wartosc_zamowienia()} PLN \n' \
               f'ilosc kalorii: {self.ilosc_kalorii()} kcal \n'
