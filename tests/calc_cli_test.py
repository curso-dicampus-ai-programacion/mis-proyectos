import unittest
from calc_cli import add, subtract, multiply, divide

class TestCalculadoraCli(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)

    def test_multiplicar(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(3, 2), 1.5)

    def test_dividir_por_cero(self):
        self.assertAlmostEqual(divide(5, 0), 0)
        
if __name__ == "__main__":
    unittest.main()