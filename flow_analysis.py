### Use Python 2.7###
#####################
from __future__ import division

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
    plt.title('Non-debris - Raw', fontsize=14)
    plt.savefig('FSC-A_SSC-A_' + filename + '.png')
    plt.clf()

    flow_data.plot(['FSC-A', 'FSC-H'], cmap=cm.Blues, colorbar=True)
    plt.title('Singles - Raw', fontsize=14)
    plt.savefig('FSC-A_FSC-H_' + filename + '.png')
    plt.clf()

    flow_data.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.title('Propidium iodide - Raw', fontsize=14)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('PI-W_PI-A_' + filename + '.png')
    plt.clf()

def plot_gated_data(filename):
    figure(figsize=(10,10))

    # Non-debris and singles plots
    flow_data.plot(['FSC-A', 'SSC-A'], gates=[non_debris_polygate], cmap=cm.Blues, colorbar=True)
    plt.title('Non-debris polygate', fontsize=14)
    plt.savefig('FSC-A_SSC-A_non_debris_polygate_' + filename + '.png')
    plt.clf()

    non_debris_gated_flow_data.plot(['FSC-A', 'SSC-A'], cmap=cm.Blues, colorbar=True)
    plt.title('Non-debris gated', fontsize=14)
    plt.savefig('Non_debris_' + filename + '.png')
    plt.clf()

    non_debris_gated_flow_data.plot(['FSC-A', 'FSC-H'], cmap=cm.Blues, colorbar=True)
    plt.title('Non-debirs singles - Raw', fontsize=14)
    plt.savefig('Non_debris_FSC-A_FSC-H_' + filename + '.png')
    plt.clf()

    non_debris_gated_flow_data.plot(['FSC-A','FSC-H'], gates=[singles_polygate], cmap=cm.Blues, colorbar=True)
    plt.title('Singles polygate', fontsize=14)
    plt.savefig('Non_debris_singles_polygate_' + filename + '.png')
    plt.clf()

    singles_flow_data.plot(['FSC-A','FSC-H'], cmap=cm.Blues, colorbar=True)
    plt.title('Singles gated', fontsize=14)
    plt.savefig('Singles_'+ filename + '.png')
    plt.clf()

    # CFP and YFP histograms
    tsingles_flow_data.plot('Alexa Fluor 405-A')
    plt.xlabel('CFP-A')
    plt.xlim(0,6000)
    plt.title('Singles CFP expression', fontsize=14)
    plt.savefig('Singles_CFP_histogram_' + filename + '.png')
    plt.clf()

    tsingles_flow_data.plot('Alexa Fluor 488-A')
    plt.xlabel('YFP-A')
    plt.xlim(0)
    plt.title('Singles YFP-A3G expression', fontsize=14)
    plt.savefig('Singles_YFP_histogram_'+ filename + '.png')
    plt.clf()

    # CFP / YFP scatter plot
    tsingles_flow_data.plot(['Alexa Fluor 405-A', 'Alexa Fluor 488-A'], cmap=cm.Blues, colorbar=True)
    plt.title('Singles CFP x YFP-A3G', fontsize=14)
    plt.xlabel('CFP-A')
    plt.ylabel('YFP-A3G-A')
    plt.savefig('Singels_CFP_YFP-A3G_scatter_' + filename + '.png')
    plt.clf()

    # CFP expression plots
    tsingles_flow_data.plot('Alexa Fluor 405-A', gates=[cfp_expressing_gate])
    plt.xlabel('CFP-A')
    plt.xlim(0,6000)
    plt.title('Singles CFP expressing cells threashold gate', fontsize=14)
    plt.savefig('Singles_CFP_threashold_gate_' + filename + '.png')
    plt.clf()

    cfp_expressing_flow_data.plot('Alexa Fluor 405-A')
    plt.xlabel('CFP-A')
    plt.title('CFP expressing cells gated')
    plt.savefig('CFP_expressing_cells_histogram_' + filename + '.png')
    plt.clf()

    non_cfp_expressing_flow_data.plot('Alexa Fluor 405-A')
    plt.xlabel('CFP-A')
    plt.title('Non-CFP expressing cells gated')
    plt.savefig('Non-CFP_expressing_cells_histogram_' + filename + '.png')
    plt.clf()   

    # Cell cycle status plots - CFP expressing
    cfp_expressing_flow_data.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.title('Propidium iodide CFP expressing - Raw', fontsize=14)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('CFP_expressing_PI-A_PI-W_' + filename + '.png')
    plt.clf()

    cfp_expressing_flow_data.plot(['CyChrome-W', 'CyChrome-A'], gates=[cfp_expressing_cell_cycle_polygate], cmap=cm.Blues, colorbar=True)
    plt.title('Propidium iodide CFP expressing polygate', fontsize=14)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('CFP_expressing_cell_cycle_polygate_' + filename + '.png')
    plt.clf()

    cfp_expressing_cell_cycle_flow_data.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.title('CFP expressing cell cycle gated', fontsize=14)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('CFP_expressing_cell_cycle_'+ filename + '.png')
    plt.clf()

    cfp_expressing_cell_cycle_flow_data.plot('CyChrome-A')
    plt.title('CFP expressing cell cycle - Propidium iodide histogram', fontsize=14)
    plt.xlabel('PI-A')
    plt.savefig('CFP_expressing_cell_cycle_histogram_' + filename + '.png')
    plt.clf()

    # Cell cycle status plots - Non CFP expressing
    non_cfp_expressing_flow_data.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.title('Propidium iodide Non-CFP expressing - Raw', fontsize=14)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('non-CFP_expressing_PI-A_PI-W_' + filename + '.png')
    plt.clf()

    non_cfp_expressing_flow_data.plot(['CyChrome-W', 'CyChrome-A'], gates=[non_cfp_expressing_cell_cycle_polygate], cmap=cm.Blues, colorbar=True)
    plt.title('Propidium iodide Non-CFP expressing polygate', fontsize=14)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('non-CFP_expressing_cell_cycle_polygate_' + filename + '.png')
    plt.clf()

    non_cfp_expressing_cell_cycle_flow_data.plot(['CyChrome-W', 'CyChrome-A'], cmap=cm.Blues, colorbar=True)
    plt.title('Non-CFP expressing cell cycle gated', fontsize=14)
    plt.xlabel('PI-W')
    plt.ylabel('PI-A')
    plt.savefig('non-CFP_expressing_cell_cycle_'+ filename + '.png')
    plt.clf()

    non_cfp_expressing_cell_cycle_flow_data.plot('CyChrome-A')
    plt.title('Non-CFP expressing cell cycle - Propidium iodide histogram', fontsize=14)
    plt.xlabel('PI-A')
    plt.savefig('non-CFP_expressing_cell_cycle_histogram_' + filename + '.png')
    plt.clf()

