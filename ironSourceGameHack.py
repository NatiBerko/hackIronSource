import autopy
import win32api
import win32con
from serial import Serial


def click(x, y):
    autopy.mouse.move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


ser = Serial('COM5', baudrate=19200, timeout=1)
ready = False
while True:
    arduinoData = ser.readline()
    arduinoData = str(arduinoData).split("'")[1]
    arduinoData = arduinoData.split("\\")[0]
    #print(arduinoData)
    if arduinoData == "True":
        ready = True
    if arduinoData != "" and arduinoData != "True":
        if int(arduinoData) > 320 and ready is True:
            print(arduinoData)
            click(400, 500)
            ready = False
