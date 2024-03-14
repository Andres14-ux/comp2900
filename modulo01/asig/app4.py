def es_numero_entero(cadena):
    # Verifica si la cadena es vacía
    if cadena == "":
        return False

    # Verifica si el primer carácter es un signo
    if cadena[0] in '+-':
        # Si la cadena tiene solo un signo, no es un entero
        if len(cadena) == 1:
            return False
        # Verifica que los caracteres restantes sean dígitos
        cadena = cadena[1:]

    # Verifica que todos los caracteres restantes sean dígitos
    return cadena.isdigit()

# Ejemplo de uso
cadena = input("Introduce una cadena para validar si es un número entero: ")
print(es_numero_entero(cadena))
