__author__ = ("Georgios-Ioannis Brokos, "
              "Natural Language Processing Group, "
              "Department of Informatics, "
              "Athens University of Economics and Business, Greece.")
__copyright__ = "Copyright (c) 2016, " + __author__
__license__ = "3-clause BSD"
__email__ = "g.brokos@gmail.com"

import sys

def progress(i, total, suffix):
    sys.stdout.write('Progress: %d/%d %s completed.\r' % (i, total, suffix))
    sys.stdout.flush()