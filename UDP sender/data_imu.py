#!/usr/bin/env python
import socket
import json
import sys

import rospy
from geometry_msgs.msg import Vector3Stamped

if len(sys.argv)<3:
    print("usage cmd ip_address topic_name")
    exit()
ip = sys.argv[1]
port = 7005

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(0.3)
# Send to server using created UDP socket

pub = rospy.Publisher(sys.argv[2], Vector3Stamped, queue_size=10)
rospy.init_node("orientation")
rate = rospy.Rate(1000) # 100hz
while not rospy.is_shutdown():
    try:
        UDPClientSocket.sendto(" ".encode(), (ip,port))
        i=0
        while i<100:
            msgFromServer = UDPClientSocket.recvfrom(1024)
            data = json.loads(msgFromServer[0].decode())
            timestamp = data["timestamp"]
            angles = (data["fusionPose"])
            # print(data)

            dataToPublish =  Vector3Stamped()
            dataToPublish.vector.x = angles[2]
            dataToPublish.vector.y = angles[1]
            dataToPublish.vector.z = angles[0]
            pub.publish(dataToPublish)
            # rospy.spinonce()
            # print(angles)
            # print("\n")
            rate.sleep()

            i=i+1

    except socket.timeout as e:
        pass
    except rospy.ROSInterruptException:
        pass
