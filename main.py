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
eeg = df[
    (df['type'] >= 2) &
    (df['type'] <= 5)
]

print(eeg)

#extract axy data
axy = df[
    (df['type'] >= 7) &
    (df['type'] <= 12)
]
print(axy)


#STUFF TO DO:
#add column that shows type (mapped to dictionary)
#plot graphs