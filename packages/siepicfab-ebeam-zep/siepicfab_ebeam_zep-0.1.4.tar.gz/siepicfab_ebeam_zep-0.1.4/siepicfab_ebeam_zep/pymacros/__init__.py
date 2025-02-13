# $autorun

version = "0.1.4"

print('SiEPICfab-EBeam-ZEP Python module: pymacros, v%s' % version)

import pya
from SiEPIC.scripts import load_klayout_library

verbose=False

tech='SiEPICfab_EBeam_ZEP'

# Load the library
load_klayout_library(tech, 'SiEPICfab_EBeam_ZEP', "v%s, Components with models" % version, 
    'pymacros/SiEPICfab_EBeam_ZEP_fixed','pymacros/SiEPICfab_EBeam_ZEP_pcells', 
    verbose=verbose)
load_klayout_library(tech, 'SiEPICfab_EBeam_ZEP_Beta', "v%s, Beta components" % version, 
    'pymacros/SiEPICfab_EBeam_ZEP_beta_fixed','pymacros/SiEPICfab_EBeam_ZEP_beta_pcells', 
    verbose=verbose)


# Load OPICS simulation library
# import sys, os
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# import opics_ebeam

