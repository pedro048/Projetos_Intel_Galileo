import mraa
import time

PWM_PIN = 5
ADC_PIN = 0           # Analog in pin
ROT_MAX = 1024.0      # Max value as measured by ADC when pot is connected

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
    time.sleep(0.5)