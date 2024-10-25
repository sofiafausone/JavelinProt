'''
Central runtime protocol takes parameters either from CLI or read in .yaml from main or
from user script (if using as a package) and triggers solver function which establishes
model as class objects and uses scipy's solve function
'''


import numpy as np
import matplotlib.pyplot as plt
import scipy
from utils import Stdout, Config
import os
import datetime


def run(**kwargs):

    '''
    
    '''

    outpath = kwargs.get("outpath", "C:/JavelinProt/Runs")
    stdout = Stdout(outpath)

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
        settings = _settings
    
    stdout.write(f"Using settings:\n {settings}")

    X = settings["General"]["doseX"]

    solve(X, settings, outpath)


def solve(X, settings, outpath):

    '''
    
    '''

    import pkmodel.model as model

    stdout = Stdout(outpath)

    if isinstance(settings["Protocol"]["times"], list):
        t_eval = settings["Protocol"]["times"]
    else:
        t_eval = range(1, int(settings["Protocol"]["times"])+1)
    #t_eval = np.linspace(0, 1, 1000)
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
    
    stdout.write(f"Solution: {sol}")

    plt.plot(sol.t, sol.y[0, :], label=model.name + '- q_c')
    plt.plot(sol.t, sol.y[1, :], label=model.name + '- q_p1')