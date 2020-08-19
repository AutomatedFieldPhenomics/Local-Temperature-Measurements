#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import datetime
import os
from gpiozero import LED
import csv


#### GET THE MOST RECENT VALUE FROM THE LIGHTLUX CSV FILE ####
def readCSV():
	csvFile = 'lightlux.csv'
	with open(csvFile) as f:
		csv_reader = csv.reader(f, delimiter=',')
		lineCount =0
		for row in f:
			lineCount +=1
	with open(csvFile) as d:
		csv_reader = csv.reader(d, delimiter=',')
		lineCount2 = 0
		for row in d:
			lineCount2 +=1
			if lineCount2 == lineCount:
				row = row.split(',')
				lightVal = row[1]
				#print(row)
		return lightVal
lightVal = int(readCSV())
########################
led1 = LED(23)
led2 = LED(24)
led1.on()
led2.on()
camera = PiCamera()
#### READ THE LIGHTLUX CSV AND IF THE VALUE IS 0, THEN INITIATE NIGHT MODE ####
if lightVal ==0:
	camera.start_preview()
	sleep(2)
	now = datetime.datetime.now()
	dir = "images/%s" % now.strftime("%Y-%m-%d")
	if not os.path.exists(dir):
		os.makedirs(dir)
	camera.ISO = 100
	gains = (8,8)
	camera.awb_mode = 'off'
	camera.awb_gains = gains
	camera.capture('%s/%s.png' % (dir, now.strftime("%H:%M:%S")))


#### IF THE LIGHTLUX CSV VALUE IS GREATER THAN 0, INITIATE AUTOMATIC CAMERA SETTINGS ####
if lightVal >0:
	camera.start_preview()
	sleep(2)
	now = datetime.datetime.now()
	dir = "images/%s" % now.strftime("%Y-%m-%d")
	if not os.path.exists(dir):
		os.makedirs(dir)
	gains2 = (0.74,1.18)
	camera.awb_mode = 'off'
	camera.awb_gains = gains2
	camera.capture('%s/%s.png' % (dir, now.strftime("%H:%M:%S")))


camera.stop_preview()
led1.off()
led2.off()
