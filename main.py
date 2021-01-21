import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# imports CSV file as a dataframe
df = pd.read_csv('HRdata.csv', header = None)

# rename rows
df = df.rename({0 : 'data',
                1 : 'type'})

# clean data to make sure only types only include 0-15


# creates dictionary for data types
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
                        'Version']}

typetable = pd.DataFrame(datatypes)
print(typetable)


# prints df
print(df)