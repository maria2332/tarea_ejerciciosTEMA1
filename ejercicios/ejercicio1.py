"""
Ejercicio 1
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
Ayuda
Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
cadena = "zeréP nauJ,01"
"""

from ast import main 

class Alumno:
    def __init__(self, cadena):
        self.cadena = cadena

    @staticmethod
    def formatear_cadena(cadena):
        cadena_correcta = cadena[::-1]
        nota, nombre = cadena_correcta.split(",")
        return f"{nombre} ha sacado un {nota}"
    
# cadena = "zeréP nauJ,01"
# alumno = Alumno(cadena)
# print(alumno.formatear_cadena(cadena))

if __name__ == "__main__":
    cadena = input("Introduce una cadena: ")
    alumno = Alumno(cadena)
    print(alumno.formatear_cadena(cadena))