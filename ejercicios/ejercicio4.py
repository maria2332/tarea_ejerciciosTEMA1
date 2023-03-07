"""
Ejercicio 4
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
Sugerencia
Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
"""

cola= [
        {'tarea 3': 'ir a clase', 'prioridad':'3'},
        {'tarea 1': 'levantarme', 'prioridad':'1'},
        {'tarea 2': 'comer', 'prioridad':'2'}
    ]

def ordenar(c):
    return c['prioridad']


def estructura_cola(cola):
    cola.sort(key=ordenar)
    lista=[]
    for i in cola:
        print(i)
        lista.append(i)
    return lista

if __name__=="main_":
    estructura_cola(cola)
    