"""Tag 4 v. simplen Taschenrechner f. Grundrechenarten"""   

# ===== KONSTANTEN =====
BREITE = 40          # Gesamtbreite
INNENBREITE = 36     # Breite ohne Rahmen
RAHMEN = "="         # Rahmen-Zeichen
EINRUECKUNG = 13     # Leerzeichen f. Zentrierung

# ===== FUNKTIONEN F. OPTIK =====
def header():                                         
    """Zeigt den Header."""                                 
    print("\n" + RAHMEN*BREITE)                                  
    print(" Dave's Taschenrechner ".center(BREITE, RAHMEN))        
    print(RAHMEN*BREITE)                                  
def footer():                                         
    """Zeigt den Footer."""
    leer()                                 
    print(RAHMEN*BREITE)                                  
    print(" Ende des Programms ".center(BREITE, RAHMEN))           
    print(RAHMEN*BREITE + "\n")                                  
def leer():
    """Leere Zeile einfügen"""
    print(RAHMEN*2 + "".center(INNENBREITE) + RAHMEN*2)
def trennung():
    """Trennlinie"""
    print(RAHMEN*BREITE)
def zeige_zeile(text):
    """Zeigt eine zentrierte Zeile mit Rahmen."""
    print(RAHMEN*2 + text.center(INNENBREITE) + RAHMEN*2)
def zeige_fehler(text):
    """Zeigt einen Fehler schön formatiert."""
    print()
    trennung()
    zeige_zeile(f"FEHLER: {text}")
    trennung()
def zeige_ergebnis(text):
    """Zeigt ein Ergebnis schön formatiert."""
    print()
    trennung()
    zeige_zeile(text)
    trennung()

# ===== RECHEN-FUNKTIONEN =====
def addiere(zahl1, zahl2):  
    """Addiert zwei Zahlen a und b."""                      
    return zahl1 + zahl2
def subtrahiere(zahl1, zahl2):
    """Subtrahiert Zahl b von Zahl a."""
    return zahl1 - zahl2
def multipliziere(zahl1, zahl2):                                   
    """Multipliziert zwei Zahlen a und b."""                
    return zahl1 * zahl2                                            
def dividiere(zahl1, zahl2):                                       
    """Dividiert Zahl a durch Zahl b."""                    
    return zahl1 / zahl2                                            
def quadrat(zahl):
    """Zahl zum Quadrat"""
    return zahl * zahl
def wurzel(zahl):
    """Quadratwurzel von a"""
    return zahl ** 0.5
def rabatt(preis, prozent):
    """Berechnet Preis nach Rabatt."""
    return preis * (1 - prozent / 100)
def proz_von(wert, prozent):
    """Berechnet b% von a."""
    return wert * prozent / 100
def aufschlag(preis, prozent):
    """Berechnet Preis mit Aufschlag."""
    return preis * (1 + prozent / 100)

# ===== INPUT-FUNKTIONEN =====
def hohle_zahl(prompt, zentriert=True):                                         
    """Abfrage einer Zahl"""
    if zentriert:
        prompt = " " * EINRUECKUNG + prompt  # Spaces für Zentrierung
    
    while True:                                                 
        try:                                                    
            zahl = float(input(prompt))                         
            return zahl                                         
        except ValueError:                                      
            print("\nFehler: Bitte nur Zahlen eingeben!\n")                         
def hole_wahl():
    """Fragt nach der Nutzer-Wahl"""
    trennung()
    wahl = input(" " * EINRUECKUNG + "Deine Wahl: ")
    trennung()
    return wahl
def menue():
    """Zeigt das Menü mit allen Optionen."""
    leer()
    zeige_zeile("Optionen:")
    zeige_zeile("[1] Addition")
    zeige_zeile("[2] Subtraktion")
    zeige_zeile("[3] Multiplikation")
    zeige_zeile("[4] Division")
    zeige_zeile("[5] Quadrat")
    zeige_zeile("[6] Wurzel")
    zeige_zeile("[7] Rabatt")
    zeige_zeile("[8] Prozent von")
    zeige_zeile("[9] Aufschlag")
    zeige_zeile("[0] Beenden")
    leer()

