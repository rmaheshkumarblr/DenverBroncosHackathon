from kulka import Kulka
import time
#from random import randint


def do_the_dance(kulka):
	speed = 0x88
	sleep_time = 5

	for angle in [1, 90, 180, 270]:
        	kulka.roll(speed, angle)
        	time.sleep(sleep_time)
    
	kulka.roll(0, 0)

ADDR = '00:06:66:4A:0C:DA'
with Kulka(ADDR) as kulka:
	print("Setting color to red")
	kulka.set_rgb(255, 0, 0)
	time.sleep(0.1)
	print("Setting color to green")
	kulka.set_rgb(0, 255, 0)
	time.sleep(0.1)
	print("Setting color to blue")
	kulka.set_rgb(0, 0, 255)
	time.sleep(0.1)
	#kulka.set_inactivity_timeout(1)
	do_the_dance(kulka);
    
    #kulka.roll(randint(0, 255), randint(0, 359))
