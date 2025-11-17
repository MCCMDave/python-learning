# 🎓 Phase 2: Quiz Engine

**🇬🇧 English Version** | **[🇩🇪 Deutsche Version](README_DE.md)**

---

An interactive quiz system for Linux Essentials 010-160 exam preparation with OOP, JSON data structure, and various learning modes.

---

## 🎯 Project Goal

Building upon [Phase 1.5 (Assignment 2)](../phase-1.5-oop/assignment2_quiz_system.py), the quiz engine was enhanced with:
- Separation of data (JSON) and logic (Python)
- Random question and answer ordering
- Multiple quiz modes (Learning, Exam, Custom)
- Timer for realistic exam conditions

---

## ✨ Features

### Version 1.0 (quiz_engine_v1.py)
- 277 questions embedded in code
- OOP with `Frage` class
- Professional formatting
- Foundation for V2 - shows code evolution

### Version 2.0 (quiz_engine_v2.py)
- ✅ **276 questions from JSON** - easily expandable
- ✅ **3 Quiz Modes:**
  - **Learning Mode:** All 276 questions
  - **Exam Mode:** 40 questions, 60 minutes timer
  - **Custom Mode:** Choose any number
- ✅ **Randomization:**
  - Questions in random order
  - Answers shuffled (A-D)
- ✅ **Statistics:**
  - Percentage evaluation
  - Correct vs. incorrect answers
  - Time display (Exam mode)
  - Pass/Fail indicator (≥60%)

---

## 📊 Question Database

**fragen.json** contains 276 exam questions from all official topics.

### Category Distribution

| Category | Count |
|----------|-------|
| 1.1 Linux Evolution | 28 |
| 4.3 Where Data is Stored | 27 |
| 4.4 Computer on Network | 26 |
| 3.2 Searching and Extracting | 24 |
| 2.1 Command Line Basics | 21 |
| 3.3 Shell Scripting | 19 |
| 4.2 Computer Hardware | 18 |
| 1.2 Open Source Applications | 16 |
| 4.1 Choosing an OS | 14 |
| *...and 10 more* | 83 |

### JSON Structure

```json
{
  "metadata": {
    "version": "1.0",
    "total_fragen": 276,
    "kategorien": {...},
    "beschreibung": "Linux Essentials 010-160 v1.6"
  },
  "fragen": [
    {
      "frage": "Who originally developed the Linux kernel?",
      "optionen": [
        "Richard Stallman",
        "Linus Torvalds",
        "Dennis Ritchie",
        "Ken Thompson"
      ],
      "richtige_antwort": 1,
      "kategorie": "1.1 Linux Evolution"
    }
  ]
}
```

---

## 🎮 Usage

### Start
```bash
python quiz_engine_v2.py
```

### Menu Options
```
==============================================================================================
==                                   CHOOSE QUIZ MODE                                       ==
==============================================================================================
==                                                                                          ==
==                          [1] Learning Mode - All Questions (276)                        ==
==                          [2] Exam Mode - 40 Questions, 60 Min                           ==
==                          [3] Custom - Choose Number                                     ==
==                          [0] Exit                                                       ==
==                                                                                          ==
==============================================================================================
```

### Mode Details

#### 🎓 Learning Mode
- All 276 questions
- No time limit
- Immediate feedback after each question
- Ideal for comprehensive learning

#### ⏱️ Exam Mode
- 40 random questions
- 60 minute time limit
- Timer runs in background
- Time warning at <5 minutes
- Pass/Fail display (≥60% = pass)
- Realistic like actual Linux Essentials exam

#### 🎛️ Custom Mode
- Choose any number (1-276)
- No time limit
- Ideal for targeted practice
- Flexible for different learning goals

---

## 🧠 Phase 2 Learning Goals

### Technical Skills
- ✅ JSON Import/Export
- ✅ `random` module (shuffle, sample)
- ✅ `time` module for timer
- ✅ `os` module for paths
- ✅ List slicing
- ✅ Enumerate with start index

### OOP Concepts
- ✅ Extending instance methods (`shuffle_optionen`)
- ✅ Improving class design
- ✅ Separating data from logic

### Best Practices
- ✅ Using external data sources
- ✅ User-friendly menus
- ✅ Input validation
- ✅ Error handling
- ✅ Relative paths (portable)

---

## 📁 Project Structure

```
phase-2/
├── quiz_engine_v1.py       # Version 1 (277 embedded questions)
├── quiz_engine_v2.py       # Version 2 (loads from JSON)
├── fragen.json             # Question database (276 questions)
├── README.md               # This file
└── README_DE.md            # German documentation
```

---

## 🔗 Related Projects

### Phase 1
- [Calculator](../phase-1/t4_taschenrechner_optimiert.py) - 9 operations with match/case
- [Assignment 1: Service Monitor](../phase-1/david_vaupel_assignment1.py) - Homelab monitoring

