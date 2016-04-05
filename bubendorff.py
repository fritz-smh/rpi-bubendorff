#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

# set up the way to access the GPIO inputs
GPIO.setmode(GPIO.BOARD)
# no warning displayed
GPIO.setwarnings(False)


"""
 TODO
 - configure logging option
 - add calculation on current position
 - use GPIO.cleanup() ???
"""

class Bubendorff:
    """
       Class to manage Bubendorff rolling shutter with a rpi thanks to the board : 
         8 canaux 5V Solid State Board Module relais OMRON SSR AVR DSP Arduino 
         Reference ASIN : B00AZEVSQG

       This relay board close a relay for a down (0) level on an input pin !!!

       In this class, I choose to set : 
         gpio = LOW  ==> bubendorff remote button not activated
         gpio = HIGH ==> bubendorff remote button activated
       This is better in case of reboot (gpio will be set to LOW on startup)
    """
     

    def __init__(self, gpio_for_opening, gpio_for_closing, time_for_opening, time_for_closing):
        """ Set up the rolling shutter python engine
        """

        #print("Bubendorff > start init...")
        ### set constants
        self.pulse_duration_s = 0.5   # 500ms of pulse to do an up or down action

        ### set parameters
        self.gpio_for_opening = gpio_for_opening
        self.gpio_for_closing = gpio_for_closing
        self.time_for_opening = time_for_opening
        self.time_for_closing = time_for_closing

        ### check GPIO status before init 
        #print(u"GPIO version = {0}".format(GPIO.VERSION))
        #print(u"GPIO function for opening ({0}) : {1}".format(self.gpio_for_opening, GPIO.gpio_function(self.gpio_for_opening)))
        #print(u"GPIO function for closing ({0}) : {1}".format(self.gpio_for_closing, GPIO.gpio_function(self.gpio_for_closing)))
        #print(u"""GPIO functions values : 
        #          0 = GPIO.OUT
        #          1 = GPIO.IN
        #          40 = GPIO.SERIAL
        #          41 = GPIO.SPI
        #          42 = GPIO.I2C
        #          43 = GPIO.HARD_PWM
        #          -1 = GPIO.UNKNOWN""")


        ### init GPIO values
        GPIO.setup(self.gpio_for_opening, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.gpio_for_closing, GPIO.OUT, initial=GPIO.HIGH)

        #print("Bubendorff > end of init!")

    def open(self, percent = None):
        """ Open the rolling shutter
        """
        #print("Bubendorff > start opening the rolling shutter")
        GPIO.output(self.gpio_for_opening, GPIO.LOW)
        time.sleep(self.pulse_duration_s)
        GPIO.output(self.gpio_for_opening, GPIO.HIGH)

    def close(self, percent = None):
        """ Close the rolling shutter
        """
        #print("Bubendorff > start closing the rolling shutter")
        GPIO.output(self.gpio_for_closing, GPIO.LOW)
        time.sleep(self.pulse_duration_s)
        GPIO.output(self.gpio_for_closing, GPIO.HIGH)



if __name__ == "__main__":
    ## 22 => close
    ## 18 => open
    vr1 = Bubendorff(22, 18, 22, 20)  
    vr1.open()
    time.sleep(10)
    vr1.close()
