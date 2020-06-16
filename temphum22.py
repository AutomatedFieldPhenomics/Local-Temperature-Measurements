#!/usr/bin/env python3

# for use with a DHT22 sensor 

import Adafruit_DHT as dht
import datetime
import os
import csv

# call the date and time
now = datetime.datetime.now()
# file to work with
csvFile = 'THstats22.csv'
# create csv header if not already
firstRow = 'Temperature [C], Humidity [%], Date [ymd], Time\n'
if not os.access(csvFile,os.F_OK):
	with open(csvFile, 'a') as fd:
		fd.write(firstRow)

# set data pin
DHT = 22
# read temp and hum from DHT22
humidity, temperature = dht.read_retry(dht.DHT22, DHT)
# append data to csv
currentRow = '{T},{H},{D},{t}\n'.format(T=temperature,H=humidity,D=now.strftime("%Y-%m-%d"),t=now.strftime("%H:%M:%S"))
with open(csvFile, 'a') as fd:
	fd.write(currentRow)


