
This a modified version of the RTIMULIB from 

##Aim
How to extract IMU data from EMLID reach RS+ and M+

while the previous version had a embedded compiler, this one require cross compilation
 we are going to use the spi port 0.0,
Even if it not the case usually, the build files are included in the repo, and if needed the cross compilation can be avoided.
The RTIMULib calibration step can performed, and a pdf document as been attached as a demonstration.
##IMUtest
A exemple project is available from Emlead to implement to see a simple C++ implementation, with the executable file.
To test the IMU, you can simply copy the executable to the target and execute it.
If this work you could go further.

##dependency

For cross compilation the following target are available
sudo apt-get install gcc make   gcc-aarch64-linux-gnu g++-aarch64-linux-gnu 
 
#test

Clone MPU_emlid test
make
scp MPUtest root@XXXXX:~
password is emlidreach
ssh root@XXXX -t MPUtest
you should see some data printed.

If so you can continue

#RTIMULib installation
While the previous generation included a compiler, this one doesn't and cross compilation is required, 
The target architecture is aarch64.
cross compilation can also be performed.
git clone https://github.com/14roiron/RTIMULIB_EMLID_REACH_2.git
cd RTIMULIB_EMLID_REACH_2
cd Linux
mkdir build
cd Linux
cmake ..
make -j

#To calibrate
scp RTIMULibCal/RTIMULibCal root@xxxx:~
ssh root@XXX -t RTIMULibCal
#you can't perfrom the ellispse, but the rest should be fine

#you should have all the require filed
# if you require python interface,
# you should find the so files in the python folder
cd ..
scp -r python root@XXX:~
ssh root@xxx
cd python


#not working yet, need to be added to path somehow
mkdir -p /usr/local/python2.7/dist-packages/ 
cp RTIMU.so /usr/local/python2.7/dist-packages/ 
mkdir -p /usr/local/python3.5/dist-packages/
cp RTIMU.cpython-35m-aarch64-linux-gnu.so /usr/local/python3.5/dist-packages/ 

#get the ini file
cp ~/RTIMULib.ini test/
you should be able to test it:
python3 test/fusion.py

To send the Ima data, if emlid, 
