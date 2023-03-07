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
        frase = cadena_correcta.split(",")
        nota = frase[0]
        nombre = frase[1]
        return f"{nombre} ha sacado un {nota}"
    
# cadena = "zeréP nauJ,01"
nombre1=Alumno("zeréP nauJ,01")

if __name__ == "__main__":
    print(Alumno.formatear_cadena(nombre1.cadena))
