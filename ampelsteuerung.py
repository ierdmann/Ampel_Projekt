import time
import pifacedigitalio
pfd = pifacedigitalio.PiFaceDigital()


while True:
	pfd.output_pins[5].turn_on()
	pfd.output_pins[6].turn_off()
	pfd.output_pins[7].turn_off()
	
		
	if pfd.input_pins[7].value == True:
		pfd.output_pins[6].turn_on()
		pfd.output_pins[5].turn_off()
		time.sleep(1)
		pfd.output_pins[7].turn_on()
		pfd.output_pins[6].turn_off()
		time.sleep(5)	
		pfd.output_pins[7].turn_off()
		pfd.output_pins[6].turn_on()
		time.sleep(1)
		pfd.output_pins[5].turn_on()
		pfd.output_pins[6].turn_off()

