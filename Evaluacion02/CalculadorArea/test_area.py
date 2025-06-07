import unittest 

def multiplicar(base , altura):
    return base * altura

class TestMultiplicar(unittest.TestCase):
    
    def test_multiplicacion_simple(self):
        self.assertEqual(multiplicar(5, 4), 20)
        self.assertEqual(multiplicar(1, 100), 100)
        self.assertEqual(multiplicar(2.5, 2), 5.0)

if __name__ == '__main__':
    unittest.main()