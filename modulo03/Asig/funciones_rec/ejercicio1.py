def suma_naturales(n):
    #Si n es igual a 0, la suma es 0
    if n == 0:
        return 0
    #Suma el número actual (n) con la suma de los primeros (n-1) números
    return n + suma_naturales(n-1)

# Prueba de la función
n1 = 4
n2 = 12
n3 = 16

print(f"La suma de los primeros n: {n1}, números naturales es: {suma_naturales (n1)}")
print(f"La suma de los primeros n: {n2}, números naturales es: {suma_naturales (n2)}")
print(f"La suma de los primeros n: {n3}, números naturales es: {suma_naturales (n3)}")
