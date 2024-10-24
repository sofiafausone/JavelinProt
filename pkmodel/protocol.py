#from pkmodel.model import Model
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

import click
import datetime
import os


class Protocol:
    """A Pharmokinetic (PK) protocol"""

def dose(t, X):
    return X

def rhs_ib_dose(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

def rhs_s_dose(t, y, k_a, Q_p1, V_c, V_p1, CL, X):
    q_0, q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dq0_dt = dose(t,X) - k_a*q_0
    dqc_dt = k_a*q_0 - (q_c/V_c)*CL - transition
    dqp1_dt = transition
    return [dq0_dt, dqc_dt, dqp1_dt] 

def rhs(t, y, k_a, Q_p1, V_c, V_p1, CL, X, sub_bool):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqp1_dt = transition
    if sub_bool: #if subcutaneous dose
        q_0, q_c, q_p1 = y
        dq0_dt = dose(t,X) - k_a*q_0
        dqc_dt = k_a*q_0 - (q_c/V_c)*CL - transition
        return [dq0_dt, dqc_dt, dqp1_dt] 
    
    else:
        dqc_dt = dose(t, X) - q_c / V_c * CL - transition
        return [dqc_dt, dqp1_dt]

def solve(model1:Model, model2:Model):
    t_eval = np.linspace(0, 1, 1000)
    y0 = np.array([0.0, 0.0])

    fig = plt.figure()
    for model in [model1, model2]:
        args = [
            model.Q_p1, model.V_c, model.V_p1, model.CL, model.X
        ]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        plt.plot(sol.t, sol.y[0, :], label=model.name + '- q_c')
        plt.plot(sol.t, sol.y[1, :], label=model.name + '- q_p1')


path = os.getcwd()
outdir = path.split("pkmodel")[0] + "runs/"
try: os.mkdir(outdir)
except: pass

@click.command()
@click.option("--dev")
@click.option("--out", default=outdir, help="Provide an alternative output directory by specifying path from root")
@click.option("--model", default="intr", help="Choose either sub or intr for subcutaneous or intraveous respectively")
def run_protocol(dev, out, model):

    from utils import Stdout, Config

    _date = str(datetime.date.today())
    outpath = outdir + _date + str(len([name for name in os.listdir(outdir) if name.startswith(_date)]))

    stdout = Stdout(outpath)
    stdout.write(f"model = {model}")
    stdout.write(f"outpath = {outpath}")

    if dev != None:
        verbose = True

#solving just for central chamber quantity of drugs, returning quantity over time
def solve_c(model1:Model, model2:Model):
    t_eval = np.linspace(0, 1, 1000)
    y0 = np.array([0.0, 0.0])

    fig = plt.figure()
    for model in [model1, model2]:
        args = [
            model.Q_p1, model.V_c, model.V_p1, model.CL, model.X
        ]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        plt.plot(sol.t, sol.y[0, :], label=model.name + '- q_c')

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()


#solving just for peripheral chamber quantity of drugs,
def solve_p(model1:Model, model2:Model):
    t_eval = np.linspace(0, 1, 1000)
    y0 = np.array([0.0, 0.0])

    fig = plt.figure()
    for model in [model1, model2]:
        args = [
            model.Q_p1, model.V_c, model.V_p1, model.CL, model.X
        ]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        plt.plot(sol.t, sol.y[1, :], label=model.name + '- q_p1')

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()

if __name__ == "__main__":

    run_protocol()





