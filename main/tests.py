from django.test import TestCase

class Tests(TestCase):
	def testA(self):
		self.assertEqual(2, 2)

	def testB(self):
		self.assertNotEqual(3, 5)

	def testC(self):
		self.assertTrue(True)

	def testD(self):
		self.assertFalse(False)

	def testE(self):
		self.assertIs(True, True)

	def testF(self):
		self.assertIsNot(False, True)

	def testG(self):
		self.assertIsNone(None)

	def testH(self):
		self.assertIsNotNone(True)

	def testI(self):
		self.assertIn(2, [3, 2, 5])

	def testJ(self):
		self.assertNotIn(9, [0, 10, 13, 6])