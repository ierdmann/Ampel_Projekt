import time

print("Bitte wähle eine Zeit in Sekunden:")
t = int(input())
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
		

		if int(time.time())-n >= t:		# Zeit wird verglichen und wenn t geich der wahr ist die Ampel abgeschaltet
			b = 1					# schaltet die Schleife frei wenn die Ampel aus ist, um den Schleifenprozess frei zugeben
			a_v_gruen.turn_off()
			a_v_gelb.turn_off()
			a_v_rot.turn_off()
			a_f_rot.turn_off()
			a_f_gruen.turn_off()  						#Wenn die aktuelle Zeit minus der gespeicherten Zeit gleich 10. Dann Ampel aus.
			print("Ampel_aus seit:", int(time.time())-n, "Sekunden")