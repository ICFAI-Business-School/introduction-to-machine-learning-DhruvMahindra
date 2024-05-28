import unittest
import regression

class TestRegression(unittest.TestCase):
    def test_model(self):
        # Ensure the regression script has a trained model and calculates MSE
        self.assertTrue(hasattr(regression, 'b0'), "The intercept (b0) is not defined in the script")
        self.assertTrue(hasattr(regression, 'b1'), "The slope (b1) is not defined in the script")
        self.assertTrue(hasattr(regression, 'mse'), "The mean squared error (mse) is not defined in the script")
        self.assertLess(regression.mse, 100, "The mean squared error is too high")

if __name__ == '__main__':
    unittest.main()
