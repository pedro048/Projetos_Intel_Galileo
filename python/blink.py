import mraa
import time

gpio_1 = mraa.Gpio(7) # initialise gpio 7
gpio_1.dir(mraa.DIR_OUT) # set gpio 7 to output
 
while True:
   gpio_1.write(1)
   time.sleep(1)
   gpio_1.write(0)
   time.sleep(1)
    
    
