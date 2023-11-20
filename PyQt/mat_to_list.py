from scipy.io import *
import numpy as np
import matplotlib.pylab as plt

mat_file = loadmat("D:/004_Tools/#_SEOMPA/MtIDdata/DN8PFR/01. CvtData/#6-1 +30rpm_ramp1(+25A)_128A.mat")
whos_matfile = whosmat("D:/004_Tools/#_SEOMPA/MtIDdata/DN8PFR/01. CvtData/#6-1 +30rpm_ramp1(+25A)_128A.mat")
# print(mat_file['ConvertedData'])
print(mat_file['ConvertedData'].dtype)
print(mat_file['ConvertedData'].shape, end = '\n\n')

print(mat_file['ConvertedData'][0,0].dtype)
print(mat_file['ConvertedData'][0,0].shape, end = '\n\n')

print(mat_file['ConvertedData'][0,0]['Data'].dtype)
print(mat_file['ConvertedData'][0,0]['Data'].shape, end = '\n\n')

print(mat_file['ConvertedData'][0,0]['Data'][0,0].dtype)
print(mat_file['ConvertedData'][0,0]['Data'][0,0].shape, end = '\n\n')

print(mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'].dtype)
print(mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'].shape, end = '\n\n')

print(mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'][0,14].dtype)
print(mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'][0,14].shape, end = '\n\n')

print(mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'][0,14]['Data'].dtype)
print(mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'][0,14]['Data'].shape, end = '\n\n')

print('Finally find it! :\n',  mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'][0,14], end = '\n\n\n')
print('Found list ([0,14] is Time) : ',mat_file['ConvertedData'][0,0]['Data'][0,0]['MeasuredData'][0,14]['Data'])
