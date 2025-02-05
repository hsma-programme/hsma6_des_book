import pytest
from full_model import Param, Trial


@pytest.mark.parametrize("param_name, value", [
    ("sim_duration", 0),
    ("patient_inter", 0)
])
@pytest.mark.timeout(3)
def test_zero_inputs(param_name, value):
    """
    Check that the model fails when inputs that are zero are used.

    Arguments:
        param_name (string):
            Name of parameter to change in the Param() class.
        value (float|int):
            Invalid value for parameter.
    """
    # Create parameter class with an invalid value
    param = Param()
    setattr(param, param_name, value)

    # Verify that initialising the model raises an error
    with pytest.raises(ValueError):
        Trial(param).run_trial()
