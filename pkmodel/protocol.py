#%%

import numpy as np
import matplotlib.pyplot as plt
import scipy


def run(**kwargs):
    """
    Executes the pharmacokinetic (PK) model configuration using parameters from a YAML file or default values.

    Args
    ----
    kwargs : dict, optional
        Keyword arguments for PK model configuration:
            - model (bool): Determines the type of model; `False` indicates a default subcutaneous model.
            - compartments (int): Number of compartments in the model (default is 2).
            - rate (float): Rate parameter for the model (default is 1.0).
            - doseX (float): Initial dose (default is 1.0).
            - times (array-like, optional): Time intervals for simulation (default is `np.linspace(0, 1, 1000)`).
            - scale (int): Scaling factor for the model (default is 0).
            - V_c (float): Volume of the central compartment (default is 1.0).
            - V_p1 (float): Volume of the peripheral compartment (default is 1.0).
            - CL (float): Clearance rate from the central compartment (default is 1.0).
            - Q_p1 (float): Inter-compartmental clearance rate (default is 1.0).

    Returns
    -------
    None

    """
    
    _settings = kwargs.get("settings", None)
    if _settings in ({}, None, ""):
        settings = {"General":{},"Protocol":{},"Output":{},"Parameters":{}}

        for x in kwargs:
            if x in ("model", "compartments", "rate", "doseX"):
                settings["General"][x] = args[x]
            elif x in ("times", "scale"):
                settings["Protocol"][x] = args[x]
            elif x in ("V_c", "V_p1", "CL", "Q_p1"):
                settings["Parameters"][x] = args[x]
            else:
                raise Exception(f"Arg not in settings {args[x]}")
    else:
        settings = args
    
    X = settings["General"]["doseX"]

    solve(X, settings)


def solve(X, settings):
    """
    Solves the pharmacokinetic (PK) model differential equations and plots the results.

    Args
    ----
    X : float
        Initial dose of the drug for the simulation.
    settings : dict
        Dictionary containing model configuration and parameters, organized as:
            - General: Model type and general settings, including:
                - model (bool): Specifies if the subcutaneous model (`True`) or intravenous model (`False`) is used.
            - Protocol: Protocol settings for simulation, e.g., time intervals.
            - Parameters: Model parameters including:
                - V_c (float): Volume of the central compartment.
                - V_p1 (float): Volume of the peripheral compartment.
                - CL (float): Clearance rate from the central compartment.
                - Q_p1 (float): Inter-compartmental clearance rate.

    Returns
    -------
    None

    """

    import pkmodel.model as model

    t_eval = np.linspace(0, 1, 1000)
    y0 = np.array([0.0, 0.0])

    sub_bool = bool(settings["General"]["model"])

    fig = plt.figure()
    if sub_bool == True:
        model = model.Subc(t_eval, settings)
    else:
        model = model.Intr(t_eval, settings)

    args = [
        model.Q_p1, model.V_c, model.V_p1, model.CL, X
    ]
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: model.rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
    )
    print(sol)
    plt.plot(sol.t, sol.y[0, :], label=model.name + '- q_c')
    plt.plot(sol.t, sol.y[1, :], label=model.name + '- q_p1')
    plt.show()


args = {
    "model": False,  #Sets model to subcutaenous, here is a Bug
    "compartments": 2,
    "rate": 1.0,
    "doseX": 1.0,
    #"times": np.linspace(0, 1, 1000),
    "scale": 0,
    "V_c": 1.0,
    "V_p1": 1.0,
    "CL": 1.0,
    "Q_p1": 1.0
}

#run(**args)

# %%

