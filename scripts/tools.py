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

	def global_temp(self):
		year, month, temp = [], [], []
		rows = np.loadtxt(
			fname=self.global_temp_filepath,
			delimiter=',',
			unpack=True,
			skiprows=2,
		)

		# 1980, 1981, 1982, ...
		yearcol = rows[0]
		# [ [jan1980, jan1981, ...], [feb1980, feb1981, ...], ... ]
		monthcols = rows[1:13]
		
		# collect years
		for y in yearcol:
			year += [y for i in range(12)]
		# collect months
		for y in yearcol:
			for n in range(1, 13):
				month.append(n)
		# collect temps
		num_iter = 0
		monthindex = 0
		yearindex = 0
		while num_iter < len(year):
			t = monthcols[monthindex][yearindex]
			temp.append(t)

			monthindex += 1
			if monthindex == 12:
				monthindex = 0  # return to first columns
				yearindex += 1  # move to next row
			
			num_iter += 1

		# year, month, temp
		a = np.array([year, month, temp])
		return np.transpose(a)

	def data(self):
		local_temp = self.local_temp()
		global_temp = self.global_temp()

		return {
			'local': local_temp,
			'global': global_temp,
		}

dl = DataLoader()
print( dl.data() )