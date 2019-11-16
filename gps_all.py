import serial
import os #用pyton下linux指令的package
import gpxpy.gpx
import folium
import pynmea2
import datetime
import matplotlib.pylab as plt
import time
import GCP_storge as gcp
# read data from /dev/ttyACM0 are bytes
ser = serial.Serial('/dev/ttyACM0', 9600)
# time of start exercise
start = datetime.datetime.now()
# name for every file
name = str(start.year)+str(start.month)+str(start.day)
# save gps data in file
gps = open("gps"+name+".nmea","ab")
# initialization data for start exercise
total_pace = 0
total_speed = 0
count = 0
# list for axis in record_picture
pace_list = []
time_list = []
distance_list = []
while True:
    t = datetime.datetime.now()
    try:
        line = ser.readline()
        if line:
            gps.write(line)
            # transfer bytes to string and filter
            record = pynmea2.parse(str(line)[2:-5])
            # get Latitude, Longitude and Altitude
            if str(line)[5:8] == "GGA":
                Latitude = record.latitude
                Longitude = record.longitude
                Altitude = record.altitude
            # get about speed and distance
            elif str(line)[5:8] == "VTG":
                now = datetime.datetime.now()
                diff = (now - start).seconds
                h = diff // 3600
                m = (diff % 3600) // 60
                s = diff % 60
                time_total = "{0:02d}:{1:02d}:{2:02d}".format(h, m, s)
                try:
                    speed = float(str(line).split(",")[7])
                    count += 1
                    total_speed += speed
                    avg_speed = total_speed / count
                    # make total distance of exercise
                    distance = round(avg_speed * diff / 3600, 2)
                    pace = round(60 / float(speed), 2)
                    total_pace += pace
                    avg_pace = total_pace / count
                    pace_list.append(pace)
                    distance_list.append(distance)
                    time_list.append(diff * 10)
                    print("Pace:", pace, "min/km")
                    print("Distance:", distance, "km")
                    time.sleep(1)
                except:
                    pass
    except KeyboardInterrupt:
        # transfer to gpx and upload to google cloud storage
        common = 'gpsbabel -i nmea -f gps' + name + '.nmea -o gpx -F gps' + name + '.gpx'
        os.system(common)
        gcp.upload_blob_gpx('gps' + name + '.gpx', 'gps' + name + '.gpx')
        gpx_file = open('gps'+name+'.gpx', 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        ave_lat = sum(p[0] for p in points) / len(points)
        ave_lon = sum(p[1] for p in points) / len(points)

        # Load map centred on average coordinates
        my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=14)

        # add a markers
        for each in points:
            folium.Marker(each).add_to(my_map)

        # fadd lines
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(my_map)

        # Save map
        my_map.save("./gpx_tracker"+name+".html")
        gcp.upload_blob_html("gpx_tracker"+name+".html", "gpx_tracker"+name+".html")

        # make and save area picture for record of exercise
        plt.subplot(2, 1, 1)
        plt.plot(time_list, pace_list)
        plt.ylabel("Pace")
        plt.subplot(2, 1, 2)
        plt.plot(time_list, distance_list)
        plt.ylabel("Distance")
        plt.xlabel("Time")
        plt.savefig('runarea' + name + '.png')
        gcp.upload_blob_png('runarea' + name + '.png', 'runarea' + name + '.png')
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")