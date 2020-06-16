#!/usr/bin/env python3

# NOTE: BEFORE USING SEE https://github.com/maxlklaxl/python-tsl2591 


import tsl2591
import os
import datetime
import csv

tsl = tsl2591.Tsl2591() # initialize
full, ir = tsl.get_full_luminosity() # read raw values (full spectrum and ir spectrum)
lux = tsl.calculate_lux(full, ir) # convert raw values to lux


# call the date and time from datetime
now = datetime.datetime.now()
# file to work with
csvFile = 'lightlux.csv'
# create csv header if not already
firstRow = "Lux, Full, IR, Date (ymd), Time\n"
if not os.access(csvFile,os.F_OK):
	with open(csvFile, 'a') as fd:
		fd.write(firstRow)
# append data to csv
currentRow = "{L},{F},{I},{D},{t}\n".format(L=lux,F=full,I=ir,D=now.strftime("%Y-%m-%d"),t=now.strftime("%H:%M:%S"))
with open(csvFile, 'a') as fd:
	fd.write(currentRow)



