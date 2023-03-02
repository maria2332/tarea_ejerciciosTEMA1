import unittest
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio5
import ejercicio6
import ejercicio7

class TestEjercicios(unittest.TestCase):
    def test_ejercicio1(self):
        nombre = ejercicio1.Alumno.formatear_cadena("zeréP nauJ,01")
        self.assertEqual(ejercicio1.Alumno.formatear_cadena)

    def test_ejercicio2(self):
        self.assertEqual(ejercicio2.ejercicio2(), 1111111088888888)

    def test_ejercicio3(self):
        self.assertEqual(ejercicio3.ejercicio3(), "Hola mundo")

    def test_ejercicio4(self):
        self.assertEqual(ejercicio4.ejercicio4(), "Hola mundo")

    def test_ejercicio5(self):
        self.assertEqual(ejercicio5.ejercicio5(), "Hola mundo")

    def test_ejercicio6(self):
        self.assertEqual(ejercicio6.ejercicio6(), "Hola mundo")

    def test_ejercicio7(self):
        self.assertEqual(ejercicio7.ejercicio7(), "Hola mundo")