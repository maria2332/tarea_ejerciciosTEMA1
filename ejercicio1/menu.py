import os 

def iniciar():
    while True:
        os.system('clear')

        print("========================")
        print("  BIENVENIDO AL SISTEMA ")
        print("========================")
        print("[1] Listar alumnos      ")
        print("[2] Bucar alumno        ")
        print("[3] Añadir alumno       ")
        print("[4] Modificar alumno    ")
        print("[5] Borrar alumno       ")
        print("[6] Cerrar el sistema   ")
        print("========================")

        opcion = input("Seleccione una opción: ")
        os.system('clear')

        if opcion == "1":
            print("Listando los alumnos...\n")
        if opcion == "2":
            print("Buscando un alumno...\n")
        if opcion == "3":
            print("Añadiendo un alumno...\n")
        if opcion == "4":
            print("Modificando un alumno...\n")
        if opcion == "5":
            print("Borrando un alumno...\n")
        if opcion == "6":
            print("Cerrando el sistema...\n")
            break

        input("\n Presione ENTER para continuar...")


