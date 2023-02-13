"""
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

Nombre Apellido ha sacado un Nota de nota.

Ayuda

Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"
"""

#CORRECCION CADENA DE TEXTO CORRUPTO
cadena = "zeréP nauJ,01"
def cambio(cadena):
    cadena=(cadena[::-1])
    nota = cadena.split(",")
    nombre = nota[1].split(" ")
    return alumno(nombre[0], nombre[1], nota[0])



class alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

    def __str__(self):
        return f"{self.nombre} {self.apellido} ha sacado un {self.nota}"

#GUARDAR EN UNA LISTA
    # print(cambio(cadena))                 #imprime el __str__
    # print(cambio(cadena).nombre)          #imprime el nombre
    # print(cambio(cadena).apellido)        #imprime el apellido
    # print(cambio(cadena).nota)            #imprime la nota

class alumnos:
    #lista de alumnos 
    lista = []

    @staticmethod
    def buscar(nombre):
        for alumno in alumnos.lista:
            if alumno.nombre == nombre:
                return alumno

    @staticmethod
    def crear(nombre, apellido, nota):
       alumno = alumno(nombre, apellido, nota)
       alumnos.lista.append(alumno)
       return alumno

    @staticmethod
    def modificar (nombre, apellido, nota):
        for i, alumno in enumerate (nombre, apellido, nota):
            if alumno.nombre == nombre:
                alumnos.lista[i].nombre = nombre
                alumnos.lista[i].apellido = apellido
                alumnos.lista[i].nota = nota
                return alumnos.lista[i]

    @staticmethod
    def borrar(nombre):
        for i, alumno in enumerate (alumnos.lista):
            if alumno.nombre == nombre:
                alumno = alumnos.lista.pop(i)
                return alumno
       
