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
t = np.array(list(set(year)))  # 1980, 1981, ..., 2019
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
temp = globaldata[2]
temp = np.mean(temp.reshape(-1, 12), axis=1)
plt.scatter(t, temp, marker='.', c='black')
plt.title('Global Temperature Trend Over Last 40 Years')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly ($^{\circ}$ C)')
m, b = np.polyfit(t, temp, deg=1)
plt.plot(t, m*t+b, c='green')
plt.savefig('../plots/fits/global.png')
plt.clf()
# ---------------------------------------------------------
## soi vs. time
soi = soidata[2]
soi = np.mean(soi.reshape(-1, 12), axis=1)
plt.scatter(t, soi, marker='.', c='black')
plt.title('Southern Oscillation Index Trend Over Last 40 Years')
plt.ylabel('SOI')
plt.xlabel('Year')
m, b = np.polyfit(t, soi, deg=1)
plt.plot(t, m*t+b, c='purple')
plt.savefig('../plots/fits/soi.png')
plt.clf()