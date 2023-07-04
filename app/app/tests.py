"""
Sample test file
"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """
    Sample test class
    """
    def test_add_numbers(self):
        res=calc.add(3,8)
        self.assertEqual(res,11)

    def test_sub_numbers(self):
        res=calc.sub(3,8)
        self.assertEqual(res,5)
