Minimo_Alumnos = 1
Maximo_Alumnos = 30
Nota_Minima = 0
Nota_Maxima = 10
Minimo_caracteres_nombre = 5


def validar_entero(texto):
    """Valida que el texto contenga solamente números enteros"""

    if len(texto) == 0:
        return False

    valido = True

    for i in range(len(texto)):
        caracter = texto[i]

        if caracter < "0" or caracter > "9":
            valido = False

    return valido


def pedir_cantidad():
    """Pide la cantidad de alumnos y valida que esté entre 1 y 30."""

    cantidad = 0
    valido = False

    while valido == False:
        texto = input("Ingrese la cantidad de alumnos: ")

        if validar_entero(texto):
            cantidad = int(texto)

            if cantidad >= Minimo_Alumnos and cantidad <= Maximo_Alumnos:
                valido = True
            else:
                print("La cantidad debe estar entre 1 y 30.")
        else:
            print("Por favor, ingresar un numero entero.")

    return cantidad


def validar_nombre(nombre):
    """Valida que el nombre tenga al menos 5 caracteres, solo letras y espacios."""

    if len(nombre) < Minimo_caracteres_nombre:
        return False

    valido = True

    for i in range(len(nombre)):
        caracter = nombre[i]

        la_letra = False

        if caracter >= "a" and caracter <= "z":
            la_letra = True
        elif caracter >= "A" and caracter <= "Z":
            la_letra = True
        elif caracter == " ":
            la_letra = True

        if la_letra == False:
            valido = False

    return valido


def pedir_nombre():
    """Pide un nombre hasta que sea válido."""

    nombre = ""

    while validar_nombre(nombre) == False:
        nombre = input("Ingrese el nombre: ")

        if validar_nombre(nombre) == False:
            print("Es un nombre invalido.")

    return nombre


def pedir_nota(numero_del_parcial):
    """Pide una nota con valor entero entre 0 y 10."""

    nota = -1
    valido = False

    while valido == False:
        texto = input("Ingrese la nota del parcial " + str(numero_del_parcial) + ": ")

        if validar_entero(texto):
            nota = int(texto)

            if nota >= Nota_Minima and nota <= Nota_Maxima:
                valido = True
            else:
                print("La nota debe estar entre 0 y 10.")
        else:
            print("Debe ingresar un numero entero y valido.")

    return nota


