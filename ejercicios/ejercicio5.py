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

def num():
    while True:
        try:
            num = int(input("Introduce un número entero positivo: "))
            if num < 0:
                print("El número debe ser positivo")
                continue
            break
        except ValueError:
            print("El valor introducido no es un número entero")
            continue
    return num

def descomposicion(num):
    num = str(num)
    num = num[::-1]
    ceros_izquierda = 0
    while True:
        for i in str(num):
            ceros_izquierda += 1
            print((i.ljust(int(ceros_izquierda), "0")).zfill(len(num)))
        if ceros_izquierda >= len(num):
            break

# descomposicion(3647) 

if __name__ == "__main__":
    main()

   


    







