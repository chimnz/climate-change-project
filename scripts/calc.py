from tools import DataLoader
import numpy as np
from scipy.stats.stats import pearsonr
from scipy.stats import ttest_ind

dl = DataLoader()
data = dl.load(unpack=True)

local_temp = data['local'][2]
global_temp = data['global'][2]
soi =  data['soi'][2]

# return (correlation coefficient, two-tailed p-value)
r, p  = pearsonr(local_temp, global_temp)

msg = '''correlation_coefficient = {r}
p_value = {p}'''
print(msg.format(r=r, p=p))