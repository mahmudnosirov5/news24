from django.test import TestCase

class Tests(TestCase):
	def test1(self):
		self.assertFalse(True)

	def test5(self):
		self.assertFalse(False)

	def test10(self):
		self.assertEqual(5 == 5)