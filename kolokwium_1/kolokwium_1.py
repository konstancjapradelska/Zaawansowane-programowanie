class Produkt:
    def __init__(self, nazwa: str, cena: int, kolor: str, rozmiar: str, numer_seryjny: str):
        self.__nazwa = nazwa
        self.__cena = cena
        self.__kolor = kolor
        self.__rozmiar = rozmiar
        self.__numer_seryjny = numer_seryjny

    @property
    def nazwa(self):
        return self.__nazwa

    def cena(self):
        return self.__cena

    def kolor(self):
        return self.__kolor

    def rozmiar(self):
        return self.__rozmiar

    def numer_seryjny(self):
        return self.__numer_seryjny

    def __str__(self):
        return f'Nazwa produktu: {self.nazwa} ' \
               f'cena produktu: {self.cena()} ' \
               f'kolor produktu: {self.kolor()} ' \
               f'rozmiar produktu: {self.rozmiar()}' \
               f' numer seryjny produktu: {self.numer_seryjny()}'

class Magazyn:
    def __init__(self, nazwa: str, miasto: str, kod_pocztowy: str, ulica: str, numer_budynku: str):
        self.__nazwa = nazwa
        self.__miasto = miasto
        self.__kod_pocztowy = kod_pocztowy
        self.__ulica = ulica
        self.__numer_budynku = numer_budynku

    @property
    def nazwa(self):
        return self.__nazwa

    def miasto(self):
        return self.__miasto

    def kod_pocztowy(self):
        return self.__kod_pocztowy

    def ulica(self):
        return self.__ulica

    def numer_budynku(self):
        return self.__numer_budynku

    def __str__(self):
        return f'Nazwa magazynu: {self.nazwa} ' \
               f'miasto magazynu: {self.miasto()} ' \
               f'kolor kod_pocztowy: {self.kod_pocztowy()} ' \
               f'ulica magazynu: {self.ulica()}' \
               f' numer_budynku magazynu: {self.numer_budynku()}'


class KlientDetaliczny:
    def __init__(self, imie: str, nazwisko: str, pesel: str, miasto: str,
                 ulica: str, numer_budynku: str, kod_pocztowy:str):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__pesel = pesel
        self.__miasto = miasto
        self.__ulica = ulica
        self.__numer_budynku = numer_budynku
        self.__kod_pocztowy = kod_pocztowy


    @property
    def imie(self):
        return self.__imie

    def nazwisko(self):
        return self.__nazwisko

    def pesel(self):
        return self.__pesel

    def miasto(self):
        return self.__miasto

    def kod_pocztowy(self):
        return self.__kod_pocztowy

    def ulica(self):
        return self.__ulica

    def numer_budynku(self):
        return self.__numer_budynku

    def __str__(self):
        return f'imie klienta: {self.imie} ;' \
               f'nazwisko klienta: {self.nazwisko()}; ' \
               f'pesel klienta: {self.pesel()}; ' \
               f'miasto klienta: {self.miasto()}; ' \
               f'kod_pocztowy klienta: {self.kod_pocztowy()}; ' \
               f'ulica klienta: {self.ulica()};' \
               f' numer_budynku klienta: {self.numer_budynku()};'

class KlientBiznesowy:
    def __init__(self, nazwa: str, nip: str, regon: str,miasto: str,
                 ulica: str, numer_budynku: str, kod_pocztowy:str):
        self.__nazwa = nazwa
        self.__nip = nip
        self.__regon = regon
        self.__miasto = miasto
        self.__ulica = ulica
        self.__numer_budynku = numer_budynku
        self.__kod_pocztowy = kod_pocztowy

    @property
    def nazwa(self):
        return self.__nazwa

    def nip(self):
        return self.__nip

    def regon(self):
        return self.__regon

    def miasto(self):
        return self.__miasto

    def kod_pocztowy(self):
        return self.__kod_pocztowy

    def ulica(self):
        return self.__ulica

    def numer_budynku(self):
        return self.__numer_budynku

    def __str__(self):
        return f'nazwa klienta: {self.nazwa} ' \
               f'nip klienta: {self.nip} ' \
               f'regon klienta: {self.regon} ' \
               f'miasto klienta: {self.miasto} ' \
               f'kolor klienta: {self.kod_pocztowy()} ' \
               f'ulica klienta: {self.ulica()}' \
               f' numer_budynku klienta: {self.numer_budynku()}'

class Zamowienie:
    def __init__(self, produkt: list, magazyn: object, klient: object, data_zamowienia: str, godzina_zamowienia: str):
        self.__produkt = produkt
        self.__magazyn = magazyn
        self.__klient = klient
        self.__data_zamowienia = data_zamowienia
        self.__godzina_zamowienia = godzina_zamowienia

    @property
    def produkt(self):
        return self.__produkt

    @property
    def magazyn(self):
        return self.__magazyn

    @property
    def klient(self):
        return self.__klient

    @property
    def data_zamowienia(self):
        return self.__data_zamowienia

    @property
    def godzina_zamowienia(self):
        return self.__godzina_zamowienia

    def set_produkt(self, produkt):
        self.__produkt = produkt

    def set_magazyn(self, magazyn):
        self.__magazyn = magazyn

    def set_klient(self, klient):
        self.__klient = klient

    def set_data_zamowienia(self, data_zamowienia):
        self.__data_zamowienia = data_zamowienia

    def set_godzina_zamowienia(self, godzina_zamowienia):
        self.__godzina_zamowienia = godzina_zamowienia

    # def wartosc_zamowienia(self) -> int:
    #     return sum(Zamowienie.produkt.cena())
    #
    # def adres_klienta(self) -> str:
    #     return Zamowienie.klient.miasto

    def __str__(self):
        return f'Zamowienie:\n klient: {self.klient} \n' \
               f'magazyn: {self.magazyn} \n' \
               f'produkty: {self.produkt} \n' \
               f'data_zamowienia: {self.data_zamowienia} \n' \
               f'godzina_zamowienia: {self.godzina_zamowienia} \n'


p1 = Produkt(nazwa='pe1', cena = 500, kolor = 'czarny', rozmiar = 'mały', numer_seryjny = '26546854164')
p2 = Produkt(nazwa='pe2', cena = 900, kolor = 'szary', rozmiar = 'średni', numer_seryjny = '541849792564')
m1 = Magazyn(nazwa='m1', miasto='Katowice', kod_pocztowy='40-260', ulica='Sowinskiego', numer_budynku='40')
kd1 = KlientDetaliczny(imie='Jan', nazwisko='Kowalski', pesel='464864948', miasto='Warszawa',
                 ulica='Paderewskiego', numer_budynku='14', kod_pocztowy='25-626')

lista = []
lista.append(p1)
lista.append(p2)

z1 = Zamowienie(produkt=lista, magazyn=m1, klient=kd1, data_zamowienia='26.02.2020', godzina_zamowienia='15:00')

print(z1)
