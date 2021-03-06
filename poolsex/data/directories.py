import os
from poolsex.data.variables import variables

names = {
    variables.directories.genome: 'genome',
    variables.directories.qsub: 'qsub',
    variables.directories.output: 'output',
    variables.directories.reads: 'reads',
    variables.directories.results: 'results',
    variables.directories.poolsex: 'poolsex',
    variables.directories.shell: 'shell'
}


def get_directories_info(root_dir):

    '''
    Directories names are defined in this function.
    The function returns a dictionary giving the full path to each directory.
    '''

    root_dir = os.path.abspath(root_dir)

    directories = {
        variables.directories.root: root_dir,
        variables.directories.genome: os.path.join(root_dir, names[variables.directories.genome]),
        variables.directories.qsub: os.path.join(root_dir, names[variables.directories.qsub]),
        variables.directories.output: os.path.join(root_dir, names[variables.directories.qsub], names[variables.directories.output]),
        variables.directories.reads: os.path.join(root_dir, names[variables.directories.reads]),
        variables.directories.results: os.path.join(root_dir, names[variables.directories.results]),
        variables.directories.poolsex: os.path.join(root_dir, names[variables.directories.poolsex]),
        variables.directories.shell: os.path.join(root_dir, names[variables.directories.shell])
    }

    return directories
