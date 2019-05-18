import thread
import mraa
import time

#---- configuracao do PWM, ADC e LEDs (intensidade do incendio) ----
PWM_PIN = 5
ADC_PIN = 0           # Analog in pin
ROT_MAX = 1024.0      # Max value as measured by ADC when pot is connected
global led_intensity 

# Set up the PWM
pwm = mraa.Pwm(PWM_PIN)
pwm.enable(True)
pwm.period_us(5000)

# Set up the ADC
adc = mraa.Aio(ADC_PIN)

# Define a function for the thread
def thread1( threadName, delay):
   #while 1:
   time.sleep(delay)
   value = adc.read()             # ler valor do ADC
   led_intensity = value/ROT_MAX  # determina o duty cycle baseado em value

def thread2( threadName, delay):
   #while 1:
    time.sleep(delay)
    pwm.write(led_intensity)

try:
    thread.start_new_thread( thread1, (1, 2 ) )
    thread.start_new_thread( thread2, (2, 3 ) )
    adc = Thread(target)
    
except:
   print ("Error: unable to start thread")

'''
while 1:
	value = adc.read()             # ler valor do ADC
   	led_intensity = value/ROT_MAX
	pwm.write(led_intensity)
'''

        
