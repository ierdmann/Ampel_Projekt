#Erweiterung der Ampelsteuerung
# Ampel Projekt

import time
import pifacedigitalio
import atexit


pfd = pifacedigitalio.PiFaceDigital()

# a = ausgabe
# v = verkehrsampel
a_v_gruen = pfd.output_pins[5]
a_v_gelb = pfd.output_pins[6]
a_v_rot = pfd.output_pins[7]

# f = Fussgaenger
a_f_gruen = pfd.output_pins[3]
a_f_rot = pfd.output_pins[4]

schalter = pfd.input_pins[7]

def status_anzeigen():
	print("TODO")

# Ampel ausschalten, wenn Programm beendet wird
def ausschalten():
	a_v_gruen.turn_off()
	a_v_gelb.turn_off()
	a_v_rot.turn_off()
	a_f_gruen.turn_off()
	a_f_rot.turn_off()

atexit.register(ausschalten)

#Countdown initialisieren



# Hauptprogramm

while True:
#	print("Initialisiere Durchfahrt Verkehr")
	a_v_gruen.turn_on()
	a_v_gelb.turn_off()
	a_v_rot.turn_off()
	a_f_rot.turn_on()
	a_f_gruen.turn_off()

	
		
if schalter.value == True:
	print("Schalter aktiviert")
	time.sleep(3)
	a_v_gelb.turn_on()
	a_v_gruen.turn_off()
	time.sleep(1)
	a_v_rot.turn_on()
	a_v_gelb.turn_off()
	time.sleep(3)
	print("Verkehr gestoppt. Fussgaenger gruen")
	a_f_gruen.turn_on()
	a_f_rot.turn_off()
	time.sleep(5)
	print("Fussgaenger-Phase beendet")
	a_f_gruen.turn_off()
	a_f_rot.turn_on()
	time.sleep(3)
	print("Verkehr starten")
	a_v_gelb.turn_on()
	time.sleep(1)
	a_v_gruen.turn_on()
	a_v_rot.turn_off()
	a_v_gelb.turn_off()
	print("Fussgaenger-phase beendet")

#elif schalter.value == False:
#	def countdown(n):
#		while n > 0:
#			print(time.sleep(1),"Zahl",n)
#			n = n - 1
#		if n == 0:
#			print("ende")
#countdown(10)

