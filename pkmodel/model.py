'''
Model Module
------------

This module holds class definitions for model objects which contain the differential
equations and associated parameters for our pharmokinetic model for either the intraveneous
or subcutaneous model.
'''

import numpy as np  

class Model:
    
    '''
    This class acts as a parent class for the mathematical model by carrying the parameters
    (settings) required and holding the dosing function set_dose() which provides utility
    for alternative dosing strategies.

    Args
    ----
    times: (1d array) of dosing time intervals - should be a numpy linspace of any length
           in intervals of 1 
    settings: (nested dictionary) of settings as set in a script (if importing as a package),
              or given by the CLI or .yaml config file. Seperated into named sections which are
              the keys of the document with sub dictionaries as the values where each key:pair
              is a setting variable and it's associated value
    '''

    def __init__(self, times, settings):

        # set as attributes for reference by external functions
        self.ka = settings["General"]["rate"]
        self.times = times
        self.exponent = settings["Protocol"]["scale"]

        self.V_c, self.V_p1, self.CL, self.Q_p1 = list(settings["Parameters"].values())

    def set_dose(self, t, X, times=[0], exponent=0):

        '''
        Simple dosing function provides functionality for alternative dosing strategies. Given
        a quantity of drug to dose (X) this functions allows the user to split it over a number
        of time points in both a flat distribution but also a linearly increasing quantity by
        specifying an exponent.

        Args
        ----
        t: (int) the current time step
        X: (float) initial quantity of drug being administered
        times: (1d array) of dose time intervals
        exponent: (int) determines whether to use a flat dosage distribution or a linear gradient increase

        Returns
        -------
        (float) dosage value for given time point
        '''
        
        if exponent == 0: # flat dosing = split dose equally over time points
            return X/len(times)

        elif exponent == 1: # gradient dosing = incrementally increase over linear scale
            return lin_gradient(X, times)[int(t)]


def lin_gradient(X, times):

    '''
    External function called by the Model Class's set_dose() func which returns a set of values
    for a given dose quantity over a number of ime intervals which increases in a linear fashion
    with each time point.

    Args
    ----
    X: (float) initial quantity of drug being administered
    times: (1d array) of dose time intervals

    Returns
    -------
    values: (1d array) of gradient adjusted values for each time interval
    '''

    tri_func = lambda n: (n*(n+1))/2
    values = (X/tri_func(np.max(times))) * np.float64(times)

    return values


class Intr(Model):

    '''
    Intraveneous model child class that inherits from the Model parent class. Holds a specific rhs 
    equation function that is different to the Subcutaneous model.

    Args
    ----
    Model: (class) parent class to inherit from
    '''

    name = "intreveneous"
    
    def __init__(self, times, settings):

        super().__init__(times, settings)
    

    def rhs(self, t, y, Q_p1, V_c, V_p1, CL, X):

        '''
        
        '''
        
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = self.set_dose(t, X, self.times, self.exponent) - q_c / V_c * CL - transition
        dqp1_dt = transition
    
        return [dqc_dt, dqp1_dt]


class Subc(Model):

    '''
    Intraveneous model child class that inherits from the Model parent class. Holds a specific rhs 
    equation function that is different to the Subcutaneous model.

    Args
    ----
    Model: (class) parent class to inherit from
    '''

    name = "subcutaneous"

    def __init__(self, times, settings):

        super().__init__(times, settings)


    def rhs(self, t, y, k_a, Q_p1, V_c, V_p1, CL, X):

        '''
        
        '''
        
        q_0, q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dq0_dt = self.set_dose(t,X) - k_a*q_0
        dqc_dt = k_a*q_0 - (q_c/V_c)*CL - transition
        dqp1_dt = transition
    
        return [dq0_dt, dqc_dt, dqp1_dt]