# -*- coding: utf-8 -*-
import unittest

def coba():
	try:
		import php
		return True
	except BaseException as e:
		print("ERROR:", e)
		return False

class DummyTest(unittest.TestCase):
	def test_ok(self):
		self.assertTrue(coba())

if __name__ == '__main__':
    unittest.main()