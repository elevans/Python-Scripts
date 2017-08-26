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
def plot_raw_data(filename):
    figure(figsize=(10,10))
    flow_data.plot(['FSC-A', 'SSC-A'], cmap=cm.Blues, colorbar=True)
    plt.savefig('FSC-A_SSC-A_' + filename)
    plt.clf()
    flow_data.plot(['FSC-A', 'FSC-H'], cmap=cm.Blues, colorbar=True)
    plt.savefig('FSC-A_FSC-H_' + filename)
    plt.clf()
    flow_data.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('PI-W_PI-A_' + filename)
    plt.clf()


def plot_gated_data(filename):
    figure(figsize=(10,10))
    flow_data.plot(['FSC-A', 'SSC-A'], gates=[non_debris_polygate], cmap=cm.Blues, colorbar=True)
    plt.savefig('FSC-A_SSC-A_non_debris_polygate_' + filename)
    plt.clf()
    non_debris_gated_flow_data.plot(['FSC-A', 'SSC-A'], cmap=cm.Blues, colorbar=True)
    plt.savefig('Non_debris_' + filename)
    plt.clf()
    non_debris_gated_flow_data.plot(['FSC-A','FSC-H'], gates=[singles_polygate], cmap=cm.Blues, colorbar=True)
    plt.savefig('Non_debris_singles_polygate_' + filename)
    plt.clf()
    singles_flow_data.plot(['FSC-A','FSC-H'], cmap=cm.Blues, colorbar=True)
    plt.savefig('Singles_'+ filename)
    plt.clf()
    singles_flow_data.plot(['CyChrome-W', 'CyChrome-A'], gates=[cell_cycle_polygate], cmap=cm.Blues, colorbar=True)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('Cell_cycle_polygate_' + filename)
    plt.clf()
    cell_cycle_flow_data.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('Cell_cycle_'+ filename)
    plt.clf()
    cell_cycle_flow_data.plot('CyChrome-A')
    plt.xlabel('PI-A')
    plt.savefig('Cell_cycle_histogram_' + filename)
    plt.clf()
    tcell_cycle_flow_data.plot(['Alexa Fluor 405-W', 'Alexa Fluor 405-A'], cmap=cm.Blues, colorbar=True)
    plt.xlabel('405-W')
    plt.ylabel('405-A')
    plt.savefig('Cell_cycle_405-W_405-A_' + filename)
    plt.clf()
    tcell_cycle_flow_data.plot('Alexa Fluor 405-A')
    plt.xlabel('405-A')
    plt.savefig('Cell_cycle_405-A_histogram_' + filename)
    plt.clf()

# Input_file points to specific FCS file
input_file = raw_input("Enter FCS file location: ")

# Load the flow data
flow_data = FCMeasurement(ID='Flow data', datafile=input_file)
data = flow_data.data

# Print channel information
print flow_data.channels

# Print the number of events in the data
print 'Number of events in file: ', data.shape[0]

# Gating samples
non_debris_polygate = PolyGate([(55000,50000),(140000,120000),(120000,150000),(55000,90000)],['FSC-A','SSC-A'], region='in', name='live')
non_debris_gated_flow_data = flow_data.gate(non_debris_polygate)
singles_polygate = PolyGate([(50000,27000),(130000,75000),(130000,96000),(50000,41000)],['FSC-A','FSC-H'], region='in', name='singles')
singles_flow_data = non_debris_gated_flow_data.gate(singles_polygate)
cell_cycle_polygate = PolyGate([(71000,41000),(100000,41000),(100000,110000),(73000,110000)],['CyChrome-W','CyChrome-A'],region='in',name='cell cycle')
cell_cycle_flow_data = singles_flow_data.gate(cell_cycle_polygate)

# Transform data
tcell_cycle_flow_data = cell_cycle_flow_data.transform('hlog', channels=['Alexa Fluor 405-W', 'Alexa Fluor 405-A'], b=500)

# Save plots
user_filename = raw_input("Enter plot file name: ")
plot_raw_data(user_filename)
plot_gated_data(user_filename)
