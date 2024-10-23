'''

'''


class Stdout:

    '''

    '''

    def __init__(fself, ile):

        self.file = file

    def write(self, msg):

        '''

        '''

        with open (self.file, 'a') as f:
            f.write(msg)

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
                        name, value = line.split(": ")
                        if value in ("", " " "\t"):
                            value = None
                        dict[section][name] = value
                
                    else:
                        section = line.strip().rstrip(":")
           
                else:
                    continue

    self.dict = dict
    
    return dict