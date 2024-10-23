from model import Model
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

<<<<<<< HEAD
import click
import datetime

class Protocol:
    """A Pharmokinetic (PK) protocol
=======
def dose(t, X):
    return X
>>>>>>> origin/dev

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
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

<<<<<<< HEAD

path = os.getcwd()
outdir = path.split("pkmodel")[0] + "/runs"
try: os.mkdir(outdir)

@click.command()
@click.option("--dev")
@click.option("--out", default=outdir, help="Provide an alternative output directory by specifying path from root")
@click.option("--model", default="intr", help="Choose either sub or intr for subcutaneous or intraveous respectively")
def run_protocol(dev, out, model):

    from pkmodel.utils import Stdout, Config

    _date = datetime.date.today()
    outpath = outdir + _date + len([name for name in os.listdir(outdir) if name.startswith(_date)])

    stdout = Stdout(outpath)
    stdout.write("hello world")

    if dev != None:
        verbose = True

    
    





=======
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()

if __name__ == "__main__":
    model1 =  Model('model1', 1.0, 1.0, 1.0, 1.0, 1.0,)
    model2 =  Model('model2', 2.0, 1.0, 1.0, 1.0, 1.0,)

    solve(model1=model1,model2=model2)
>>>>>>> origin/dev
