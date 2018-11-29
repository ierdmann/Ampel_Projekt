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
schleife = pfd.input_pins[6]
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

#eingabe = input(schalter)
print("Bitte gebe eine Zeit in Sekunden an:")
t = int(input())
z = 0

def Zeit():
	while int(time.time())-n <= t and schalter.value != True:
		#print("Initialisiere Durchfahrt Verkehr")
		a_v_gruen.turn_on()
		#print("Ampel_Verkehr=gruen")
		a_v_gelb.turn_off()
		a_v_rot.turn_off()
		a_f_rot.turn_on()
		#print("Ampel_Fussgaenger=rot")
		a_f_gruen.turn_off()
		print(n)
		

		if int(time.time())-n >= t:
			a_v_gruen.turn_off()
			a_v_gelb.turn_off()
			a_v_rot.turn_off()
			a_f_rot.turn_off()
			a_f_gruen.turn_off()  						#Wenn die aktuelle Zeit minus der gespeicherten Zeit gleich 10. Dann Ampel aus.
			print("Ampel_aus seit:", int(time.time())-n, "Sekunden")
			
		
	
# Hauptprogramm

n = int(time.time())
while True:
	Zeit()
	
	
	

	
	if schalter.value == True and int(time.time())-n <= t or z == 1:
		a_f_rot.turn_on()
		a_v_gruen.turn_on()
		print("Schalter aktiviert")
		time.sleep(3)
		a_v_gelb.turn_on()
		print("Ampel_Verkehr=gelb")
		a_v_gruen.turn_off()
		time.sleep(1)
		a_v_rot.turn_on()
		print("Ampel_Verkehr=rot")
		a_v_gelb.turn_off()
		time.sleep(3)
		print("Verkehr gestoppt. Fussgaenger gruen")
		a_f_gruen.turn_on()
		print("Ampel_Fussgaenger=gruen")
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
		z = 0
	if int(time.time())-n >= t and schalter.value == True and z != 1:
		a_v_rot.turn_on()
		a_f_rot.turn_on()
		time.sleep(4)
		a_v_rot.turn_off()
		a_v_gruen.turn_on()
		z = 1

		

		
		
		
