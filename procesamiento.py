def cargar_alumnos(cantidad: int):
    """Carga los datos de todos los alumnos.

    Args:
        cantidad: Cantidad de alumnos a cargar.

    Returns:
        Los nombres y las notas de los alumnos.
    """

    nombres = []
    parcial_1 = []
    parcial_2 = []

    for i in range(cantidad):
        print()
        print("Alumno", i + 1)

        nombre = pedir_nombre()
        nota_1 = pedir_nota(1)
        nota_2 = pedir_nota(2)

        nombres = nombres + [nombre]
        parcial_1 = parcial_1 + [nota_1]
        parcial_2 = parcial_2 + [nota_2]

    return nombres, parcial_1, parcial_2


def mostrar_listado(
    nombres: list[str],
    parcial_1: list[float],
    parcial_2: list[float],
    promedios: list[float]
):
    """Muestra todos los alumnos con sus respectivas notas y promedios.

    Args:
        nombres: Lista con los nombres de los alumnos.
        parcial_1: Lista con las notas del primer parcial.
        parcial_2: Lista con las notas del segundo parcial.
        promedios: Lista con los promedios de los alumnos.
    """

    for i in range(len(nombres)):
        print()
        print("Alumno:", nombres[i])
        print("Parcial 1:", parcial_1[i])
        print("Parcial 2:", parcial_2[i])
        print("Promedio:", promedios[i])


def mostrar_estadisticas(
    nombres: list[str],
    promedios: list[float]
):
    """Muestra las estadísticas generales de todo el curso.

    Args:
        nombres: Lista con los nombres de los alumnos.
        promedios: Lista con los promedios de los alumnos.
    """

    general = promedio_general(promedios)

    nombre_mejor, mejor = mejor_promedio(nombres,promedios)

    nombre_peor, peor = peor_promedio(nombres,promedios)

    promocionan, aprueban, desaprueban = contar_condiciones(promedios)

    print()
    print("Promedio General:", general)
    print("Mejor Promedio:", nombre_mejor, "-", mejor)
    print("Peor Promedio:", nombre_peor, "-", peor)

    print()
    print("Promocionan:", promocionan)
    print("Aprueban:", aprueban)
    print("Desaprueban:", desaprueban)


def jugar_con_un_nombre(nombres: list[str]):
    """Busca un alumno y muestra sus vocales y su nombre invertido.

    Args:
        nombres: Lista con los nombres de los alumnos.
    """

    nombre_buscado = input("Ingrese el nombre del alumno: ")

    encontrado = False

    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            vocales = contar_las_vocales(nombres[i])
            invertido = invertir_nombre(nombres[i])

            print("Cantidad de vocales:", vocales)
            print("Nombre invertido:", invertido)

            encontrado = True

    if encontrado == False:
        print("El nombre del alumno no existe.")

def hay_alumnos(nombres: list[str]):
    """Indica si hay alumnos cargados.

    Args:
        nombres: Lista con los nombres de los alumnos.

    Returns:
        True si hay alumnos cargados o False si la lista está vacía.
    """

    if len(nombres) == 0:
        print("No hay alumnos cargados.")
        return False

    return True   


def calcular_promedios(
    parcial_1: list[float],
    parcial_2: list[float]
):
    """Calcula el promedio de cada uno de los alumnos.

    Args:
        parcial_1: Lista con las notas del primer parcial.
        parcial_2: Lista con las notas del segundo parcial.

    Returns:
        Lista con los promedios de los alumnos.
    """

    promedios = []

    for i in range(len(parcial_1)):
        promedio = (parcial_1[i] + parcial_2[i]) / 2
        promedios = promedios + [promedio]

    return promedios


def promedio_general(promedios: list[float]):
    """Calcula el promedio general de todo el curso.

    Args:
        promedios: Lista con los promedios de los alumnos.

    Returns:
        Promedio general del curso.
    """

    acumulador = 0

    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]

    promedio = acumulador / len(promedios)

    return promedio


def mejor_promedio(
    nombres: list[str],
    promedios: list[float]
):
    """Busca el mejor promedio y el nombre del alumno que lo obtuvo.

    Args:
        nombres: Lista con los nombres de los alumnos.
        promedios: Lista con los promedios de los alumnos.

    Returns:
        Nombre del alumno con mejor promedio y su promedio.
    """

    mejor = promedios[0]
    nombre_mejor = nombres[0]

    for i in range(1, len(promedios)):
        if promedios[i] > mejor:
            mejor = promedios[i]
            nombre_mejor = nombres[i]

    return nombre_mejor, mejor


def peor_promedio(
    nombres: list[str],
    promedios: list[float]
):
    """Busca el peor promedio y el nombre del alumno que lo obtuvo.

    Args:
        nombres: Lista con los nombres de los alumnos.
        promedios: Lista con los promedios de los alumnos.

    Returns:
        Nombre del alumno con peor promedio y su promedio.
    """

    peor = promedios[0]
    nombre_peor = nombres[0]

    for i in range(1, len(promedios)):
        if promedios[i] < peor:
            peor = promedios[i]
            nombre_peor = nombres[i]

    return nombre_peor, peor


def contar_condiciones(promedios: list[float]):
    """Cuenta los alumnos que promocionan, aprueban y desaprueban.

    Args:
        promedios: Lista con los promedios de los alumnos.

    Returns:
        Cantidad de alumnos que promocionan, aprueban y desaprueban.
    """

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


def ordenar_burbuja(
    nombres: list[str],
    parcial_1: list[float],
    parcial_2: list[float],
    promedios: list[float]
):
    """Ordena a los alumnos de mayor a menor promedio.

    Args:
        nombres: Lista con los nombres de los alumnos.
        parcial_1: Lista con las notas del primer parcial.
        parcial_2: Lista con las notas del segundo parcial.
        promedios: Lista con los promedios de los alumnos.
    """


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


def contar_las_vocales(nombre: str):
    """Cuenta las vocales del nombre.

    Args:
        nombre: Nombre del alumno.

    Returns:
        Cantidad de vocales que contiene el nombre.
    """

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


def invertir_nombre(nombre: str):
    """Devuelve el nombre del alumno pero escrito al revés.

    Args:
        nombre: Nombre del alumno.

    Returns:
        Nombre escrito en orden inverso.
    """

    invertido = ""

    for i in range(len(nombre) - 1, -1, -1):
        invertido = invertido + nombre[i]

    return invertido


def buscar_alumno(
    nombre_buscado: str,
    nombres: list[str],
    parcial_1: list[float],
    parcial_2: list[float],
    promedios: list[float]
):
    """Busca un alumno y muestra sus datos.

    Args:
        nombre_buscado: Nombre del alumno que se desea buscar.
        nombres: Lista con los nombres de los alumnos.
        parcial_1: Lista con las notas del primer parcial.
        parcial_2: Lista con las notas del segundo parcial.
        promedios: Lista con los promedios de los alumnos.
    """

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
