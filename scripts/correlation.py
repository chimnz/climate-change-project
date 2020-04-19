from tools import DataLoader, year_wise_average
import numpy as np
from scipy.stats.stats import pearsonr
from scipy.stats import ttest_ind

dl = DataLoader()
data = dl.load(unpack=True)

local_temp = data['local'][2]
global_temp = data['global'][2]
soi =  data['soi'][2]

# convert to year-wise averages
local_temp = year_wise_average(local_temp)
global_temp = year_wise_average(global_temp)
soi = year_wise_average(soi)

msg = '''{title}:
correlation_coefficient = {r}
p_value = {p}
'''

# (a) correlation for local temp and global temp
## return (correlation coefficient, two-tailed p-value)
r, p  = pearsonr(local_temp, global_temp)
## print message to stdout
title = 'local temp and global temp correlation'
print(msg.format(title=title, r=r, p=p))

# (b) correlation for local temp and soi
title = 'local temp and SOI correlation'
r, p  = pearsonr(local_temp, soi)
print(msg.format(title=title, r=r, p=p))