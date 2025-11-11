"""Tag 1 v. simplen Taschenrechner f. Grundrechenarten"""   # Modul-Dokstring

def zeige_header():                                         # Funktion definieren
    """Zeigt den Header."""                                 # Dokstring f. die Funktion
    print("\n" + "=" * 40)                                  # obere Trennlinie
    print(" Dave's Taschenrechner ".center(40, "="))        # zentrierter Text
    print("=" * 40 + "\n")                                  # untere Trennlinie
def zeige_footer():                                         # Funktion definieren
    """Zeigt den Footer."""                                 # Dokstring f. die Funktion
    print("\n" + "=" * 40)                                  # obere Trennlinie
    print(" Ende des Programms ".center(40, "="))           # zentrierter Text
    print("=" * 40 + "\n")                                  # untere Trennlinie
def multipliziere (a, b):                                   # Funktion definieren
    """Multipliziert zwei Zahlen a und b."""                # Dokstring f. die Funktion
    return a * b                                            # Ausgabe des Ergebnisses
def dividiere (a, b):                                       # Funktion definieren
    """Dividiert Zahl a durch Zahl b."""                    # Dokstring f. die Funktion
    return a / b                                            # Ausgabe des Ergebnisses
def addiere (a, b):                                         # Funktion definieren  
    """Addiert zwei Zahlen a und b."""                      # Dokstring f. die Funktion
    return a + b                                            # Ausgabe des Ergebnisses
def subtrahiere (a, b):                                     # Funktion definieren
    """Subtrahiert Zahl a von Zahl b."""                    # Dokstring f. die Funktion
    return a - b                                            # Ausgabe des Ergebnisses

zeige_header()                                              # Header anzeigen
print(f"4 * 5 = {multipliziere(4, 5)}")                     # Multiplikation ausgeben
print(f"20 / 4 = {dividiere(20, 4)}")                       # Division ausgeben
print(f"10 + 15 = {addiere(10, 15)}")                       # Addition ausgeben
print(f"30 - 12 = {subtrahiere(30, 12)}")                   # Subtraktion ausgeben
zeige_footer()                                              # Footer anzeigen