#
# Protocol class
#

import click
import datetime

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=43):
        self.value = value


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

    
    





