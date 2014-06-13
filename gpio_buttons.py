import RPi.GPIO as GPIO
import uinput
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)





def btn23(channel):
  #print("btn23")
  device.emit_click(uinput.KEY_UP)

def btn22(channel):
  #print("btn22")
  device.emit_click(uinput.KEY_DOWN)

def btn27(channel):
  pass

def btn18(channel):
  device.emit_click(uinput.KEY_ENTER)



events = ([uinput.KEY_ENTER, uinput.KEY_UP, uinput.KEY_DOWN] )
device = uinput.Device(events)

GPIO.add_event_detect(23, GPIO.RISING, callback=btn23, bouncetime=600)
GPIO.add_event_detect(22, GPIO.RISING, callback=btn22, bouncetime=600)
GPIO.add_event_detect(27, GPIO.RISING, callback=btn27, bouncetime=600)
GPIO.add_event_detect(18, GPIO.RISING, callback=btn18, bouncetime=600)


while True:
  if(1 == 0):
    print("The universe is broken")
GPIO.cleanup()
