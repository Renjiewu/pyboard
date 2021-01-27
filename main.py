# main.py -- put your code here!
import pyb
from pyb import Switch
def f():
	pyb.delay(50)
	if(sw()):
		for i in range(1,5):
			pyb.LED(i).toggle()
			pyb.delay(200)
sw=Switch()
sw.callback(f)