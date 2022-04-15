import csv
import time
import serial 

# get current time in ms
def millis():
    return int(time.time_ns()/1000000)

start_time = millis()

# '/dev/cu.usbmodem142201'
PORT = 'COM4'
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE)

# fieldnames = ["time", "TC1", "TC2", "TC3", "TC4", "PT1", "PT2", "PT3", "PT4", "LC"]
fieldnames = ["time", "value"]


with open('logs/data.csv', 'w+') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    t = millis()-start_time
    with open('logs/data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        line = ser.readline().decode()[:-1] #TC1,TC2,TC3,TC4,PT1,PT2,PT3,PT4,LC
        data = line.split(',')
        if len(data) == 1 : 
            info = {
                "time": t,
                "value" : data[0]
            }

            csv_writer.writerow(info)
            print(t, data)


    # time.sleep(0.2)