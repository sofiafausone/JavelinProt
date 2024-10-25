import pkmodel as pk
import numpy as np 
import numpy.testing as npt

def test_lin_gradient():
    """
    test for the lin_gradient module across different time steps

    Args
    ----
    None 
    
    Returns
    -------
    None

    """
    for X in (1, 12, 100):
        for time in (1, 3, 8, 1000):

            y = pk.lin_gradient(X, range(1,time+1))

            assert len(y) == len(range(1, time+1))
            assert round(np.sum(y)) == X
