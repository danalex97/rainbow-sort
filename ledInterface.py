import time

import RPi.GPIO as GPIO

def setup():
	GPIO.setmode(GPIO.BCM)

def led1(state):
	GPIO.setup(2, GPIO.OUT)
	GPIO.output(2, state)	
	GPIO.setup(3, GPIO.OUT)
	GPIO.output(3, not state)

def led3(state):
	GPIO.setup(4, GPIO.OUT)
	GPIO.output(4, state)	

def led4(state):
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, state)
	GPIO.setup(27, GPIO.OUT)
	GPIO.output(27, not state)

def led5(state):
	GPIO.setup(10, GPIO.OUT)
	GPIO.output(10, state)
	GPIO.setup(9, GPIO.OUT)
	GPIO.output(9, not state)

def led6(state):
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, state)

def led7(state):
	GPIO.setup(14, GPIO.OUT)
	GPIO.output(14, state)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15, not state)

def led8(state):
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, state)

# def setup():
# 	pass

# def led1(state):
# 	pass

# def led3(state):
# 	pass

# def led4(state):
# 	pass

# def led5(state):
# 	pass

# def led6(state):
# 	pass

# def led7(state):
# 	pass

# def led8(state):
# 	pass


def wait(secs):
	time.sleep(secs)

ledmap = {}
ledmap[1] = (led1, True)
ledmap[3] = (led3, True)
ledmap[4] = (led4, True)
ledmap[5] = (led5, True) #
ledmap[6] = (led6, True)
ledmap[7] = (led7, True)
ledmap[8] = (led8, True)

def testLed(nbr):
	led, onOff = ledmap[nbr]
	
	print "Test led " + str(nbr)

	led(onOff)
	wait(1)
	led(not onOff)
	wait(1)

	print "Done " + str(nbr)

setup()

for nbr in [1,3,4,5,6,7,8]:
	testLed(nbr)