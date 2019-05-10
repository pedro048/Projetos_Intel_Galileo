#include <mraa.h>

/*
Projeto liga LED ao apertar um botao e desliga ao soltar
*/

#define LED_PIN 7
#define BUTTON 2

int main(void){
	// Configuracoes iniciais
    mraa_gpio_context	ledPin;
	mraa_gpio_context	botao;
	mraa_init(); // inicializa o mraa
	ledPin = mraa_gpio_init(LED_PIN); // seta ledPin com valor do pino LED_PIN
	botao = mraa_gpio_init(BUTTON);	  // seta botao com valor do pino BUTTON
	mraa_gpio_dir(ledPin, MRAA_GPIO_OUT); // configura o pino do LED como saida
	mraa_gpio_dir(botao, MRAA_GPIO_IN);	// configura o pino do BOTAO como entrada
	int leitura = 0;
    while(1){
		leitura = mraa_gpio_read(botao);
		if(leitura == 1){
			mraa_gpio_write(ledPin, 1); // liga o LED se o botao for apertado (config pull-down)
		}else{
			mraa_gpio_write(ledPin, 0); // desliga o LED se o botao nao tiver pressionado (config pull-down)
		}

    }
    return 0;
}
