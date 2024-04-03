def mcd_euclides(a, b):
    #Si b es 0, entonces el MCD es a
    if b == 0:
        return a
    #Llama recursivamente con b y el residuo de a dividido por b
    return mcd_euclides(b, a % b)

num1, num2 = 38, 28
num3, num4 = 93, 62
num5, num6 = 61, 37

print(f"El MCD de {num1} y {num2} es: {mcd_euclides(num1, num2)}")
print(f"El MCD de {num3} y {num4} es: {mcd_euclides(num3, num4)}")
print(f"El MCD de {num5} y {num6} es: {mcd_euclides(num5, num6)}")
