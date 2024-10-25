'''

'''


import click
import datetime
import os
from utils import Stdout, Config

@click.command()
@click.option("--dev", default=None)
@click.option("--out", "-o", default=None, help="Provide an alternative output directory by specifying path from root")
@click.option("--model", "-m", default=None, help="Choose either sub or intr for subcutaneous or intraveous respectively")
@click.option("--rate", "-k", default=None, help="Set the absorption rate (Ka)")
@click.option("--num", "-n", default=2, help="Number of compartments to model")
@click.option("--yaml", default=None, help="Set alternative yaml config path")
def run_protocol(dev, out, model, rate, num, yaml):

    '''
    
    '''

    params = {"model":model, "rate":rate, "compartments":num} # set dictionary of click command arguments to later override .yaml config file parameters

    # establish file output directory
    _date = str(datetime.date.today())
    if out in (None, "", " "): # default is /runs in repo directory
        outdir = os.getcwd().split("pkmodel")[0] + "runs/"
        try: os.mkdir(outdir)
        except: pass

        outpath = outdir + _date + str(len([name for name in os.listdir(outdir) if name.startswith(_date)]))
    else: # can be overriden by click command argument
        outpath = out + _date + str(len([name for name in os.listdir(outdir) if name.startswith(_date)]))
    
    try: os.mkdir(outpath)
    except: pass

    # establish the .yaml config file path
    if yaml not in (None, "", " "):
        yaml_path = yaml
    else: yaml_path = os.getcwd().split("pkmodel")[0] + "config.yaml"
    if yaml_path in (None, "" " "):
        yaml_path = cdir + "config.yaml"
    else: yaml_path = yaml_path

    # read the yaml config file as a nested dictionary
    _settings = Config("c1").read_yaml(yaml_path)
    
    # .yaml config settings are overriden by the click command line arguments
    for p in params:
        if p not in (None, "", " "):
            _settings["General"][p] = params[p]

    #if dev != None:
    #    verbose = True

    if click.confirm("Would you like to enter model parameters?\n Note if No then will read from config.yaml"):
        click.prompt("Central compartment volume (V_c)", default=1.0)
        click.prompt("Peripheral compartment volume (V_p1)", default=1.0)
        click.prompt("Clearance/elimination rate from central compartment (CL))", default=1.0)
        click.prompt("Transition rate between comparments (Q_p1)", default=1.0)

    from protocol import run

    run(settings=_settings, outpath=outpath)


if __name__ == "__main__":

    run_protocol()