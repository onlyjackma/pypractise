#!/usr/bin/env python 
import datetime
t = datetime.datetime(2014,2,28,11,6)
print t.weekday()
print t.month
print t.year
print t.day

tdt = datetime.datetime.now()

print tdt.strftime("%A")
print tdt.strftime("%U")
