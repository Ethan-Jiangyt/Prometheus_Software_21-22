import csv
import random
import time

t = 0
hz = 16
delay = 1/hz
# get current time in ms
def millis():
    return int(time.time_ns()/1000000)

start_time = millis()

fieldnames = ["time", "TC1", "TC2", "TC3", "TC4", "PT1", "PT2", "PT3", "PT4", "LC"]
data = [1000 for i in range(len(fieldnames)-1)] # tmp for dummy data

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        t = millis()-start_time
        info = {
                "time": t,
                "TC1": data[0],
                "TC2": data[1],
                "TC3": data[2],
                "TC4": data[3],
                "PT1": data[4],
                "PT2": data[5],
                "PT3": data[6],
                "PT4": data[7],
                "LC" : data[8],
            }

        csv_writer.writerow(info)
        print(t, data)

        for i in range(9):
            data[i] += random.randint(-10, 10)

    time.sleep(delay)