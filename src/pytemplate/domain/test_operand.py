import unittest
import models


class TestOperand(unittest.TestCase):
    def test_initialization(self):
        # Test the initialization of Operand
        op = models.Operand(3, 5)
        self.assertEqual(op.first_operand, 3, "First operand should be 3")
        self.assertEqual(op.second_operand, 5, "Second operand should be 5")

    def test_initialization_with_negative_values(self):
        # Test initialization with negative values
        op = models.Operand(-1, -2)
        self.assertEqual(op.first_operand, -1, "First operand should be -1")
        self.assertEqual(op.second_operand, -2, "Second operand should be -2")

    def test_initialization_with_zero(self):
        # Test initialization with zero values
        op = models.Operand(0, 0)
        self.assertEqual(op.first_operand, 0, "First operand should be 0")
        self.assertEqual(op.second_operand, 0, "Second operand should be 0")

    def test_initialization_with_large_numbers(self):
        # Test initialization with large numbers
        op = models.Operand(123456789, 987654321)
        self.assertEqual(op.first_operand, 123456789, "First operand should be 123456789")
        self.assertEqual(op.second_operand, 987654321, "Second operand should be 987654321")

if __name__ == '__main__':
    unittest.main()