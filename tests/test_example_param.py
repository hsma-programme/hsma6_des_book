import pytest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_positive_param(number):
    """
    Confirm that the number is positive.

    Arguments:
        number (float):
            Number to check.
    """
    assert number > 0, f"The number {number} is not positive."
