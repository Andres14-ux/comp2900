def potencia(base, exponente):
    #Si el exponente es 0, la potencia es 1
    if exponente == 0:
        return 1
    #Multiplica la base por la potencia(base, exponente-1)
    return base * potencia(base, exponente - 1)

base1, exp1 = 6, 9
base2, exp2 = 5, 8
base3, exp3 = 7, 0

print(f"Potencia de {base1}, elevado a {exp1} es: potencia{base1, exp1}")
print(f"Potencia de {base2}, elevado a {exp2} es: potencia{base2, exp2}")
print(f"Potencia de {base3}, elevado a {exp3} es: potencia{base3, exp3}")