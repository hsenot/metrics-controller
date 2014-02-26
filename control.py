#!/usr/bin/python

import os
import urllib, urllib2
import json

url = "http://www.temporary-agency.com/ws/ws_get_metrics.php"

response = urllib2.urlopen(url)
data = json.load(response)   
print data

last_mn=int(str(data['rows'][0]['last_mn']))
last_5mn=int(str(data['rows'][0]['last_5mn']))
last_h=int(str(data['rows'][0]['last_hour']))
last_4h=int(str(data['rows'][0]['last_4hour']))
print last_mn,last_5mn,last_h,last_4h

sector=1
if last_mn>0:
	sector=4
elif last_5mn>0:
	sector=3
elif last_h>0:
	sector=2
print "Going to sector ",sector

# Control the servo based on this information
os.system("/home/pi/Projects/arduino-controller/servocontrol.py "+str(sector))



