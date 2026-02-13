#!/usr/bin/env python3

import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import (
    add, subtract, multiply, divide,
    modulus, power, handle_operation
)

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

    def test_dividir_correctamente(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(3, 2), 1.5)

    @patch("builtins.print")
    def test_dividir_por_cero(self, mock_print):
        result = divide(5, 0)

        self.assertIsNone(result)
        mock_print.assert_called_once_with("No se puede dividir entre 0.\n")

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(4, 2), 0)
        self.assertEqual(modulus(-5, 3), -5 % 3)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)

    def test_handle_operation_sumar(self):
        self.assertEqual(handle_operation(1, 2, 3), 5)

    def test_handle_operation_restar(self):
        self.assertEqual(handle_operation(2, 5, 3), 2)

    def test_handle_operation_multiplicar(self):
        self.assertEqual(handle_operation(3, 4, 3), 12)

    def test_handle_operation_dividir(self):
        self.assertEqual(handle_operation(4, 10, 2), 5)

    def test_handle_operation_modulus(self):
        self.assertEqual(handle_operation(5, 10, 3), 1)

    def test_handle_operation_power(self):
        self.assertEqual(handle_operation(6, 2, 3), 8)

    def test_handle_operation_opcion_invalida(self):
        self.assertEqual(handle_operation(99, 2, 3), 0)

if __name__ == "__main__":
    unittest.main()
