from functools import reduce

lista = [47, 11, 42, 13]

def soma(a,b):
    x = a + b
    return x

reduce(soma, lista)
print('Soma total: ',reduce(soma, lista))


max_find2 = lambda a,b: a if (a > b) else b
print('Maior elemento dentro da lista: ', reduce(max_find2, lista))

