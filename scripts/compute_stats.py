# compute basic stats for local-temp, global-temp, and soi
from mako.template import Template
import numpy as np
from tools import DataLoader
import sys

dl = DataLoader()
data = dl.load(unpack=True)

local_temp = data['local'][2]
global_temp = data['global'][2]
soi = data['soi'][2]

# output templates
# ---------------------------------------------------------
msg_template = Template(
'''${title}:
mean: ${mean}
stddev: ${stddev}
max: ${max}
min: ${min}
'''
)
celsius_table_template = Template(
'''${title}:
$T_{avg} \\textrm{ } (^{\circ} \\textrm{C})$ &
$\sigma T \\textrm{ } (^{\circ} \\textrm{C})$ &
$T_{max} \\textrm{ } (^{\circ} \\textrm{C})$ &
$T_{min} \\textrm{ } (^{\circ} \\textrm{C})$ \\\\ %%
\hline
${mean} & ${stddev} & ${max} & ${min} \\\\ %%
'''
)
unitless_table_template = Template(
'''${title}:
avg & $\sigma$ & max & min \\\\ %%
\hline
${mean} & ${stddev} & ${max} & ${min} \\\\ %%
'''
)
# ---------------------------------------------------------
	
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

def print_stats(datacol, msgtitle='', template=msg_template):
	mean = round(np.mean(datacol), 2)
	stddev = round(np.std(datacol), 2)
	maxval = round(np.max(datacol), 2)
	minval = round(np.min(datacol), 2)

	print(
		template.render(
			title=msgtitle,
			mean=mean,
			stddev=stddev,
			max=maxval,
			min=minval,
		)
	)

def print_all_stats(output_template):
	for data in datasets:
		print(data['duration'])
		print('-'*20)
		for k in ['local-temp', 'global-temp', 'soi']:
			print_stats(
				datacol=data[k],
				msgtitle=k,
				template=output_template
			)

if sys.argv[1] == 'unitless':
	output_template = unitless_table_template
else:
	output_template = celsius_table_template

print_all_stats(output_template)