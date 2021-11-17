# Shifter Class

import RPi.GPIO as GPIO
import time

class Shifter():

  'Shift register class'

  def __init__(self, data, latch, clock):
    self.dataPin, self.latchPin, self.clockPin = data, latch, clock
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.dataPin, GPIO.OUT) 
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

  def ping(self, pin):  # ping the clock or latch pin
    GPIO.output(pin,1)
    time.sleep(0)
    GPIO.output(pin,0)

  def shiftByte(self, byteVal):  # display a given byte pattern
    for i in range(8):           # 8 bits in register
      #GPIO.output(self.dataPin, ~(byteVal & (1<<i)))  # if common anode
      GPIO.output(self.dataPin, byteVal & (1<<i))    # if common cathode
      self.ping(self.clockPin)
      #self.ping(self.latchPin) # GET rid of

  def latch(self):
    self.ping(self.latchPin)
    
'''To fix this for your lab code, my suggestion is to remove the latch step from shiftByte, and add a new method to Shifter called latch that will perform the latching function.  Then in your main code (or whatever code is calling shiftByte), call latch immediately after calling shiftByte twice.  This way you will only latch the registers after both bytes have been loaded.  This should eliminate strange flickering issues that some of you were seeing in class yesterday, and make your firefly output look much nicer in the lab.'''


