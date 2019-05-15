
import mraa
import thread
import time

#---- configuracoes de ligar e desligar ----
gpio_1 = mraa.Gpio(2)
gpio_1.dir(mraa.DIR_IN) # botao de ligar
gpio_2 = mraa.Gpio(4)
gpio_2.dir(mraa.DIR_IN) # boatao de desligar
liga = 0
desliga = 0
aux = 0

#---- configuracao do PWM, ADC e LEDs (intensidade do incendio) ----
PWM_PIN = 5
ADC_PIN = 0           # Analog in pin
ROT_MAX = 1024.0      # Max value as measured by ADC when pot is connected

gpio_3 = mraa.Gpio(7) # LED verde
gpio_3.dir(mraa.DIR_OUT)
gpio_4 = mraa.Gpio(8) # LED amarelo
gpio_4.dir(mraa.DIR_OUT)
gpio_5 = mraa.Gpio(12)# LED vermelho
gpio_5.dir(mraa.DIR_OUT)

# Set up the PWM
pwm = mraa.Pwm(PWM_PIN)
pwm.enable(True)
pwm.period_us(5000)

# Set up the ADC
adc = mraa.Aio(ADC_PIN)

#---- configuracao do BUZZER ----
gpio_6 = mraa.Gpio(11)
gpio_6.dir(mraa.DIR_OUT)

while True:
	# ler o estado dos botoes de ligar e desligar
	liga = gpio_1.read()
	desliga = gpio_2.read()
	if liga == 1: 
		aux = 1

	if desliga == 1: 
	    aux = 0
		
	if aux == 1:	# sistema acionado
		value = adc.read()             # ler valor do ADC
		led_intensity = value/ROT_MAX  # determina o duty cycle baseado em value
		pwm.write(led_intensity)

		if value >= 0 and value < 100:
			gpio_3.write(1) # liga LED verde (ausencia de incendio)
			gpio_4.write(0)
			gpio_5.write(0)
			# alarme desligado
			gpio_6.write(0)
	
		if value >= 100 and value < 200:
			gpio_3.write(0)
			gpio_4.write(1) # liga LED amarelo (incendio com intensidade moderada, mas preocupante)
			gpio_5.write(0)
			# alarme de incendio moderado
			time.sleep(2)
			gpio_6.write(1)
			time.sleep(2)
			gpio_6.write(0)
	
		if value >= 200 and value < 1023:
			gpio_3.write(0)
			gpio_4.write(0)
			gpio_5.write(1) # liga LED vermelho (incendio intenso)
			# alarme de incendio intenso
			time.sleep(0.5)
			gpio_6.write(1)
			time.sleep(0.5)
			gpio_6.write(0)
    
		time.sleep(0.5)
	else:	# sistema desacionado
	
		# vazao de agua cortada
		pwm.write(0) 
		# LEDs indicadores de intensidade de incendio desligados
		gpio_3.write(0) # LED verde deligado
		gpio_4.write(0)	# LED amarelo desligado
		gpio_5.write(0)	# LED vermelho desligado
		# alarme desligado
		gpio_6.write(0)
	
	
		



