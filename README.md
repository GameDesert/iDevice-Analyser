# iDevice Analyser
This program is intended to run on Linux with Python 3, and will only work correctly for Apple iPhones.

I am not affiliated with Apple, Libimobiledevice, or any other software developers related to this project unless oterwise stated.

# How to install

Firstly, install all the necessary Python packages:
`pip3 install tk`

And then the external software:
`sudo apt install libimobiledevice-utils`

And finally, this program:
`cd [Wherever you want to install the program]`
`git clone https://github.com/GameDesert/idevice-analyser.git`

# How to use

Start up the program by navigating to its directory using `cd`, then use `python3 idevice_analyser.py` to start it.

You will be asked to enter your sudo password, this is so the program can pair with your device when needed (you may have to re-enter the password when clicking the pair button anyway).

Once the program opens, connect your device to your computer via a Lightning to USB (or USB-C) cable.

Finally, press the `Analyse` button. It generally won't be necessary to pair the device -- or even unlock it -- but if you run into trouble with using the program, restart it, unlock the device, and press `Pair` before analysing.
