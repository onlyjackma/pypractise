#!/usr/bin/env python
re = iter(range(5))
try:
	for i in range(100):
		print re.next()
except StopIteration:
	print 'you are reach the end ', i
finally:
	print 'finally you are ended'

print "i ma here haha!"
def func(x):
    try:
        return ++x
    finally:
        return x+1
print func(11)
