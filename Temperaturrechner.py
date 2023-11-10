print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")

auswahl = float (input("Welche Umrechnung möchtest du? "))

temperatur = float (input("Wie viel Grad sind es? "))

if auswahl == 1:
   ausgang = temperatur - 273.15
elif auswahl == 2:
   ausgang = (temperatur + 9/5) + 32 
elif auswahl == 3:
    ausgang = (temperatur - 273,15)    
elif auswahl == 4:
    ausgang = (temperatur - 273,15)
elif auswahl == 5:
    ausgang = (temperatur - 32) * 5/9
elif auswahl == 6:
    ausgang = (temperatur - 32) * 5/9 + 273,15
else:
    print("Layer 8 Problem/ PEBKAC")

print(ausgang)
        

