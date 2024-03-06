arreglo = [1, 2, 3, 4, 5]

ultimo_elemento = arreglo.pop()  # Remueve el último elemento
arreglo.insert(0, ultimo_elemento)  # Inserta el último elemento al principio del arreglo

print(f"Arreglo con los elementos rotados: {arreglo}")
