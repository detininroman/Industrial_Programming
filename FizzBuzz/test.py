import unittest

from fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_normal(self):
        """ Normal test.
        """
        arr, result = [1, 2, 3, 5, 15], []
        fizz_buzz(arr, result)
        self.assertEqual(result, [1, 2, 'buzz', 'fizz', 'fizzbuzz'])

    def test_big_numbers(self):
        """ Test with big numbers.
        """
        arr, result = [535555555555, 5500000000000000000000000,
                       10, 15, 35, 0, -2, -67, -55], []
        fizz_buzz(arr, result)
        self.assertEqual(result, ['fizz', 'fizz', 'fizz', 'fizzbuzz',
                                  'fizz', 'fizzbuzz', -2, -67, 'fizz'])

    def test_double(self):
        """ Test with a fractional number.
        """
        arr, result = [0.1, 0.02, 0.0003], []
        fizz_buzz(arr, result)
        self.assertEqual(result, [0.1, 0.02, 0.0003])

    def test_word(self):
        """ Test with a word.
        """
        arr, result = ['Acronis', 0, 333, 450], []
        fizz_buzz(arr, result)
        self.assertEqual(result, ['Acronis', 'fizzbuzz', 'buzz', 'fizzbuzz'])


if __name__ == '__main__':
    unittest.main()
