# Encontrar el número más grande en una lista de números.
import timeit
# Enfoque 1: Utilizando la función max() de Python para encontrar el
# número más grande en una lista.
def max_lista(lista):
    return max(lista)

# Enfoque 2: Recorriendo la lista y comparando cada número con un valor
# de referencia para encontrar el número más grande
def max_iterativo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

lista = list(range(1, 1001))

time_lista = timeit.timeit (lambda: max_lista(lista), number=10000)
print("Enfoque 1: ", time_lista)

time_iterativo = timeit.timeit (lambda: max_iterativo(lista), number=10000)
print("Enfoque 2: ", time_iterativo)