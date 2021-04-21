import pyb
from pyb import UART
import re

# 串口6初始化
uart = UART(6, 115200, timeout=100)
# 响应报文
servo1 = pyb.Servo(1)
servo2 = pyb.Servo(2)
servo1.angle(-45)
servo2.angle(-45)

servo_x = {
    '1': servo1,
    '2': servo2,
}

def click_ukey(servo1=servo1, times=1):
    if servo1:
        pass
    else:
        return 0
    for i in range(times):
        servo1.angle(-30)
        pyb.delay(200)
        servo1.angle(-45)
        pyb.delay(200)
    return 1

def click_op(params, servo_x):
    t = int(params.get('time')) if params.get('time') else 1
    x = params.get('ID') if params.get('ID') else '0'
    res = click_ukey(servo1=servo_x.get(x), times=t)
    return res

header = """HTTP/1.1 200 OK
Content-Type:text/html
Content-Length:{0}

{1}
"""
# HTML页面
html = """<!DOCTYPE html>
<html>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <head> <title>TPYBoard</title> </head>
    <body>
      <h1>TPYBoard v201</h1><br />
      <h2>Simple HTTP server</h2>
    </body>
</html>
"""
def get_res(header, data):
    return header.format(len(data), data)

def get_request(data):
    x1 = re.compile('GET')
    x1_sub = re.compile('favicon.ico')
    x2 = re.compile('click_ukey')
    if x1.match(data) and not x1_sub.search(data):
        if x2.search(data):
            return 1
        else:
            return 2
    else:
        return 0

def get_params(data):
    res = {}
    try:
        x0 = re.compile('GET.+ HTTP')
        data = x0.search(data).group(0)
        print(data)
        x1 = re.compile(r'[\? ]+')
        x2 = re.compile(r'&')
        x3 = re.compile(r'=')
        if x1.search(data):
            tmp_x = x1.split(data.split(' ')[1])[1]
            print(tmp_x)
            for i in x2.split(tmp_x):
                print(i)
                xx = x3.split(i)
                print(xx)
                res[str(xx[0])] = str(xx[1])
        print(res)
    except Exception as e:
        print(e)
        pass
    finally:
        return res

while True:
    if uart.any() > 0:
        params = {}
        request = uart.read().decode()
        print('request:', request)
        # 当接收到GET请求头时，进行响应
        flag = 0
        flag = get_request(request)
        if flag == 2:
            data = get_res(header, html)
            uart.write(data)
        elif flag == 1:
            res = click_op(get_params(request), servo_x)
            data = get_res(header, '{code:200, data:"click_ukey", res:' + str(res) + '}')
            print(data)
            uart.write(data)