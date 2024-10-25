'''

'''

import os

class Stdout:

    '''

    '''

    def __init__(self, file):

        self.file = file + "/stdout.txt"

    def write(self, msg):

        '''

        '''

        with open (self.file, 'a') as f:
            f.write(f"{msg}\n")

        print(msg)



class Config:

    '''

    '''

    def __init__(self, _id):

        self.id = _id


    def read_yaml(self, file):

        '''

        '''

        with open(file, "r") as f:

            dict = {}

            for line in f:
                if len(line.strip()) > 0:

                    line = line.split("#")[0]

                    if line.startswith(" "):
                        name, value = line.split(":")
                        name = name.strip()
                        if value in ("", " " "\t"):
                            value = None

                        if name in ("compartments", "scale"):
                            value = int(value.strip())
                        elif name in ("rate", "doseX", "V_c", "V_p1", "CL", "Q_p1"):
                            value = float(value.strip())
                        elif name in ("visualise", "verbose"):
                            value = bool(value.strip())
                        elif name == "times":
                            if "," in value:
                                value = list([int(x) for x in value.strip().split(",")])
                            else:
                                value = list(range(1, int(value.strip())))
                        else:
                            value = str(value.strip())

                        dict[section][name] = value
                
                    else:
                        section = line.strip().rstrip(":")
                        dict[section] = {}
           
                else:
                    continue

        self.dict = dict
    
        return dict