import serial
import os
import pynmea2
import time
import datetime
import matplotlib.pylab as plt
import GCP_storge as gcp
# read data from /dev/ttyACM0 are bytes
ser = serial.Serial('/dev/ttyACM0', 9600)
# time of start exercise
start = datetime.datetime.now()
# name for every file
name = str(start.year)+str(start.month)+str(start.day)

# initialization data for start exercise
total_pace = 0
total_speed = 0
count = 0
# list for axis in record_picture
pace_list = []
time_list = []
distance_list = []
try:
    while True:
        line = ser.readline()
        if line:
            if str(line)[5:8] == "VTG":
                try:
                    # make total time of exercise
                    now = datetime.datetime.now()
                    diff = (now - start).seconds
                    h = diff // 3600
                    m = (diff % 3600) // 60
                    s = diff % 60
                    time_total = "{}H {}M {}S".format(h, m, s)
                    speed = float(str(line).split(",")[7])
                    count += 1
                    total_speed += speed
                    avg_speed = total_speed / count
                    distance = round(avg_speed * diff / 3600, 2)
                    distance_list.append(distance)
                    time_d_list.append(diff * 10)
                    print("distance:", distance)
                    pace = round(60 / float(speed), 2)  # 分速
                    pace_list.append(pace)
                    time_p_list.append(diff * 10)
                    print("pace:", pace)
                    time.sleep(1)
                except:
                    pass
except KeyboardInterrupt:
    plt.subplot(2, 1, 1)
    plt.plot(time_p_list, pace_list)
    plt.ylabel("Pace")
    plt.subplot(2, 1, 2)
    plt.plot(time_d_list, distance_list)
    plt.ylabel("Distance")
    plt.xlabel("Time")
    plt.savefig('runarea'+name+'.png')
    gcp.upload_blob_png('runarea'+name+'.png', 'runarea'+name+'.png')
    quit()
except StopIteration:
    session = None
    print("GPSD has terminated")