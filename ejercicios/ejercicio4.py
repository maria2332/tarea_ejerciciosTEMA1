"""
Ejercicio 4
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
Sugerencia
Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
"""

def ordenar(lista):
    lista.sort()
    lista_2 = []
    for i in lista:
        lista_2.append(i[1])
    return lista_2

if __name__ == "__main__":
    lista = [(2, 'Preparar ropa'), (4, 'Hacer la cama'), (3, 'Sacar al perro'), (1, 'Lavar los platos')]
    print(ordenar(lista))

    