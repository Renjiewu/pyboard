# main.py -- put your code here!
import pyb
import math
import random

switch = pyb.Switch()
accel = pyb.Accel()
hid = pyb.USB_HID()


def hcf(x, y):
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x
    res = 0
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            res = i
    return res


def change_mouse():
    while True:
        # if switch.value()
        hid.send((switch.value(), accel.x(), accel.y(), 0))
        pyb.delay(20)


def change_mouse_to(x, y, k, d):
    for i in range(abs(x)):
        hid.send((k, int(x / abs(x)), 0, 0))
        pyb.delay(d)
    for i in range(abs(y)):
        hid.send((k, 0, int(y / abs(y)), 0))
        pyb.delay(d)


def change_mouse_to_x(x, y, k, d):
    for i in range(int(abs(x) / 5)):
        hid.send((k, int(x / abs(x) * 5), random.randint(-2, 2), 0))
        pyb.delay(d)
    for i in range(int(abs(y) / 5)):
        hid.send((k, 0, int(y / abs(y) * 5), 0))
        pyb.delay(d)
    change_mouse_to(50, 0, k, d)
    change_mouse_to(-50, 0, k, d)
    hid.send((0, 0, 0, 0))

def change_mouse_to_s(x, y, k, d):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(int(abs(smaller) / 5)):
        hid.send((k, int(x / abs(x) * 5), random.randint(-2, 2), 0))
        pyb.delay(d)

    # change_mouse_to(50, 0, k, d)
    # change_mouse_to(-50, 0, k, d)
    hid.send((0, 0, 0, 0))