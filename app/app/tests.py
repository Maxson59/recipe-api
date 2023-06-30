from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(4, 5)

        self.assertEqual(res, 9)

    def test_subtract_numbers(self):
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
