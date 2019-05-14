import mraa

gpio_1 = mraa.Gpio(11)
gpio_1.dir(mraa.DIR_OUT)

while True:
	gpio_1.write(1)
