#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, name,Q_p1, V_c, V_p1, CL, X, sub_bool):
        self.name = name
        self.Q_p1 =Q_p1
        self.V_c =V_c
        self.V_p1 = V_p1
        self.CL = CL
        self.X=X
        self.sub_bool = sub_bool

    def dose(self, t, X):
        return X

    def rhs(self, t, y, k_a, Q_p1, V_c, V_p1, CL, X, sub_bool):

        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqp1_dt = transition

        if sub_bool: #if subcutaneous dose
            q_0, q_c, q_p1 = y
            dq0_dt = self.dose(t,X) - k_a*q_0
            dqc_dt = k_a*q_0 - (q_c/V_c)*CL - transition
            return [dq0_dt, dqc_dt, dqp1_dt] 
        
        else:
            dqc_dt = self.dose(t, X) - q_c / V_c * CL - transition
            return [dqc_dt, dqp1_dt]


