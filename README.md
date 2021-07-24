# iDevice Analyser
This program is intended to run on Linux with Python 3, and will only work correctly for Apple iPhones.

I am not affiliated with Apple, Libimobiledevice, or any other software developers related to this project unless oterwise stated.

Feel free to modify the script to your liking to fix any issues or to better suit your needs. Just don't redistribute it without attributing me, and the people listed above. This script can be used for commercial purposes, where it corresponds with the licences of any software it depends on.



[![CC-BY-SA](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)]( http://creativecommons.org/licenses/by-sa/4.0/)

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
