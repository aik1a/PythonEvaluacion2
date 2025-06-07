import unittest
from validarRut import validar_rut

class TestValidadorRut(unittest.TestCase):

    def test_rut_valido(self):
        #Prueba con RUT correcto de 8 numeros
        self.assertTrue(validar_rut("12345678"))
        self.assertTrue(validar_rut("87654321"))
#Rut muy corto
    def test_rut_muy_corto(self):
        self.assertFalse(validar_rut("1234567"))
#Rut Largo
    def test_rut_muy_largo(self):
        self.assertFalse(validar_rut("123456789"))
#Letra incorrecta
    def test_rut_con_letras(self):
        self.assertFalse(validar_rut("1234567a"))
#Simbolos o espacios
    def test_rut_con_simbolos(self):
        self.assertFalse(validar_rut("12345-67"))
        self.assertFalse(validar_rut("1234 5678"))
#Sin ingresar
    def test_rut_vacio(self):
        self.assertFalse(validar_rut(""))


if __name__ == '__main__':
    unittest.main()