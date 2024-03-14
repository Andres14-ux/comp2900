def calcular_promedio(arreglo):
    suma = 0
    cantidad_elementos = 0
    for elemento in arreglo:
        suma += elemento
        cantidad_elementos += 1
    if cantidad_elementos == 0:
        return 0
    else:
        promedio = suma / cantidad_elementos
        return promedio


arreglo = [15, 23, 38, 46, 55]
promedio = calcular_promedio(arreglo)
print(f"El promedio de los elementos del arreglo es: {promedio}")
