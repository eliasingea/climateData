import re
import os
from collections import defaultdict
print 'hello'
def main(): 
	print 'what type of data would you like to look at? '
	product = raw_input("> ")
	print "Now, what is the name of the name of the file you would like to use: "
	filename = raw_input("> ")
	while os.path.exists(product + '/' + filename) != True: 
		print 'the file does not exist please choose one that does: '
		filename = raw_input("> ")
	if 'dly' in filename:
		itemList = readDly(filename, product)
		stationList = getStations()
		writeDly(itemList, stationList)
	elif 'mly' in filename:
		itemArray = readMonthly(filename, product)
		stationList = getStations()
		writemly(itemArray, stationList)
	else:
		itemList = readFile(filename, product)
		stationList = getStations()
		writeData(itemList, stationList)

def readFile(filename, product): 
	fileOpen = open(product +'/' + filename, 'r')
	stations = []
	data = []
	code = []
	dataNums = []
	
	finalItems = {}
	itemlist = []
	r = re.compile("[-]?([0-9]+)([A-Z]+)")
	if 'htdd' in filename:
		for line in fileOpen:
			items = {}
			p = line.split()
			stations.append(p[0])
			m = r.match(p[1])
			print m.groups()
			# dataNums.append(float(m.group(1))/10.0)
			# code.append(m.group(2))
			#items = {float(m.group(1))/10.0, m.group(2)}
			if '-7777' in line:
				print 'yes'
				continue
			else:
				items["data"] = m.group(1)
				items["code"] = m.group(2)
				items["stations"] = p[0]
				itemlist.append(items)
	elif 'cldd' in filename:
		for line in fileOpen:
			items = {}
			p = line.split()
			stations.append(p[0])
			m = r.match(p[1])
			print m.groups()
			# dataNums.append(float(m.group(1))/10.0)
			# code.append(m.group(2))
			#items = {float(m.group(1))/10.0, m.group(2)}
			if '-7777' in line:
				print 'yes'
				continue
			else:
				items["data"] = m.group(1)
				items["code"] = m.group(2)
				items["stations"] = p[0]
				itemlist.append(items)
	elif 'prcp' in filename: 
		for line in fileOpen:
			items = {}
			p = line.split()
			stations.append(p[0])
			m = r.match(p[1])
			print m.groups()
			# dataNums.append(float(m.group(1))/10.0)
			# code.append(m.group(2))
			#items = {float(m.group(1))/10.0, m.group(2)}
			if '-7777' in line:
				print 'yes'
				continue
			else:
				items["data"] = float(m.group(1))*.01
				items["code"] = m.group(2)
				items["stations"] = p[0]
				itemlist.append(items)
	elif 'snow' in filename:
		for line in fileOpen:
			items = {}
			p = line.split()
			stations.append(p[0])
			m = r.match(p[1])
			print m.groups()
			# dataNums.append(float(m.group(1))/10.0)
			# code.append(m.group(2))
			#items = {float(m.group(1))/10.0, m.group(2)}
			if '-7777' in line:
				print 'yes'
				continue
			else:
				items["data"] = float(m.group(1))*.10
				items["code"] = m.group(2)
				items["stations"] = p[0]
				itemlist.append(items)
	elif 'snwd' in filename: 
		for line in fileOpen:
			items = {}
			p = line.split()
			stations.append(p[0])
			m = r.match(p[1])
			print m.groups()
			# dataNums.append(float(m.group(1))/10.0)
			# code.append(m.group(2))
			#items = {float(m.group(1))/10.0, m.group(2)}
			if '-7777' in line:
				print 'yes'
				continue
			else:
				items["data"] = m.group(1)
				items["code"] = m.group(2)
				items["stations"] = p[0]
				itemlist.append(items) 
	else:
		for line in fileOpen:
			items = {}
			p = line.split()
			stations.append(p[0])
			m = r.match(p[1])
			print m.groups()
			# dataNums.append(float(m.group(1))/10.0)
			# code.append(m.group(2))
			#items = {float(m.group(1))/10.0, m.group(2)}
			if '-7777' in line:
				print 'yes'
				continue
			else:
				items["data"] = float(m.group(1))*.10
				items["code"] = m.group(2)
				items["stations"] = p[0]
				itemlist.append(items)
	fileOpen.close()
	return itemlist
def getStations(): 
	filename = ("station-inventories/allstations.txt")
	fileOpen = open(filename, 'r')
	stationList = []
	for line in fileOpen: 
		stationInfo = {}
		p = line.split()
		stationInfo["stations"] = p[0]
		stationInfo["lat"] = p[1]
		stationInfo["long"] = p[2]
		stationList.append(stationInfo)
		#print stationInfo
	fileOpen.close()
	return stationList

