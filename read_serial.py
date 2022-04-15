import csv
import random
import time
import serial 
import os
from constants import PORT, BAUDRATE

# get current time in ms
def millis():
    return int(time.time_ns()/1000000)

start_time = millis()
logname = 'logs/data' + str(start_time) + '.csv'
ser = serial.Serial(PORT, BAUDRATE)

fieldnames = ["time", "TC1", "TC2", "TC3", "TC4", "PT1", "PT2", "PT3", "PT4", "LC"]


with open(logname, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    t = millis()-start_time
    with open(logname, 'a') as csv_file:
        try:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            line = ser.readline().decode()[:-1] #TC1,TC2,TC3,TC4,PT1,PT2,PT3,PT4,LC
            data = line.split(',')
            if len(data) == 9 : 
                info = {
                    "time": time,
                    "TC1": data[0],
                    "TC2": data[1],
                    "TC3": data[2],
                    "TC4": data[3],
                    "PT1": data[4],
                    "PT2": data[5],
                    "PT3": data[6],
                    "PT4": data[7],
                    "LC": data[8],
                }

                csv_writer.writerow(info)
                print(t, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        except:
            os._exit(1)


    # time.sleep(0.2)