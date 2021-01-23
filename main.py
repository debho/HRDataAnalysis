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
eeg_1 = df[df['type'] == 2]
eeg_2 = df[df['type'] == 3]
eeg_3 = df[df['type'] == 4]
eeg_4 = df[df['type'] == 5]

#extract axy data
axy_x = df[df['type'] == 7]
axy_y = df[df['type'] == 8]
axy_z = df[df['type'] == 9]

#fix the x-axis to reflect seconds rather than some crazy huge number
##change x-ticks by dividing values by 250 each??
#add legends

#EEG PLOT
#setting up graph
fig, ax = plt.subplots(figsize = (10,5))
ax.set_title('EEG Data')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude (a.u.)')
#ax.set_xlim(0, 20)
#ax.set_xticks(range(0,21))

#plt.xticks(range(min(valueX), max(valueX)+1))

#defining values
x_val = pd.Series(range(0, eeg_1['value'].size))
x_val2 = pd.Series(range(0, eeg_4['value'].size)) #EEG4 has diff number of readings
y_val = eeg_1['value']
y_val2 = eeg_2['value']
y_val3 = eeg_3['value']
y_val4 = eeg_4['value']

#adjusting x-ticks


#plotting EEG data
ax.plot(x_val, y_val, label = 'EEG1')
ax.plot(x_val, y_val2, label = 'EEG2')
ax.plot(x_val, y_val3, label = 'EEG3')
ax.plot(x_val2, y_val4, label = 'EEG4')

#adding legend
ax.legend()

fig.savefig('EEG.png')

#AXY PLOT
#setting up figure
fig, ax = plt.subplots(figsize = (10,5))
ax.set_title('Axy Data')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude (a.u.)')

#defining values
x_val = pd.Series(range(0, axy_x['value'].size))
x_val1 = pd.Series(range(0, axy_y['value'].size))
x_val2 = pd.Series(range(0, axy_z['value'].size))
y_val = axy_x['value']
y_val1 = axy_y['value']
y_val2 = axy_z['value']

#plotting axy data
ax.plot(x_val, y_val, label = 'Axy X')
ax.plot(x_val1, y_val1, label = 'Axy Y')
ax.plot(x_val2, y_val2, label = 'Axy Z')

#adding legend
ax.legend()
plt.savefig('axy.png')

