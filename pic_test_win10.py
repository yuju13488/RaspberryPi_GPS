import serial
import pynmea2
import datetime
import requests, json
import time

import matplotlib.pylab as plt

#樹莓派ID
id="yoyo"
#port口和topics
start = datetime.datetime.now()
total_speed = 0
count = 0
with open("gps20191112.nmea", 'r') as gps:
    pace_list = []
    time_d_list = []
    time_p_list = []
    distance_list = []
    while True:
        line = gps.readline()
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            if line[3:6] == "VTG":
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
                if 2.5 <= speed and speed <= 20:
                    pace = round(60 / float(speed), 2)  # 分速
                    pace_list.append(pace)
                    time_p_list.append(diff*10)
                    print("pace:", pace)
                time.sleep(1)
            elif line[0:1] != "$":
                break
        except ValueError:
            plt.subplot(2,1,1)
            plt.plot(time_p_list, pace_list)
            plt.ylabel("Pace")
            plt.subplot(2,1,2)
            plt.plot(time_d_list, distance_list)
            plt.ylabel("Distance")
            plt.xlabel("Time")
            plt.savefig('gps20191112.png')
            plt.show()
            break