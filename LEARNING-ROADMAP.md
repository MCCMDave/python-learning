# 📚 PYTHON LEARNING ROADMAP

**Version:** 1.0  
**Für:** Dave's Python-Lernreise  
**Zeitrahmen:** 8-12 Wochen (flexibel)  
**Status:** ✅ Phase 1 & 1.5 abgeschlossen | 🔄 Phase 2 läuft

---

## 📍 AKTUELLER STAND (November 2025)

```
✅ Phase 1: Taschenrechner (3 Wochen)         - ABGESCHLOSSEN
✅ Phase 1.5: OOP-Grundlagen                  - ABGESCHLOSSEN  
🔄 Phase 2: Quiz-Engine (2 Wochen)            - IN ARBEIT
⏳ Phase 3: Quiz-Merger (4 Wochen)            - GEPLANT
💡 Bonus: Homelab-Integration (ongoing)       - PARALLEL
```

**Abgeschlossene Projekte:**
- ✅ [Taschenrechner mit 9 Operationen](../phase-1/t4_taschenrechner_optimiert.py)
- ✅ [Assignment 1: Service Monitor](../phase-1/david_vaupel_assignment1.py)
- ✅ [Assignment 2: Quiz-System (OOP)](../phase-1.5/david_vaupel_assignment2.py)

---

## 📑 INHALTSVERZEICHNIS

