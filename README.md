## Using the script
`python3 start.py` if you have a pi camera module or `python3 start.py --picamera 1` to use a webcam

## Files 
1. `VideoStream.py` - great helper class for webcam and pi camera video capture as taught by [pyimagesearch](https://www.pyimagesearch.com/2016/01/04/unifying-picamera-and-cv2-videocapture-into-a-single-class-with-opencv/).
2. `start.py` - main file for facial detection and saving!
3. `haarcascade_frontalface_default.xml` - prebuilt Haar feature-based cascade classifier provided in the OpenCV library.

## What you need
### Hardware
1. A Raspberry Pi (RPi) with OpenCV installed. 
    a. RPi 3 or 4 is recommended
    b. This write-up uses the RPi 3 Model B, with Raspbian Stretch
2. A suitable camera to use with RPi.
    a. The script mentioned uses a RPi camera v2 module!
3. A power source for the RPi. This can be via a power bank or a direct power source.

### Software and Python libraries needed

`Python3.6` to be installed on your RPi.

These are the Python libraries needed for this application 

1. picamera[array] (requires numpy dependency, which should be installed with OpenCV)
2. imutils
3. argparse
4. pillow

## Setting up the device

In the case of a newly bought RPi with the Debian OS at it's cleanest state, there are a number of things that need to be done.

### Enabling the GPIO RPi Camera module

In your RPi, use `sudo raspi-config` to access the configuration menu. Access `Interfacing Options` and enable the `Camera`.

### Accessing the RPi GUI

There are many ways to do this, but the most straight forward and hasslefree way to do this is to set up a direct connection with a monitor, mouse and keyboard using the USB and HDMI slots on the RPi

When developing this application, I set it up the headless way, and then a VNCServer on the RPi to access it remotely. 
Here are some references on how to do it!

1. [Setting up RPi headless](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md)
2. [Setting up and connecting to an RPi using VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)

### Installation of OpenCV

#### Official yet time-consuming method
Installing OpenCV can be quite a tedious and time-consuming chore. That is if you want to do it the official way and compile it from source.  
[pyimagesearch](https://www.pyimagesearch.com/) provides very detailed steps on installing OpenCV on the RPi 3 with Raspbian Stretch with optimization [here](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/).

#### Not so official but time-saving method
Fortunately, if you do not mind unofficial, pre-built binaries, you can simply make use of Python's `pip` to install OpenCV using `sudo pip install opencv-contrib-python` if you do not mind installing it on global, or `pip install open-contrib-python` if you are using a virtualenv to manage Python workspaces.

Do note that the following libraries will need to be installed too. 

```
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
```
