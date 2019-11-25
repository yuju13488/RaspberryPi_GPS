Use Raspberry Pi 3B+, GPS sensor U-BLOX  NEO-6M
1. Use microUSE cable connect Pi and sensor
2. Use Rest Proxy(IP and port8082), transfer data to kafka
3. Save GPS data to nmea file
4. Use software gpsbabel transfer nmea to gpx file
5. Use gpx file make OpenStreetMap tracker(html file)
6. Draw abour pace and distanct make line graph

install packages
01. sudo apt-get install gpsd gpsd-clients python-gps # install package for GPS
02. sudo systemctl stop gpsd.socket # stop GPS environment setting
03. sudo systemctl disable gpsd.socket  # close GPS environment setting
04. sudo systemctl enable gpsd.socket # start GPS environment setting
05. sudo systemctl start gpsd.socket # open GPS environment setting
06. udo apt-get update && sudo apt-get -y upgrade #update
07. sudo lsusb # check USB 
08. dmesg | grep -i usb #ttyACM0 port 
09. sudo cat /dev/ttyACM0 # check USE signal
10. sudo gpsd /dev/ttyACM0 -n -F /var/run/gpsd.sock # setting GPSD
11. sudo killall gpsd
12. cgps -s # report of GPS
13. xgps # report of GPS
14. gpsmon # report of GPS
15. sudo apt-get install  microcom # install package for writing GPS signal
16. microcom -p /dev/ttyACM0 -s 9600 > /tmp/file_name.nmea # writing log in nmea file

install packages of python<br/>
17. sudo apt-get install python3-pip<br/>
18. sudo pip3 install gps3<br/>
19. sudo pip3 install pynmea2<br/>
20. sudo pip3 install microstacknode<br/>
21. do pip3 install modeldb<br/>
22. If function serial can't work:<br/>
      sudo pip3 uninstall serial<br/>
      sudo pip3 uninlstall pyserial<br/>
      sudo pip3 install pyseria<br/>
23. sudo apt-get install gpsbabel # gpsbabel -i nmea -f file_name.nmea -o gpx -F file_name.gpx<br/>
24. sudo pip3 install gpxpy # package for gpx analysis<br/>
25. sudo pip3 install folium # package for html analysis
