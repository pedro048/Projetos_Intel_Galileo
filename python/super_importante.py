import mraa 
import threading
import time

#---- configuracoes de ligar e desligar ----
botao_ligar = mraa.Gpio(2)
botao_ligar.dir(mraa.DIR_IN) # botao de ligar
botao_desligar = mraa.Gpio(4)
botao_desligar.dir(mraa.DIR_IN) # boatao de desligar
liga = 0
desliga = 0
aux = 0

#---- configuracao do PWM, ADC e LEDs (intensidade do incendio) ----
PWM_PIN = 5
ADC_PIN = 0           # Analog in pin
ROT_MAX = 1024.0      # Max value as measured by ADC when pot is connected

led_verde = mraa.Gpio(7) # LED verde
led_verde.dir(mraa.DIR_OUT)
led_amarelo = mraa.Gpio(8) # LED amarelo
led_amarelo.dir(mraa.DIR_OUT)
led_vermelho = mraa.Gpio(12)# LED vermelho
led_vermelho.dir(mraa.DIR_OUT)

# Set up the PWM
pwm = mraa.Pwm(PWM_PIN)
pwm.enable(True)
pwm.period_us(5000)

# Set up the ADC
adc = mraa.Aio(ADC_PIN)

#---- configuracao do BUZZER ----
buzzer = mraa.Gpio(11)
buzzer.dir(mraa.DIR_OUT)

def thread_ADC_PWM(ROT_MAX): 
    
    value = adc.read()             # ler valor do ADC
    led_intensity = value/ROT_MAX  # determina o duty cycle baseado em value 
    pwm.write(led_intensity)

def time_1(): # conta 2s
    
    time.sleep(2)

def time_2(): # conta 0.2s
    
    time.sleep(0.2)

while True: 
	# ler o estado dos botoes de ligar e desligar
	liga = botao_ligar.read()
	desliga = botao_desligar.read()
	if liga == 1: 
		aux = 1

	if desliga == 1: 
	    aux = 0
		
	if aux == 1:	# sistema acionado
		t1 = threading.Thread(target=thread_ADC_PWM,args=(1024.0,)) 
		t1.start() # ADC e PWM
		t1.join()
		
		if adc.read() >= 0 and adc.read() < 100:
			led_verde.write(1) # liga LED verde (ausencia de incendio)
			led_amarelo.write(0)
			led_vermelho.write(0)
			# alarme desligado
			buzzer.write(0)
	
		if adc.read() >= 100 and adc.read() < 200:
			led_verde.write(0)
			led_amarelo.write(1) # liga LED amarelo (incendio com intensidade moderada, mas preocupante)
			led_vermelho.write(0)
			# alarme de incendio moderado
			t2 = threading.Thread(target=time_1,args=()) 
			t2.start() 
			t2.join()
			buzzer.write(1)
			t3 = threading.Thread(target=time_2,args=()) 
			t3.start() 
			t3.join()
			buzzer.write(0)
	
		if adc.read() >= 200 and adc.read() < 1024:
			led_verde.write(0)
			led_amarelo.write(0)
			led_vermelho.write(1) # liga LED vermelho (incendio intenso)
			# alarme de incendio intenso
			t3 = threading.Thread(target=time_2,args=()) 
			t3.start() 
			t3.join()
			buzzer.write(1)
			t3 = threading.Thread(target=time_2,args=()) 
			t3.start() 
			t3.join()
			buzzer.write(0)
    
	else:	# sistema desacionado
	
		# vazao de agua cortada
		pwm.write(0) 
		# LEDs indicadores de intensidade de incendio desligados
		led_verde.write(0) # LED verde deligado
		led_amarelo.write(0)	# LED amarelo desligado
		led_vermelho.write(0)	# LED vermelho desligado
		# alarme desligado
		buzzer.write(0)
	 
