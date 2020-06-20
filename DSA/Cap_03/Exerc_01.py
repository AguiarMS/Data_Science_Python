semana = input('Qual o dia da semana ?: ')
if semana == 'Domingo' or semana == 'Sabado':
    print('Hoje é dia de descanso')
elif semana == 'Segunda' or 'Terça':
    print('Dia de trabalho !')
elif semana == 'Quarta' or 'Quinta':
    print('Dia de trabalho !')
elif semana == 'Sexta':
    print('Dia de trabalho !')
else:
    print('Dia da semana não existe.')
