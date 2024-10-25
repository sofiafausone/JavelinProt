################################################################# Example #############################################################

args = {
    "model": False, # Sets model to subcutaenous if True
    "compartments": 2,
    "rate": 1.0,
    "doseX": 1.0,
    "times": range(1, 1001),
    "scale": 0,
    "V_c": 1.0,
    "V_p1": 1.0,
    "CL": 1.0,
    "Q_p1": 1.0
}

from protocol import run

run(**args)
