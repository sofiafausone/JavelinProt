import unittest
#import pkmodel as pk
import numpy as np 
import numpy.testing as npt



#class ModelTest(unittest.TestCase):
#    """
#    Tests the :class:`Model` class.
#    """
#    def test_create(self):
#        """
#
#         Tests Model creation.
#        """
#        model = pk.Model()
#        self.assertEqual(model.value, 42)


def test_lin_gradient():

    #from Model2 import lin_gradient
    for X in (1, 12, 100):
        for time in (1, 3, 8, 1000):

            y = lin_gradient(X, range(1, time+1))

            assert len(y) == len(range(1, time+1))
            assert round(np.sum(y)) == X

