frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
cont = 0
for caracter in frase:
    if caracter == 'r':
        cont += 1
print('A letra R encontra-se %s vezes nesta frase. '%(cont))