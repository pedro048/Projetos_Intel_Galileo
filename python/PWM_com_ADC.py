import mraa
import time

PWM_PIN = 5
ADC_PIN = 0           # Analog in pin
ROT_MAX = 1024.0      # Max value as measured by ADC when pot is connected

gpio_1 = mraa.Gpio(6) # LED verde
gpio_1.dir(mraa.DIR_OUT)
gpio_2 = mraa.Gpio(8) # LED amarelo
gpio_2.dir(mraa.DIR_OUT)
gpio_3 = mraa.Gpio(11)# LED vermelho
gpio_3.dir(mraa.DIR_OUT)

# Set up the PWM
pwm = mraa.Pwm(PWM_PIN)
pwm.enable(True)
pwm.period_us(5000)

# Set up the ADC
adc = mraa.Aio(ADC_PIN)

while 1:
    value = adc.read()             # Read the ADC value
    led_intensity = value/ROT_MAX  # Determine the duty cycle based on ADC value
    pwm.write(led_intensity)
    if value >= 0 and value < 1365:
		gpio_1.write(1) # liga LED verde (principio de incendio)
		gpio_2.write(0)
		gpio_3.write(0)
	
    if value >= 1365 and value < 2730:
		gpio_1.write(0)
		gpio_2.write(1) # liga LED amarelo (incendio com intensidade moderada, mas preocupante)
		gpio_3.write(0)
	
    if value >= 2730 and value < 4095:
		gpio_1.write(0)
		gpio_2.write(0)
		gpio_3.write(1) # liga LED vermelho (incendio intenso)
	
    time.sleep(0.5)
	
