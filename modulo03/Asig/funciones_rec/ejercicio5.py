def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    #Utiliza la identidad nCk = (n-1)C(k-1) + (n-1)Ck
    return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)

n1, k1 = 5, 2
n2, k2 = 6, 3
n3, k3 = 8, 4

print(f"Coeficiente binomial de {n1}, tomados de {k1} es: {coeficiente_binomial(n1, k1)}")
print(f"Coeficiente binomial de {n2}, tomados de {k2} es: {coeficiente_binomial(n2, k2)}")
print(f"Coeficiente binomial de {n3}, tomados de {k3} es: {coeficiente_binomial(n3, k3)}")
