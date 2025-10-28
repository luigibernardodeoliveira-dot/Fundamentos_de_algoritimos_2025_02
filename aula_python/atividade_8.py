from random import randint, random

lista1 = []
lista2 = []
lista3 = ["a", "b", "c", "d", "e", "f", "g"]
lista_geral = []

for i in range (10):
    nro = random() * 10
    lista2.append(nro)

for i in range(5):
    nro = random() * 10
    lista2.append(nro)

lista_geral.append(lista1)
lista_geral.append(lista2)
lista_geral.append(lista3)

del(lista1)
del(lista2)
del(lista3)
print( lista_geral)