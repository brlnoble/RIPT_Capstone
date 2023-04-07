import time
import sys
referenceUnit = -12.6
import RPi.GPIO as GPIO
from hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")

while True:
     try:
          init_val = abs(int(hx.get_weight(5)))
          val = max(0, int(hx.get_weight(5)))
          print(val-init_val)
          hx.power_down()
          hx.power_up()
          time.sleep(100e-6)
     except (KeyboardInterrupt, SystemExit):
          GPIO.cleanup()

