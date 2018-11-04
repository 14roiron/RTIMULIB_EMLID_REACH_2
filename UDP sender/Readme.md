# First tests, with a udp sender and maincomputer receiver to a ros node
The idea is to launch the file, from the python folder.
For that a python file is placed in the exemple folder Publisher_data_udp.py

bash file is executed from a ssh command line:
```bash
echo "#!/bin/bash \n cd path/to/pythonfolder  \n python test/Publisher_data_udp.py" >> launch_file.sh
chmod +x launch_file
```

then to start it from a computer:
```bash 
ssh root@IP.OF.REACH.RS -t path/to/launch_file/launch_file.sh
```
and a client can be executed from the receiver computer to publish data to ROS, is the ros node is not needed, part of the code could be removed
```bash
python data_imu.py IP_of_reach topic_name
```
of from a roslaunch
```xml
<node name="$(anon gps_streamer_sub)" pkg="your_package" output="screen" type="data_imu.py" args=" ip topic_name />
```

This is just an exemple
Every 1000 messages a new message need to be send to get the mew ip address, this is used to be able to relaunch the program as UDP is state less.

