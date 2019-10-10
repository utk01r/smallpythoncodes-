import camelot
import pandas as pd
import os
import glob

for i in range(1,148):
	ini_d = "lok/" + "As"
	ex = "00" + str(i)
	if len(ex) == 4:
		ex = ex[1:]
		temp_d = ini_d + ex
	elif len(ex) == 5:
		ex = ex[2:]
		temp_d = ini_d + ex
	else:
		temp_d = ini_d + ex
	try:
		tables = camelot.read_pdf(temp_d + ".pdf", pages="1-end")
		a = 1
		for table in tables:
			name = str(a) + ".csv"
			table.to_csv(name)
			a = a*10 + 1
	except FileNotFoundError:
		print("Peace Maaro")
	try:
		extension = 'csv'
		all_filenames = [y for y in glob.glob('*.{}'.format(extension))]
		combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
		combined_csv.to_csv((temp_d + ".csv"), index=False, encoding='utf-8-sig')
		a = 1
		for table in tables:
			name = str(a) + ".csv"
			os.remove(name)
			a = a*10 + 1
	except ValueError:
		print("ValueError occured in " + temp_d + ".pdf")

