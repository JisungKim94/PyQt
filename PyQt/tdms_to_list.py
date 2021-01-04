from scipy.io import *
import numpy as np
import matplotlib.pylab as plt
from nptdms import TdmsFile

tdms_file = TdmsFile("D:/Git/Tools/PyQt/FolderTest/Test_for_tdms.tdms")

# show groups
groups_data = tdms_file.groups()
print(groups_data)
# show channels
channels_data = tdms_file['Motor Performace Test Data'].channels()
print(channels_data)
# show data in channel
selected_data = tdms_file['Motor Performace Test Data']['Time']
print(selected_data.data)