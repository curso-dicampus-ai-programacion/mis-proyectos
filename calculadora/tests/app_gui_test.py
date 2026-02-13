#!/usr/bin/env python3

import os
import sys
import unittest

from app_gui import (
        press_number, press_operation, press_equal, clear,
                      backspace, format_result
)

class DummyEntry:
    def __init__(self):
        self.text = ""
    def delete(self, start, end):
        self.text = ""
    def insert(self, index, value):
        self.text = value
    def get(self):
        return self.text

import calc_gui
calc_gui.display = DummyEntry()

class TestCalculadoraGui(unittest.TestCase):

    def setUp(self):
        clear()  # Resetea la calculadora antes de cada test

    def test_pulsar_numeros(self):
        press_number('1')
        press_number('2')
        self.assertEqual(calc_gui.display.get(), '12')

    def test_operacion_suma(self):
        press_number('5')
        press_operation('+')
        press_number('3')
        press_equal()
        self.assertEqual(calc_gui.display.get(), '8')

    def test_division_por_cero(self):
        press_number('5')
        press_operation('/')
        press_number('0')
        press_equal()
        self.assertEqual(calc_gui.display.get(), 'Error')

    def test_backspace(self):
        press_number('9')
        press_number('8')
        backspace()
        self.assertEqual(calc_gui.display.get(), '9')

if __name__ == "__main__":
    unittest.main()
