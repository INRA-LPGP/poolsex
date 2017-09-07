import os


class Shell():

    def __init__(self, directories):
        self.directories = directories

    def mapping(self, info):
        file_name = '_'.join(['mapping', info['sex'], info['lane']]) + '.sh'
        return(os.path.join(self.directories.shell, file_name))
