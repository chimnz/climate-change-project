import numpy as np
import matplotlib.pyplot as plt
from tools import DataLoader

dl = DataLoader()
data = dl.load(unpack=True)

localdata = data['local']
globaldata = data['global']
soidata =  data['soi']

# set figure size
plt.figure(figsize=(10,5))

# fits
# ---------------------------------------------------------
## local vs. time
### scatter data points
year, month, temp = localdata
t = np.array(list(set(year)))
temp = np.mean(temp.reshape(-1, 12), axis=1)  # year-wise average
plt.scatter(t, temp, marker='.', c='black')
### label axes and title graph
plt.title('Local Temperature Trend Over Last 40 Years')
plt.xlabel('Year')
plt.ylabel('Temperature ($^{\circ}$ C)')
### plot best fit line
m, b = np.polyfit(t, temp, deg=1)
plt.plot(t, m*t+b, c='red')
### output plot to png
plt.savefig('../plots/fits/local.png')
### clear figure
plt.clf()
# ---------------------------------------------------------
## global vs. time
### scatter data points
year, month, temp = globaldata
t = np.array(list(set(year)))
temp = np.mean(temp.reshape(-1, 12), axis=1)  # year-wise average
plt.scatter(t, temp, marker='.', c='black')
### label axes and title graph
plt.title('Global Temperature Trend Over Last 40 Years')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly ($^{\circ}$ C)')
### plot best fit line
m, b = np.polyfit(t, temp, deg=1)
plt.plot(t, m*t+b, c='green')
### output plot to png
plt.savefig('../plots/fits/global.ps')
### clear figure
plt.clf()
# ---------------------------------------------------------
