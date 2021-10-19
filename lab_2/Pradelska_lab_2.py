# zadanie 2a
def two_a(list):
    print(list)

lista_a=['Martin','Eva','Tom','Daria','Pawel']

print('Zadanie 2a: ')
two_a(lista_a)

# zadanie 2b
def two_b1(list):
    lista=[]
    for i in list:
        i=i*2
        lista.append(i)
    return lista

def two_b2(list):
    lista=[i*2 for i in list]
    return lista

lista_b=[3,5,2,8,4]

print('Zadanie 2b, for: ',two_b2(lista_b))
print('Zadanie 2b, lista skladana: ',two_b2(lista_b))

# zadanie 2c
print('Zadanie 2c:')
for i in range(10):
    if i%2==0: print(i)

# zadanie 2d
print('Zadanie 2d:')
for i in range(0,10,2):
    print(i)
