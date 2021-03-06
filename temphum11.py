#!/usr/bin/env python

# This is for use with a DHT11 sensor

import Adafruit_DHT
import datetime
import csv
import os

# call the time and date from datetime
now = datetime.datetime.now()

# file to work with
csvFile = 'THstats.csv'

# create csv heading if not already existant
firstRow = "Temperature [C], Humidity [%], Date [ymd], Time\n"
if not os.access(csvFile,os.F_OK):
  with open(csvFile, 'a') as fd:
    fd.write(firstRow)

# get T & H values
humidity, temperature = Adafruit_DHT.read_retry(11, 22)

# append the data to existing csv or create new one if csv does not exist
currentRow = "{T},{H},{D},{t}\n".format(T=temperature,H=humidity,D=now.strftime("%Y-%m-%d"),t=now.strftime("%H:%M:%S"))
with open(csvFile, 'a') as fd:
  fd.write(currentRow)
