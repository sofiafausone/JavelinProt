#%%


import pkmodel as pk
import numpy as np
import numpy.testing as npt
import pytest



#%%
times = np.linspace(0, 1, 1000)
testing_args = {
    "model": True,  #Sets model to subcutaenous, here is a Bug
    "compartments": 2,
    "rate": 2.0,
    "doseX": 10.0,
    "scale": 0,
    "V_c": 1.0,
    "V_p1": 1.0,
    "CL": 10.0,
    "Q_p1": 2.0
}

#Attempt to to test the rhs function in Intr, result should be an array of 0s for the following parameters
@pytest.mark.parametrize(
    "test, expected",
    [
        ([times,  {"model": False, 
                   "compartments": 2,
                   "rate": 1.0,
                   "doseX": 0.0,
                   "scale": 0,
                   "V_c": 1,
                   "V_p1": 1,
                   "CL": 0.0,
                   "Q_p1": 0.0}   ], [0,0]),
    ])
def test_rhs_ib(test, expected):
    
    """Test mean function works for array of zeroes and positive integers."""
    from pkmodel.model import Intr
    #test_model = Intr(test)
    test_model = Intr([times, testing_args])
    rhs_result = Intr.rhs(test_model)
    print(rhs_result)
    check_result = rhs_result[:,:-1]
    print('check result')
    print(check_result)
    
    npt.assert_array_equal((np.array(check_result)), np.array(expected))


# %%
