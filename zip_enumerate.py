import itertools  #usado somente para prencher automaticamente quando listas tem menos valores que outras

'''
para unir mais de duas lista respectivamente, devemos usar a funçao zip()
A importaçao itertool (itertools.zip_longest), nos permite unir mais de duas listas respectivamente prenchendo automaticamente
com None se a quantidade de valores de uma lista for menor que a outra
'''

lista1 = ['Sandra', 'Joao', 'Felipe', 'Gabriel', 'Rafael']
lista2 = [20, 33, 35, 17, 12]
lista3 = ['SP', 'MG', 'RJ', 'BA', 'MT']

for (i, t, a) in zip(lista1, lista2, lista3):
    print(f'Se chama {i}, tem {t} anos e mora em {a}')

print('-' * 30)

num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]
  
for (a, b, c) in zip(num, color, value):
     print (f'{a} tem a cor {b} e tamanho {c}')

print('-' * 30)    

num = [1, 2, 3, 4]
color = ['red', 'while', 'black']
value = [255, 256, 569]
  
for (a, b, c) in itertools.zip_longest(num, color, value):
    print (f'{a} tem a cor {b} e tamanho {c}')
    
    