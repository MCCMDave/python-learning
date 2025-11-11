"""
Test-Script für Homelab Service Monitor
Manuelles Testen der einzelnen Funktionen

Autor: Dave
Datum: 07.11.2025
"""

from practical_automation.homelab_service_monitor import (
    services,
    service_check,
    alarm_generator,
    alarm_historie,
    durchschnitt,
    kopf,
    alarm,
    durch,
    ende
)

def test_service_checks():
    """Testet die service_check Funktion mit allen Services."""
       
    # Nextcloud testen
    status = service_check("Nextcloud", services["Nextcloud"])
    print("="*2 + f"Nextcloud: {status}".center(54) + "="*2)
    
    # Tailscale testen (sollte WARNUNG sein wegen CPU > 80)
    status = service_check("Tailscale", services["Tailscale"])
    print("="*2 + f"Tailscale: {status}".center(54) + "="*2)
    
    # Pi-hole testen
    status = service_check("Pi-hole", services["Pi-hole"])
    print("="*2 + f"Pi-hole: {status}".center(54) + "="*2)
    print("="*2 + "".center(54) + "="*2)

def test_alarm_generator():
    """Testet ob Alarme korrekt erstellt werden."""
    alarm()
    
    # Alarm erstellen
    alarm_generator("Tailscale", "CPU-Auslastung (85%)")
    
    # Prüfen ob Alarm in Historie ist
    print("="*2 + f"Alarme in Historie: {len(alarm_historie)}".center(54) + "="*2)
    
    # Ersten Alarm schön formatiert ausgeben (nicht das ganze Dictionary!)
    if len(alarm_historie) > 0:
        erster = alarm_historie[0]
        print("="*2 + f"Service: {erster['Service']}".center(54) + "="*2)
        print("="*2 + f"Grund: {erster['Grund']}".center(54) + "="*2)
        print("="*2 + f"Datum: {erster['Datum']}".center(54) + "="*2)
    
    print("="*2 + "".center(54) + "="*2)

def test_durchschnitt():
    """Testet die Durchschnittsberechnung."""
    durch()
    
    # Durchschnitt berechnen
    durch_cpu, durch_ram = durchschnitt()
    
    print("="*2 + f"Durchschnitt CPU: {durch_cpu:.1f}%".center(54) + "="*2)
    print("="*2 + f"Durchschnitt RAM: {durch_ram:.0f}MB".center(54) + "="*2)
    print("="*2 + "".center(54) + "="*2)
    print("="*58)

# Hauptprogramm - alle Tests durchlaufen
if __name__ == "__main__":
    kopf()

    # Einzelne Tests aufrufen
    test_service_checks()
        
    test_alarm_generator()
     
    test_durchschnitt()
    
    ende()