### Phase 1.5
- [Assignment 2: Quiz System](../phase-1.5/david_vaupel_assignment2.py) - OOP fundamentals, foundation for Phase 2

### Roadmap
- [Learning Roadmap](../docs/LEARNING-ROADMAP.md) - Complete learning plan (Phases 1-3)

---

## 🎓 Linux Essentials Certification

This quiz is based on the **Linux Essentials 010-160 v1.6** exam format:

### Exam Details
- **Duration:** 60 minutes
- **Questions:** 40 multiple-choice
- **Format:** 4 answer options (A-D)
- **Topics:** 5 main areas
- **Passing Score:** ~60% (24 of 40 correct)

### Topic Coverage

| Topic | Weight | Questions |
|-------|--------|-----------|
| 1. Linux Community & Open Source | 17.5% | 7 |
| 2. Finding Your Way | 22.5% | 9 |
| 3. The Power of the Command Line | 25% | 10 |
| 4. The Linux Operating System | 27.5% | 11 |
| 5. Security & File Permissions | 7.5% | 3 |

### Exam Preparation
- ✅ All official topics covered
- ✅ Realistic question format
- ✅ Exam timer simulates time pressure
- ✅ Percentage evaluation like real exam

---

## 📊 Development Statistics

### Code Evolution
- **V1:** 1885 lines (with embedded questions)
- **V2:** ~320 lines (without question data)
- **Reduction:** 83% leaner through JSON separation!

### Development Time
- **Phase 2:** ~1 week (November 2025)
- **Questions:** Expanded from 10 to 276
- **Features:** 3 modes, timer, custom selection

### Database
- **Questions:** 276 total
- **Categories:** 19 different
- **Duplicates:** 0 (verified)

---

## 💡 Lessons Learned

### What Works Well
- ✅ JSON separation makes code maintainable
- ✅ Random shuffle prevents memorization
- ✅ Custom mode provides flexibility
- ✅ Timer motivates and simulates exam pressure

### Challenges
- Shuffling answers + adjusting index (solved with `enumerate`)
- Timer in background without threading (solved with `time.time()`)
- Formatting 276 questions manually (solved: HTML parser!)
- Relative paths for portability (solved with `os.path`)

### Next Steps
- **Phase 3:** HTML parser for automatic import
- Implement category filters
- Save results to JSON (history)
- Highscore system

---

## 🛠️ Tech Stack

### Python 3.13
**Standard Library:**
- `json` - Data import/export
- `random` - Shuffling (shuffle, sample)
- `time` - Timer functionality
- `os` - Path handling (portable)

**No external dependencies!** ✅

---

## 🚀 Installation & Setup

### Requirements
- Python 3.10+ (for match/case in V1)
- Windows / Linux / macOS

### Setup
```bash
# Clone repository
git clone https://github.com/MCCMDave/python-learning.git
cd python-learning/phase-2

# Run
python quiz_engine_v2.py
```

### Files
Make sure these files are in the same folder:
- `quiz_engine_v2.py`
- `fragen.json`

---

## 📖 Code Examples

### Question Class
```python
class Frage:
    def __init__(self, fragetext, optionen, richtige_antwort, kategorie):
        self.frage = fragetext
        self.optionen = optionen
        self.richtige_antwort = richtige_antwort
        self.kategorie = kategorie
    
    def shuffle_optionen(self):
        """Shuffles answers and adjusts index."""
        # ...
```

### Loading JSON
```python
def lade_fragen():
    """Loads questions from JSON."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_pfad = os.path.join(script_dir, 'fragen.json')
    
    with open(json_pfad, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create Question objects
    fragen_liste = [Frage(...) for q in data['fragen']]
    random.shuffle(fragen_liste)
    return fragen_liste
```

---

## 📄 License

MIT License - Free to use for learning & exam preparation

---

## 👨‍💻 Author

**David Vaupel**  
Python Learner | Linux Essentials Certified (85%+)

- 📧 Contact via [GitHub Issues](https://github.com/MCCMDave/python-learning/issues)
- 💼 [LinkedIn](https://www.linkedin.com/in/david-vaupel)
- 🏠 [Homelab-Automation](https://github.com/MCCMDave/homelab-automation)
- 💻 [Windows-Automation](https://github.com/MCCMDave/windows-automation)

---

## 📝 Changelog

### v2.0 (November 2025)
- ✅ JSON database with 276 questions
- ✅ 3 quiz modes (Learning/Exam/Custom)
- ✅ Timer system for exam mode
- ✅ Answer shuffling
- ✅ Pass/Fail logic

### v1.0 (November 2025)
- ✅ Basic quiz with 277 embedded questions
- ✅ OOP with Question class
- ✅ First version from Assignment 2

---

**Status:** ✅ Phase 2 completed (v2.0)  
**Last Update:** November 2025

---

**[⬆ Back to top](#-phase-2-quiz-engine)**
