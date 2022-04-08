import unittest
from fizzbuzz import fizzbuzz


class TestFizz(unittest.TestCase):
    def test_fizz(self):
        for i in [3, 6, 9, 12, 18]:
            print('testing', i)
            assert fizzbuzz(i) == 'Fizz'

    def test_buzz(self):
        for i in [5, 10, 20, 25, 35]:
            print('testing', i)
            assert fizzbuzz(i) == 'Buzz'

    def test_fizzbuzz(self):
        for i in [15, 30, 45, 60, 75, 90]:
            print('testing', i)
            assert fizzbuzz(i) == 'FizzBuzz'

    def test_fizz_numbers(self):
        for i in [1, 2, 4, 7, 8, 11, 13, 14]:
            print('testing', i)
            assert fizzbuzz(i) == i