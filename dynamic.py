#!/usr/bin/env python
def f1(x):
	x = 100
	print x
a=1
f1(a)
print a

def f2(c):
	c[0] = 210
	print c

b = [1,2,3]
f2(b)
print b
