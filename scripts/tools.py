import numpy as np
import re, csv

class DataLoader(object):
	def __init__(self):
		self.local_temp_filepath = '../data/local-temp.csv'
		self.global_temp_filepath = '../data/global-temp.csv'
		self.soi_filepath = '../data/soi.dat'

	def local_temp(self):
		year, month, temp = [], [], []

		with open(self.local_temp_filepath) as f:
			reader = csv.reader(f)
			next(reader)  # skip first row
			for row in reader:
				# collect year and month
				date = row[1]
				date = date.split('-')
				y = int(date[0])
				m = int(date[1])
				year.append(y)
				month.append(m)
				# collect temp
				t = float(row[2])
				temp.append(t)

		# year, month, temp
		a = np.array([year, month, temp])
		return np.transpose(a)

	def data(self):
		local_temp = self.local_temp()

		return local_temp

dl = DataLoader()
print( dl.data() )