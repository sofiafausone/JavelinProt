'''

'''


class Stdout:

    '''

    '''

    def __init__(file):

        self.file = file

    def write(msg):

        '''

        '''

        with open (self.file, 'a') as f:
            f.write(msg)

        print(msg)



