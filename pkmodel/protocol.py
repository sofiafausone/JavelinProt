#%%

import numpy as np
import matplotlib.pyplot as plt
import scipy


def run(**kwargs):
    
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

run(**args)

# %%

