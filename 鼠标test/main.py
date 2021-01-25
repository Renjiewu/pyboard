# main.py -- put your code here!
import pyb

switch = pyb.Switch()
accel = pyb.Accel()
hid = pyb.USB_HID()

f = 1

while True:
	# if switch.value()
	hid.send((switch.value(), accel.x(), accel.y(), 0))
	pyb.delay(20)