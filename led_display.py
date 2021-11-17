# LEDdisplay class

import time
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  numbers = [ 
    0b10000000, # 0
    0b01000000, # 1
    0b00100000, # 2
    0b00010000, # 3
    0b00001000, # 4
    0b00000100, # 5
    0b00000010, # 6
    0b00000001,] # 7

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    row=1 #change this value to pick which row the pattern appears on 
    self.shifter.shiftByte(LEDdisplay.numbers[num])#load the row values
    self.shifter.shiftByte(1<<(row-1)) #select the given row
    self.shifter.latch()

    '''To fix this for your lab code, my suggestion is to remove the latch step from shiftByte, and add a new method to Shifter called latch that will perform the latching function.  Then in your main code (or whatever code is calling shiftByte), call latch immediately after calling shiftByte twice.  This way you will only latch the registers after both bytes have been loaded.  This should eliminate strange flickering issues that some of you were seeing in class yesterday, and make your firefly output look much nicer in the lab.'''