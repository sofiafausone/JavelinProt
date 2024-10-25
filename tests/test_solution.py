#%%


import pkmodel as pk
import numpy as np
import numpy.testing as npt
import pytest



#%%
#THIS IS AN EXAMPLE OF A UNIT TEST
@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))
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

#SOFIA: trying to test the rhs function in Intr 
@pytest.mark.parametrize(
    "test, expected",
    [
        ([times,  {"model": False, 
                   "compartments": 2,
                   "rate": 2.0,
                   "doseX": 10.0,
                   "scale": 0,
                   "V_c": 1.0,
                   "V_p1": 1.0,
                   "CL": 10.0,
                   "Q_p1": 2.0}           ]),
        ([]),
    ])
def test_rhs_ib(test, expected):
    
    """Test mean function works for array of zeroes and positive integers."""
    from pkmodel.Model2 import Intr
    test_model = Intr(test)
    rhs_result = Intr.rhs(test_model)
    
    npt.assert_array_equal((np.array(rhs_result)), np.array(expected))



class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        model = pk.Solution()
        self.assertEqual(model.value, 44)


# %%
