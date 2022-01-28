
__author__ = "Teagan Nicholas Doyle"
__version__ = "0.1.0"
__license__ = "The Unlicense"

import sys
import pkg_resources

from subprocess import call

def main():
    '''Perfoms a check for OS and then executes the upgrades'''
    os = sys.platform

    try:
        if os == "win32":
            packages = [dist.project_name for dist in pkg_resources.working_set]
            call("pip install --upgrade " + ' '.join(packages), shell=True)
        elif os == "darwin":
            packages = [dist.project_name for dist in pkg_resources.working_set]
            call("pip3 install --upgrade " + ' '.join(packages), shell=True)
        else:
            print("Operating System not supported.")
    except:
        print("Something went wrong...")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()