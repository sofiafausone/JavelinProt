import pytest
import os
import utils

def test_read_yaml():

    '''
    
    '''

    path = os.getcwd()
    file = path.split("pkmodel")[0] + "config.yaml"

    settings = utils.Config("test1").read_yaml(file)

    assert isinstance(settings, dict)
    
    for x in settings:
        assert instance(settings[x], dict)
        assert all([isinstance(y, str) for y in list(settings[x].values())]) == True


path = os.getcwd()
file = path.split("pkmodel")[0] + "config.yaml"

settings = utils.Config("c1").read_yaml(file)
print(settings)
