# OCUFLY

Ocufly is a combination of flight software and image recognition software with the intent of being able to fly a drone and recognize potential hazards that law enforcement or fire personell may encounter before they arrive or enter a potentially dangerous scene. It may also help in the search and rescue of missing persons.

This software works with the tello-edu drone from DJI. Currently we have a working GUI and working Image recognition using cvlib.

Requirements:
A python 3 64-bit installation is required. We recommend that python 3.6 or higher be used as there has been no testing done on earlier versions.
The Image recognition will not work with python 2.7.
matplotlib, opencv-python, tensorflow, and cvlib are all dependcies that must be installed in order for the image recognition to work. It is recommended to use the ObjTest folder and run ObjTest.py to see how it works.

There is an install folder that will run an install script for the dependencies for linux. Th
ubuntu v18 has been tested with success.

Currently we are unable to get the video decoder to work. The one reccommened by DJI that was included in their sdk is optimized for python 2.7 which is incompatible with the image recognition library that we used. There are also many issues with testing that have arisen when trying to install the SDK for testing that apparently is a common issue. We have included in the folder Tello_Video the SDK from DJI and it has a seperate installation script that can be used for testing their software.