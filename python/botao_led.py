import mraa

# Projeto LED e botao na lógica retentiva

# Configuracoes iniciais
	
	
#gpio_1 = mraa.Gpio(7)   # initialise gpio 7
#gpio_1.dir(mraa.DIR_OUT) # set gpio 7 to output (LED)
#gpio_2 = mraa.Gpio(2)	# initialise gpio 2
# gpio_2.dir(mraa.DIR_IN)  # set gpio 2 to INPUT	(botao)
leitura = 0
cont = 0
	
while True:
# leitura = gpio_2.read()
if leitura == 1:
	cont++
	if cont == 2:
		cont = 0
			
# logica retentiva
if cont == 1:
	#gpio_1.write(1) # liga o LED se o botao for apertado (config pull-down) e permanece ligado ate o proximo aperto
else:
	#gpio_1.write(0) # desliga o LED na config pull-down. O aperto apos o acendimento desliga
		
    
	
