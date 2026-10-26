Es un programa de consola en Python para cargar las notas de un curso y obtener promedios, estadísticas y un ranking de alumnos.
 
¿Qué hace?
 
Se cargan los alumnos con su nombre y las notas de los dos parciales. A partir de eso, el programa calcula el promedio de cada uno y ofrece un menú con estas opciones:

 
1 = Cargar alumnos: Pide la cantidad de alumnos y para cada uno, el nombre y las dos notas (con validación de datos).

2 = Mostrar listados: Muestra cada alumno con sus notas y su promedio.

3 = Mostrar estadísticas: Promedio general del curso, mejor y peor promedio, y cuántos alumnos promocionan, aprueban o desaprueban.

4 = Ver ranking: Ordena a los alumnos por promedio (método burbuja, tal cual se solicitó) y muestra el listado.

5 = Buscar alumno: Busca un alumno por nombre y muestra sus datos.

6 = Juegos con un nombre: Cuenta las vocales del nombre de un alumno y lo muestra invertido.

0 = Salir.

   
Si se elige una opción antes de cargar alumnos, el programa avisa que todavía no hay datos.

Estructura:
 
- main.py: menú principal y funciones para cargar y mostrar datos.
- validaciones.py: funciones que piden y validan la cantidad, los nombres y las notas.
- procesamiento.py: cálculos (promedios, estadísticas, ordenamiento, búsqueda y funciones sobre nombres).
  
¿Cómo ejecutarlo?
 
python3 main.py
