import unittest
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio5
import ejercicio6
import ejercicio7
from unittest.mock import patch

class TestEjercicio(unittest.TestCase):
    def test_formatear_cadena(self):
        self.assertEqual(ejercicio1.Alumno.formatear_cadena("zeréP nauJ,01"), "Juan Pérez ha sacado un 10")

    def test_ejercicio2(self):
        self.assertRaises(ValueError, ejercicio2.excepcion, "hola")
        self.assertRaises(ValueError, ejercicio2.excepcion, "1000")

    def test_ejercicio3(self):
        lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
        lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
        self.assertEqual(ejercicio3.listas(lista_1, lista_2), ['h', 'o', 'l', 'a', ' ', 'u', 'n'])

    def test_ejercicio4(self):
        cola= [
        {'tarea 3': 'ir a clase', 'prioridad':'3'},
        {'tarea 1': 'levantarme', 'prioridad':'1'},
        {'tarea 2': 'comer', 'prioridad':'2'}
        ]
        self.assertEqual(ejercicio4.estructura_cola(cola), [{'tarea 1': 'levantarme', 'prioridad': '1'},
                                                        {'tarea 2': 'comer', 'prioridad': '2'},
                                                        {'tarea 3': 'ir a clase', 'prioridad': '3'}])
    def test_ejercicio5(self):
        self.assertEqual(ejercicio5.descomponer("1234"), ["0004", "0030", "0200", "1000"])
    
    def test_ejercicio6(self):
        self.assertEqual(ejercicio6.separar([1,2,3,4,5,6,7,8,9,10]), ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))

    def test_ejercicio7(self):
        self.assertEqual(ejercicio7.agregar_una_vez([1,3,5,7,"g"], 6), [1, 3, 5, 7, 'g', 6])
