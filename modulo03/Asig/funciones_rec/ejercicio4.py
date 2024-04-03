def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    return invertir_cadena(cadena[1:]) + cadena[0]

cadena1 = "Buenas Tardes"
cadena2 = "Muchas Gracias"
cadena3 = "Buen Fin De Semana"

print(f"Cadena original: {cadena1}")
print(f"Cadena invertida: {invertir_cadena(cadena1)}")

print(f"Cadena original: {cadena2}")
print(f"Cadena invertida: {invertir_cadena(cadena2)}")

print(f"Cadena original: {cadena3}")
print(f"Cadena invertida: {invertir_cadena(cadena3)}")
