import numpy as np
import matplotlib.pyplot as plt
from tools import DataLoader

dl = DataLoader()
data = dl.load()

localdata = data['local']
globaldata = data['global']
soidata =  data['soi']

# set figure size
plt.figure(figsize=(10,5))

# fits
## local vs. time
### scatter data points
year, month, temp = soidata
t = np.array(list(set(year)))  # years since January, 1980
temp = np.mean(temp.reshape(-1, 12), axis=1)  # year-wise average
plt.scatter(t, temp, marker='.', c='black')
### label axes and title graph
plt.title('Local Temperature Trend')
plt.xlabel('Years since January 1980')
plt.ylabel('Temperature ($^{\circ}$ C)')
### plot best fit line
m, b = np.polyfit(t, temp, deg=1)
plt.plot(t, m*t+b, c='red')
### output plot to png
plt.savefig('../plots/fits/local.png')
### clear figure
plt.clf()

## global vs. time