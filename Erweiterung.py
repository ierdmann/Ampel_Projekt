# Ampel Projekt
#Erweiterung der basis Ampelschaltung
# Ein Timer ist implementiert worden, da durch ist ein vergleich von Zeit möglich.
# Es wurde zu diesem Zweck UNIX Zeit verwendet, da es sich um eine vordlaufende Zahl handelt
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
n = int(time.time())		#Zeitspeicher für das Abschalten der Ampel nach der gewählten Zeit bei Programmstart
x = int(time.time())		#Zeitspeicher für die Reaktivierung der Kontaktschleife um die 10 Sekunden einzuhalten


# Funktion um Zeit zu vergleichen 
def Zeit():
	while int(time.time())-n <= t and schalter.value != True:	#Die Zeit ist kleiner als die geählte Zeit, es ist kein Schalter gedrückt!
		a_v_gruen.turn_on()
		a_v_gelb.turn_off()
		a_v_rot.turn_off()
		a_f_rot.turn_on()
		a_f_gruen.turn_off()
		print(int(time.time())-n)		#Zeigt die Zeit welch nach Programmstart vergangen ist
		

		if int(time.time())-n >= t:		# Zeit wird verglichen und wenn t größer als die gewählte Zeit ist dann Ampel abgeschalten.	
			a_v_gruen.turn_off()		
			a_v_gelb.turn_off()
			a_v_rot.turn_off()
			a_f_rot.turn_off()
			a_f_gruen.turn_off()  						
			print("Ampel aus!")
			
		
	
# Hauptprogramm

									
while True:
	Zeit()					# fortwährend wird die Funktion Zeit geprüft und ausgeführt
	print("Ampel aus seit:", int(time.time())-n, "Sekunden")
	
	

	
	if schalter.value == True and int(time.time())-n <= t or z == 1: #Solange die Ampel an ist wird diese Schaltsequenz abgearbeitet
		a_f_rot.turn_on()											#Bedingung sind das die gemessene Zeit kleiner als die Eingegebene Zeit
		a_v_gruen.turn_on()											#ist
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
		
	elif int(time.time())-n >= t and schalter.value == True:	#Ist die Ampel nach der gewählten Zeit ausgegangen und der Schalter
		a_v_rot.turn_on()										#wird gedrückt, wird Verkehrsampel und Fußgänger Ampel rot
		a_f_rot.turn_on()										#und folgt einem bestimmten Ablauf. Am ende begint dann der normale 
		time.sleep(4)											#Fußgängerzyklus
		a_v_rot.turn_off()
		a_v_gruen.turn_on()
		z = int(1)

	elif schleife.value == True and schalter.value != True and int(time.time())-x >= 10: #Eine Kontaktschleife wird durch Fahrzeuge ausgelöst
		print("Schleife aktiv")															#welche im Boden 500m vor der Ampel plaziert ist
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
		
	elif schleife.value == True and schalter.value != True and int(time.time())-x <=10:	#Wird die Kontaktschleife erneut  innerhalb von 10sec
		print("Schleife erneut aktiviert")												#überfahren, bleibt die Ampel grün und geht wieder aus
		a_v_gruen.turn_on()
		a_f_rot.turn_on()
		time.sleep(3)
		a_v_gruen.turn_off()
		a_f_rot.turn_off()
		print("Schleife beendet")
