import serial
from time import localtime, strftime
import csv
import os
import sys
import glob
import temp_hum2png


ser = serial.Serial(sys.argv[1])
ser.flushInput()

for file in glob.glob("*.csv"):
    temp_hum2png.plot_image(file, 20)

while True:
    try:
        data = ser.readline().decode("utf-8").strip()
        vals = data.split(" ")
        print(vals)
        log_file = strftime("%Y_%m_%d.csv", localtime())
        if not os.path.exists(log_file):
            for file in glob.glob("*.csv"):
                temp_hum2png.plot_image(file, 20)
            with open(log_file, 'w') as f:
                f.write('time,temp,hum,tvoc\n')

        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([strftime("%H:%M:%S", localtime()),
                             vals[0], vals[1], vals[2]])
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        break
    except Exception as e:
        print(e)
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([strftime("%H:%M:%S", localtime())])
