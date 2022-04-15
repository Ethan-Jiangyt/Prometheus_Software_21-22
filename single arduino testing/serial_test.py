import os
import serial

ser = serial.Serial('COM4', 9600)

while True:
    try:
        line = ser.readline().decode()[:-1] #TC1,TC2,TC3,TC4,PT1,PT2,PT3,PT4,LC
        data = line.split(',')
        print(data)
    except:
        os._exit(1)
