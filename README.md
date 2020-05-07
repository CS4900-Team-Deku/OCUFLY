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

Linux is the preferred environment for this 
The first requirement to run this program is that you have 64-bit python3, >= 3.6.x preferred, installed. In order to do that you must install it from python.org
***Do not just press the download button at the top of the page. This is only a default 32-bit version***
Windows:
https://www.python.org/ftp/python/3.8.3/python-3.8.3rc1-amd64.exe

Mac OS X:
https://www.python.org/ftp/python/3.8.3/python-3.8.3rc1-macosx10.9.pkg

Ubuntu 18.04 should come preinstalled with python 3.6 but if needed:
Linux(Ubuntu 18.04):
https://www.python.org/ftp/python/3.8.3/Python-3.8.3rc1.tgz

or (preferred method):

sudo apt-get update
sudo apt-get install python 3.8


For Linux(Ubuntu):
After python is installed navigate to Install/Linux in terminal

chmod +x linux_install.sh
./linux_install.sh

After this has run all dependencies should be installed.
You may now ‘cd ..’ to the OCUFLY folder

To fly the drone, type the command:
python3 fligh_software.py

To run an image recognition test:
cd ObjTest
python3 ObjRec.py
*** The first time this runs it make take considerably longer than normal***
