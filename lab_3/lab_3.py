# zadanie 1
def zad1(name, surname):
    return 'Cześć '+name+' '+surname+'!'


zmienna1 = zad1('Konstancja', 'Pradelska')
print('Zadanie 1:', zmienna1)

# zadanie 2


def zad2(a, b):
    return a*b


print('Zadanie 2:', zad2(4, 5))

# zadanie 3


def zad3(a):
    if a % 2 == 0:
        return True
    else:
        return False


if zad3(8):
    print('Zadanie 3: Liczba parzysta')
else:
    print('Zadanie 3: Liczba nieparzysta')

# zadanie 4


def zad4(a, b, c):
    if a+b >= c:
        return True
    else:
        return False


print('Zadanie 4:', zad4(4, 5, 13))

# zadanie 5


def zad5(list, a):
    if a in list:
        return True
    else:
        return False


list = [2, 6, 3, 8]
print('Zadanie 5:', zad5(list, 8))

# zadanie 6


def zad6(list1, list2):
    list3 = list1+list2
    counter = 1
    for i in list3:
        if i in list3[counter:]:
            list3.remove(i)
        counter += 1
    list3 = [i*i*i for i in list3]
    return list3


list1 = [3, 3, 5, 8]
list2 = [4, 5, 6, 2]

print('Zadanie 6:', zad6(list1, list2))
