import array

aNumber = array.array('i')

for i in range(1, 4): # from 1 to 3
    number = int(input('Enter a number: '))
    aNumber.append(number)

for i in range(3): # from 0 to 2
    print (f'Indice {i} - Valor {aNumber[i]}')