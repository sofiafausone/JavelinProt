


class Model:

    def __init__(self, ka):

        self.ka = ka


    def set_dose(self, t, X, times=(0), exponent=0):

        '''
        
        '''
        
        if exponent == 0: # flat dosing = split dose equally over time points
            return X/len(times)

        elif func == 1: # gradient dosing = incrementally increase over linear scale
            tri_func = lambda n: (n*(n+1))/2
            return (X/tri_func(np.max(times))) * times


    def int_rhs(self, t, y, Q_p1, V_c, V_p1, CL, X):
        
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = dose(t, X) - q_c / V_c * CL - transition
        dqp1_dt = transition
    
        return [dqc_dt, dqp1_dt]


    def sub_rhs(self, t, y, k_a, Q_p1, V_c, V_p1, CL, X):
        
        q_0, q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dq0_dt = dose(t,X) - k_a*q_0
        dqc_dt = k_a*q_0 - (q_c/V_c)*CL - transition
        dqp1_dt = transition
    
        return [dq0_dt, dqc_dt, dqp1_dt] 


class intr(model):

    dosing = "intr"

    def __init__(self):

        super().__init__()

        self.ib_rhs()


class subc(model):

    dosing = "subc"

    def __init__(self):

        super().__init__()

        self.sub_rhs()


#intr(t, y, ka, Q_p1, V_c, V_p1, CL, X)
#subc(t, y, ka, Q_p1, V_c, V_p1, CL, X)
