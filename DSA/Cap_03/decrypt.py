import sys
import string
arquivo = open(sys.argv[1] , 'r').read().lower()
rotacao = int(sys.argv[2])
alfabeto = string.lowercase
resultado = ''
for letra in arquivo:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)
        posicao = (posicao + rotacao) % 26
        resultado = resultado + alfabeto[posicao]
print(resultado)