def linha():
    print('-' * 30)

# loop comum

lista = []
for i in range(1, 11):
    lista.append(i)
print(lista)

# list comprehensions

lista2 = [i for i in range(1, 11)]
print(lista2)

linha()

# loop comum

lista3 = []
for i in [1,2,3]:
    for v in [4,5,6]:
        lista3.append((i,v))
print(lista3)

# list comprehension (for dentro de for)

lista4 = [(i,v) for i in [1,2,3,] for v in [4,5,6]]
print(lista4)

linha()

# loop comum

lista3 = []
for i in [1,2,3]:
    for v in [4,5,6]:
        if v % 2 == 0:
            lista3.append((i,v))
print(lista3)

# list comprehension (for dentro de for)

lista4 = [(i,v) for i in [1,2,3,] for v in [4,5,6] if v % 2 == 0]
print(lista4)

linha()

lista5 = [[i for i in range(0,4)] for i in range(0,3)] # vai gerar 3 listas com 4 elementos, dentro de uma litsa
print(lista5)

linha()
