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
		return np.array([year, month, temp])

	def __linearize_month_data_cols(self, yearcol, monthcols):
		'''Linerarize data stored in month columns (global and soi).'''
		temp = []
		monthindex = 0
		yearindex = 0
		years_processed = 0
		while years_processed < len(yearcol):
			t = monthcols[monthindex][yearindex]
			temp.append(t)

			monthindex += 1
			if monthindex == 12:
				monthindex = 0  # return to first columns
				yearindex += 1  # move to next row
				years_processed += 1
		# [jan1980, feb1980, ..., dec2019]
		return temp

	def global_temp(self):
		year, month = [], []
		rows = np.loadtxt(
			fname=self.global_temp_filepath,
			delimiter=',',
			unpack=True,
			skiprows=2,
		)

		# 1980, 1981, 1982, ...
		yearcol = rows[0]
		# [ [temp(jan1980), temp(jan1981), ...],
		#   [temp(feb1980), temp(feb1981), ...],
		#   [..., temp(dec1980), temp(dec1981)] ]
		monthcols = rows[1:13]
		
		for y in yearcol:
			year += [y for i in range(12)]
		for y in yearcol:
			for n in range(1, 13):
				month.append(n)
		temp = self.__linearize_month_data_cols(yearcol, monthcols)

		# year, month, temp
		return np.array([year, month, temp])

	def soi(self):
		# same format as global temp
		year, month = [], []
		rows = np.loadtxt(
			fname=self.soi_filepath,
			unpack=True,
			skiprows=1,
		)

		yearcol = rows[0]
		monthcols = rows[1:]

		for y in yearcol:
			year += [y for i in range(12)] 
		for y in yearcol:
			for n in range(1, 13):
				month.append(n)
		temp = self.__linearize_month_data_cols(yearcol, monthcols)

		# year, month, temp
		return np.array([year, month, temp])

	def load(self, unpack=False):
		# 3 arrays: year, month, temp
		local_temp = self.local_temp()
		global_temp = self.global_temp()
		soi = self.soi()

		if unpack == False:
			# 1 array: [year month temp]
			local_temp = np.transpose(local_temp)
			global_temp = np.transpose(global_temp)
			soi = np.transpose(soi)

		return {
			'local': local_temp,
			'global': global_temp,
			'soi': soi
		}