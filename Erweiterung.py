# Ampel Projekt
#Erweiterung der basis Ampelschaltung
# Ein Timer ist implementiert worden, durch vergleich von Zeit.
# es wurde zu diesem Zweck UNIX Zeit verwendet da es sich um eine vordlaufende Zahl handelt
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


print("Bitte gebe eine Zeit in Sekunden an:") # Bevor das Programm startet, muss eine Zeit in Sekunden eingegeben werden mit dem das 
t = int(input())   							  # Programm arbeitet. 
z = int(0)		# Zyklus Variable um einen Schalter zu verlängern
b = int(0)
n = int(time.time())
x = int(time.time())
# Funktion um Zeit zu vergleichen 
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
		print(int(time.time())-n)
		

		if int(time.time())-n >= t:		# Zeit wird verglichen und wenn t geich der wahr ist die Ampel abgeschaltet
			b = int(1)					# schaltet die Schleife frei wenn die Ampel aus ist, um den Schleifenprozess frei zugeben
			a_v_gruen.turn_off()
			a_v_gelb.turn_off()
			a_v_rot.turn_off()
			a_f_rot.turn_off()
			a_f_gruen.turn_off()  						#Wenn die aktuelle Zeit minus der gespeicherten Zeit gleich 10. Dann Ampel aus.
			print("Ampel aus!")
			
		
	
# Hauptprogramm

		# bei Programmstart wird die Zeit in "n" gespeichert
while True:
	Zeit()					# fortwährend wird die Funktion Zeit geprüft und ausgeführt
	print("Ampel aus seit:", int(time.time())-n, "Sekunden")
	
	

	
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
		z = int(0)
		b = int(0)
	elif int(time.time())-n >= t and schalter.value == True:
		a_v_rot.turn_on()
		a_f_rot.turn_on()
		time.sleep(4)
		a_v_rot.turn_off()
		a_v_gruen.turn_on()
		z = int(1)

	elif schleife.value == True and schalter.value != True and int(time.time())-x >= 10:
		print("Schleife aktiv")
		a_f_rot.turn_on()
		a_v_rot.turn_on()
		time.sleep(4)
		a_v_gelb.turn_on()
		time.sleep(2)
		a_v_rot.turn_off()
		time.sleep(2)
		a_v_gelb.turn_off()
		a_v_gruen.turn_on()
		time.sleep(10)
		a_v_gruen.turn_off()
		a_v_gelb.turn_on()
		a_v_rot.turn_on()
		time.sleep(2)
		a_v_rot.turn_off()
		a_f_rot.turn_off()
		a_v_gelb.turn_off()
		x = int(time.time())
		print("Schleife beendet")
		
	elif schleife.value == True and schalter.value != True and int(time.time())-x <=10:
		print("Schleife erneut aktiviert")
		a_v_gruen.turn_on()
		a_f_rot.turn_on()
		time.sleep(3)
		a_v_gruen.turn_off()
		a_f_rot.turn_off()
		print("Schleife beendet")
