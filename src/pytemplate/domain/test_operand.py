from models import Operands


def test_initialization():
    # Test the initialization of Operands
    op = Operands(3, 5)
    assert op.first_operand == 3
    assert op.second_operand == 5


def test_initialization_with_negative_values():
    # Test initialization with negative values
    op = Operands(-1, -2)
    assert op.first_operand == -1
    assert op.second_operand == -2


def test_initialization_with_zero():
    # Test initialization with zero values
    op = Operands(0, 0)
    assert op.first_operand == 0
    assert op.second_operand == 0


def test_initialization_with_large_numbers():
    # Test initialization with large numbers
    op = Operands(123456789, 987654321)
    assert op.first_operand == 123456789
    assert op.second_operand == 987654321
