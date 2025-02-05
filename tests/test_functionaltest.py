import pytest
from full_model import Param, Trial


@pytest.mark.parametrize('param_name, initial_value, adjusted_value', [
    ('number_of_nurses', 3, 9),
    ('patient_inter', 2, 15),
    ('mean_n_consult_time', 30, 3),
])
def test_waiting_time_utilisation(param_name, initial_value, adjusted_value):
    """
    Test that adjusting parameters decreases the waiting time and utilisation.

    Arguments:
        param_name (string):
            Name of parameter to change in the Param() class.
        initial_value (float|int):
            Value with which we expect longer waiting times.
        adjusted_value (float|int):
            Value with which we expect shorter waiting time.
    """
    # Define helper function for the test
    def helper_param(param_name, value):
        """
        Helper function to set a specific parameter value, run the model for
        a single replication and return the results of that run.

        Arguments:
            param_name (string):
                Name of the parameter to modify.
            value (float|int):
                Value to assign to the parameter.

        Returns:
            dataframe:
                Dataframe with the trial-level results.
        """
        # Create instance of parameter class with default values but one run
        param = Param()
        param.number_of_runs = 1

        # Modify specific parameter
        setattr(param, param_name, value)

        # Run replications and return the results from the run as a series
        trial = Trial(param)
        trial.run_trial()
        return trial.df_trial_results.iloc[0]

    # Run model with initial and adjusted values
    initial_results = helper_param(param_name, initial_value)
    adjusted_results = helper_param(param_name, adjusted_value)

    # Check that nurse waiting times from adjusted model are lower
    initial_wait = initial_results["Mean Q Time Nurse"]
    adjusted_wait = adjusted_results["Mean Q Time Nurse"]
    assert initial_wait > adjusted_wait, (
        f"Changing '{param_name}' from {initial_value} to {adjusted_value} " +
        "did not decrease waiting time for the nurse as expected: observed " +
        f"waiting times of {initial_wait} and {adjusted_wait}, respectively."
    )
