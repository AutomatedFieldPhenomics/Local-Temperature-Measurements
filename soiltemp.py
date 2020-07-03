#!/usr/bin/env python3 

# for use with DS18b20 sensor 

import os
import datetime
import csv
import subprocess
# NOTE: BEFORE THIS PROGRAM WILL WORK FOR THE FIRST TIME,
# "dtoverlay=w1-gpio" MUST BE APPENDED TO THE BOTTOM OF /boot/config.txt
# PI SHOULD THEN BE REBOOTED

# Identify the w1 slave name:
com = subprocess.check_output('ls -l /sys/bus/w1/devices', shell=True)
devName = com[46:61]

# function to read the temperature from ds18b20 sensor on i2cdef 
def read_temperature():
	tempfile = open('/sys/bus/w1/devices/{}/w1_slave'.format(devName))
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split('\n')[1].split(' ')[9]
	temperature = float(tempdata[2:])
	temperature = temperature/1000
	return temperature
temperature = read_temperature()
# create soiltemp.csv file
csvFile = 'soiltemp.csv'
now = datetime.datetime.now()
firstRow = 'Soil Temperature (C), Date (ymd), Time\n'
if not os.access(csvFile,os.F_OK):
	with open(csvFile, 'a') as fd:
		fd.write(firstRow)

currentRow = '{T},{D},{t}\n'.format(T=temperature,D=now.strftime("%Y-%m-%d"),t=now.strftime("%H:%M:%S"))
with open(csvFile, 'a') as fd:
	fd.write(currentRow)
