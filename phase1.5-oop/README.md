# Phase 1.5: OOP Fundamentals

**[🇩🇪 Deutsche Version](README_DE.md)** | 🇬🇧 English Version

---

**Duration:** 2 weeks  
**Focus:** Object-Oriented Programming  
**Status:** ✅ Completed

---

## 📖 Overview

This phase introduced object-oriented programming (OOP) through two practical assignments that solve real-world problems.

---

## 🎯 Assignments

### Assignment 1: Homelab Service Monitor

**File:** `assignment1_homelab_monitor.py`

A monitoring system for Raspberry Pi services with alarm functionality.

**Features:**
- Monitors CPU, RAM, and uptime of services
- Generates alarms for critical values
- Calculates average resource usage
- Formatted console output with borders

**OOP Concepts Used:**
- Dictionaries for service data
- Functions for modularization
- Lists for alarm history

**Monitored Services:**
- Nextcloud (Cloud Storage)
- Pi-hole (DNS Ad-Blocker)
- Tailscale (VPN)

**[Production Version →](https://github.com/MCCMDave/homelab-automation/tree/main/service-monitor)**

---

### Assignment 2: Quiz System for Linux Essentials

**File:** `assignment2_quiz_system.py`

An interactive quiz system for exam preparation with OOP.

**Features:**
- 10 Linux Essentials questions
- Multiple-choice format (A-D)
- Instant feedback
- Score system with percentage display
- Input validation

**OOP Concepts:**
- ✅ Question class with 4 instance attributes
- ✅ Class attribute `anzahl_fragen`
- ✅ 3 instance methods (zeige_frage, checke_antwort, zeige_antwort)
- ✅ Constructor with error handling
- ✅ 10 Question objects created

**Categories:**
- Linux Evolution & Distributions
- Open Source Software
- Command Line & Shell
- Filesystem & Directories
- System Administration

**Extended in:** [Phase 2 - Quiz Engine](../phase2-quiz-engine/)

---

## 💡 What I Learned

### OOP Fundamentals:
- **Classes** as blueprints for objects
- **Objects** as instances of a class
- **self parameter** for accessing instance attributes
- **Constructor** (`__init__`) for initialization
- **Class attributes** vs. **instance attributes**

### Best Practices:
- Error handling in constructor
- Docstrings for classes and methods
- Input validation with while loops
- Code organization into separate functions
- Formatting for better readability

### Practical Application:
- How OOP solves real problems
- When classes make sense
- How to create and use objects

---

## 🛠️ Tech Stack

- Python 3.13
- Object-Oriented Programming
- Standard Library (datetime, os)
- Error Handling (ValueError)

---

## 🚀 Execution

### Assignment 1:
```bash
python assignment1_homelab_monitor.py
```

### Assignment 2:
```bash
python assignment2_quiz_system.py
```

---

## 📊 Success Criteria

- [x] Both assignments successfully completed
- [x] OOP concepts understood and applied
- [x] Code cleanly structured and documented
- [x] Functional programs without bugs
- [x] Practical applications created

---

## ➡️ Next Phase

**Phase 2: Quiz Engine** with extended features:
- Random question selection
- Category filter
- JSON import/export
- Timer system
- Highscores

---

**Time Investment:** ~2 weeks  
**Completed:** November 2025  
**Next Step:** Phase 2 - Quiz Engine 🚀
