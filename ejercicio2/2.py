"""
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
"""

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
print(cambio(cadena).nota)

