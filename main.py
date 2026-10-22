from validaciones import pedir_cantidad
from validaciones import pedir_nombre
from validaciones import pedir_nota

from procesamiento import calcular_promedios
from procesamiento import promedio_general
from procesamiento import mejor_promedio
from procesamiento import peor_promedio
from procesamiento import contar_condiciones
from procesamiento import ordenar_burbuja
from procesamiento import contar_las_vocales
from procesamiento import invertir_nombre
from procesamiento import buscar_alumno


def cargar_alumnos(cantidad):
    """Carga los datos de todos los alumnos."""

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


def mostrar_listado(nombres, parcial_1, parcial_2, promedios):
    """Muestra todos los alumnos con sus respectivas notas y promedios."""

    for i in range(len(nombres)):
        print()
        print("Alumno:", nombres[i])
        print("Parcial 1:", parcial_1[i])
        print("Parcial 2:", parcial_2[i])
        print("Promedio:", promedios[i])


def mostrar_estadisticas(nombres, promedios):
    """Muestra las estadísticas generales de todo el curso."""

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


def jugar_con_un_nombre(nombres):
    """Busca un alumno y muestra sus vocales y su nombre invertido."""

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

def hay_alumnos(nombres): 
    if len(nombres) >0:
        return True
    else:
        return False    

def main():
    """Ejecuta el programa principal."""

    nombres = []

    opcion = ""

    while opcion != "0":
        print()
        print("------- NOTA FACIL -------")
        print("1. Cargar alumnos")
        print("2. Mostrar listados")
        print("3. Mostrar estadisticas")
        print("4. Ver ranking (ordenado)")
        print("5. Buscar alumno")
        print("6. Juegos con un nombre")
        print("0. Salir")
        print("--------------------------")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                nombres, parcial_1, parcial_2 = cargar_alumnos(pedir_cantidad())

                promedios = calcular_promedios(parcial_1,parcial_2)

            case "2":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:
                    mostrar_listado(nombres,parcial_1,parcial_2,promedios)
                else:
                    print ("aun no se cargó ningun alumno")    

            case "3":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:
                    mostrar_estadisticas(nombres,promedios)
                else:
                   print ("aun no se cargó ningun alumno")      

            case "4":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:
                    ordenar_burbuja(nombres,parcial_1,parcial_2,promedios)

                    print()
                    print("Ranking Del Curso")
                    
                    mostrar_listado(nombres,parcial_1,parcial_2,promedios)

                else:
                    print ("aun no cargó ningun alumno")    

            case "5":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:
                    nombre_buscado = input("Ingrese el nombre a buscar: ")

                    buscar_alumno(nombre_buscado,nombres,parcial_1,parcial_2,promedios)

                else:
                    print ("aun no se cargó ningun alumno")    

            case "6":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:      
                    jugar_con_un_nombre(nombres)

                else:
                    print ("aun no cargó ningun alumno")     


            case "0":
                print("Programa finalizado.")

            case _:
                print("Opcion invalida.")


main()