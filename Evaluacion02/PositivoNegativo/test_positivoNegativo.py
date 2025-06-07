import unittest
from verificador_numeros import verificar_numeros

class TestVerificarNumeros(unittest.TestCase):

    def test_numero_positivo(self):
        self.assertEqual(verificar_numeros(10), "positivo")
        self.assertEqual(verificar_numeros(1), "positivo")

    def test_numero_negativo(self):
        self.assertEqual(verificar_numeros(-5), "negativo")
        self.assertEqual(verificar_numeros(-100), "negativo")

    def test_numero_cero(self):
        self.assertEqual(verificar_numeros(0), "cero")

if __name__ == '__main__':
    unittest.main()