def calculate_cell_cycle_status():

    # Gate for G1 and G2 peaks (CFP expressing)
    cfp_cell_cycle_g1_gate = ThresholdGate(65000.0, 'CyChrome-A', region='below')
    cfp_cell_cycle_g1_flow_data = cfp_expressing_cell_cycle_flow_data.gate(cfp_cell_cycle_g1_gate)
    cfp_cell_cycle_g2_gate = ThresholdGate(89000.0, 'CyChrome-A', region='above')
    cfp_cell_cycle_g2_flow_data = cfp_expressing_cell_cycle_flow_data.gate(cfp_cell_cycle_g2_gate)

    # Gate for S phase, isolating the data between G1 and G2 peaks (CFP expressing)
    cfp_cell_cycle_s_a_gate = ThresholdGate(65000.0, 'CyChrome-A', region='above')
    cfp_cell_cycle_s_flow_data = cfp_expressing_cell_cycle_flow_data.gate(cfp_cell_cycle_s_a_gate)
    cfp_cell_cycle_s_b_gate = ThresholdGate(89000.0, 'CyChrome-A', region='below')
    cfp_cell_cycle_s_flow_data = cfp_cell_cycle_s_flow_data.gate(cfp_cell_cycle_s_b_gate)

    cfp_cells_in_g1 = cfp_cell_cycle_g1_flow_data.shape[0]
    cfp_cells_in_g2 = cfp_cell_cycle_g2_flow_data.shape[0]
    cfp_cells_in_s = cfp_cell_cycle_s_flow_data.shape[0]

    cfp_total_cells = cfp_cells_in_g1 + cfp_cells_in_g2 + cfp_cells_in_s

    cfp_percent_g1 = 100 * (cfp_cells_in_g1 / cfp_total_cells)
    cfp_percent_g2 = 100 * (cfp_cells_in_g2 / cfp_total_cells)
    cfp_percent_s = 100 * (cfp_cells_in_s / cfp_total_cells)

    print 'CFP expressing cells in G1: ' + str(cfp_percent_g1) + ' %'
    print 'CFP expressing cells in G2: ' + str(cfp_percent_g2) + ' %'
    print 'CFP expressing cells in S: ' + str(cfp_percent_s) + ' %'

    print '-------------------------------'

    # Gate for G1 and G2 peaks (non-GFP expressing)
    non_cfp_cell_cycle_g1_gate = ThresholdGate(65000.0, 'CyChrome-A', region='below')
    non_cfp_cell_cycle_g1_flow_data = non_cfp_expressing_cell_cycle_flow_data.gate(non_cfp_cell_cycle_g1_gate)
    non_cfp_cell_cycle_g2_gate = ThresholdGate(89000.0, 'CyChrome-A', region='above')
    non_cfp_cell_cycle_g2_flow_data = non_cfp_expressing_cell_cycle_flow_data.gate(non_cfp_cell_cycle_g2_gate)

    # Gate for S phase, isolating the data between G1 and G2 peaks (non-GFP expressing)
    non_cfp_cell_cycle_s_a_gate = ThresholdGate(65000.0, 'CyChrome-A', region='above')
    non_cfp_cell_cycle_s_flow_data = non_cfp_expressing_cell_cycle_flow_data.gate(non_cfp_cell_cycle_s_a_gate)
    non_cfp_cell_cycle_s_b_gate = ThresholdGate(89000.0, 'CyChrome-A', region='below')
    non_cfp_cell_cycle_s_flow_data = non_cfp_cell_cycle_s_flow_data.gate(non_cfp_cell_cycle_s_b_gate)

    non_cfp_cells_in_g1 = non_cfp_cell_cycle_g1_flow_data.shape[0]
    non_cfp_cells_in_g2 = non_cfp_cell_cycle_g2_flow_data.shape[0]
    non_cfp_cells_in_s = non_cfp_cell_cycle_s_flow_data.shape[0]

    non_cfp_total_cells = non_cfp_cells_in_g1 + non_cfp_cells_in_g2 + non_cfp_cells_in_s

    non_cfp_percent_g1 = 100 * (non_cfp_cells_in_g1 / non_cfp_total_cells)
    non_cfp_percent_g2 = 100 * (non_cfp_cells_in_g2 / non_cfp_total_cells)
    non_cfp_percent_s = 100 * (non_cfp_cells_in_s / non_cfp_total_cells)

    print 'Non-CFP expressing cells in G1: ' + str(non_cfp_percent_g1) + ' %'
    print 'Non-CFP expressing cells in G2: ' + str(non_cfp_percent_g2) + ' %'
    print 'Non-CFP expressing cells in S: ' + str(non_cfp_percent_s) + ' %'

