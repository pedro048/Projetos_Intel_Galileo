import mraa
import time

gpio_1 = mraa.Gpio(7)
gpio_1.dir(mraa.DIR_OUT)
gpio_2 = mraa.Gpio(2)
gpio_2.dir(mraa.DIR_IN)
leitura = 0
cont = 0

while True:
	leitura = gpio_2.read()
	if leitura == 1:
		gpio_1.write(1)
		time.sleep(1)
	else:
		gpio_1.write(0)
		time.sleep(1)
