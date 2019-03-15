import unittest

from multiples import multiples_of_five


class MultiplesOfFive(unittest.TestCase):
	def test_multiples_of_five(self):
		expected = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
		actual = multiples_of_five()
		self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
