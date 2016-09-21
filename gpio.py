import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

for nbr in range(0, 27):
  print nbr
  GPIO.setup(nbr, GPIO.OUT)

  GPIO.output(nbr, True)
  print "Led on"
  time.sleep(1)

  GPIO.output(nbr, False)
  print "Led off"
  time.sleep(1)
