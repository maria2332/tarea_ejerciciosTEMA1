"""Ejercicio 7
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.
Sugerencia
Puedes utilizar la sintaxis "elemento in lista"
elementos = [1, 5, -2]
 
# Completa el ejercicio aquí
"""

def agregar_una_vez(lista, el):
    if el not in lista:
        lista.append(el)
    else:
        raise ValueError(f'Error: Imposible añnadir elementos duplicados=>{el}')
    return lista


if __name__ == "__main__":
    print(agregar_una_vez([1,2,8,"g"], 6))