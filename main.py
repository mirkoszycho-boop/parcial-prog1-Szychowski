from validaciones import pedir_cantidad, pedir_nombre, pedir_nota
from procesamiento import (
    calcular_promedios, promedio_general,
    mejor_promedio, peor_promedio,
    contar_condiciones, ordenar_burbuja,
    contar_las_vocales, invertir_nombre,
    buscar_alumno, cargar_alumnos,
    mostrar_listado, mostrar_estadisticas,
    jugar_con_un_nombre, hay_alumnos
    )


def main() -> None:
    """Ejecuta el programa principal."""

    cantidad = 0
    opcion = -1
    nombres = [""]
    parcial_1 = [0]
    parcial_2 = [0]
    promedios = [0.0]

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
                
            case "3":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:
                    mostrar_estadisticas(nombres,promedios)   

            case "4":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:
                    ordenar_burbuja(nombres,parcial_1,parcial_2,promedios)

                    print()
                    print("Ranking Del Curso")
                    
                    mostrar_listado(nombres,parcial_1,parcial_2,promedios)

            case "5":
                existen_alumnos= hay_alumnos(nombres)
                if existen_alumnos:
                    nombre_buscado = input("Ingrese el nombre a buscar: ")

                    buscar_alumno(nombre_buscado,nombres,parcial_1,parcial_2,promedios)

                    pedir_cantidad = 0

            case "6":    
                    jugar_con_un_nombre(pedir_cantidad, nombres)  

            case "0":
                print("Programa finalizado.")

            case _:
                print("Opcion invalida.")


main()