"""
OOP Assignment: Quiz-Fragen-System für Linux Essentials
Ein Programm zum Erstellen u. Abfragen von Prüfungsfragen

Autor: Dave
Datum: 16.11.2025
Assignment: Python OOP Grundlagen
"""

# Konstanten f. d. Formatierung
BREITE = 95
INNENBREITE = 91
RAHMEN = "="         
EINRUECKUNG = 31
OPT_EINRUECKUNG = 38
# Funktionen f. d. Formatierung
def header():
    """Header mit Rahmen ausgeben."""
    trennung()
    zeige_zeile(" Linux Essentials Quiz-System ")
    trennung()
    leer()
def footer():
    """Zeigt den Programm-Footer."""
    trennung()
    zeige_zeile(" Ende vom Quiz ")
    trennung()
def leer():
    """Leere Zeile einfügen"""
    print(RAHMEN*2 + "".center(INNENBREITE) + RAHMEN*2)
def trennung():
    """Trennlinie"""
    print(RAHMEN*BREITE)
def tren_leer():
    """Trennlinie mit leerer Zeile."""
    leer()
    trennung()
    leer()
def zeige_zeile(text):
    """Zeigt eine zentrierte Zeile mit Rahmen."""
    print(RAHMEN*2 + text.center(INNENBREITE) + RAHMEN*2)
def zeige_option(text):
    """Zeigt eine linksbündige Option mit Rahmen."""
    print(RAHMEN*2 + " " * OPT_EINRUECKUNG + text.ljust(INNENBREITE - OPT_EINRUECKUNG) + RAHMEN*2)
def einr_input(prompt):
    """Nutzt Input mit Rahmen."""
    leer()
    input(RAHMEN*2 + " " * EINRUECKUNG + prompt)
def erstelle_fragen():
    """
    Erstellt u. gibt alle Quiz-Fragen zurück.
    
    Returns:
        list: Liste mit Frage-Objekten für das Quiz
    """
    fragen = [
        Frage(
            fragetext="Wer hat den Linux-Kernel ursprünglich entwickelt?",
            optionen=["Richard Stallman", "Linus Torvalds", "Dennis Ritchie", "Ken Thompson"],
            richtige_antwort=1,
            kategorie="Linux Evolution"
        ),
        Frage(
            fragetext="Welche Distribution-Familie verwendet das .deb-Paketformat?",
            optionen=["Red Hat Familie", "Debian Familie", "SUSE Familie", "Arch Familie"],
            richtige_antwort=1,
            kategorie="Linux Evolution"
        ),
        Frage(
            fragetext="Welcher Webserver ist am weitesten verbreitet in der Open-Source-Welt?",
            optionen=["IIS", "Apache HTTP Server", "WebLogic", "Tomcat"],
            richtige_antwort=1,
            kategorie="Open Source"
        ),
        Frage(
            fragetext="Welche Desktop-Umgebung wird standardmäßig bei Ubuntu verwendet?",
            optionen=["KDE Plasma", "GNOME", "Xfce", "LXDE"],
            richtige_antwort=1,
            kategorie="Desktop"
        ),
        Frage(
            fragetext="Wie setzt man eine Umgebungsvariable für Kindprozesse?",
            optionen=["set VARIABLE=value", "export VARIABLE=value",
                "env VARIABLE=value", "var VARIABLE=value"],
            richtige_antwort=1,
            kategorie="Kommandozeile"
        ),
        Frage(
            fragetext="Was gibt der Befehl 'echo $PATH' aus?",
            optionen=["Das aktuelle Verzeichnis", "Die Suchpfade für ausführbare Dateien",
                "Den Pfad zur Home-Directory", "Alle installierten Programme"],
            richtige_antwort=1,
            kategorie="Kommandozeile"
        ),
        Frage(
            fragetext="Welcher Befehl zeigt den Typ eines Befehls an (alias, builtin, file)?",
            optionen=["which", "type", "whereis", "locate"],
            richtige_antwort=1,
            kategorie="Kommandozeile"
        ),
        Frage(
            fragetext="Mit welchem Befehl durchsucht man die Man-Pages nach einem Stichwort?",
            optionen=["man -s keyword", "man -k keyword",
                "man -f keyword", "man -w keyword"],
            richtige_antwort=1,
            kategorie="Hilfe-System"
        ),
        Frage(
            fragetext="Welches Verzeichnis enthält Benutzer-Home-Verzeichnisse?",
            optionen=["/etc", "/var", "/home", "/root"],
            richtige_antwort=2,
            kategorie="Dateisystem"
        ),
        Frage(
            fragetext="Mit welcher Tastenkombination wechselt man zu einer virtuellen Konsole (tty)?",
            optionen=["Alt + F1-F6", "Ctrl + Alt + F1-F6", 
                "Ctrl + F1-F6", "Shift + F1-F6"],
            richtige_antwort=1,
            kategorie="System"
        )
    ]
    return fragen
def hole_antwort(prompt):
    """Holt Nutzer-Input mit Validierung u. Rahmen."""
    while True:
        leer()
        nutzer_input = input(RAHMEN*2 + " " * EINRUECKUNG + prompt).upper()
        
        if nutzer_input in ["A", "B", "C", "D"]:
            return nutzer_input
        else:
            leer()
            zeige_zeile(" FEHLER: Bitte nur A, B, C oder D! ")

