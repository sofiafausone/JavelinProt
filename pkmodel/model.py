import numpy as np  

class Model:

    def __init__(self, times, settings):

        self.ka = settings["General"]["rate"]
        self.times = times
        self.exponent = settings["Protocol"]["scale"]

        self.V_c, self.V_p1, self.CL, self.Q_p1 = list(settings["Parameters"].values())

    def set_dose(self, t, X, times=(0), exponent=0):

        '''
        
        '''
        
        if exponent == 0: # flat dosing = split dose equally over time points
            return X/len(times)

        elif exponent == 1: # gradient dosing = incrementally increase over linear scale
            return lin_gradient(X, times)[int(t)]

    def int_rhs(self, t, y, Q_p1, V_c, V_p1, CL, X):
        
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = self.dose(t, X, self.times, self.exponent) - q_c / V_c * CL - transition
        dqp1_dt = transition
    
        return [dqc_dt, dqp1_dt]


def lin_gradient(X, times):

    tri_func = lambda n: (n*(n+1))/2
    values = (X/tri_func(np.max(times))) * np.float64(times)

    return values


class Intr(Model):

    name = "intreveneous"
    
    def __init__(self, times, settings):

        super().__init__(times, settings)
    

    def rhs(self, t, y, Q_p1, V_c, V_p1, CL, X):
        
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = self.set_dose(t, X, self.times, self.exponent) - q_c / V_c * CL - transition
        dqp1_dt = transition
    
        return [dqc_dt, dqp1_dt]


class Subc(Model):

    name = "subcutaneous"

    def __init__(self, times, settings):

        super().__init__(times, settings)


    def rhs(self, t, y, k_a, Q_p1, V_c, V_p1, CL, X):
        
        q_0, q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dq0_dt = self.set_dose(t,X) - k_a*q_0
        dqc_dt = k_a*q_0 - (q_c/V_c)*CL - transition
        dqp1_dt = transition
    
        return [dq0_dt, dqc_dt, dqp1_dt]