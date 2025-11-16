# Phase 1.5: OOP-Grundlagen

**Dauer:** 2 Wochen  
**Fokus:** Objektorientierte Programmierung  
**Status:** ✅ Abgeschlossen

---

## 📖 Übersicht

Diese Phase diente der Einführung in objektorientierte Programmierung (OOP) mit zwei praktischen Assignments.

---

## 🎯 Assignments

### Assignment 1: Homelab Service Monitor

**Datei:** `assignment1_homelab_monitor.py`

Ein Monitoring-System für Raspberry Pi Services mit Alarm-Funktion.

**Features:**
- Überwacht CPU, RAM und Laufzeit von Services
- Generiert Alarme bei kritischen Werten
- Berechnet Durchschnitts-Auslastung
- Formatierte Konsolen-Ausgabe mit Rahmen

**Genutzte OOP-Konzepte:**
- Dictionaries für Service-Daten
- Funktionen zur Modularisierung
- Listen für Alarm-Historie

**Services im Monitor:**
- Nextcloud (Cloud-Storage)
- Pi-hole (DNS Ad-Blocker)
- Tailscale (VPN)

**[Produktive Version →](https://github.com/MCCMDave/homelab-automation/tree/main/service-monitor)**

---

### Assignment 2: Quiz-System für Linux Essentials

**Datei:** `assignment2_quiz_system.py`

Ein interaktives Quiz-System zur Prüfungsvorbereitung mit OOP.

**Features:**
- 10 Linux Essentials Fragen
- Multiple-Choice Format (A-D)
- Sofortiges Feedback
- Score-System mit Prozentanzeige
- Input-Validierung

**OOP-Konzepte:**
- ✅ Klasse `Frage` mit 4 Instanzattributen
- ✅ Klassenattribut `anzahl_fragen`
- ✅ 3 Instanzmethoden (zeige_frage, checke_antwort, zeige_antwort)
- ✅ Konstruktor mit Fehlerbehandlung
- ✅ 10 Frage-Objekte erstellt

**Kategorien:**
- Linux Evolution & Distributionen
- Open Source Software
- Kommandozeile & Shell
- Dateisystem & Verzeichnisse
- System-Administration

**Erweitert in:** [Phase 2 - Quiz-Engine](../phase2-quiz-engine/)

---

## 💡 Was ich gelernt habe

### OOP-Grundlagen:
- **Klassen** als Baupläne für Objekte
- **Objekte** als Instanzen einer Klasse
- **self-Parameter** für Zugriff auf Instanzattribute
- **Konstruktor** (`__init__`) zur Initialisierung
- **Klassenattribute** vs. **Instanzattribute**

### Best Practices:
- Fehlerbehandlung im Konstruktor
- Docstrings für Klassen und Methoden
- Input-Validierung mit While-Schleifen
- Code-Organisation in separate Funktionen
- Formatierung für bessere Lesbarkeit

### Praktische Anwendung:
- Wie OOP reale Probleme löst
- Wann Klassen sinnvoll sind
- Wie man Objekte erstellt und nutzt

---

## 🛠️ Tech Stack

- Python 3.13
- Objektorientierte Programmierung
- Standard Library (datetime, os)
- Error Handling (ValueError)

---

## 🚀 Ausführung

### Assignment 1:
```bash
python assignment1_homelab_monitor.py
```

### Assignment 2:
```bash
python assignment2_quiz_system.py
```

---

## 📊 Erfolgs-Kriterien

- [x] Beide Assignments erfolgreich abgeschlossen
- [x] OOP-Konzepte verstanden und angewendet
- [x] Code sauber strukturiert und dokumentiert
- [x] Funktionsfähige Programme ohne Bugs
- [x] Praktische Anwendungen erstellt

---

## ➡️ Nächste Phase

**Phase 2: Quiz-Engine** mit erweiterten Features:
- Zufällige Fragenauswahl
- Kategorie-Filter
- JSON Import/Export
- Timer-System
- Highscores

---

**Zeitaufwand:** ~2 Wochen  
**Abgeschlossen:** November 2025  
**Nächster Schritt:** Phase 2 - Quiz-Engine 🚀
