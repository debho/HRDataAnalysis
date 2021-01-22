import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#imports CSV file as a dataframe
df = pd.read_csv('hrdata.csv', header = None)
#transpose rows and cols
df = df.T
df.reset_index()

#rename cols
df = df.rename(columns = {0 : 'value',
                        1 : 'type'})

#for easy reference
datatypes = {
            'typenum' : [0, 1, 2, 3, 4, 5, 6, 7, 8,
                         9, 10, 11, 12, 13, 14, 15],
            'name' : ['Absolute Time',
                        'Relative Time',
                        'EEG1',
                        'EEG2',
                        'EEG3',
                        'EEG4',
                        'Battery Voltage',
                        'AxyXlx',
                        'AxyXly',
                        'AxyXlz',
                        'AxyMgx',
                        'AxyMgy',
                        'AxyMgz',
                        'Temperature',
                        'Error',
                        'Version']
                        }

typetable = pd.DataFrame(datatypes)
print(typetable) 

#extract EEG data
eeg1 = df[df['type'] == 2]
eeg1.reset_index()
print(eeg1)

eeg2 = df[df['type'] == 3]
print(eeg2)

eeg3 = df[df['type'] == 4]
print(eeg3)

eeg4 = df[df['type'] == 5]
print(eeg4)

#extract axy data
axy = df[
    (df['type'] >= 7) &
    (df['type'] <= 12)
]
print(axy)

#REALLY MESSY CODE NEED TO CLEAN UP
#recode using OOP API rather than global API
#fix the x-axis to reflect seconds rather than some crazy huge number
##change x-ticks by dividing values by 250 each??
#plotting eeg data
x_val = pd.Series(range(0, eeg1['value'].size))
x_val2 = pd.Series(range(0, eeg4['value'].size))
y_val = eeg1['value']
y_val2 = eeg2['value']
y_val3 = eeg3['value']
y_val4 = eeg4['value']
plt.plot(x_val, y_val)
plt.plot(x_val, y_val2)
plt.plot(x_val, y_val3)
plt.plot(x_val2, y_val4)
plt.show()

#plotting axy data

