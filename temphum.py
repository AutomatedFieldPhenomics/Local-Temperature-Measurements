#!/usr/bin/env python
import sys
import Adafruit_DHT
import datetime
import csv

# call the time and date from datetime
now = datetime.datetime.now()

# get T & H values
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

# append the data to existing csv or create new one if csv does not exist
currentRow = "Temperature: {T}, Humidity: {H}, Date: {D}, Time: {t}\n".format(T=temperature,H=humidity,D=now.strftime("%Y-%m-%d"),t=now.strftime("%H:%M:%S"))
with open('THstats.csv', 'a') as fd:
  fd.write(currentRow)
