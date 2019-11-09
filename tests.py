import app
import unittest


class Test(unittest.TestCase):

    def test_fun(self):
        a = app.fun(1)
        self.assertEqual(a, 11, "Should be 11")

