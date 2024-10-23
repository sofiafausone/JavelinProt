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
    def __init__(self, name,Q_p1, V_c, V_p1, CL, X):
        self.name = name
        self.Q_p1 =Q_p1
        self.V_c =V_c
        self.V_p1 = V_p1
        self.CL = CL
        self.X=X




