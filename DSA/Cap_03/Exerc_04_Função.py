def argumento(arg1, *lista):
    print(arg1)
    for i in lista:
        print(i)
    return

argumento('Argumento')
argumento('teste01', 'teste02', 'teste03')
