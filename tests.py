from app import fun
import unittest


class Test(unittest.TestCase):

    def test_fun(self):
        a = fun(1)
        self.assertEqual(a, 11, "Should be 11")

if __name__ == '__main__':
    unittest.main()
