#!/usr/bin/env python
with open("new.txt","a+") as f:
	print(f.closed)
	f.write("hello man!\n")
print(f.closed)



