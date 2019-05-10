/**
 * 
 * This is a 'c' program that demos the usage of the mraa library 
 * to blink an LED connected to port D5 on Intel Edison/Galileo
 * 
 * setup:
 * The LED is connected to port D5
 * 
 * Compilation:
 * gcc -o blink blink.c -lmraa
 * 
 * Demo:
 * Run the application
 * ./blink
 * You should see the LED blink 
 * 
 * You can exit this demo by hitting ctrl+c
 * 
 * 
 */

#include <mraa.h>

#define LED_PIN      7       /**< The pin where the LED is connected */


int main(void)
{
    mraa_gpio_context      ledPin;
    
    /* Step1: Init the mraa subsystem */
    mraa_init();
    
    /* Step2: Set the ledPin as port D5 */
    ledPin = mraa_gpio_init(LED_PIN);
     
    /* Step3: Set the said pin as output */
    mraa_gpio_dir(ledPin, MRAA_GPIO_OUT);
    
    while(1)
    {
        /* Step4: Set the desired voltage level at the pin */
        mraa_gpio_write(ledPin, 1);
        sleep(1);
        mraa_gpio_write(ledPin, 0);
        sleep(1);
    }
    
    return 0;
}
