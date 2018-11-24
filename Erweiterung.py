# Ampel Projekt
#Versuch einen Countdown zu integrieren
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

def Zeit():
	a_v_gruen.turn_off()
	a_v_gelb.turn_off()
	a_v_rot.turn_off()
	a_f_rot.turn_off()
	a_f_gruen.turn_off()
	
	if int(time.time())-n >= 10:
		b = 1
		print("Ampel_aus", n)
		read(schalter.value == True)

# Hauptprogramm
b = 0
n = int(time.time())
while True:
#	print("Initialisiere Durchfahrt Verkehr")
	a_v_gruen.turn_on()
	a_v_gelb.turn_off()
	a_v_rot.turn_off()
	a_f_rot.turn_on()
	a_f_gruen.turn_off()
	Zeit()
	
	
	

	
	if schalter.value == True:
		b = 1
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
		n = int(time.time())
		b = 0

	

		
		
		