# Klasse f. d. Fragen
class Frage:
    """
    Eine Quiz-Frage für Linux Essentials Prüfungsvorbereitung.
    
    Diese Klasse repräsentiert eine Multiple-Choice-Frage mit vier
    Antwortmöglichkeiten u. Kategorisierung nach Themengebiet.
    
    Attributes:
        fragetext (str): Der Text der Frage
        optionen (list): Liste mit 4 Antwortmöglichkeiten
        richtige_antwort (int): Index der richtigen Antwort (0-3)
        kategorie (str): Kategorie der Frage (z.B. "Kommandozeile")
    """
    # Klassenattribut - zählt alle erstellten Fragen
    anzahl_fragen = 0

    def __init__(self, fragetext, optionen, richtige_antwort, kategorie):
        """
        Initialisiert eine neue Quiz-Frage.
        
        Args:
            fragetext (str): Der Text der Frage
            optionen (list): Liste mit 4 Antwortmöglichkeiten
            richtige_antwort (int): Index der richtigen Antwort (0-3)
            kategorie (str): Kategorie der Frage
        """
        # Kontrolle d eingereichten Fragen-Daten
        if len(optionen) != 4:
            raise ValueError("Es müssen genau 4 Optionen sein!")
        
        if not 0 <= richtige_antwort <= 3:
            raise ValueError("Richtige Antwort muss 0-3 sein!")
    
        # Fragen-Anzahl steigern
        Frage.anzahl_fragen += 1 

        # Attribute setzen
        self.frage = fragetext
        self.optionen = optionen
        self.richtige_antwort = richtige_antwort
        self.kategorie = kategorie
        
    def zeige_frage(self):
        """
        Zeigt die Frage mit allen Antworten an.
        
        Die Ausgabe zeigt Kategorie, Fragetext u. vier Optionen
        mit den Buchstaben A-D in einem Rahmen.
        """
        zeige_zeile(f" Kategorie: {self.kategorie} ")
        leer()
        zeige_zeile(f" Frage: {self.frage} ")
        leer()
        buchstaben = ["A", "B", "C", "D"]
        for i, option in enumerate(self.optionen):
            zeige_option(f" {buchstaben[i]}: {option} ")

    def checke_antwort(self, nutzer_antwort):
        """
        Checkt ob die Antwort des Users korrekt ist.
        
        Args:
            nutzer_antwort (str): Die Antwort des Users ("A", "B", "C", oder "D")
            
        Returns:
            bool: True wenn die Antwort richtig ist, False sonst
        """
        # Dictionary z. Zuordnung d. Buchstaben zu Indizes
        antwort_zuordnen = {"A": 0, "B": 1, "C": 2, "D": 3}
        nutzer_index = antwort_zuordnen.get(nutzer_antwort)

        # Kontrolle der Antwort
        if nutzer_index is None:
            return False
        # Vergleich mit richtiger Antwort
        elif nutzer_index == self.richtige_antwort:
            return True

    def zeige_antwort(self):
        """
        Zeigt die richtige Antwort an.
        
        Die Ausgabe erfolgt mit dem entsprechenden 
        Buchstaben (A-D) u. dem Text d. richtigen Antwort.
        """
        buchstaben = ["A", "B", "C", "D"]
        richtige_buchstabe = buchstaben[self.richtige_antwort]
        richtige_option = self.optionen[self.richtige_antwort]
        zeige_zeile(f" {richtige_buchstabe}: {richtige_option} ")

# Hauptprogramm
def main():
    """
    Hauptfunktion - Testet die Frage-Klasse mit Beispiel-Fragen.
    
    Erstellt Test-Fragen, zeigt sie an, fragt den User nach Antworten
    u. gibt Feedback ob die Antwort richtig oder falsch war.
    """
    header()

    fragen_liste = erstelle_fragen()
    richtige_antworten = 0
    zeige_zeile(f" Insgesamt {Frage.anzahl_fragen} Fragen geladen ")
    leer()

    # Quiz durchlaufen
    for i, frage in enumerate(fragen_liste, 1):
        
        zeige_zeile(f" Frage {i} von {len(fragen_liste)} ")
        leer()
        
        # Frage anzeigen u. Antwort holen
        frage.zeige_frage()
        antwort = hole_antwort("Deine Antwort (A/B/C/D): ")
        
        # Antwort kontrollieren u. Feedback geben
        if frage.checke_antwort(antwort):
            leer()
            zeige_zeile(" RICHTIG! Sehr gut! ")
            tren_leer()
            richtige_antworten += 1
        else:
            leer()
            zeige_zeile(" FALSCH! Die richtige Antwort ist: ")
            frage.zeige_antwort()
            tren_leer()

    # Endergebnis
    zeige_zeile(f" ENDERGEBNIS: {richtige_antworten}/{len(fragen_liste)} richtig ")
    zeige_zeile(f" Das sind {richtige_antworten/len(fragen_liste)*100:.0f}% ")
    leer()
    trennung()
    leer()

    input(" " * EINRUECKUNG + "Drücke Enter zum Beenden... ")

    footer()

if __name__ == "__main__":
    main()