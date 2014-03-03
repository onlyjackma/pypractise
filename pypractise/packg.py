#!/usr/bin/env python
flist = []
 
for i in xrange(3):
    def func(x): return x * i
    flist.append(func)
 
for f in flist:
    print f(2)

def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

def gen2():
    for i in range(4):
        yield i

for j in gen2():
	print j

xl = [1,3,5]
yl = [9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]

print L
