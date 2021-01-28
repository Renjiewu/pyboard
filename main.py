# main.py -- put your code here!
import pyb
hid=pyb.USB_HID()
def release_key_once():
    buf = bytearray(8) # report is 8 bytes long
    buf[2] = 0
    hid.send(buf) # key released
    pyb.delay(10)
def press_key_once(key):
    buf = bytearray(8) # report is 8 bytes long
    buf[2] = key
    hid.send(buf) # key released
    pyb.delay(10)
def press_2key(key1,key2):
    buf = bytearray(8) # report is 8 bytes long
    buf[0] = key1
    buf[2] = key2
    hid.send(buf) # key released
    pyb.delay(10)
def release_2key():
    buf = bytearray(8) # report is 8 bytes long
    buf[0] = 0
    buf[2] = 0
    hid.send(buf) # key released
    pyb.delay(10)