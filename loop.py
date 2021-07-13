import time #import time module
max = 255 #max rgb value for LED
min = 0 #min rbg value for LED
count = max-1 #current start point for the LEDS (on)
glow = "blinkt.set_all({},0,0)" #Set where the count variable will be put

while True: #loop
	if count == max-1: #check if current count is 1 less than max rgb val
		for count in range(max,min,-1): 
			time.sleep(0.01)
			print glow.format(count) #format glow string with the count variable

	if count == min+1: #check if current count is 1 more than the min rgb val
		for count in range(min,max,1):
			time.sleep(0.01)
			print glow.format(count)
