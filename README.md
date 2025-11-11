# Python Learning Repository

My Python learning projects and practical automation scripts for homelab & everyday use.

**Author:** David Vaupel  
**Status:** 🟢 Active Development  
**Python Version:** 3.13+

---

## 📦 Project Structure

```
python-learning/
├── practical_automation/          # Homelab automation
│   ├── __init__.py
│   ├── homelab_service_monitor.py # Service monitoring for Raspberry Pi
│   └── power_savings_tracker.py   # Power cost tracking
├── calculator_evolution/          # Calculator project (learning)
│   └── __init__.py
├── testing/                       # Tests for all modules
│   ├── __init__.py
│   └── test.py
├── setup.py                       # Package setup
└── README.md
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.13 or higher
- pip (Python Package Manager)

### Installation

```bash
# Clone repository
git clone https://github.com/MCCMDave/python-learning.git
cd python-learning

# Install package in development mode (recommended)
pip install -e .
```

**What does `pip install -e .` do?**
- Installs the package as an editable/development package
- Changes to code take effect immediately (no reinstallation needed)
- Package can be imported from anywhere on the system

---

## 💻 Usage

### Importing Modules

After installation with `pip install -e .`, you can import modules from anywhere:

```python
# Homelab Service Monitor
from practical_automation.homelab_service_monitor import (
    services,
    service_check,
    alarm_generator
)

# Power Savings Tracker
from practical_automation.power_savings_tracker import track_savings

# Example usage
status = service_check("nextcloud")
print(f"Nextcloud Status: {status}")
```

### Running Tests

```bash
# From main directory
python testing/test.py

# Or using Python module
python -m testing.test
```

---

## 📚 Modules & Features

### 🏠 practical_automation

#### homelab_service_monitor.py
**Purpose:** Monitor critical services on Raspberry Pi 5 homelab

**Features:**
- Service status checks (Nextcloud, Pi-hole, Tailscale)
- Alarm generation on failures
- History tracking
- Docker container monitoring

**Services:**
```python
services = {
    "nextcloud": "http://192.168.2.54:8080",
    "pihole": "http://192.168.2.54/admin",
    "tailscale": "http://100.103.86.47:8080"
}
```

**Example:**
```python
from practical_automation.homelab_service_monitor import service_check

# Check Nextcloud
status = service_check("nextcloud")
if not status:
    print("⚠️ Nextcloud is down!")
```

#### power_savings_tracker.py
**Purpose:** Track power cost savings

**Features:**
- Calculate savings
- CSV export for analysis
- Before/after optimization comparison

---

### 🧮 calculator_evolution

**Purpose:** Learning project for Python fundamentals

Different evolution stages of a calculator:
- Simple calculations
- Error handling
- Advanced functions

---

## 🛠️ Tech Stack

- **Python 3.13** - Main language
- **Docker** - For service monitoring
- **setuptools** - Package management
- **pathlib** - Modern path handling

---

## 📖 Development

### Code Conventions

This project follows **PEP8** Python Style Guide:
- ✅ `snake_case` for files, functions, variables
- ✅ Package structure with `__init__.py`
- ✅ Type hints (planned)
- ✅ Docstrings for all functions

### Extending the Project

```bash
# 1. Make changes to code
# 2. No reinstallation needed (thanks to -e flag)
# 3. Simply run your new code
python your_script.py
```

---

## 🔗 Related Projects

- **[homelab-automation](https://github.com/MCCMDave/homelab-automation)** - Raspberry Pi 5 homelab setup
- **[windows-automation](https://github.com/MCCMDave/windows-automation)** - Universal Update Manager v2.1

---

## 🎯 Roadmap

- [ ] Unit tests with pytest
- [ ] Type hints for all functions
- [ ] CI/CD with GitHub Actions
- [ ] Docker container for service monitor
- [ ] Web dashboard for monitoring
- [ ] Integrate logging framework

---

## 👨‍💻 Author

**David Vaupel**
- 🔗 [LinkedIn](https://www.linkedin.com/in/david-vaupel)
- 💻 [GitHub](https://github.com/MCCMDave)
- 📧 221494616+MCCMDave@users.noreply.github.com

**Background:**
- IHK Training: Cloud IT Administrator (Module 2/4)
- 8.5 years Customer Service Experience (Amazon Prime Video, DKB Bank)
- Goal: Customer Success Engineer (CSE) Position

---

## 📄 License

Private Learning Repository - All Rights Reserved.

---

## 🙏 Acknowledgments

This project was created as part of my Cloud IT Administrator training and serves as a practical portfolio project for CSE applications.

**Special Thanks:**
- Claude (Anthropic) - For support with code reviews and best practices
- IHK Berlin - Training program
- Raspberry Pi Community - For homelab inspiration

---

**Last Updated:** November 2025  
**Version:** 1.0.0  
**Status:** 🟢 Production Ready