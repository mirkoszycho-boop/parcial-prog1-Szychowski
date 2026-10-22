def calcular_promedios(parcial_1, parcial_2):
    """Calcula el promedio de cada uno de los alumnos."""

    promedios = []

    for i in range(len(parcial_1)):
        promedio = (parcial_1[i] + parcial_2[i]) / 2
        promedios = promedios + [promedio]

    return promedios


def promedio_general(promedios):
    """Calcula el promedio general de todo curso."""

    acumulador = 0

    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]

    promedio = acumulador / len(promedios)

    return promedio


def mejor_promedio(nombres, promedios):
    """Busca el mejor promedio y el nombre del alumno que lo obtuvo."""

    mejor = promedios[0]
    nombre_mejor = nombres[0]

    for i in range(1, len(promedios)):
        if promedios[i] > mejor:
            mejor = promedios[i]
            nombre_mejor = nombres[i]

    return nombre_mejor, mejor


def peor_promedio(nombres, promedios):
    """Busca el peor promedio y el nombre del alumno que lo obtuvo."""

    peor = promedios[0]
    nombre_peor = nombres[0]

    for i in range(1, len(promedios)):
        if promedios[i] < peor:
            peor = promedios[i]
            nombre_peor = nombres[i]

    return nombre_peor, peor


def contar_condiciones(promedios):
    """Cuenta los alumnos que promocionan, aprueban y desaprueban."""

    promocionan = 0
    aprueban = 0
    desaprueban = 0

    for i in range(len(promedios)):
        if promedios[i] >= 6:
            promocionan = promocionan + 1
        elif promedios[i] >= 4:
            aprueban = aprueban + 1
        else:
            desaprueban = desaprueban + 1

    return promocionan, aprueban, desaprueban


def ordenar_burbuja(nombres,parcial_1,parcial_2,promedios):
    """Ordena a los alumnos de mayor a menor promedio."""

    for i in range(len(promedios) - 1):
        for j in range(len(promedios) - 1 - i):

            if promedios[j] < promedios[j + 1]:

                auxiliar = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = auxiliar

                auxiliar = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = auxiliar

                auxiliar = parcial_1[j]
                parcial_1[j] = parcial_1[j + 1]
                parcial_1[j + 1] = auxiliar

                auxiliar = parcial_2[j]
                parcial_2[j] = parcial_2[j + 1]
                parcial_2[j + 1] = auxiliar


def contar_las_vocales(nombre):
    """Cuenta las vocales del nombre."""

    contador = 0

    for i in range(len(nombre)):
        caracter = nombre[i]

        if caracter == "a" or caracter == "e" or caracter == "i":
            contador = contador + 1
        elif caracter == "o" or caracter == "u":
            contador = contador + 1
        elif caracter == "A" or caracter == "E" or caracter == "I":
            contador = contador + 1
        elif caracter == "O" or caracter == "U":
            contador = contador + 1

    return contador


def invertir_nombre(nombre):
    """Devuelve el nombre del alumno pero escrito al revés."""

    invertido = ""

    for i in range(len(nombre) - 1, -1, -1):
        invertido = invertido + nombre[i]

    return invertido


def buscar_alumno(nombre_buscado, nombres, parcial_1, parcial_2,promedios):
    """Busca un alumno y muestra sus datos."""

    encontrado = False

    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            print("Alumno:", nombres[i])
            print("Parcial 1:", parcial_1[i])
            print("Parcial 2:", parcial_2[i])
            print("Promedio:", promedios[i])

            encontrado = True

    if encontrado == False:
        print("El alumno ingresado no existe.")
