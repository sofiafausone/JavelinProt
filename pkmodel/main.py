import click
import datetime
import os

path = os.getcwd()
outdir = path.split("pkmodel")[0] + "runs/"
try: os.mkdir(outdir)
except: pass

@click.command()
@click.option("--dev")
@click.option("--out", default=outdir, help="Provide an alternative output directory by specifying path from root")
@click.option("--dose", default="intr", help="Choose either sub or intr for subcutaneous or intraveous respectively")
@click.option("--rate", "-k", default=1, help="Set the absorption rate (Ka)")








def run_protocol(dev, out, dose, rate):

    from utils import Stdout, Config

    _date = str(datetime.date.today())
    outpath = outdir + _date + str(len([name for name in os.listdir(outdir) if name.startswith(_date)]))
    try: os.mkdir(outpath)
    except: pass

    stdout = Stdout(outpath)
    stdout.write(f"dosing = {dose}")
    stdout.write(f"outpath = {outpath}")
    stdout.write(f"absorption rate = {rate}")

    if dev != None:
        verbose = True


if __name__ == "__main__":

    run_protocol()