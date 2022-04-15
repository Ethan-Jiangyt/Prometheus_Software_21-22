import csv
import random
import time
import serial 

time = 0

ser = serial.Serial('/dev/cu.usbmodem142201', 9600) 

fieldnames = ["time", "TC1", "TC2", "TC3", "TC4", "PT1", "PT2", "PT3", :"PT4", "LC"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
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

            time += 1
            csv_writer.writerow(info)
            print(x_value, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])


    time.sleep(0.2)