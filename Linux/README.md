# RTIMULib for Linux

This directory contains the applications for embedded Linux systems such as the Raspberry Pi and Intel Edison. This description assumes that the Edison image was built using the meta-edison-rt layer, available on the GitHub repo.

The RTIMULibvrpm demo app, which shows how to integrate RTIMULib with vrpn, has its own build and run instructions in a README.md within the RTIMULibvrpn directory.


### Run the RTIMULibCal App

RTIMULibCal can either add calibration data to an existing RTIMULib.ini or else create a new one with the calibration data. RTIMULib.ini is used/created in the working directory.

If magnetometer ellipsoid fit isn't required, RTIMULibCal can be run anywhere. If ellipsoid fit is required, then the program assumes that the RTEllipsoidFit directory is at the same level as the working directory so that "../RTEllipsoidFit" refers to the directory holding the RTEllipsoidFit.m octave program. If not, ellipsoid fitting will fail. Note - ellipsoid fit is not supported on the Intel Edison.

The normal process is to run the magnetometer min/max option followed by the magnetometer ellipsoid fit option followed finally by the accelerometer min/max option. The program is self-documenting in that the instructions for every option will be displayed when the option is selected.

The resulting RTIMULib.ini can then be used by any other RTIMULib application.

### Run the RTIMULibDrive, RTIMULibDrive10 and RTIMULibDrive11 Demo Apps

RTIMULibDrive is a simple command line program that shows how simple it is to use RTIMULib. RTIMULibDrive10 extends this to also support 10-dof IMUs with pressure/temperature sensors. RTIMULibDrive11 adds humidity sensor support to RTIMULibDrive10.

You should be able to run the program just by entering RTIMULibDrive(10/11). It will try to auto detect the connected IMU If all is well, you should see a line showing the sample rate and the current Euler angles. This is updated 10 times per second, regardless of the sensor sample rate. By default, the driver runs at 50 samples per second in most cases. So, you should see the sample rate indicating around 50 samples per second. The sample rate can be changed by editing the .ini file entry for the appropriate IMU type.

The displayed pose shows the roll, pitch and yaw seen by the IMU. Using an aircraft analogy, the roll axis points from the pilot towards the nose, the pitch axis points from the pilot along the right wing and the yaw axis points from the pilot down towards the ground. Right wing down is a positive roll, nose up is a positive pitch and clockwise rotation is a positive yaw.

Various parameters can be changed by editing the RTIMULib.ini file. These are described later.

Take a look at RTIMULibDrive.cpp. Quite a few of the code lines are just to calculate rates and display outputs!


