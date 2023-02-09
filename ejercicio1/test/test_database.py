import copy 
import unittest
from database import db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.alumnos.lista = [
            db.alumno("Juan", "Perez", 10),
        ]

    def test_buscar_alumno(self):
        alumno_existente = db.alumnos.buscar("Juan")
        alumno_no_existente = db.alumnos.buscar("Pedro")
        self.assertIsNotNone(alumno_existente)
        self.assertIsNone(alumno_no_existente)

    def test_crear_alumno(self):
        nuevo_alumno = db.alumnos.crear("Pedro", "Gomez", 5)
        self.assertEqual(len(db.alumnos.lista), 2)
        self.assertEqual(nuevo_alumno.nombre, "Pedro")
        self.assertEqual(nuevo_alumno.apellido, "Gomez")
        self.assertEqual(nuevo_alumno.nota, 5)

    def test_modificar_alumno(self):
        alumno_a_modificar = copy.copy(db.alumnos.buscar("Juan"))
        alumno_modificado = db.alumnos.modificar("Juan", "Gonzalez", 7)
        self.assertEqual(alumno_a_modificar.apellido, "Perez")
        self.assertEqual(alumno_modificado.apellido, "Gonzalez")

    def test_borrar_alumno(self):
        alumno_borrado = db.alumnos.borrar("Juan")
        alumno_rebuscado = db.alumnos.buscar("Juan")
        self.assertNotEqual(alumno_borrado, alumno_rebuscado)

if __name__ == "__main__":
    unittest.main()




