#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys
import datetime
import os
import shutil
from sys import argv

csv.register_dialect('excel', delimiter='|', quoting=csv.QUOTE_NONE)
now = datetime.datetime.now()

myDate = now.strftime("%Y%m%d%H%M%S")
shortDate = now.strftime("%M%S")

# destynacje w jestblue
dest = [ "ANC","ABQ","ACK","ALB","ANU","AUA","AUS","AZS","BDA","BDL","BGI","BOG","BOS","BQN","BTV","BUF","BUR","BWI","CHS","CLE","CLT","CTG","CUN","CUR","DCA","DEN","DFW","DTW","EWR","FLL","GCM","GND","HOU","HPN","HYA","IAD","JAX","JFK","KIN","LAS","LAX","LGA","LGB","LIM","LIR","LRM","MBJ","MCO","MDE","MEX","MSY","MVY","NAS","OAK","ORD","ORH","PAP","PBI","PDX","PHL","PHX","PIT","PLS","POP","POS","PSE","PSP","PUJ","PVD","PWM","RDU","RIC","RNO","ROC","RSW","SAN","SAV","SDQ","SEA","SFO","SJC","SJO","SJU","SLC","SMF","SRQ","STI","STT","STX","SWF","SXM","SYR","TPA","UVF"]

# for i in dest:
#     print i



ileuserow = input("Ile elementow > ")


print dest[1]

for i in range (0, ileuserow):
    print dest[i]
