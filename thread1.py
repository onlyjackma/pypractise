#!/usr/bin/env python
import threading
import time
import os

def doChore():
	time.sleep(1)

def booth(tid):
	global i 
	global lock
	while True:
		lock.acquire()
		if i != 0 :
			i = i - 1
			print(tid,':now left :',i)
			doChore()
		else:
			print('Thread_id',tid,"No more tickets")
			os._exit(0)
		lock.release()
		doChore()

i = 100
lock = threading.Lock()

for k in range(10):
	new_thread = threading.Thread(target=booth,args=(k,))
	new_thread.start();
