import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)

while True:
  temp = os.popen('vcgencmd measure_temp').readline()
  temp = (temp.replace("temp=", "").replace("'C\n", ""))

  if float(temp) > 80:
    GPIO.output(18, True)
  else:
    if float(temp) < 70:
      GPIO.output(18, False)
  sleep(1)
