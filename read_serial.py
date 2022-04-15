import csv
import random
import time
import serial 

x_value = 0
total_1 = 1000
total_2 = 1000


ser = serial.Serial('/dev/cu.usbmodem142201', 9600) 

fieldnames = ["x_value", "total_1", "total_2"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        line = ser.readline().decode()[:-1] #TC1,TC2,TC3,TC4,PT1,PT2,PT3,PT4,LC
        data = line.split(',')
        if len(data) == 9 
            info = {
                "x_value": x_value,
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
            print(x_value, data)


    time.sleep(0.2)