import mraa

gpio_1 = mraa.Gpio(2)
gpio_2 = mraa.Gpio(4)
gpio_3 = mraa.Gpio(12)
gpio_1.dir(mraa.DIR_IN)
gpio_2.dir(mraa.DIR_IN)
gpio_3.dir(mraa.DIR_OUT)
liga = 0
desliga = 0

while True:
	liga = gpio_1.read()
	desliga = gpio_2.read()
	if liga == 1:
		gpio_3.write(1)

	if desliga == 1:
		gpio_3.write(0)
	
	
