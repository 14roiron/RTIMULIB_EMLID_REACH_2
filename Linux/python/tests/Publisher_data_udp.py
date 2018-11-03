import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import socket
import json

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 7005))
server_socket.settimeout(1)
while True:
    try:
        message, address = server_socket.recvfrom(1024)
        i=0
        while i<1000:
            if imu.IMURead():
                # x, y, z = imu.getFusionData()
                # print("%f %f %f" % (x,y,z))
                data = imu.getIMUData()
                server_socket.sendto(json.dumps(data),address)
                fusionPose = data["fusionPose"]
                # print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]),
                    # math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
                time.sleep(5*poll_interval*1.0/1000.0)
                i+=1
            time.sleep(1.0/1000.0)
    except socket.timeout as e:
        pass
