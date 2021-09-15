import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.addition(-2,3),1)
        self.assertEqual(calc.addition(1,5),6)
        self.assertEqual(calc.addition(-1,-3),-4)
        self.assertEqual(calc.addition(6,8),14)
    def test_subtract(self):
        self.assertEqual(calc.subtract(-2,3),-5)
        self.assertEqual(calc.subtract(1,5),-4)
        self.assertEqual(calc.subtract(-1,0),-1)
        self.assertEqual(calc.subtract(6,8),-2)
    def test_multiply(self):
        self.assertEqual(calc.multiply(-2,3),-6)
        self.assertEqual(calc.multiply(1,5),5)
        self.assertEqual(calc.multiply(-1,-3),3)
        self.assertEqual(calc.multiply(6,8),48)
    def test_divide(self):
        self.assertEqual(calc.divide(20,5),4)
        self.assertEqual(calc.divide(-5,-10),0.5)
        self.assertEqual(calc.divide(-1,-4),0.25)
        self.assertEqual(calc.divide(81,9),9)   

        self.assertRaises(ValueError,calc.divide,5,0)
        self.assertRaises(ValueError,calc.divide,0,0)

if __name__=='__main__':
    unittest.main()          