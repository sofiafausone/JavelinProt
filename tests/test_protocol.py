
#%%
import unittest
#import pkmodel as pk
import numpy as np
import numpy.testing as npt
import matplotlib.pyplot as plt



#%%

import pytest

class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        model = pk.Protocol()
        self.assertEqual(model.value, 43)


