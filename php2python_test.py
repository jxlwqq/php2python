import unittest
import php2python as p2py


class Test(unittest.TestCase):

    def test_checkdate(self):
        self.assertEquals(p2py.checkdate(12, 31, 2000), True)
        self.assertEquals(p2py.checkdate(2, 29, 2001), False)


if __name__ == '__main__':
    unittest.main()
