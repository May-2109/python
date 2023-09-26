# copy() -> função para criar uma cópia de uma lista, sem afetar a original
lista = [1, 'Python', [40, 30, 20]]

l2 = lista.copy() #cria uma cópia da lista, sem afetar a original

print(lista)

print(id(l2), id(lista))

l2[0] = 2
print(lista)
print(l2)