### Use Python 2.7###
#####################

import matplotlib
matplotlib.use('Agg')

import FlowCytometryTools

from FlowCytometryTools import test_data_dir, test_data_file
from FlowCytometryTools import FCMeasurement
from pylab import *

def generate_plots(X, Y, title, filename):
    figure()
    sample.plot([X, Y])
    plt.savefig(filename)

# datadir points to directory of data, input_file points to specific FCS file
#input_dir = test_data_dir
input_file = raw_input("Enter FCS file location: ")

# Load the flow data
sample = FCMeasurement(ID='Test Sample', datafile=input_file)
data = sample.data

# Transform datasets

# Print channel information
print sample.channels

# Print the number of events in the data
print 'Number of events in file: ', data.shape[0]

user_x = raw_input("X axis to plot: ")
user_y = raw_input("Y axis to plot: ")
user_filename = raw_input("Enter plot file name: ")

# Show plot
generate_plots(user_x, user_y, user_filename)