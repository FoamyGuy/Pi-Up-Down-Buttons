Pi-Up-Down-Buttons
==================

This is a python script that is meant to be run on a Raspberry Pi with [2.8" TFT Touchscreen](https://www.adafruit.com/products/1601) with the 4 optional pushbuttons soldered onto the shield

It will enable 2 of the buttons to function as up/down arrows, and a third to function as the enter key. Which will give you the ability to scroll through and execute previously utilized commands.

**Requirements:**
* python-uinput

**To get requirements:**

    $ sudo pip install python-uinput

**To launch the app:**

    $ sudo python gpio_buttons.py

**Optional**

To launch it automatically in the background add this to .profile:

    # Enable gpio buttons for up/down and enter
    sudo python gpio_buttons.py &

