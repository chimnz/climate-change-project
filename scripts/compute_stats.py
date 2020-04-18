# compute basic stats for local-temp, global-temp, and soi
import numpy as np
from tools import DataLoader

dl = DataLoader()
data = dl.load()

local_temp = np.transpose(data['local'])[2]
global_temp = np.transpose(data['global'])[2]
soi = np.transpose(data['soi'])[2]

msg = '''{title}:
mean: {mean}
stddev: {stddev}
max: {max}
min: {min}
'''
	
data_40_years = {
	'duration': 'last 40 years',
	'local-temp': local_temp,
	'global-temp': global_temp,
	'soi': soi
}

data_first_20_years = {
	'duration': 'first 20 years',
	'local-temp': local_temp[:20],
	'global-temp': global_temp[:20],
	'soi': soi[:20]
}

data_last_20_years = {
	'duration': 'last 20 years',
	'local-temp': local_temp[20:],
	'global-temp': global_temp[20:],
	'soi': soi[20:]
}

datasets = [data_40_years, data_first_20_years, data_last_20_years]

def print_stats(datacol, msgtitle=''):
	mean = round(np.mean(datacol), 3)
	stddev = round(np.std(datacol), 3)
	maxval = np.max(datacol)
	minval = np.min(datacol)

	print(
		msg.format(
			title=msgtitle,
			mean=mean,
			stddev=stddev,
			max=maxval,
			min=minval,
		)
	)

def print_all_stats():
	for data in datasets:
		print(data['duration'])
		print('-'*20)
		for k in ['local-temp', 'global-temp', 'soi']:
			print_stats(data[k], k)

print_all_stats()