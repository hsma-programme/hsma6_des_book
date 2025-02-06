from pathlib import Path
import pandas as pd
from full_model import Param, Trial


def test_reproduction():
    """
    Check that results from particular run of the model match those previously
    generated using the code.
    """
    # Define model parameters
    param = Param()
    param.patient_inter = 5
    param.mean_reception_time = 2
    param.mean_n_consult_time = 6
    param.mean_d_consult_time = 20
    param.number_of_receptionists = 1
    param.number_of_nurses = 1
    param.number_of_doctors = 2
    param.prob_seeing_doctor = 0.6
    param.sim_duration = 600
    param.number_of_runs = 100

    # Run trial
    trial = Trial(param)
    trial.run_trial()

    # Compare the trial results
    exp_trial = pd.read_csv(
        Path(__file__).parent.joinpath("exp_results/trial.csv"), index_col=0)
    pd.testing.assert_frame_equal(trial.df_trial_results, exp_trial)