def readDly(filename, product):
	fileOpen = open(product +'/' + filename, 'r')
	finalItems = {}
	itemList = []
	days = []
	codes = []
	i = 2
	r = re.compile("([-]?[0-9]+)([A-Z]+)")
	if 'htdd' in filename:
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			items['month'] = p[1]
			m1 = r.match(p[2])
			m2 = r.match(p[3])
			m3 = r.match(p[4])
			m4 = r.match(p[5])
			m5 = r.match(p[6])
			m6 = r.match(p[7])
			m7 = r.match(p[8])
			m8 = r.match(p[9])
			m9 = r.match(p[10])
			m10 = r.match(p[11])
			m11 = r.match(p[12])
			m12 = r.match(p[13])
			m13 = r.match(p[14])
			m14 = r.match(p[14])
			m15 = r.match(p[15])
			m16 = r.match(p[16])
			m17 = r.match(p[17])
			m18 = r.match(p[18])
			m19 = r.match(p[19])
			m20 = r.match(p[20])
			m21 = r.match(p[21])
			m22 = r.match(p[22])
			m23 = r.match(p[23])
			m24 = r.match(p[24])
			m25 = r.match(p[25])
			m26 = r.match(p[26])
			m27 = r.match(p[27])
			m28 = r.match(p[28])
			m29 = r.match(p[29])
			m30 = r.match(p[30])
			m31 = r.match(p[31])
			items['m1'] = m1.group(1)
			items['m2'] = m2.group(1)
			items['m3'] = m3.group(1)
			items['m4'] = m4.group(1)
			items['m5'] = m5.group(1)
			items['m6'] = m6.group(1)
			items['m7'] = m7.group(1)
			items['m8'] = m8.group(1)	
			items['m9'] = m9.group(1)
			items['m10'] = m10.group(1)
			items['m11'] = m11.group(1)
			items['m12'] = m12.group(1)
			items['m13'] = m13.group(1)
			items['m14'] = m14.group(1)
			items['m15'] = m15.group(1)
			items['m16'] = m16.group(1)
			items['m17'] = m17.group(1)
			items['m18'] = m18.group(1)
			items['m19'] = m19.group(1)
			items['m20'] = m20.group(1)
			items['m21'] = m21.group(1)
			items['m22'] = m22.group(1)
			items['m23'] = m23.group(1)
			items['m24'] = m24.group(1)
			items['m25'] = m25.group(1)
			items['m26'] = m26.group(1)
			items['m27'] = m27.group(1)
			items['m28'] = m28.group(1)
			items['m29'] = m29.group(1)
			items['m30'] = m30.group(1)
			#items['m31'] = m31.group(1)
			items['m1Code'] = m1.group(2)
			items['m2Code'] = m2.group(2)
			items['m3Code'] = m3.group(2)	
			items['m4Code'] = m4.group(2)
			items['m5Code'] = m5.group(2)
			items['m6Code'] = m6.group(2)
			items['m7Code'] = m7.group(2)
			items['m8Code'] = m8.group(2)
			items['m9Code'] = m9.group(2)
			items['m10Code'] = m10.group(2)
			items['m11Code'] = m11.group(2)
			items['m12Code'] = m12.group(2)
			items['m13Code'] = m13.group(2)
			items['m14Code'] = m14.group(2)
			items['m15Code'] = m15.group(2)
			items['m16Code'] = m16.group(2)
			items['m17Code'] = m17.group(2)
			items['m18Code'] = m18.group(2)
			items['m19Code'] = m19.group(2)		
			items['m20Code'] = m20.group(2)
			items['m21Code'] = m21.group(2)
			items['m22Code'] = m22.group(2)
			items['m23Code'] = m23.group(2)
			items['m24Code'] = m24.group(2)
			items['m25Code'] = m25.group(2)
			items['m26Code'] = m26.group(2)
			items['m27Code'] = m27.group(2)
			items['m28Code'] = m28.group(2)
			items['m29Code'] = m29.group(2)
			items['m30Code'] = m30.group(2)
			#items['m31Code'] = m31.group(2)
			itemList.append(items)
	elif 'cldd' in filename:
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			items['month'] = p[1]
			m1 = r.match(p[2])
			m2 = r.match(p[3])
			m3 = r.match(p[4])
			m4 = r.match(p[5])
			m5 = r.match(p[6])
			m6 = r.match(p[7])
			m7 = r.match(p[8])
			m8 = r.match(p[9])
			m9 = r.match(p[10])
			m10 = r.match(p[11])
			m11 = r.match(p[12])
			m12 = r.match(p[13])
			m13 = r.match(p[14])
			m14 = r.match(p[14])
			m15 = r.match(p[15])
			m16 = r.match(p[16])
			m17 = r.match(p[17])
			m18 = r.match(p[18])
			m19 = r.match(p[19])
			m20 = r.match(p[20])
			m21 = r.match(p[21])
			m22 = r.match(p[22])
			m23 = r.match(p[23])
			m24 = r.match(p[24])
			m25 = r.match(p[25])
			m26 = r.match(p[26])
			m27 = r.match(p[27])
			m28 = r.match(p[28])
			m29 = r.match(p[29])
			m30 = r.match(p[30])
			m31 = r.match(p[31])
			items['m1'] = m1.group(1)
			items['m2'] = m2.group(1)
			items['m3'] = m3.group(1)
			items['m4'] = m4.group(1)
			items['m5'] = m5.group(1)
			items['m6'] = m6.group(1)
			items['m7'] = m7.group(1)
			items['m8'] = m8.group(1)	
			items['m9'] = m9.group(1)
			items['m10'] = m10.group(1)
			items['m11'] = m11.group(1)
			items['m12'] = m12.group(1)
			items['m13'] = m13.group(1)
			items['m14'] = m14.group(1)
			items['m15'] = m15.group(1)
			items['m16'] = m16.group(1)
			items['m17'] = m17.group(1)
			items['m18'] = m18.group(1)
			items['m19'] = m19.group(1)
			items['m20'] = m20.group(1)
			items['m21'] = m21.group(1)
			items['m22'] = m22.group(1)
			items['m23'] = m23.group(1)
			items['m24'] = m24.group(1)
			items['m25'] = m25.group(1)
			items['m26'] = m26.group(1)
			items['m27'] = m27.group(1)
			items['m28'] = m28.group(1)
			items['m29'] = m29.group(1)
			items['m30'] = m30.group(1)
			#items['m31'] = m31.group(1)
			items['m1Code'] = m1.group(2)
			items['m2Code'] = m2.group(2)
			items['m3Code'] = m3.group(2)	
			items['m4Code'] = m4.group(2)
			items['m5Code'] = m5.group(2)
			items['m6Code'] = m6.group(2)
			items['m7Code'] = m7.group(2)
			items['m8Code'] = m8.group(2)
			items['m9Code'] = m9.group(2)
			items['m10Code'] = m10.group(2)
			items['m11Code'] = m11.group(2)
			items['m12Code'] = m12.group(2)
			items['m13Code'] = m13.group(2)
			items['m14Code'] = m14.group(2)
			items['m15Code'] = m15.group(2)
			items['m16Code'] = m16.group(2)
			items['m17Code'] = m17.group(2)
			items['m18Code'] = m18.group(2)
			items['m19Code'] = m19.group(2)		
			items['m20Code'] = m20.group(2)
			items['m21Code'] = m21.group(2)
			items['m22Code'] = m22.group(2)
			items['m23Code'] = m23.group(2)
			items['m24Code'] = m24.group(2)
			items['m25Code'] = m25.group(2)
			items['m26Code'] = m26.group(2)
			items['m27Code'] = m27.group(2)
			items['m28Code'] = m28.group(2)
			items['m29Code'] = m29.group(2)
			items['m30Code'] = m30.group(2)
			#items['m31Code'] = m31.group(2)
			itemList.append(items)
	elif 'prcp' in filename:
		if 'pctall' in filename: 
			for line in fileOpen:
				items = {}
				p = line.split()
				items['stations'] = p[0]
				items['month'] = p[1]
				m1 = r.match(p[2])
				m2 = r.match(p[3])
				m3 = r.match(p[4])
				m4 = r.match(p[5])
				m5 = r.match(p[6])
				m6 = r.match(p[7])
				m7 = r.match(p[8])
				m8 = r.match(p[9])
				m9 = r.match(p[10])
				m10 = r.match(p[11])
				m11 = r.match(p[12])
				m12 = r.match(p[13])
				m13 = r.match(p[14])
				m14 = r.match(p[14])
				m15 = r.match(p[15])
				m16 = r.match(p[16])
				m17 = r.match(p[17])
				m18 = r.match(p[18])
				m19 = r.match(p[19])
				m20 = r.match(p[20])
				m21 = r.match(p[21])
				m22 = r.match(p[22])
				m23 = r.match(p[23])
				m24 = r.match(p[24])
				m25 = r.match(p[25])
				m26 = r.match(p[26])
				m27 = r.match(p[27])
				m28 = r.match(p[28])
				m29 = r.match(p[29])
				m30 = r.match(p[30])
				m31 = r.match(p[31])
				items['m1'] = float(m1.group(1))*.10
				items['m2'] = float(m2.group(1))*.10
				items['m3'] = float(m3.group(1))*.10
				items['m4'] = float(m4.group(1))*.10
				items['m5'] = float(m5.group(1))*.10
				items['m6'] = float(m6.group(1))*.10
				items['m7'] = float(m7.group(1))*.10
				items['m8'] = float(m8.group(1))*.10	
				items['m9'] = float(m9.group(1))*.10
				items['m10'] = float(m10.group(1))*.10
				items['m11'] = float(m11.group(1))*.10
				items['m12'] = float(m12.group(1))*.10
				items['m13'] = float(m13.group(1))*.10
				items['m14'] = float(m14.group(1))*.10
				items['m15'] = float(m15.group(1))*.10
				items['m16'] = float(m16.group(1))*.10
				items['m17'] = float(m17.group(1))*.10
				items['m18'] = float(m18.group(1))*.10
				items['m19'] = float(m19.group(1))*.10
				items['m20'] = float(m20.group(1))*.10
				items['m21'] = float(m21.group(1))*.10
				items['m22'] = float(m22.group(1))*.10
				items['m23'] = float(m23.group(1))*.10
				items['m24'] = float(m24.group(1))*.10
				items['m25'] = float(m25.group(1))*.10
				items['m26'] = float(m26.group(1))*.10
				items['m27'] = float(m27.group(1))*.10
				items['m28'] = float(m28.group(1))*.10
				items['m29'] = float(m29.group(1))*.10
				items['m30'] = float(m30.group(1))*.10
				#items['m31'] = m31.group(1)
				items['m1Code'] = m1.group(2)
				items['m2Code'] = m2.group(2)
				items['m3Code'] = m3.group(2)	
				items['m4Code'] = m4.group(2)
				items['m5Code'] = m5.group(2)
				items['m6Code'] = m6.group(2)
				items['m7Code'] = m7.group(2)
				items['m8Code'] = m8.group(2)
				items['m9Code'] = m9.group(2)
				items['m10Code'] = m10.group(2)
				items['m11Code'] = m11.group(2)
				items['m12Code'] = m12.group(2)
				items['m13Code'] = m13.group(2)
				items['m14Code'] = m14.group(2)
				items['m15Code'] = m15.group(2)
				items['m16Code'] = m16.group(2)
				items['m17Code'] = m17.group(2)
				items['m18Code'] = m18.group(2)
				items['m19Code'] = m19.group(2)		
				items['m20Code'] = m20.group(2)
				items['m21Code'] = m21.group(2)
				items['m22Code'] = m22.group(2)
				items['m23Code'] = m23.group(2)
				items['m24Code'] = m24.group(2)
				items['m25Code'] = m25.group(2)
				items['m26Code'] = m26.group(2)
				items['m27Code'] = m27.group(2)
				items['m28Code'] = m28.group(2)
				items['m29Code'] = m29.group(2)
				items['m30Code'] = m30.group(2)
				#items['m31Code'] = m31.group(2)
				itemList.append(items)
		else:
			for line in fileOpen:
				items = {}
				p = line.split()
				items['stations'] = p[0]
				items['month'] = p[1]
				m1 = r.match(p[2])
				m2 = r.match(p[3])
				m3 = r.match(p[4])
				m4 = r.match(p[5])
				m5 = r.match(p[6])
				m6 = r.match(p[7])
				m7 = r.match(p[8])
				m8 = r.match(p[9])
				m9 = r.match(p[10])
				m10 = r.match(p[11])
				m11 = r.match(p[12])
				m12 = r.match(p[13])
				m13 = r.match(p[14])
				m14 = r.match(p[14])
				m15 = r.match(p[15])
				m16 = r.match(p[16])
				m17 = r.match(p[17])
				m18 = r.match(p[18])
				m19 = r.match(p[19])
				m20 = r.match(p[20])
				m21 = r.match(p[21])
				m22 = r.match(p[22])
				m23 = r.match(p[23])
				m24 = r.match(p[24])
				m25 = r.match(p[25])
				m26 = r.match(p[26])
				m27 = r.match(p[27])
				m28 = r.match(p[28])
				m29 = r.match(p[29])
				m30 = r.match(p[30])
				m31 = r.match(p[31])
				items['m1'] = float(m1.group(1))*.10
				items['m2'] = float(m2.group(1))*.10
				items['m3'] = float(m3.group(1))*.10
				items['m4'] = float(m4.group(1))*.10
				items['m5'] = float(m5.group(1))*.10
				items['m6'] = float(m6.group(1))*.10
				items['m7'] = float(m7.group(1))*.10
				items['m8'] = float(m8.group(1))*.10	
				items['m9'] = float(m9.group(1))*.10
				items['m10'] = float(m10.group(1))*.10
				items['m11'] = float(m11.group(1))*.10
				items['m12'] = float(m12.group(1))*.10
				items['m13'] = float(m13.group(1))*.10
				items['m14'] = float(m14.group(1))*.10
				items['m15'] = float(m15.group(1))*.10
				items['m16'] = float(m16.group(1))*.10
				items['m17'] = float(m17.group(1))*.10
				items['m18'] = float(m18.group(1))*.10
				items['m19'] = float(m19.group(1))*.10
				items['m20'] = float(m20.group(1))*.10
				items['m21'] = float(m21.group(1))*.10
				items['m22'] = float(m22.group(1))*.10
				items['m23'] = float(m23.group(1))*.10
				items['m24'] = float(m24.group(1))*.10
				items['m25'] = float(m25.group(1))*.10
				items['m26'] = float(m26.group(1))*.10
				items['m27'] = float(m27.group(1))*.10
				items['m28'] = float(m28.group(1))*.10
				items['m29'] = float(m29.group(1))*.10
				items['m30'] = float(m30.group(1))*.10
				#items['m31'] = m31.group(1)
				items['m1Code'] = m1.group(2)
				items['m2Code'] = m2.group(2)
				items['m3Code'] = m3.group(2)	
				items['m4Code'] = m4.group(2)
				items['m5Code'] = m5.group(2)
				items['m6Code'] = m6.group(2)
				items['m7Code'] = m7.group(2)
				items['m8Code'] = m8.group(2)
				items['m9Code'] = m9.group(2)
				items['m10Code'] = m10.group(2)
				items['m11Code'] = m11.group(2)
				items['m12Code'] = m12.group(2)
				items['m13Code'] = m13.group(2)
				items['m14Code'] = m14.group(2)
				items['m15Code'] = m15.group(2)
				items['m16Code'] = m16.group(2)
				items['m17Code'] = m17.group(2)
				items['m18Code'] = m18.group(2)
				items['m19Code'] = m19.group(2)		
				items['m20Code'] = m20.group(2)
				items['m21Code'] = m21.group(2)
				items['m22Code'] = m22.group(2)
				items['m23Code'] = m23.group(2)
				items['m24Code'] = m24.group(2)
				items['m25Code'] = m25.group(2)
				items['m26Code'] = m26.group(2)
				items['m27Code'] = m27.group(2)
				items['m28Code'] = m28.group(2)
				items['m29Code'] = m29.group(2)
				items['m30Code'] = m30.group(2)
				#items['m31Code'] = m31.group(2)
				itemList.append(items)

	elif 'snow' in filename:
			for line in fileOpen:
				items = {}
				p = line.split()
				items['stations'] = p[0]
				items['month'] = p[1]
				m1 = r.match(p[2])
				m2 = r.match(p[3])
				m3 = r.match(p[4])
				m4 = r.match(p[5])
				m5 = r.match(p[6])
				m6 = r.match(p[7])
				m7 = r.match(p[8])
				m8 = r.match(p[9])
				m9 = r.match(p[10])
				m10 = r.match(p[11])
				m11 = r.match(p[12])
				m12 = r.match(p[13])
				m13 = r.match(p[14])
				m14 = r.match(p[14])
				m15 = r.match(p[15])
				m16 = r.match(p[16])
				m17 = r.match(p[17])
				m18 = r.match(p[18])
				m19 = r.match(p[19])
				m20 = r.match(p[20])
				m21 = r.match(p[21])
				m22 = r.match(p[22])
				m23 = r.match(p[23])
				m24 = r.match(p[24])
				m25 = r.match(p[25])
				m26 = r.match(p[26])
				m27 = r.match(p[27])
				m28 = r.match(p[28])
				m29 = r.match(p[29])
				m30 = r.match(p[30])
				m31 = r.match(p[31])
				items['m1'] = float(m1.group(1))*.10
				items['m2'] = float(m2.group(1))*.10
				items['m3'] = float(m3.group(1))*.10
				items['m4'] = float(m4.group(1))*.10
				items['m5'] = float(m5.group(1))*.10
				items['m6'] = float(m6.group(1))*.10
				items['m7'] = float(m7.group(1))*.10
				items['m8'] = float(m8.group(1))*.10	
				items['m9'] = float(m9.group(1))*.10
				items['m10'] = float(m10.group(1))*.10
				items['m11'] = float(m11.group(1))*.10
				items['m12'] = float(m12.group(1))*.10
				items['m13'] = float(m13.group(1))*.10
				items['m14'] = float(m14.group(1))*.10
				items['m15'] = float(m15.group(1))*.10
				items['m16'] = float(m16.group(1))*.10
				items['m17'] = float(m17.group(1))*.10
				items['m18'] = float(m18.group(1))*.10
				items['m19'] = float(m19.group(1))*.10
				items['m20'] = float(m20.group(1))*.10
				items['m21'] = float(m21.group(1))*.10
				items['m22'] = float(m22.group(1))*.10
				items['m23'] = float(m23.group(1))*.10
				items['m24'] = float(m24.group(1))*.10
				items['m25'] = float(m25.group(1))*.10
				items['m26'] = float(m26.group(1))*.10
				items['m27'] = float(m27.group(1))*.10
				items['m28'] = float(m28.group(1))*.10
				items['m29'] = float(m29.group(1))*.10
				items['m30'] = float(m30.group(1))*.10
				#items['m31'] = m31.group(1)
				items['m1Code'] = m1.group(2)
				items['m2Code'] = m2.group(2)
				items['m3Code'] = m3.group(2)	
				items['m4Code'] = m4.group(2)
				items['m5Code'] = m5.group(2)
				items['m6Code'] = m6.group(2)
				items['m7Code'] = m7.group(2)
				items['m8Code'] = m8.group(2)
				items['m9Code'] = m9.group(2)
				items['m10Code'] = m10.group(2)
				items['m11Code'] = m11.group(2)
				items['m12Code'] = m12.group(2)
				items['m13Code'] = m13.group(2)
				items['m14Code'] = m14.group(2)
				items['m15Code'] = m15.group(2)
				items['m16Code'] = m16.group(2)
				items['m17Code'] = m17.group(2)
				items['m18Code'] = m18.group(2)
				items['m19Code'] = m19.group(2)		
				items['m20Code'] = m20.group(2)
				items['m21Code'] = m21.group(2)
				items['m22Code'] = m22.group(2)
				items['m23Code'] = m23.group(2)
				items['m24Code'] = m24.group(2)
				items['m25Code'] = m25.group(2)
				items['m26Code'] = m26.group(2)
				items['m27Code'] = m27.group(2)
				items['m28Code'] = m28.group(2)
				items['m29Code'] = m29.group(2)
				items['m30Code'] = m30.group(2)
				#items['m31Code'] = m31.group(2)
				itemList.append(items)

	elif 'snwd' in filename:
		if 'pctall' in filename: 
			for line in fileOpen:
				items = {}
				p = line.split()
				items['stations'] = p[0]
				items['month'] = p[1]
				m1 = r.match(p[2])
				m2 = r.match(p[3])
				m3 = r.match(p[4])
				m4 = r.match(p[5])
				m5 = r.match(p[6])
				m6 = r.match(p[7])
				m7 = r.match(p[8])
				m8 = r.match(p[9])
				m9 = r.match(p[10])
				m10 = r.match(p[11])
				m11 = r.match(p[12])
				m12 = r.match(p[13])
				m13 = r.match(p[14])
				m14 = r.match(p[14])
				m15 = r.match(p[15])
				m16 = r.match(p[16])
				m17 = r.match(p[17])
				m18 = r.match(p[18])
				m19 = r.match(p[19])
				m20 = r.match(p[20])
				m21 = r.match(p[21])
				m22 = r.match(p[22])
				m23 = r.match(p[23])
				m24 = r.match(p[24])
				m25 = r.match(p[25])
				m26 = r.match(p[26])
				m27 = r.match(p[27])
				m28 = r.match(p[28])
				m29 = r.match(p[29])
				m30 = r.match(p[30])
				m31 = r.match(p[31])
				items['m1'] = float(m1.group(1))*.10
				items['m2'] = float(m2.group(1))*.10
				items['m3'] = float(m3.group(1))*.10
				items['m4'] = float(m4.group(1))*.10
				items['m5'] = float(m5.group(1))*.10
				items['m6'] = float(m6.group(1))*.10
				items['m7'] = float(m7.group(1))*.10
				items['m8'] = float(m8.group(1))*.10	
				items['m9'] = float(m9.group(1))*.10
				items['m10'] = float(m10.group(1))*.10
				items['m11'] = float(m11.group(1))*.10
				items['m12'] = float(m12.group(1))*.10
				items['m13'] = float(m13.group(1))*.10
				items['m14'] = float(m14.group(1))*.10
				items['m15'] = float(m15.group(1))*.10
				items['m16'] = float(m16.group(1))*.10
				items['m17'] = float(m17.group(1))*.10
				items['m18'] = float(m18.group(1))*.10
				items['m19'] = float(m19.group(1))*.10
				items['m20'] = float(m20.group(1))*.10
				items['m21'] = float(m21.group(1))*.10
				items['m22'] = float(m22.group(1))*.10
				items['m23'] = float(m23.group(1))*.10
				items['m24'] = float(m24.group(1))*.10
				items['m25'] = float(m25.group(1))*.10
				items['m26'] = float(m26.group(1))*.10
				items['m27'] = float(m27.group(1))*.10
				items['m28'] = float(m28.group(1))*.10
				items['m29'] = float(m29.group(1))*.10
				items['m30'] = float(m30.group(1))*.10
				#items['m31'] = m31.group(1)
				items['m1Code'] = m1.group(2)
				items['m2Code'] = m2.group(2)
				items['m3Code'] = m3.group(2)	
				items['m4Code'] = m4.group(2)
				items['m5Code'] = m5.group(2)
				items['m6Code'] = m6.group(2)
				items['m7Code'] = m7.group(2)
				items['m8Code'] = m8.group(2)
				items['m9Code'] = m9.group(2)
				items['m10Code'] = m10.group(2)
				items['m11Code'] = m11.group(2)
				items['m12Code'] = m12.group(2)
				items['m13Code'] = m13.group(2)
				items['m14Code'] = m14.group(2)
				items['m15Code'] = m15.group(2)
				items['m16Code'] = m16.group(2)
				items['m17Code'] = m17.group(2)
				items['m18Code'] = m18.group(2)
				items['m19Code'] = m19.group(2)		
				items['m20Code'] = m20.group(2)
				items['m21Code'] = m21.group(2)
				items['m22Code'] = m22.group(2)
				items['m23Code'] = m23.group(2)
				items['m24Code'] = m24.group(2)
				items['m25Code'] = m25.group(2)
				items['m26Code'] = m26.group(2)
				items['m27Code'] = m27.group(2)
				items['m28Code'] = m28.group(2)
				items['m29Code'] = m29.group(2)
				items['m30Code'] = m30.group(2)
				#items['m31Code'] = m31.group(2)
				itemList.append(items)
		else:
			for line in fileOpen:
				items = {}
				p = line.split()
				items['stations'] = p[0]
				items['month'] = p[1]
				m1 = r.match(p[2])
				m2 = r.match(p[3])
				m3 = r.match(p[4])
				m4 = r.match(p[5])
				m5 = r.match(p[6])
				m6 = r.match(p[7])
				m7 = r.match(p[8])
				m8 = r.match(p[9])
				m9 = r.match(p[10])
				m10 = r.match(p[11])
				m11 = r.match(p[12])
				m12 = r.match(p[13])
				m13 = r.match(p[14])
				m14 = r.match(p[14])
				m15 = r.match(p[15])
				m16 = r.match(p[16])
				m17 = r.match(p[17])
				m18 = r.match(p[18])
				m19 = r.match(p[19])
				m20 = r.match(p[20])
				m21 = r.match(p[21])
				m22 = r.match(p[22])
				m23 = r.match(p[23])
				m24 = r.match(p[24])
				m25 = r.match(p[25])
				m26 = r.match(p[26])
				m27 = r.match(p[27])
				m28 = r.match(p[28])
				m29 = r.match(p[29])
				m30 = r.match(p[30])
				m31 = r.match(p[31])
				items['m1'] = float(m1.group(1))
				items['m2'] = float(m2.group(1))
				items['m3'] = float(m3.group(1))
				items['m4'] = float(m4.group(1))
				items['m5'] = float(m5.group(1))
				items['m6'] = float(m6.group(1))
				items['m7'] = float(m7.group(1))
				items['m8'] = float(m8.group(1))	
				items['m9'] = float(m9.group(1))
				items['m10'] = float(m10.group(1))
				items['m11'] = float(m11.group(1))
				items['m12'] = float(m12.group(1))
				items['m13'] = float(m13.group(1))
				items['m14'] = float(m14.group(1))
				items['m15'] = float(m15.group(1))
				items['m16'] = float(m16.group(1))
				items['m17'] = float(m17.group(1))
				items['m18'] = float(m18.group(1))
				items['m19'] = float(m19.group(1))
				items['m20'] = float(m20.group(1))
				items['m21'] = float(m21.group(1))
				items['m22'] = float(m22.group(1))
				items['m23'] = float(m23.group(1))
				items['m24'] = float(m24.group(1))
				items['m25'] = float(m25.group(1))
				items['m26'] = float(m26.group(1))
				items['m27'] = float(m27.group(1))
				items['m28'] = float(m28.group(1))
				items['m29'] = float(m29.group(1))
				items['m30'] = float(m30.group(1))
				#items['m31'] = m31.group(1)
				items['m1Code'] = m1.group(2)
				items['m2Code'] = m2.group(2)
				items['m3Code'] = m3.group(2)	
				items['m4Code'] = m4.group(2)
				items['m5Code'] = m5.group(2)
				items['m6Code'] = m6.group(2)
				items['m7Code'] = m7.group(2)
				items['m8Code'] = m8.group(2)
				items['m9Code'] = m9.group(2)
				items['m10Code'] = m10.group(2)
				items['m11Code'] = m11.group(2)
				items['m12Code'] = m12.group(2)
				items['m13Code'] = m13.group(2)
				items['m14Code'] = m14.group(2)
				items['m15Code'] = m15.group(2)
				items['m16Code'] = m16.group(2)
				items['m17Code'] = m17.group(2)
				items['m18Code'] = m18.group(2)
				items['m19Code'] = m19.group(2)		
				items['m20Code'] = m20.group(2)
				items['m21Code'] = m21.group(2)
				items['m22Code'] = m22.group(2)
				items['m23Code'] = m23.group(2)
				items['m24Code'] = m24.group(2)
				items['m25Code'] = m25.group(2)
				items['m26Code'] = m26.group(2)
				items['m27Code'] = m27.group(2)
				items['m28Code'] = m28.group(2)
				items['m29Code'] = m29.group(2)
				items['m30Code'] = m30.group(2)
				#items['m31Code'] = m31.group(2)
				itemList.append(items)
	else:
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			items['month'] = p[1]
			m1 = r.match(p[2])
			m2 = r.match(p[3])
			m3 = r.match(p[4])
			m4 = r.match(p[5])
			m5 = r.match(p[6])
			m6 = r.match(p[7])
			m7 = r.match(p[8])
			m8 = r.match(p[9])
			m9 = r.match(p[10])
			m10 = r.match(p[11])
			m11 = r.match(p[12])
			m12 = r.match(p[13])
			m13 = r.match(p[14])
			m14 = r.match(p[14])
			m15 = r.match(p[15])
			m16 = r.match(p[16])
			m17 = r.match(p[17])
			m18 = r.match(p[18])
			m19 = r.match(p[19])
			m20 = r.match(p[20])
			m21 = r.match(p[21])
			m22 = r.match(p[22])
			m23 = r.match(p[23])
			m24 = r.match(p[24])
			m25 = r.match(p[25])
			m26 = r.match(p[26])
			m27 = r.match(p[27])
			m28 = r.match(p[28])
			m29 = r.match(p[29])
			m30 = r.match(p[30])
			m31 = r.match(p[31])
			items['m1'] = float(m1.group(1))*.10
			items['m2'] = float(m2.group(1))*.10
			items['m3'] = float(m3.group(1))*.10
			items['m4'] = float(m4.group(1))*.10
			items['m5'] = float(m5.group(1))*.10
			items['m6'] = float(m6.group(1))*.10
			items['m7'] = float(m7.group(1))*.10
			items['m8'] = float(m8.group(1))*.10	
			items['m9'] = float(m9.group(1))*.10
			items['m10'] = float(m10.group(1))*.10
			items['m11'] = float(m11.group(1))*.10
			items['m12'] = float(m12.group(1))*.10
			items['m13'] = float(m13.group(1))*.10
			items['m14'] = float(m14.group(1))*.10
			items['m15'] = float(m15.group(1))*.10
			items['m16'] = float(m16.group(1))*.10
			items['m17'] = float(m17.group(1))*.10
			items['m18'] = float(m18.group(1))*.10
			items['m19'] = float(m19.group(1))*.10
			items['m20'] = float(m20.group(1))*.10
			items['m21'] = float(m21.group(1))*.10
			items['m22'] = float(m22.group(1))*.10
			items['m23'] = float(m23.group(1))*.10
			items['m24'] = float(m24.group(1))*.10
			items['m25'] = float(m25.group(1))*.10
			items['m26'] = float(m26.group(1))*.10
			items['m27'] = float(m27.group(1))*.10
			items['m28'] = float(m28.group(1))*.10
			items['m29'] = float(m29.group(1))*.10
			items['m30'] = float(m30.group(1))*.10
			#items['m31'] = m31.group(1)
			items['m1Code'] = m1.group(2)
			items['m2Code'] = m2.group(2)
			items['m3Code'] = m3.group(2)	
			items['m4Code'] = m4.group(2)
			items['m5Code'] = m5.group(2)
			items['m6Code'] = m6.group(2)
			items['m7Code'] = m7.group(2)
			items['m8Code'] = m8.group(2)
			items['m9Code'] = m9.group(2)
			items['m10Code'] = m10.group(2)
			items['m11Code'] = m11.group(2)
			items['m12Code'] = m12.group(2)
			items['m13Code'] = m13.group(2)
			items['m14Code'] = m14.group(2)
			items['m15Code'] = m15.group(2)
			items['m16Code'] = m16.group(2)
			items['m17Code'] = m17.group(2)
			items['m18Code'] = m18.group(2)
			items['m19Code'] = m19.group(2)		
			items['m20Code'] = m20.group(2)
			items['m21Code'] = m21.group(2)
			items['m22Code'] = m22.group(2)
			items['m23Code'] = m23.group(2)
			items['m24Code'] = m24.group(2)
			items['m25Code'] = m25.group(2)
			items['m26Code'] = m26.group(2)
			items['m27Code'] = m27.group(2)
			items['m28Code'] = m28.group(2)
			items['m29Code'] = m29.group(2)
			items['m30Code'] = m30.group(2)
			#items['m31Code'] = m31.group(2)
			itemList.append(items)
	fileOpen.close()
	return itemList

