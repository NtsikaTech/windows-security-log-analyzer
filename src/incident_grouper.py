from collections import defaultdict
from datetime import datetime


def group_incidents(alerts):
    """
    Converts multiple alerts into structured SOC incidents.
    This simulates SIEM correlation logic.
    """

    incident_map = defaultdict(list)

    # ---------------------------
    # CLASSIFY ALERTS INTO GROUPS
    # ---------------------------
    for alert in alerts:
        alert_lower = alert.lower()

        if "failed login" in alert_lower or "invalid password" in alert_lower:
            incident_map["Brute Force Attempt"].append(alert)

        elif "credential" in alert_lower:
            incident_map["Credential Access Abuse"].append(alert)

        elif "privilege" in alert_lower:
            incident_map["Privilege Escalation"].append(alert)

        elif "logon" in alert_lower or "login success" in alert_lower:
            incident_map["Authentication Activity"].append(alert)

        else:
            incident_map["General Suspicious Activity"].append(alert)

    # ---------------------------
    # BUILD INCIDENT OBJECTS
    # ---------------------------
    incidents = []

    for incident_type, related_alerts in incident_map.items():

        # Severity logic (simple SOC triage)
        if incident_type == "Privilege Escalation":
            severity = "CRITICAL"
        elif incident_type == "Brute Force Attempt":
            severity = "HIGH" if len(related_alerts) > 3 else "MEDIUM"
        elif incident_type == "Credential Access Abuse":
            severity = "MEDIUM"
        else:
            severity = "LOW"

        incidents.append({
            "incident_type": incident_type,
            "severity": severity,
            "event_count": len(related_alerts),
            "alerts": related_alerts,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return incidents