def gated_counts():

    percent_non_debris = 100 * (non_debris_gated_flow_data.shape[0]/flow_data.shape[0])
    percent_singles = 100 * (singles_flow_data.shape[0]/non_debris_gated_flow_data.shape[0])

    # Print number of cells in debris and singles
    print 'Cells in non-debris gate: ' + str(non_debris_gated_flow_data.shape[0]) + ', ' + str(percent_non_debris) + ' %'
    print 'Cells in singles gate: ' + str(singles_flow_data.shape[0]) + ', ' + str(percent_singles) + ' %'

# Input_file points to specific FCS file
input_file = raw_input("Enter FCS file location: ")

# Load the flow data
flow_data = FCMeasurement(ID='Flow data', datafile=input_file)

# Print channel information
print flow_data.channels

# Print the number of events in the data
print 'Events in file: ', flow_data.shape[0]

# Primary gates
non_debris_polygate = PolyGate([(45000,50000),(150000,55000),(200000,75000),(230000,150000),(180000,225000),(60000,200000),(30000,100000)],['FSC-A','SSC-A'], region='in', name='live')
non_debris_gated_flow_data = flow_data.gate(non_debris_polygate)
singles_polygate = PolyGate([(45000,25000),(190000,99000),(170000,135000),(55000,43000)],['FSC-A','FSC-H'], region='in', name='singles')
singles_flow_data = non_debris_gated_flow_data.gate(singles_polygate)

# Transform data
tsingles_flow_data = singles_flow_data.transform('hlog', channels=['Alexa Fluor 405-A', 'Alexa Fluor 405-H', 'Alexa Fluor 405-W', 'Alexa Fluor 488-A','Alexa Fluor 488-H','Alexa Fluor 488-W'], b=500.0)

# Continue gating data
cfp_expressing_gate = ThresholdGate(2000.0,'Alexa Fluor 405-A', region='above')
cfp_expressing_flow_data = tsingles_flow_data.gate(cfp_expressing_gate)
non_cfp_expressing_gate = ThresholdGate(2000.0,'Alexa Fluor 405-A', region='below')
non_cfp_expressing_flow_data = tsingles_flow_data.gate(non_cfp_expressing_gate)
cfp_expressing_cell_cycle_polygate = PolyGate([(65000,23000),(115000,23000),(115000,120000),(65000,120000)],['CyChrome-W','CyChrome-A'],region='in',name='cell cycle')
cfp_expressing_cell_cycle_flow_data = cfp_expressing_flow_data.gate(cfp_expressing_cell_cycle_polygate)
non_cfp_expressing_cell_cycle_polygate = PolyGate([(65000,23000),(115000,23000),(115000,120000),(65000,120000)],['CyChrome-W','CyChrome-A'],region='in',name='cell cycle')
non_cfp_expressing_cell_cycle_flow_data = non_cfp_expressing_flow_data.gate(non_cfp_expressing_cell_cycle_polygate)

# Print non-debris and singles gated counts and percentages
gated_counts()

# Save plots
user_filename = raw_input("Enter plot file name: ")
plot_raw_data(user_filename)
plot_gated_data(user_filename)

# Calculate cell cycle status
calculate_cell_cycle_status()
