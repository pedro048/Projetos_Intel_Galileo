 
import mraa 
import threading
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
#global ROT_MAX = 1024.0      # Max value as measured by ADC when pot is connected

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
global led_intensity

# Set up the ADC
adc = mraa.Aio(ADC_PIN)
global value

#---- configuracao do BUZZER ----
gpio_6 = mraa.Gpio(11)
gpio_6.dir(mraa.DIR_OUT)


def thread_ADC(ROT_MAX): 
    
    value = adc.read()             # ler valor do ADC
    led_intensity = value/ROT_MAX  # determina o duty cycle baseado em value 
    
def thread_PWM(): 
    
    pwm.write(led_intensity)   
  
def thread_time_1(): 
    
    time.sleep(2) 
    
def thread_time_2(): 
    
    time.sleep(0.5) 
    
def thread_servidor(): 

    #definir 


while True: 
    
    t1 = threading.Thread(target=thread_ADC,args=(1024.0,)) 
    t2 = threading.Thread(target=thread_PWM, args=(,)) 
    t3 = threading.Thread(target=thread_time_1,args=(,)) 
    t4 = threading.Thread(target=thread_time_2, args=(,)) 

        
    liga = gpio_1.read()
	desliga = gpio_2.read()
	if liga == 1: 
		aux = 1

	if desliga == 1: 
	    aux = 0
		
	if aux == 1:	# sistema acionado
		
		t1.start() # ADC
		t1.join() 
		t2.start() # PWM
		t2.join()
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
			t3.start() # time de 2s
			t3.join()
			gpio_6.write(1)
			t3.start()
			t3.join()
			gpio_6.write(0)
	
		if value >= 200 and value < 1023:
			gpio_3.write(0)
			gpio_4.write(0)
			gpio_5.write(1) # liga LED vermelho (incendio intenso)
			# alarme de incendio intenso
			t4.start() # time de 0.5s
			t4.join()
			gpio_6.write(1)
			t4.start()
			t4.join()
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
        
    time.sleep(5) #tempo de execucao
 
print("Done!")

	 
 
