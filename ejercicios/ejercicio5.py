"""
Ejercicio 5
Crea un script llamado descomposicion.py que realice las siguientes tareas:
Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:
python descomposicion.py 3647
El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
0007
0040
0600
3000
Pista
Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa
"""

from ast import main
import sys


def num(numeros):
    try:
        numeros=int(numeros)
        return str(numeros)
        sys.exit()
    except:
        raise ValueError("El caracter no aceptado")

def descomponer(numeros):
    numeros=num(numeros)
    numero=numeros[::-1]
    lista=[]
    ceros_izquierda=0
    while True:
        for i in str(numero):
            ceros_izquierda+=1
            k=((i.ljust(int(ceros_izquierda),'0')).zfill(len(numero)))
            print(k)
            lista.append(k)
        if ceros_izquierda >= len(numero):
            break
    return lista