def readMonthly(filename, product):
	fileOpen = open(product +'/' + filename, 'r')
	r = re.compile("([-]?[0-9]+)([A-Z]+)")
	itemArray = []
	if 'htdd' in filename:					#this should be whole 
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			jan = r.match(p[1])
			feb = r.match(p[2])
			mar = r.match(p[3])
			apr = r.match(p[4])
			may = r.match(p[5])
			jun = r.match(p[6])
			jul = r.match(p[7])
			aug = r.match(p[8])
			sep = r.match(p[9])
			octr = r.match(p[10])
			nov = r.match(p[11])
			dec = r.match(p[12])
			items['jan'] = jan.group(1)
			items['feb'] = feb.group(1)
			items['mar'] = mar.group(1)
			items['apr'] = apr.group(1)
			items['may'] = may.group(1)
			items['jun'] = jun.group(1)
			items['jul'] = jul.group(1)
			items['aug'] = aug.group(1)
			items['sep'] = sep.group(1)
			items['octr'] = octr.group(1)
			items['nov'] = nov.group(1)
			items['dec'] = dec.group(1)
			items['janCode'] = jan.group(2)
			items['febCode'] = feb.group(2)
			items['marCode'] = mar.group(2)
			items['aprCode'] = apr.group(2)
			items['mayCode'] = may.group(2)
			items['junCode'] = jun.group(2)
			items['julCode'] = jul.group(2)
			items['augCode'] = aug.group(2)
			items['sepCode'] = sep.group(2)
			items['octrCode'] = octr.group(2)
			items['novCode'] = nov.group(2)
			items['decCode'] = dec.group(2)
			itemArray.append(items)
	elif 'cldd' in filename: 					#this should be whole
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			jan = r.match(p[1])
			feb = r.match(p[2])
			mar = r.match(p[3])
			apr = r.match(p[4])
			may = r.match(p[5])
			jun = r.match(p[6])
			jul = r.match(p[7])
			aug = r.match(p[8])
			sep = r.match(p[9])
			octr = r.match(p[10])
			nov = r.match(p[11])
			dec = r.match(p[12])
			items['jan'] = jan.group(1)
			items['feb'] = feb.group(1)
			items['mar'] = mar.group(1)
			items['apr'] = apr.group(1)
			items['may'] = may.group(1)
			items['jun'] = jun.group(1)
			items['jul'] = jul.group(1)
			items['aug'] = aug.group(1)
			items['sep'] = sep.group(1)
			items['octr'] = octr.group(1)
			items['nov'] = nov.group(1)
			items['dec'] = dec.group(1)
			items['janCode'] = jan.group(2)
			items['febCode'] = feb.group(2)
			items['marCode'] = mar.group(2)
			items['aprCode'] = apr.group(2)
			items['mayCode'] = may.group(2)
			items['junCode'] = jun.group(2)
			items['julCode'] = jul.group(2)
			items['augCode'] = aug.group(2)
			items['sepCode'] = sep.group(2)
			items['octrCode'] = octr.group(2)
			items['novCode'] = nov.group(2)
			items['decCode'] = dec.group(2)
			itemArray.append(items)
	elif 'prcp' in filename: 		 #this should be *.01
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			jan = r.match(p[1])
			feb = r.match(p[2])
			mar = r.match(p[3])
			apr = r.match(p[4])
			may = r.match(p[5])
			jun = r.match(p[6])
			jul = r.match(p[7])
			aug = r.match(p[8])
			sep = r.match(p[9])
			octr = r.match(p[10])
			nov = r.match(p[11])
			dec = r.match(p[12])
			items['jan'] = float(jan.group(1))*.01
			items['feb'] = float(feb.group(1))*.01
			items['mar'] = float(mar.group(1))*.01
			items['apr'] = float(apr.group(1))*.01
			items['may'] = float(may.group(1))*.01
			items['jun'] = float(jun.group(1))*.01
			items['jul'] = float(jul.group(1))*.01
			items['aug'] = float(aug.group(1))*.01
			items['sep'] = float(sep.group(1))*.01
			items['octr'] = float(octr.group(1))*.01
			items['nov'] = float(nov.group(1))*.01
			items['dec'] = float(dec.group(1))*.01
			items['janCode'] = jan.group(2)
			items['febCode'] = feb.group(2)
			items['marCode'] = mar.group(2)
			items['aprCode'] = apr.group(2)
			items['mayCode'] = may.group(2)
			items['junCode'] = jun.group(2)
			items['julCode'] = jul.group(2)
			items['augCode'] = aug.group(2)
			items['sepCode'] = sep.group(2)
			items['octrCode'] = octr.group(2)
			items['novCode'] = nov.group(2)
			items['decCode'] = dec.group(2)
			itemArray.append(items)
	elif 'snwd' in filename:   #this should be a whole digit
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			jan = r.match(p[1])
			feb = r.match(p[2])
			mar = r.match(p[3])
			apr = r.match(p[4])
			may = r.match(p[5])
			jun = r.match(p[6])
			jul = r.match(p[7])
			aug = r.match(p[8])
			sep = r.match(p[9])
			octr = r.match(p[10])
			nov = r.match(p[11])
			dec = r.match(p[12])
			items['jan'] = jan.group(1)
			items['feb'] = feb.group(1)
			items['mar'] = mar.group(1)
			items['apr'] = apr.group(1)
			items['may'] = may.group(1)
			items['jun'] = jun.group(1)
			items['jul'] = jul.group(1)
			items['aug'] = aug.group(1)
			items['sep'] = sep.group(1)
			items['octr'] = octr.group(1)
			items['nov'] = nov.group(1)
			items['dec'] = dec.group(1)
			items['janCode'] = jan.group(2)
			items['febCode'] = feb.group(2)
			items['marCode'] = mar.group(2)
			items['aprCode'] = apr.group(2)
			items['mayCode'] = may.group(2)
			items['junCode'] = jun.group(2)
			items['julCode'] = jul.group(2)
			items['augCode'] = aug.group(2)
			items['sepCode'] = sep.group(2)
			items['octrCode'] = octr.group(2)
			items['novCode'] = nov.group(2)
			items['decCode'] = dec.group(2)
			itemArray.append(items)
	else: 
		for line in fileOpen:
			items = {}
			p = line.split()
			items['stations'] = p[0]
			jan = r.match(p[1])
			feb = r.match(p[2])
			mar = r.match(p[3])
			apr = r.match(p[4])
			may = r.match(p[5])
			jun = r.match(p[6])
			jul = r.match(p[7])
			aug = r.match(p[8])
			sep = r.match(p[9])
			octr = r.match(p[10])
			nov = r.match(p[11])
			dec = r.match(p[12])
			items['jan'] = float(jan.group(1))*.10
			items['feb'] = float(feb.group(1))*.10
			items['mar'] = float(mar.group(1))*.10
			items['apr'] = float(apr.group(1))*.10
			items['may'] = float(may.group(1))*.10
			items['jun'] = float(jun.group(1))*.10
			items['jul'] = float(jul.group(1))*.10
			items['aug'] = float(aug.group(1))*.10
			items['sep'] = float(sep.group(1))*.10
			items['octr'] = float(octr.group(1))*.10
			items['nov'] = float(nov.group(1))*.10
			items['dec'] = float(dec.group(1))*.10
			items['janCode'] = jan.group(2)
			items['febCode'] = feb.group(2)
			items['marCode'] = mar.group(2)
			items['aprCode'] = apr.group(2)
			items['mayCode'] = may.group(2)
			items['junCode'] = jun.group(2)
			items['julCode'] = jul.group(2)
			items['augCode'] = aug.group(2)
			items['sepCode'] = sep.group(2)
			items['octrCode'] = octr.group(2)
			items['novCode'] = nov.group(2)
			items['decCode'] = dec.group(2)
			itemArray.append(items)
	fileOpen.close()
	return itemArray
		#print itemArray

