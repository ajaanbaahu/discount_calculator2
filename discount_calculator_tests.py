import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
    def test_ten_percent_discount(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,10,'percent')
        self.assertEqual(10.0, result)

    def fifteen_percent_discount_test(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,15,'percent')
        self.assertEqual(15.0, result)

    def five_off_discount_test(self):

        discount_calculator=DiscountCalculator()
        result=discount_calculator.calculate(250,5,'absolute')
        self.assertEqual(5,result)

    def type_error_test(self):

        discount_calc=DiscountCalculator()

        self.assertRaises(ValueError,discount_calc.calculate,250,5,'random')

    def floating_point_percent_test(self):

        discount_calculator=DiscountCalculator()
        result=discount_calculator.calculate(100.0,10.0, 'percent')
        self.assertEqual(10.0,result)


    def floating_point_absolute_test(self):

        discount_calculator=DiscountCalculator()

        result=discount_calculator.calculate(250.0,5.0,'absolute')

        self.assertEqual(6.0,result)

    def excess_discount_test(self):

        discount_calculator=DiscountCalculator()
        #result=discount_calculator.calculate(100.0,110.0, 'percent')

        self.assertRaises(ValueError,discount_calculator.calculate,250,100,'percent')


