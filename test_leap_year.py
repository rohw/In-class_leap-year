import unittest
import leap_year


class SimpleTest(unittest.TestCase):
    def test_leap_year1(self):
        self.assertEqual(leap_year.ly(231), "It is not a leap year")

    def test_leap_year2(self):
        self.assertEqual(leap_year.ly(444), "It is a leap year")

    def test_leap_year3(self):
        self.assertEqual(leap_year.ly(800), "It is a leap year")

    def test_leap_year4(self):
        self.assertEqual(leap_year.ly(700), "It is not a leap year")

    def test_leap_year5(self):
        self.assertEqual(leap_year.ly("hi"), "Input is not integer")


if __name__ == '__main__':
    unittest.main()
