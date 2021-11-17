import time
from led_display import LEDdisplay
import RPi.GPIO as GPIO #for cleanup()

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 23, 24, 25 #input data, send data, load data

# Pick a number sequence
sequence = [8, 6, 7, 5, 3, 0, 9]

theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)

while True:
  try:
    for n in range(len(sequence)):
      theLEDdisplay.setNumber(sequence[n])
      time.sleep(0.5)
  except KeyboardInterrupt:
    print("\nExiting!")
    GPIO.cleanup()
    break