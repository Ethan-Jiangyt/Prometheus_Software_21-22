from tkinter import *
from random import randint
import csv
import random
import time

big_label = 'Arial 20'
small_label = 'Arial 15'
label_width = 20

t = 0
hz = 16
delay = 1/hz
# get current time in ms
def millis():
    return int(time.time_ns()/1000000)

start_time = millis()

fieldnames = ["time", "TC1", "TC2", "TC3", "TC4", "PT1", "PT2", "PT3", "PT4", "LC"]
data = [1000 for i in range(len(fieldnames)-1)] # tmp for dummy data

logname = 'logs/data' + str(start_time) + '.csv'

with open(logname, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


# Constants
num_TCs = 4
num_PTs = 4
num_LCs = 1

# Create GUI
root = Tk()
root.geometry("500x500")


# Labels
tc_label = Label(root, text="Thermocouples", font=big_label)
pt_label = Label(root, text="Pressure Transducers", font=big_label)
lc_label = Label(root, text="Load Cells", font=big_label)

## Thermocouple Labels
TC_labels = []
TC_vals = []
for i in range(num_TCs):
    TC_labels.append(Label(root, text=f'TC{i+1}: ', font=small_label))
    TC_vals.append(Label(root, font=small_label, width=label_width))

# Place in GUI
tc_label.grid(row=0, column=0)
for i in range(num_TCs):
    TC_labels[i].grid(row=i+1, column=0)
    TC_vals[i].grid(row=i+1, column=1)


## Pressure Transducer Labels
PT_labels = []
PT_vals = []
for i in range(num_PTs):
    PT_labels.append(Label(root, text=f'PT{i+1}: ', font=small_label))
    PT_vals.append(Label(root, font=small_label, width=label_width))
pt_label.grid(row=num_TCs+1, column=0)
for i in range(num_PTs):
    PT_labels[i].grid(row=i+num_TCs+2, column=0)
    PT_vals[i].grid(row=i+num_TCs+2, column=1)

## Load Cell Labels
LC_labels = []
LC_vals = []
for i in range(num_LCs):
    LC_labels.append(Label(root, text=f'LC{i+1}: ', font=small_label))
    LC_vals.append(Label(root, font=small_label, width=label_width))
lc_label.grid(row=num_PTs+num_TCs+2, column=0)
for i in range(num_LCs):
    LC_labels[i].grid(row=i+num_TCs+num_PTs+3, column=0)
    LC_vals[i].grid(row=i+num_TCs+num_PTs+3, column=1)


# Update values

def update():

    with open(logname, 'a') as csv_file:
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
            data[i] += random.random()

        # Update values to the screen
        TC_vals[0]['text'] = data[0]
        TC_vals[1]['text'] = data[1]
        TC_vals[2]['text'] = data[2]
        TC_vals[3]['text'] = data[3]

        PT_vals[0]['text'] = data[4]
        PT_vals[1]['text'] = data[5]
        PT_vals[2]['text'] = data[6]
        PT_vals[3]['text'] = data[7]

        LC_vals[0]['text'] = data[8]

    

    root.after(40, update)

update()

root.mainloop()