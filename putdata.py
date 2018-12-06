#!/usr/bin/env python3
import sys
import time
import serial
import datetime
import socket
import psutil
import os
import time
import random
from time import gmtime, strftime

baza='pomiary4'

from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.create_database(baza)
#client.get_list_database()
client.switch_database(baza)

dancpu=0
dancpu=random.random()
#dancpu=psutil.cpu_percent(interval=1)
while 1:
	now = datetime.datetime.now()
	now2 = strftime("%Y-%m-%d %H:%M:%S", gmtime());
	json_body = [
	    {
	        "measurement": "pomiary",
	        "tags": {
	            "user": "Carols",
	            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
	        },
	        "time": now2,
	        "fields": {
	            "cpuload": dancpu
	        }
	    }
	]
	client.write_points(json_body)
	print(dancpu,", ",now2)
	dancpu=random.random()
	#psutil.cpu_percent(interval=1)
	time.sleep(5)