# ===== HAUPTPROGRAMM =====
def main():
    """Hauptfunktion des Taschenrechners."""
    header()
    
    while True:
        menue()
        wahl = hole_wahl()
        
        match wahl:
            case "1":
                print()
                zahl1 = hohle_zahl("Erste Zahl: ")                          
                zahl2 = hohle_zahl("Zweite Zahl: ")
                ergebnis = addiere(zahl1, zahl2)
                zeige_ergebnis(f"{zahl1} + {zahl2} = {ergebnis}")
                
            case "2":
                print()
                zahl1 = hohle_zahl("Erste Zahl: ")                          
                zahl2 = hohle_zahl("Zweite Zahl: ")
                ergebnis = subtrahiere(zahl1, zahl2)
                zeige_ergebnis(f"{zahl1} - {zahl2} = {ergebnis}")
                
            case "3":
                print()
                zahl1 = hohle_zahl("Erste Zahl: ")                          
                zahl2 = hohle_zahl("Zweite Zahl: ")
                ergebnis = multipliziere(zahl1, zahl2)
                zeige_ergebnis(f"{zahl1} * {zahl2} = {ergebnis}")
                
            case "4":
                print()
                zahl1 = hohle_zahl("Erste Zahl: ")                          
                zahl2 = hohle_zahl("Zweite Zahl: ")
                if zahl2 == 0:
                    zeige_fehler("Division durch 0!")
                else:
                    ergebnis = dividiere(zahl1, zahl2)
                    zeige_ergebnis(f"{zahl1} : {zahl2} = {ergebnis}")
                    
            case "5":
                print()
                zahl = hohle_zahl("Zahl: ")
                ergebnis = quadrat(zahl)
                zeige_ergebnis(f"{zahl} hoch 2 = {ergebnis}")
                
            case "6":
                print()
                zahl = hohle_zahl("Zahl: ")
                if zahl < 0:
                    zeige_fehler("Negative Wurzel!")
                else: 
                    ergebnis = wurzel(zahl)
                    zeige_ergebnis(f"Wurzel von {zahl} = {ergebnis:.4f}")
                    
            case "7":
                print()
                preis = hohle_zahl("Preis in Euro: ")
                prozent = hohle_zahl("Rabatt in %: ")
                
                if prozent < 0 or prozent > 100:
                    zeige_fehler("Rabatt muss zwischen 0-100% liegen!")
                else:
                    neuer_preis = rabatt(preis, prozent)
                    ersparnis = preis - neuer_preis
                    
                    print()
                    trennung()
                    zeige_zeile(f"Originalpreis: {preis:.2f} Euro")
                    zeige_zeile(f"Rabatt: {prozent:.0f}%")
                    zeige_zeile(f"Ersparnis: {ersparnis:.2f} Euro")
                    zeige_zeile(f"Neuer Preis: {neuer_preis:.2f} Euro")
                    trennung()
                    
            case "8":
                print()
                wert = hohle_zahl("Ausgangswert: ")
                prozent = hohle_zahl("Wieviel Prozent: ")
                
                ergebnis = proz_von(wert, prozent)
                zeige_ergebnis(f"{prozent:.0f}% von {wert:.2f} = {ergebnis:.2f}")
                
            case "9":
                print()
                preis = hohle_zahl("Preis in Euro: ")
                prozent = hohle_zahl("Aufschlag in %: ")
                
                if prozent < 0:
                    zeige_fehler("Aufschlag muss positiv sein!")
                else:
                    neuer_preis = aufschlag(preis, prozent)
                    mehrpreis = neuer_preis - preis
                    
                    print()
                    trennung()
                    zeige_zeile(f"Originalpreis: {preis:.2f} Euro")
                    zeige_zeile(f"Aufschlag: {prozent:.0f}%")
                    zeige_zeile(f"Mehrpreis: {mehrpreis:.2f} Euro")
                    zeige_zeile(f"Neuer Preis: {neuer_preis:.2f} Euro")
                    trennung()
                    
            case "0":
                print()
                trennung()
                zeige_zeile("Bis bald!")
                trennung()
                footer()
                break
                
            case _:
                zeige_fehler("Ungültige Eingabe! Bitte 0-9 wählen.")

if __name__ == "__main__":
    main()