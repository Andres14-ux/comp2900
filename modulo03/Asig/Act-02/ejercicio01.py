# Funciones para hacer una búsqueda en una lista de valores
# no ordenados.

import timeit

#Enfoque 1: usando un ciclo for
def search_for (number, numbers):
    for i in range (len(numbers)):
        if numbers[i] == number:
            return i
    return -1


#Enfoque 2: usando la funcion index()
def search_index (number, numbers):
    try:
        return numbers.index(number)
    except ValueError:
        return -1
    
numbers = list(range(1, 1001))
number = list(range(1, 1001))

time_for = timeit.timeit(lambda: search_for(number, numbers), number=10000)
print("Enfoque 1: ", time_for)

time_index = timeit.timeit(lambda: search_index(number, numbers), number=10000)
print("Enfoque 2:", time_index)  