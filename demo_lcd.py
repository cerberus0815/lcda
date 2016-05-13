# Kleines Zeilen Programm
# Demonstrationsprogramm für die I2C 16x2 Displays.
# Geschrieben von IT&Web Schwendenwein!

# Importiere benötigte libraries fürs Komunizieren und Anzeigen
import lcddriver
import time

# Lade den Treiber und setze ihn auf "display"
# Beim benutzen div. Befehle aus der Library, nutze immer das Präfix "display." als erst.
display = lcddriver.lcd()

# Haupcode:
try:
    while True:
        # Maximum 16 Zeichen!!!
        print("Schreibe Display")
        display.lcd_display_string("Guten Tag!", 1) # Schreibe Text in erste Zeile des Displays
        display.lcd_display_string("Viel Spass!", 2) # Schreibe Text in zweite Zeile des Displays
        time.sleep(2)                                     # Zeit zum lesen der Zeilen
        display.lcd_display_string("Happy Coding!!", 1)  # Aktualisiert Text in erste Zeile des Displays
        time.sleep(2)                                     # Zeit zum lesen der Zeilen
        display.lcd_clear()                               # Lösche das Display
        time.sleep(2)                                     # Zeit zum lesen der Zeilen

except KeyboardInterrupt: # Tastenkombination(ctrl+c), stoppt das Programm und löscht das Display
    print("Display sauber!")
    display.lcd_clear()
