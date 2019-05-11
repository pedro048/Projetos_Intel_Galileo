import mraa
import time

gpio_1 = mraa.Gpio(7) # inicializa o pino 7 (botao que aciona o sistema)

gpio_2 = mraa.Gpio(8) # inicializa o pino 8 (LED que indica o acionamento do sistema)

gpio_3 = mraa.Gpio(9) # inicializa o pino 9 (LED que representa vazao de agua para combater o incendio)

gpio_1 = mraa.Gpio(A0) # inicializa o pino  (botao que aciona o sistema)
