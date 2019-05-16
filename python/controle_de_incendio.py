


import thread
import time

from socket import * # sockets

# definicao das variaveis para o servidor 
serverName = '' # ip do servidor (em branco)
serverPort = 2114 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para "ouvir" conexoes
print ("Servidor TCP esperando conexoes na porta %d ..." % (serverPort))
   
connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes

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

# Define a function for the thread
def threads( threadName, delay):
   while 1:
      time.sleep(delay)
      if(threadName == 1):
         msg = connectionSocket.recv(1024)
         print  msg
         if msg == "sim":
            connectionSocket.send("Valor do ADC: x ") #precisa mudar pra enviar o valor do ADC
         else: break
      elif threadName == 2:
         #print "botar thread para ADC"
		 value = adc.read()             # ler valor do ADC
         led_intensity = value/ROT_MAX  # determina o duty cycle baseado em value

      elif threadName == 3:
         #print "botar thread para ler botoes"
		 # ler o estado dos botoes de ligar e desligar
		 liga = gpio_1.read()
		 desliga = gpio_2.read()
		 if liga == 1: 
			aux = 1

		 if desliga == 1: 
			aux = 0
            
      elif threadName == 4:
         #print "interrupcao" # entra aqui a cada 5s
         

try:
   thread.start_new_thread( threads, (1, 2, ) )
   thread.start_new_thread( threads, (2, 3 ) )
   thread.start_new_thread( threads, (3, 4 ) )
   thread.start_new_thread( threads, (4, 5 ) )
except:
   print ("Error: unable to start thread")

while 1:
    rqs = str(msg.decode('utf-8'))
    if aux == 1:	# sistema acionado
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
		
        connectionSocket.close() # encerra o socket com o cliente
	serverSocket.close() # encerra o socket do servidor
