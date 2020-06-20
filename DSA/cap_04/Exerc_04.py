lista = [0, 1, 2, 3, 4]

def quadrado(x):
    return x**2
def cubo(x):
    return x**3

result = [quadrado, cubo]
for i in lista:
    valor = map(lambda x: x(i), result)
    print(list(valor))