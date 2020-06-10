#!/usr/bin/env python
import sys
import Adafruit_DHT
import datetime
import csv
import os

# call the time and date from datetime
now = datetime.datetime.now()

# file to work with
csvFile = 'THstats.csv'

# create csv heading if not already existant
firstRow = "Temperature, Humidity, Date, Time"
if not os.access(csvFile,os.F_OK):
  with open(csvFile, 'a') as fd:
    fd.write(firstRow)

# get T & H values
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

# append the data to existing csv or create new one if csv does not exist
currentRow = "{T},{H},{D},{t}\n".format(T=temperature,H=humidity,D=now.strftime("%Y-%m-%d"),t=now.strftime("%H:%M:%S"))
with open(csvFile, 'a') as fd:
  fd.write(currentRow)
