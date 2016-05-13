# Kleines Zeit Programm.
# Demonstrationsprogramm für die I2C 16x2 Displays.
# Geschrieben von IT&Web Schwendenwein!

# Importiere benötigte libraries fürs Komunizieren und Anzeigen
import lcddriver
import time
import datetime

# Lade den Treiber und setze ihn auf "display"
# Beim benutzen div. Befehle aus der Library, nutze immer das Präfix "display." als erst.
display = lcddriver.lcd()

try:
    print("Schreibe Display")
    display.lcd_display_string(">> IT & Web <<", 1) # Schreibe Text in erste Zeile des Displays
    while True:
        display.lcd_display_string(str(datetime.datetime.now().time()), 2) # Sende die Zeit an das Display in Zeile 2
        # Programm läuft endlos, keine unterbrechung (kann hinzugefügt werden: time.sleep)

except KeyboardInterrupt: # Tastenkombination(ctrl+c), stoppt das Programm und löscht das Display
    print("Display sauber!")
    display.lcd_clear()
