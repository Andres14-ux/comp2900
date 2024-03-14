def imprimir_numeros():
    number = 0
    for i in range(1, 11):
        print (i)
        number = i
    return number

assert imprimir_numeros() == 10, "El ciclo corrio correctamente"