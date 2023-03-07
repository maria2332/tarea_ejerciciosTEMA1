import os
import sys
import re
from colorama import *
from termcolor import *
import helpers
from ejercicios import ejercicio1
from ejercicios import ejercicio2
from ejercicios import ejercicio3
from ejercicios import ejercicio4
from ejercicios import ejercicio5
from ejercicios import ejercicio6
from ejercicios import ejercicio7


init(autoreset=True)


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        lineas=(Fore.BLUE +"="*50)
        print(lineas)
        print(colored((("Bienvenido al menú de ejercicios de Python").upper()).center(50), "white", "on_blue"))
        print(lineas)
        print(colored(Fore.BLUE+"[1]"),"Ejercicio 1: Alumno")
        print(colored(Fore.BLUE+"[2]"),"Ejercicio 2: Número mágico")
        print(colored(Fore.BLUE+"[3]"),"Ejercicio 3: Listas")
        print(colored(Fore.BLUE+"[4]"),"Ejercicio 4: Tareas")
        print(colored(Fore.BLUE+"[5]"),"Ejercicio 5: Descomposicion")
        print(colored(Fore.BLUE+"[6]"),"Ejercicio 6: Pares e impares")
        print(colored(Fore.BLUE+"[7]"),"Ejercicio 7: Agregar una vez")
        print(colored(Fore.RED+"[8]"),("SALIR"))
        print(lineas)

        opcion = input(colored(Fore.BLUE+"Elige una opción: ", "blue"))
        helpers.limpiar_pantalla()

        if opcion == "1":
            print(Back.CYAN+Fore.WHITE+"Ejercicio 1: Alumno")
            #ejercicicios.alumno
            ejercicio1.cadena=input(colored(Fore.BLUE+"Ingresa tu cadena corrupta: ", "blue"))
            print(ejercicio1.formatear_cadena(ejercicio1.cadena))

        

        elif opcion == "2":
            print(Back.CYAN+Fore.WHITE+"Ejercicio 2: Número mágico")
            n=int(input(colored(Fore.BLUE+"Ingresa un número: ", "blue")))
            print(ejercicio2.numeromagico.num(n))

        elif opcion == "3":
            print(Back.CYAN+Fore.WHITE+"Ejercicio 3: Listas")
            list1 =list(input(colored(Fore.BLUE+"Ingresa tu primera lista: ", "blue")))
            list2 =list(input(colored(Fore.BLUE+"Ingresa tu segunda lista: ", "blue")))
            print(ejercicio3(list1, list2))

        elif opcion == "4":
            print(Back.CYAN+Fore.WHITE+"Ejercicio 4: Tareas")
            list_cola=[]
            NumeroTareas = int(input(colored(Fore.BLUE+"Ingresa el número de tareas: ", "blue")))
            for i in range(NumeroTareas):
                # Crear un diccionario
                cola = {}
                # Agregar elementos al diccionario
                cola[f'tarea {i+1}'] = input(colored(Fore.BLUE+f'Ingresa la tarea {i+1}: ', "blue"))
                cola[f'prioridad'] = input(colored(Fore.BLUE+f'Ingresa la prioridad de la tarea {i+1}: ', "blue"))
                list_cola.append(cola)
            ejercicio4(list_cola)
            
        
        elif opcion == "5":
            print(Back.CYAN+Fore.WHITE+"Ejercicio 5: Descomposicion")
            n=input(colored(Fore.BLUE+"Ingresa un número: ", "blue"))
            ejercicio5(n)

        elif opcion == "6":
            print(Back.CYAN+Fore.WHITE+"Ejercicio 6: Pares e impares")
            n=int(input(colored(Fore.BLUE+"Longitud de la lista: ", "blue")))
            lista6=[]
            for i in range(n):
                lista6.append(int(input(colored(Fore.BLUE+"Ingresa el número: ", "blue"))))
            print(ejercicio6(lista6))


        elif opcion == "7":
            print(Back.CYAN+Fore.WHITE+"Ejercicio 7: Agregar una vez")
            # lista por inputs con ints y strings
            lista7= []
            n = int(input(colored(Fore.BLUE+"Longitud de la lista: ", "blue")))
            for i in range(n):
                lista7.append(input(colored(Fore.BLUE+"Ingresa el elemento de la lista: ", "blue")))
                if lista7[i].isnumeric():
                    lista7[i] = int(lista7[i])
            elemento = input(colored(Fore.BLUE+"Ingresa el elemento: ", "blue"))
            print(ejercicio7(lista7, elemento))



        elif opcion == "8":
            print(colored(Fore.RED+"Saliendo..."))
            break

        input(colored(Fore.CYAN+">>> Presiona ENTER para continuar <<<", "blue"))

(iniciar())