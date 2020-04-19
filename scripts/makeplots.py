import numpy as np
import matplotlib.pyplot as plt
from tools import DataLoader, year_wise_average

dl = DataLoader()
data = dl.load(unpack=True)

year, month, local_temp = data['local']
global_temp = data['global'][2]
soi =  data['soi'][2]

t = np.array(list(set(year)))  # 1980, 1981, ..., 2019

# save original month-wise
m_local_temp = local_temp
m_global_temp = global_temp
m_soi =soi

# convert all data to year-wise averages
local_temp = year_wise_average(local_temp)
global_temp = year_wise_average(global_temp)
soi = year_wise_average(soi)

# set figure size
plt.figure(figsize=(10,5))

# fits
# ---------------------------------------------------------
## local vs. time
### scatter data points
plt.scatter(t, local_temp, marker='.', c='black')
### label axes and title graph
plt.title('Local Temperature Trend Over Last 40 Years')
plt.xlabel('Year')
plt.ylabel('Temperature ($^{\circ}$ C)')
### plot best fit line
m, b = np.polyfit(t, local_temp, deg=1)
plt.plot(t, m*t+b, c='red')
### output plot to png
plt.savefig('../plots/fits/local.png')
### clear figure
plt.clf()
# ---------------------------------------------------------
## global vs. time
plt.scatter(t, global_temp, marker='.', c='black')
plt.title('Global Temperature Trend Over Last 40 Years')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly ($^{\circ}$ C)')
m, b = np.polyfit(t, global_temp, deg=1)
plt.plot(t, m*t+b, c='green')
plt.savefig('../plots/fits/global.png')
plt.clf()
# ---------------------------------------------------------
## soi vs. time
plt.scatter(t, soi, marker='.', c='black')
plt.title('Southern Oscillation Index Trend Over Last 40 Years')
plt.ylabel('SOI')
plt.xlabel('Year')
m, b = np.polyfit(t, soi, deg=1)
plt.plot(t, m*t+b, c='purple')
plt.savefig('../plots/fits/soi.png')
plt.clf()
# ---------------------------------------------------------


# compare
# ---------------------------------------------------------
## local temp vs. global temp (a)
plt.scatter(global_temp, local_temp, marker='.', c='black')
plt.title('Local Temperature vs. Global Temperature Anomaly')
plt.ylabel('Local Temperature ($^{\circ}$ C)')
plt.xlabel('Global Temperature Anomaly ($^{\circ}$ C)')
m, b = np.polyfit(global_temp, local_temp, deg=1)
plt.plot(global_temp, m*global_temp+b, c='gray')
plt.savefig('../plots/compare/local_vs_global.png')
plt.clf()
# ---------------------------------------------------------
## local temp vs. soi
plt.scatter(soi, local_temp, marker='.', c='black')
plt.title('Local Temperature vs. Global Temperature Anomaly')
plt.ylabel('Local Temperature ($^{\circ}$ C)')
plt.xlabel('SOI')
m, b = np.polyfit(soi, local_temp, deg=1)
plt.plot(soi, m*soi+b, c='gray')
plt.savefig('../plots/compare/local_vs_soi.png')
plt.clf()
# ---------------------------------------------------------


# historgram
# ---------------------------------------------------------
## local temp
nbins = 100
plt.hist(m_local_temp, nbins, color='red')
plt.title('Local Temperature Histogram')
plt.xlabel('Temperature ($^{\circ}$ C)')
plt.ylabel('Occurences')
plt.savefig('../plots/histogram/local.png')
plt.clf()
# ---------------------------------------------------------
## global temp
plt.hist(m_global_temp, nbins, color='green')
plt.title('Global Temperature Histogram')
plt.xlabel('Temperature Anomaly ($^{\circ}$ C)')
plt.ylabel('Occurences')
plt.savefig('../plots/histogram/global.png')
plt.clf()
# ---------------------------------------------------------
## soi
plt.hist(m_soi, nbins, color='purple')
plt.title('Southern Oscillation Index Histogram')
plt.xlabel('SOI')
plt.ylabel('Occurences')
plt.savefig('../plots/histogram/soi.png')
plt.clf()
# ---------------------------------------------------------