import application
import unittest

class Test_aplication(unittest.TestCase):

	def test_sum(self):
		self.assertEqual(application.sum([5, 5]), 10)

	def test_subtraction(self):
		self.assertEqual(application.subtraction([5, 3]), 2)
		self.assertEqual(application.subtraction([1, 2]), -1)

	def test_multiplication(self):
		self.assertEqual(application.multiplication([5, 5]), 25)
		self.assertEqual(application.multiplication([7, 0]),  0)

	def test_division(self):
		self.assertEqual(application.division([9, 3]), 3)

if __name__ == '__main__':
    unittest.main()
