import pifacedigitalio
import time
pifacedigital = pifacedigitalio.PiFaceDigital()

pifacedigital.input_port.value

		
		
while True:
	pifacedigital.output_pins[5].turn_on()
	pifacedigital.output_pins[6].turn_off()
	pifacedigital.output_pins[7].turn_off()
		
	if pifacedigital.input_pins[7].value == True:
		pifacedigital.leds[5].turn_off()
		pifacedigital.leds[6].turn_on()
		time.sleep(2)
		pifacedigital.leds[7].turn_on()
		pifacedigital.leds[6].turn_off()
		time.sleep(3)
		pifacedigital.leds[2].turn_on()
		time.sleep(0.4)
		pifacedigital.leds[2].turn_off()
		time.sleep(0.4)
		pifacedigital.leds[2].turn_on()
		time.sleep(0.4)
		pifacedigital.leds[2].turn_off()
		time.sleep(0.4)
		pifacedigital.leds[2].turn_on()
		time.sleep(0.4)
		pifacedigital.leds[2].turn_off()
		time.sleep(0.4)
		pifacedigital.leds[2].turn_on()
		time.sleep(0.4)
		pifacedigital.leds[2].turn_off()
		time.sleep(0.4)

