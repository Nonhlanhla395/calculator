import unittest
from loan import loan

class TestLoanFunctions(unittest.TestCase):
    def setUp(self):
        """Initialize the Loan object with an amount of 4000 and term of 3 years."""
        self.loan = loan(4000, 3)

    def test_compound_interest(self):
        """Test the compound interest calculation."""
        self.loan.calculate_compound_interest(30)  # 30% interest rate
        # Compute expected interest manually or using a trusted calculator
        expected_interest = 4000 * ((1 + 0.30) ** 3 - 1)  # Compound interest formula
        self.assertAlmostEqual(self.loan.interest, expected_interest, places=2)
        self.assertAlmostEqual(self.loan.total, 4000 + expected_interest, places=2)
        self.assertEqual(self.loan.loan_type, 'Compound interest')

    def test_simple_interest(self):
        """Test the simple interest calculation."""
        self.loan.calculate_simple_interest(50)  # 50% interest rate
        expected_interest = 4000 * 0.50 * 3  # Simple interest formula
        self.assertAlmostEqual(self.loan.interest, expected_interest, places=2)
        self.assertAlmostEqual(self.loan.total, 4000 + expected_interest, places=2)
        self.assertEqual(self.loan.loan_type, 'Simple interest')

if __name__ == '__main__':
    unittest.main()