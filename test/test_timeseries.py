# load library
import os
import physicellloader
from physicellloader import pyMCDS_timeseries

# load physicell timeseries data
mcds = pyMCDS_timeseries('/'.join([os.path.dirname(os.path.realpath(physicellloader.__file__)), 'timeseries_set']))

# command to extract basic timeseries information
mcds.get_times()

# howto extract data form a single timepoint
# check out test_single.py for more details
mcd1 = mcds.timeseries[0]
print(mcd1.get_time())
print(mcds.timeseries[0].get_time())

# plotting commands
chem_list = mcds.timeseries[0].get_substrate_names()
mcds.plot_menv_total(chem_list)
mcds.plot_cell_type_counts()