- [Übersicht](#-übersicht)
- [Phase 1: Taschenrechner](#-phase-1-taschenrechner-wochen-1-3-) ✅
- [Phase 2: Quiz-Engine](#-phase-2-quiz-engine-wochen-4-5-) 🔄
- [Phase 3: Quiz-Merger](#-phase-3-quiz-merger-wochen-6-9-) ⏳
- [Bonus: Homelab-Integration](#-bonus-homelab-integration-ongoing)
- [Tracking & Review](#-tracking--review)
- [Learning Metrics](#-learning-metrics)
- [Tipps für den Erfolg](#-tipps-für-den-erfolg)

---

## 🎯 ÜBERSICHT

Diese Roadmap führt durch drei Hauptphasen des Python-Lernens, von grundlegenden Konzepten bis zu fortgeschrittenen Techniken. Jede Phase baut auf der vorherigen auf und endet mit einem funktionierenden Projekt.

**Lernphilosophie:**
- 🎯 Projektorientiertes Lernen (kein theoretisches Buch-Lernen)
- 🔨 Hands-on Coding jeden Tag
- 📈 Kontinuierlicher Fortschritt in kleinen Schritten
- 🎉 Erfolge feiern und dokumentieren

---

## 📅 PHASE 1: TASCHENRECHNER (Wochen 1-3) ✅

**Status:** ✅ Abgeschlossen  
**Zeitraum:** November 2025  
**Projekt:** [t4_taschenrechner_optimiert.py](../phase-1/t4_taschenrechner_optimiert.py)

### 🎯 Lernziele
- ✅ Python-Syntax & Grundlagen
- ✅ Variablen & Datentypen
- ✅ Input/Output
- ✅ Funktionen
- ✅ Bedingungen (if/elif/else)
- ✅ Schleifen (while/for)
- ✅ Error-Handling (try/except)
- ✅ Listen & Dictionaries (Basics)
- ✅ Match/Case Statement
- ✅ Code-Organisation & Best Practices

---

### 📖 Woche 1: Console-Rechner Basics

#### Tag 1: Setup & Hello World (Montag) 🌱
**Lernziel:** Python-Umgebung kennenlernen

**Aufgaben:**
- [x] VS Code (oder IDE deiner Wahl) öffnen
- [x] Neue Datei: `calculator_v1.py` erstellen
- [x] Erstes "Hello World" schreiben
- [x] Script ausführen (F5 oder Terminal)
- [x] Verstehen: `print()` Funktion

**Code-Beispiel zum Nachbauen:**
```python
# Mein erstes Python-Programm
print("Willkommen zu meinem Taschenrechner!")
print("Version 1.0")
```

**Erfolgskriterium:** ✅ Script läuft ohne Fehler

---

#### Tag 2: Erste Berechnungen (Dienstag) 🔢
**Lernziel:** Variablen & Operatoren

**Aufgaben:**
- [x] Variablen erstellen
- [x] Zahlen addieren
- [x] Ergebnis ausgeben
- [x] Subtraktion implementieren
- [x] User-Input einbauen (`input()`)

**Zu lernen:**
- `input()` - User-Eingabe
- `int()` - String zu Integer
- `float()` - String zu Float
- `+` und `-` Operatoren

**Erfolgskriterium:** ✅ Addition & Subtraktion mit User-Input funktioniert

---

#### Tag 3: Mehr Operationen (Mittwoch) ✖️➗
**Lernziel:** Multiplikation, Division, Potenz

**Aufgaben:**
- [x] Multiplikation (`*`)
- [x] Division (`/`)
- [x] Ganzzahlige Division (`//`)
- [x] Modulo (`%`)
- [x] Potenz (`**`)

**Erfolgskriterium:** ✅ Alle Grundrechenarten funktionieren

---

#### Tag 4: Error-Handling (Donnerstag) 🛡️
**Lernziel:** Fehler abfangen

**Aufgaben:**
- [x] Try-Except Block verstehen
- [x] Division durch 0 abfangen
- [x] Ungültige Eingaben behandeln
- [x] Hilfreiche Fehlermeldungen

**Zu lernen:**
```python
try:
    # Code der fehlschlagen könnte
except ZeroDivisionError:
    # Was tun bei Division durch 0
except ValueError:
    # Was tun bei ungültiger Eingabe
```

**Erfolgskriterium:** ✅ Programm stürzt nicht ab bei Fehleingaben

---

#### Tag 5: Menü-System (Freitag) 📋
**Lernziel:** Programmablauf steuern

**Aufgaben:**
- [x] While-Schleife für Hauptprogramm
- [x] Menü anzeigen mit print()
- [x] User-Auswahl mit match/case
- [x] Exit-Option einbauen

**Zu lernen:**
- `while True:` - Endlosschleife
- `break` - Schleife verlassen
- `match/case` - Pattern Matching (Python 3.10+)

**Erfolgskriterium:** ✅ Menü zeigt Optionen, User kann wählen

---

#### Tag 6-7: Code-Struktur & Testing (Wochenende) 🗂️
**Lernziel:** Code organisieren & testen

**Aufgaben:**
- [x] Code aufräumen
- [x] Funktionen für alle Operationen
- [x] Konstanten definieren
- [x] Alle Features testen
- [x] Ersten Meilenstein feiern!

**Erfolgskriterium:** ✅ Taschenrechner v1.0 fertig!

---

### 📖 Woche 2: Funktionen & Features

#### Tag 8-9: Funktionen (Montag-Dienstag) 🔧
**Lernziel:** Code in Funktionen auslagern

**Aufgaben:**
- [x] Erste Funktion schreiben
- [x] Parameter & Return verstehen
- [x] Jede Operation als Funktion
- [x] Hauptprogramm vereinfachen

**Zu lernen:**
```python
def add(a, b):
    """Addiert zwei Zahlen"""
    return a + b

result = add(5, 3)
```

**Erfolgskriterium:** ✅ Alle Operationen sind Funktionen

---

### 📖 Woche 3: Finalisierung

**Aufgaben:**
- [x] 9 verschiedene Operationen implementiert
- [x] Professionelle Formatierung mit Konstanten
- [x] Error-Handling überall
- [x] Match/Case für Menü-Logik
- [x] Docstrings für alle Funktionen

**Endergebnis:** ✅ [Taschenrechner mit 9 Operationen](../phase-1/t4_taschenrechner_optimiert.py)

---

## 🎓 PHASE 1.5: OOP-GRUNDLAGEN ✅

**Status:** ✅ Abgeschlossen  
**Zeitraum:** November 2025  
**Projekt:** [david_vaupel_assignment2.py](../phase-1.5/david_vaupel_assignment2.py)

### 🎯 Lernziele
- ✅ Klassen & Objekte verstehen
- ✅ `__init__` Konstruktor
- ✅ Instanz- vs. Klassenattribute
- ✅ Methoden definieren
- ✅ OOP-Design Patterns (Basics)

### 📖 Assignment 2: Quiz-System mit OOP

**Implementiert:**
- ✅ `Frage` Klasse mit Attributen und Methoden
- ✅ 10 Linux Essentials Quiz-Fragen
- ✅ Kategorisierung nach Themengebieten
- ✅ Input-Validierung und Fehlerbehandlung
- ✅ Score-Tracking und Statistiken
- ✅ Professionelle Formatierung

**Key Learnings:**
- Klassen als Blaupausen für Objekte
- Klassenattribute vs. Instanzattribute
- Methoden für Objektverhalten
- Docstrings für Dokumentation
- `self` Parameter verstehen

---

## 📅 PHASE 2: QUIZ-ENGINE (Wochen 4-5) 🔄

**Status:** 🔄 In Arbeit  
**Basis:** [david_vaupel_assignment2.py](../phase-1.5/david_vaupel_assignment2.py)

### 🎯 Lernziele
- Dictionaries vertiefen
- Nested Data Structures
- Zufallszahlen (random)
- JSON Import/Export
- Komplexere Programmlogik

---

### 📖 Woche 4: Quiz-Grundlagen

#### Tag 22-23: Datenstruktur (Montag-Dienstag) 🗂️
**Lernziel:** Fragen als Dictionaries

**Aufgaben:**
- [ ] Bestehenden Code analysieren
- [ ] Fragen-Dictionary-Struktur verstehen
- [ ] Mehr Fragen hinzufügen (20+ insgesamt)
- [ ] Kategorien erweitern

**Struktur (bereits vorhanden):**
```python
questions = [
    {
        "question": "Was ist Python?",
        "options": ["Sprache", "Schlange", "Tool", "OS"],
        "correct": 0,
        "category": "Grundlagen"
    }
]
```

**Erfolgskriterium:** ✅ 20+ Fragen in verschiedenen Kategorien

---

#### Tag 24-25: Quiz-Logik (Mittwoch-Donnerstag) 🎲
**Lernziel:** Fragen stellen & prüfen

**Status:** ✅ Bereits implementiert in Assignment 2

**Vorhandene Features:**
- ✅ Frage anzeigen
- ✅ Antwort einlesen
- ✅ Korrektheit prüfen
- ✅ Score verwalten

**Neue Aufgaben:**
- [ ] Code refactoren für bessere Struktur
- [ ] Quiz-Modi vorbereiten (Lernen vs. Prüfung)

---

#### Tag 26-27: Zufällige Fragen (Freitag-Samstag) 🔀
**Lernziel:** Random-Modul

**Aufgaben:**
- [ ] `random` Modul importieren
- [ ] `random.shuffle()` implementieren
- [ ] Zufällige Fragenauswahl
- [ ] Kategorie-Filter implementieren
- [ ] Quiz-Modi unterscheiden:
  - **Lernmodus:** Alle Fragen, sofortiges Feedback
  - **Prüfungsmodus:** Zufällige Auswahl, Feedback am Ende

**Zu lernen:**
```python
import random

# Fragen mischen
random.shuffle(fragen_liste)

# Zufällige Auswahl
ausgewaehlte = random.sample(fragen_liste, 10)

# Filter nach Kategorie
linux_fragen = [f for f in fragen if f.kategorie == "Linux"]
```

**Erfolgskriterium:** ✅ Jedes Quiz hat andere Reihenfolge

---

#### Tag 28: Testing & Refactoring (Sonntag) 🔧

**Aufgaben:**
- [ ] Alle neuen Features testen
- [ ] Code aufräumen
- [ ] Docstrings aktualisieren
- [ ] Edge-Cases behandeln

**Erfolgskriterium:** ✅ Quiz-Engine v1.0 fertig!

---

### 📖 Woche 5: Features & Export

#### Tag 29-30: Timer & Statistiken (Montag-Dienstag) ⏱️
**Lernziel:** Zeit messen

**Aufgaben:**
- [ ] `time` Modul verwenden
- [ ] Startzeit erfassen
- [ ] Zeit pro Frage messen
- [ ] Gesamtzeit berechnen
- [ ] Statistiken erweitern:
  - Durchschnittliche Zeit pro Frage
  - Schnellste/Langsamste Antwort
  - Zeit-basierte Bestenliste

**Zu lernen:**
```python
import time

start_zeit = time.time()
# Quiz durchführen
ende_zeit = time.time()
dauer = ende_zeit - start_zeit
```

**Erfolgskriterium:** ✅ Timer funktioniert

---

#### Tag 31-32: JSON-Export (Mittwoch-Donnerstag) 💾
**Lernziel:** JSON Files

**Aufgaben:**
- [ ] JSON-Modul importieren
- [ ] Ergebnisse als JSON speichern
- [ ] Quiz-Historie laden
- [ ] Highscores verwalten
- [ ] Fortschritt speichern/laden

**Zu lernen:**
```python
import json

# Speichern
with open('ergebnisse.json', 'w') as f:
    json.dump(daten, f, indent=4)

# Laden
with open('ergebnisse.json', 'r') as f:
    daten = json.load(f)
```

**JSON-Struktur:**
```json
{
    "quiz_historie": [
        {
            "datum": "2025-11-16",
            "score": 8,
            "total": 10,
            "prozent": 80,
            "dauer": 245.5,
            "modus": "pruefung"
        }
    ],
    "highscore": {
        "beste_punktzahl": 10,
        "schnellste_zeit": 180.2,
        "durchschnitt": 7.5
    }
}
```

**Erfolgskriterium:** ✅ Ergebnisse persistent gespeichert

---

#### Tag 33-34: Polish & Features (Freitag-Samstag) ✨

**Aufgaben:**
- [ ] Code-Review durchführen
- [ ] Alle Docstrings vervollständigen
- [ ] README.md für Quiz-Engine schreiben
- [ ] Beispiel-Fragen erweitern
- [ ] User-Experience verbessern

**Optional:**
- [ ] Farben für Terminal (colorama)
- [ ] Fortschrittsbalken
- [ ] Bessere Formatierung

---

#### Tag 35: Finalisierung (Sonntag) 🎉

**Aufgaben:**
- [ ] Kompletter Test aller Features
- [ ] GitHub Repository updaten
- [ ] Dokumentation finalisieren
- [ ] Erfolg feiern!

**Erfolgskriterium:** ✅ Quiz-Engine v2.0 komplett!

---

## 📅 PHASE 3: QUIZ-MERGER (Wochen 6-9) ⏳

**Status:** ⏳ Geplant

### 🎯 Lernziele
- HTML-Parsing (BeautifulSoup)
- Regular Expressions
- File Operations (Read/Write)
- Daten-Transformation
- Komplexe Logik
- Error-Handling Advanced

---

### 📖 Woche 6: HTML-Parsing Basics

#### Tag 36-38: BeautifulSoup lernen (Montag-Mittwoch) 🍜
**Lernziel:** HTML parsen

**Aufgaben:**
- [ ] BeautifulSoup installieren (`pip install beautifulsoup4`)
- [ ] HTML-Datei einlesen
- [ ] Tags finden
- [ ] Text extrahieren
- [ ] Erste Fragen aus HTML extrahieren

**Erfolgskriterium:** ✅ Kann erste HTML-Datei parsen

---

#### Tag 39-41: Fragen extrahieren (Donnerstag-Samstag) 🔍
**Lernziel:** Daten extrahieren

**Aufgaben:**
- [ ] Fragen-Pattern erkennen
- [ ] Optionen extrahieren
- [ ] Richtige Antwort finden
- [ ] In Dictionary speichern

**Erfolgskriterium:** ✅ Erste Datei komplett extrahiert

---

#### Tag 42: Review (Sonntag) 📝
**Erfolgskriterium:** ✅ Eine HTML-Datei zu Python-Dictionary

---

### 📖 Woche 7: Multi-File Processing

#### Tag 43-45: Alle drei Dateien (Montag-Mittwoch) 📚
**Aufgaben:**
- [ ] `Modul1_Prüfung.html` parsen
- [ ] `linux.html` parsen
- [ ] `linux-essentials-short.html` parsen

**Erfolgskriterium:** ✅ Alle drei Dateien erfolgreich geparst

---

#### Tag 46-48: Daten vereinheitlichen (Donnerstag-Samstag) 🔄
**Aufgaben:**
- [ ] Gemeinsame Struktur definieren
- [ ] Unterschiede handhaben
- [ ] Duplikate erkennen
- [ ] Kategorien zuordnen

**Erfolgskriterium:** ✅ Einheitliche Datenstruktur

---

#### Tag 49: Testing (Sonntag) 🧪
**Erfolgskriterium:** ✅ Daten konsistent

---

### 📖 Woche 8: Merge & Export

#### Tag 50-52: Daten zusammenführen (Montag-Mittwoch) 🔗
**Aufgaben:**
- [ ] Alle Fragen kombinieren
- [ ] Duplikate entfernen
- [ ] Nach Kategorien sortieren
- [ ] Metadaten hinzufügen

**Erfolgskriterium:** ✅ Merged Dataset erstellt

---

#### Tag 53-55: Export-Funktionen (Donnerstag-Samstag) 💾
**Aufgaben:**
- [ ] JSON-Export
- [ ] CSV-Export (optional)
- [ ] HTML-Output generieren
- [ ] Statistiken erstellen

**Erfolgskriterium:** ✅ Mehrere Export-Formate

---

#### Tag 56: Testing (Sonntag) ✅
**Erfolgskriterium:** ✅ Export funktioniert fehlerfrei

---

### 📖 Woche 9: Polish & Features

#### Tag 57-59: Error-Handling & Edge-Cases (Montag-Mittwoch) 🛡️
**Aufgaben:**
- [ ] Alle Fehlerquellen identifizieren
- [ ] Try-Except erweitern
- [ ] Logging implementieren
- [ ] Recovery-Mechanismen

**Erfolgskriterium:** ✅ Robuster Code

---

#### Tag 60-62: CLI-Interface (Donnerstag-Samstag) 💻
**Aufgaben:**
- [ ] `argparse` Modul lernen
- [ ] Command-Line Interface
- [ ] Optionen & Flags
- [ ] Help-Text

**Erfolgskriterium:** ✅ CLI funktioniert

---

#### Tag 63: Finalisierung & Dokumentation (Sonntag) 📚
**Aufgaben:**
- [ ] Code dokumentieren
- [ ] README schreiben
- [ ] Usage-Examples
- [ ] Erfolg feiern! 🎉

**Erfolgskriterium:** ✅ Quiz-Merger v1.0 KOMPLETT! 🏆

---

## 🎁 BONUS: HOMELAB-INTEGRATION (Ongoing)

**Repository:** [homelab-automation](https://github.com/MCCMDave/homelab-automation)

### Python-Scripts für Raspberry Pi

**Abgeschlossene Projekte:**
- ✅ [Service Monitor](https://github.com/MCCMDave/homelab-automation/tree/main/service-monitor) - CPU/RAM/Uptime Monitoring
- ✅ [Power Savings Tracker](https://github.com/MCCMDave/homelab-automation/tree/main/power-savings-tracker) - Solar-Einsparungen tracken

**Mögliche weitere Projekte:**
- [ ] Nextcloud Backup-Monitor (Python)
- [ ] System-Status Dashboard
- [ ] Automated Photo-Sorting (erweitert)
- [ ] Pi-hole Statistiken visualisieren
- [ ] Log-File Analyzer
- [ ] Disk-Space Monitor mit Alerts

**Erfolgskriterium:** ✅ Mindestens ein nützliches Tool im Einsatz

---

## 📊 TRACKING & REVIEW

### Weekly Check-in:
- [ ] Was habe ich gelernt?
- [ ] Was lief gut?
- [ ] Was war schwierig?
- [ ] Nächste Woche: Was steht an?

### Nach jeder Phase:
- [ ] Code reviewen
- [ ] Dokumentation updaten
- [ ] Skills-Liste aktualisieren
- [ ] Nächste Phase planen

---

## 🎯 LEARNING METRICS

**Phase 1 Success Criteria:**
- ✅ Kann eigenständig einfache Python-Programme schreiben
- ✅ Versteht Funktionen, Schleifen, Bedingungen
- ✅ Kann mit Fehlern umgehen
- ✅ Kann Dateien lesen/schreiben

**Phase 1.5 Success Criteria:**
- ✅ Versteht Klassen und Objekte
- ✅ Kann eigene Klassen erstellen
- ✅ Versteht Instanz- vs. Klassenattribute
- ✅ Kann Methoden definieren und nutzen

**Phase 2 Success Criteria:**
- [ ] Kann komplexe Datenstrukturen nutzen
- [ ] Versteht random-Modul
- [ ] Kann JSON verarbeiten
- [ ] Kann interaktive Programme mit Modi schreiben
- [ ] Kann Zeit messen und Statistiken erstellen

**Phase 3 Success Criteria:**
- [ ] Kann externe Bibliotheken nutzen
- [ ] Kann HTML/XML parsen
- [ ] Kann Daten transformieren
- [ ] Kann CLI-Tools schreiben
- [ ] Kann komplexe Projekte strukturieren

---

## 💡 TIPPS FÜR DEN ERFOLG

**Daily Habits:**
- 🕐 30-60 Min täglich programmieren
- 📝 Code von gestern reviewen
- 💭 Über Probleme nachdenken
- 🎯 Kleine Ziele setzen

**Weekly Habits:**
- 🗓️ Sonntags: Woche planen
- 📚 Neues Konzept lernen
- 🔄 Code refactoren
- 🎉 Erfolge feiern

**Don't:**
- ❌ Mehrere Tage aussetzen
- ❌ Zu viel auf einmal versuchen
- ❌ Fehler zu persönlich nehmen
- ❌ Mit anderen vergleichen

**Do:**
- ✅ Jeden Tag etwas machen
- ✅ In kleinen Schritten denken
- ✅ Aus Fehlern lernen
- ✅ Eigenen Fortschritt sehen

---

## 🔗 WICHTIGE LINKS

**Projekt-Dokumentation:**
- [PYTHON-GUIDELINES.md](PYTHON-GUIDELINES.md) - Python Best Practices
- [CODING-GUIDELINES.md](CODING-GUIDELINES.md) - Allgemeine Coding Standards

**GitHub Repositories:**
- [python-learning](https://github.com/MCCMDave/python-learning) - Dieses Repository
- [homelab-automation](https://github.com/MCCMDave/homelab-automation) - Production Tools
- [windows-automation](https://github.com/MCCMDave/windows-automation) - PowerShell Scripts

**Projekt-Dateien:**
- Phase 1: `phase-1/` Ordner
- Phase 1.5: `phase-1.5/` Ordner
- Phase 2: `phase-2/` Ordner (in Arbeit)

---

## 🚀 NEXT STEPS

**Aktuell (November 2025):**
1. ✅ Phase 1 & 1.5 abgeschlossen
2. 🔄 Phase 2 starten
3. Assignment 2 als Basis nutzen
4. Random-Modul implementieren
5. JSON Export hinzufügen

**Diese Woche:**
- Tag 22-23: Mehr Fragen hinzufügen
- Tag 24-25: Quiz-Modi implementieren
- Tag 26-27: Random-Funktionen einbauen

---

**Let's continue this journey! 🚀**

**Erstellt:** November 2025  
**Für:** Dave's Python-Lernreise  
**Status:** Phase 2 in Arbeit 💪

**[⬆ Zurück nach oben](#-python-learning-roadmap)**
