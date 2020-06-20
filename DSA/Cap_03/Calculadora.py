n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
escolha = int(input('Escolha uma opção:\n 1º - Soma\n 2º - Subtração\n 3º - Multiplicação\n 4º - Divisão\n 5º - Todos os resultados\n'))
soma = n1 + n2
sub  = n1 - n2
mult = n1 * n2
div = n1 / n2

def resul(n1, n2):
    if escolha == 1:
        print('A soma dos valores {} e {} é:'.format(n1,n2,),soma)
    if escolha == 2:
        print('A subtração dos valores {} e {} é:'.format(n1, n2,), sub)
    if escolha == 3:
        print('A multiplicação dos valores {} e {} é:'.format(n1, n2,), mult)
    if escolha == 4:
        print('A divisão dos valores {} e {} é:'.format(n1, n2,), div)
    if escolha == 5:
        print('Todos os resuldados das operações:', '\n' 'Soma: ', soma, '\n' 'Subtração: ', sub, '\n' 'Multiplicação: ', mult, '\n' 'Divisão: ', div, '\n')
    else:
        print('Opção Invalida')
resul(n1, n2)