def writeHeader(fileName):
	header = ['lat', 'lon', 'stations', 'data', 'code']
	myFile = open('output/' + fileName, 'w')
	myFile.write('\t'.join(header) + '\n')
	myFile.close()


def writeDly(itemList, stationList):
	print 'what would you like to name the output file: '
	fileName = raw_input("> ")
	while os.path.exists('output/' + fileName):
		print 'the file already exists pick another filename please: '
		fileName = raw_input("> ")

	header = ['lat', 'lon', 'stations', 'data', 'code']
	myFile = open('output/' + fileName, 'w')
	# for (key, value) in set(fileItems.items()) & set(stationInfo.items()):
	# 	  print '%s: %s is present in both aa and bb' % (key, value)
	myFile.write(','.join(header) + '\n')
	for items in itemList:
		for stations in stationList:
			if items['stations'] in stations['stations']:
				myFile.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s\n" % (stations['lat'], stations['long'], items['stations'], items['month'], 
					items['m1'], items['m1Code'], items['m2'], items['m2Code'], items['m3'], items['m3Code'], items['m4'], items['m4Code'], items['m5'], 
					items['m5Code'], items['m6'], items['m6Code'], items['m7'], items['m7Code'], items['m8'], items['m8Code'], items['m9'], items['m9Code'], items['m10'], items['m10Code'], items['m11'], items['m11Code'], 
					items['m12'], items['m12Code'], items['m13'], items['m13Code'], items['m14'], items['m14Code'], items['m15'], items['m15Code'], items['m16'], items['m16Code'], items['m17'], 
					items['m17Code'], items['m18'], items['m18Code'], items['m19'], items['m19Code'], items['m20'], items['m20Code'], items['m21'], items['m21Code'], items['m22'], items['m22Code'], items['m23'], items['m23Code'], 
					items['m24'], items['m24Code'], items['m25'], items['m25Code'], items['m26'], items['m26Code'], items['m27'], items['m27Code'], items['m28'], items['m28Code'], items['m29'], 
					items['m29Code'], items['m30'], items['m30Code']))
	myFile.close()

