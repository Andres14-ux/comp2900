lista = [10, 3, 4, 7, 2]

print (4 in lista) #O(1)

for number in lista:
    if (number == 4): #O(n)
        print ('True')

suma = 0
for number in lista: #O(n)
    suma += number
