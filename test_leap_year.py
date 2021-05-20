import unittest
import leap_year


class SimpleTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(leap_year.ly(231), "It is not a leap year")
