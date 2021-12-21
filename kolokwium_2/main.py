from Dieta import Dieta
from Pacjent import Pacjent
from Dietetyk import Dietetyk
from Zamowienie import Zamowienie

d1 = Dieta(nazwa='Dieta Dukana', cena=750, ilosc_kalorii=2000, czy_wegetarianska='tak')
d2 = Dieta(nazwa='Dieta mięsna', cena=1040, ilosc_kalorii=3300, czy_wegetarianska='nie')
p1 = Pacjent(imie='Natalia', nazwisko='Kowalska', pesel='98070493812', plec='kobieta')
zd1 = Dietetyk(imie='Jan', nazwisko='Nowak', regon='110767239', numer_poswiadczenia_zawodowego='ZO794983')

list_diet = [d1, d2]

z1 = Zamowienie()
z1.set_pacjent(p1)
z1.set_dietetyk(zd1)
z1.set_dieta(list_diet)
z1.set_data_zamowienia('16.06.2021')

print(z1)
