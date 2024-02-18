#!/usr/bin/env python3
import unittest


def coba():
    try:
        return True
    except BaseException as e:
        print("ERROR:", e)
        return False


class DummyTest(unittest.TestCase):
    def test_ok(self):
        self.assertTrue(coba())


if __name__ == "__main__":
    unittest.main()
