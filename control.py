#!/usr/bin/python

import os
import time
import urllib, urllib2
import json

url = "http://www.temporary-agency.com/ws/ws_get_metrics.php"
previous_sector=1
while True:
	time.sleep(10)

	response = urllib2.urlopen(url)
	data = json.load(response)   
	print data

	last_10s=int(str(data['rows'][0]['last_10s']))
	last_mn=int(str(data['rows'][0]['last_mn']))
	last_5mn=int(str(data['rows'][0]['last_5mn']))
	last_h=int(str(data['rows'][0]['last_hour']))
	print last_10s,last_mn,last_5mn,last_h

	sector=1
	if last_10s>0:
		sector=4
	elif last_mn>0:
		sector=3
	elif last_5mn>0:
		sector=2

	if sector <> previous_sector:
		print "Going to sector ",sector
		previous_sector=sector

		# Control the servo based on this information
		os.system("/home/pi/Projects/arduino-controller/servocontrol.py "+str(sector))



