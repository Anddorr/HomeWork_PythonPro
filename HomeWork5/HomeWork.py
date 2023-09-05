import unittest
import typing

def addition(num1: int, num2: int) -> int:
        return num1 + num2

def is_simple_number(num: int) -> int:
        return num

def is_int(x) -> bool:
        if type(x) == int:
            return True
        else:
            return False

def is_smth_in_list(my_list: typing.List) -> None | typing.List:
        if my_list is []:
            return None
        else:
            return my_list




class TestFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(5, 7), 12, 'Mistake')
        self.assertNotEquals(addition(6, 3), 8, 'Mistake')

    def test_is_simple_number(self):
        self.assertIn(is_simple_number(5), [2, 3, 5, 7, 11, 13, 17, 19], 'Mistake')
        self.assertNotIn(is_simple_number(1), [2, 3, 5, 7, 11, 13, 17, 19], 'Mistake')

    def test_is_int(self):
        self.assertTrue(is_int(5), 'Mistake')
        self.assertFalse(is_int('hello'), 'Mistake')

    def test_is_smth_in_list(self):
        self.assertIsNone(is_smth_in_list([]), 'Mistake')
        self.assertIsNotNone(is_smth_in_list([1, 2, 3, 'smth', {'int': 7}]), 'Mistake')