def writemly(itemArray, stationList): 
	print 'what would you like to name the output file: '
	fileName = raw_input("> ")
	while os.path.exists('output/' + fileName):
		print 'the file already exists pick another filename please: '
		fileName = raw_input("> ")
	header = ['lat', 'lon', 'stations', 'data', 'code']
	myFile = open('output/' + fileName, 'w')
	# for (key, value) in set(fileItems.items()) & set(stationInfo.items()):
	# 	  print '%s: %s is present in both aa and bb' % (key, value)
	print itemArray
	myFile.write(','.join(header) + '\n')
	for items in itemArray:
		for stations in stationList:
			if items['stations'] in stations['stations']:
				
				#print items['data']
				#myFile.write('\n','	\t'.join(items['stations'], items['data']))
				myFile.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (stations['lat'], stations['long'], items['stations'], items['jan'], items['janCode'],  
					items['feb'], items['febCode'], items['mar'], items['marCode'], items['apr'], items['aprCode'], items['may'], items['mayCode'], 
					items['jun'], items['junCode'], items['jul'], items['julCode'], items['aug'], items['augCode'], items['sep'], items['sepCode'], 
					items['octr'], items['octrCode'], items['nov'], items['novCode'], items['dec'], items['decCode']))
	myFile.close()

def writeData(itemlist, stationList): 
	print 'what would you like to name the output file: '
	fileName = raw_input("> ")
	while os.path.exists('output/' + fileName):
		print 'the file already exists pick another filename please: '
		fileName = raw_input("> ")
	header = ['lat', 'lon', 'stations', 'data', 'code']
	myFile = open('output/' + fileName, 'w')
	# for (key, value) in set(fileItems.items()) & set(stationInfo.items()):
	# 	  print '%s: %s is present in both aa and bb' % (key, value)
	myFile.write(','.join(header) + '\n')
	for items in itemlist:
		for stations in stationList:
			if items['stations'] in stations['stations']:
				
				#print items['data']
				#myFile.write('\n','	\t'.join(items['stations'], items['data']))
				myFile.write("%s, %s, %s, %s, %s\n" % (stations['lat'], stations['long'], items['stations'], 
					items['data'], items['code']))
	myFile.close()
if __name__ == '__main__': 
	main()