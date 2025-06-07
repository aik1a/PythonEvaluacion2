import unittest
from calcularPares import calcular_pares

class TestPares(unittest.TestCase):

    def test_rango_normal(self):
        """Prueba un rango estándar de 1 a 10."""
        # Los pares son 2, 4, 6, 8, 10 -> 5 números
        self.assertEqual(calcular_pares(1, 10), 5)

    def test_rango_solo_impares(self):
        """Prueba un rango que no contiene números pares."""
        # No hay pares entre 3 y 5 si los límites son impares y el rango es corto
        self.assertEqual(calcular_pares(3, 4), 1) # El único par es 4
        self.assertEqual(calcular_pares(3, 3), 0)

    def test_rango_con_negativos(self):
        """Prueba un rango que incluye números negativos y el cero."""
        # Los pares son -4, -2, 0, 2 -> 4 números
        self.assertEqual(calcular_pares(-4, 3), 4)

    def test_rango_invertido(self):
        """Prueba un rango donde el inicio es mayor que el fin."""
        # El bucle no debería ejecutarse, el conteo debe ser 0.
        self.assertEqual(calcular_pares(10, 1), 0)

    def test_limites_iguales(self):
        """Prueba un rango donde los límites son el mismo número."""
        self.assertEqual(calcular_pares(8, 8), 1) # El 8 es par
        self.assertEqual(calcular_pares(7, 7), 0) # El 7 es impar

if __name__ == '__main__':
    unittest.main()