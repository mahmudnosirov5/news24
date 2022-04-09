from django.test import TestCase

class Tests(TestCase):
	def testA(self):
		assertEqual(2, 2)

	def testB(self):
		assertNotEqual(3, 5)

	def testC(self):
		assertTrue(True)

	def testD(self):
		assertFalse(False)

	def testE(self):
		assertIs(True, True)

	def testF(self):
		assertIsNot(False, True)

	def testG(self):
		assertIsNone(None)

	def testH(self):
		assertIsNotNone(None)

	def testI(self):
		assertIn(2, [3, 2, 5])

	def testJ(self):
		assertNotIn(9, [0, 10, 13, 6])