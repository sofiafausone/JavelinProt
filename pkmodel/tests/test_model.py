import unittest
import pkmodel as pk
import numpy as np 
import numpy.testing as npt



class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        model = pk.Model()
        self.assertEqual(model.value, 42)


