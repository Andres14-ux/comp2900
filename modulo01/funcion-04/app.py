def saludo():
    global nombre
    nombre = "John Doe"
    print(f'Hola {nombre}')

def despedida():
    nombre = "Sara Swan"
    print(f'Adios {nombre}')

saludo()
despedida()
print(nombre)