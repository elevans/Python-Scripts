### Use Python 2.7###
#####################

import matplotlib
matplotlib.use('Agg')

import FlowCytometryTools

from FlowCytometryTools import test_data_dir, test_data_file
from FlowCytometryTools import FCMeasurement
from FlowCytometryTools import ThresholdGate, PolyGate
from pylab import *

# Note that the names here are hard coded because I know what the output names are.
# These can be changed to user inputed names easily if necessary.
def generate_plots(filename):
    figure(figsize=(10,10))
    sample.plot(['FSC-A', 'SSC-A'], cmap=cm.Blues, colorbar=True)
    plt.savefig('FSC-A_SSC-A_' + filename)
    plt.clf()
    sample.plot(['FSC-A', 'FSC-H'], cmap=cm.Blues, colorbar=True)
    plt.savefig('FSC-A_FSC-H_' + filename)
    plt.clf()
    sample.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.savefig('PI-W_PI-A_' + filename)
    plt.clf()
    sample.plot(['FSC-A', 'SSC-A'], gates=[live_dead_polygate], cmap=cm.Blues, colorbar=True)
    plt.savefig('FSC-A_SSC-A_polygate_' + filename)
    plt.clf()
    live_dead_gated_sample.plot(['FSC-A', 'SSC-A'], cmap=cm.Blues, colorbar=True)
    plt.savefig('Live_cells_' + filename)
    plt.clf()
    live_dead_gated_sample.plot(['FSC-A','FSC-H'], gates=[singles_polygate], cmap=cm.Blues, colorbar=True)
    plt.savefig('Single_cells_' + filename)
    plt.clf()

# datadir points to directory of data, input_file points to specific FCS file
input_file = raw_input("Enter FCS file location: ")

# Load the flow data
sample = FCMeasurement(ID='Test Sample', datafile=input_file)
data = sample.data

# Transform datasets

# Gating samples
live_dead_polygate = PolyGate([(80000,50000),(120000,120000),(90000,130000),(70000,60000)],['FSC-A','SSC-A'], region='in', name='live')
live_dead_gated_sample = sample.gate(live_dead_polygate)
singles_polygate = PolyGate([(80000,0),(100000,65000),(75000,60000),(70000,0)],['FSC-A','FSC-H'], region='in', name='singles')

# Print channel information
print sample.channels

# Print the number of events in the data
print 'Number of events in file: ', data.shape[0]

# Save plots
user_filename = raw_input("Enter plot file name: ")
generate_plots(user_filename)