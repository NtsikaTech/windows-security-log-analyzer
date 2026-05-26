def map_to_mitre(incident_type):
    """
    Maps incident types to MITRE ATT&CK techniques.
    """

    mappings = {
        "Brute Force Attempt": {
            "technique_id": "T1110",
            "technique_name": "Brute Force",
            "tactic": "Credential Access"
        },

        "Credential Access Abuse": {
            "technique_id": "T1555",
            "technique_name": "Credentials from Password Stores",
            "tactic": "Credential Access"
        },

        "Privilege Escalation": {
            "technique_id": "T1068",
            "technique_name": "Exploitation for Privilege Escalation",
            "tactic": "Privilege Escalation"
        },

        "Authentication Activity": {
            "technique_id": "T1078",
            "technique_name": "Valid Accounts",
            "tactic": "Defense Evasion"
        }
    }

    return mappings.get(
        incident_type,
        {
            "technique_id": "UNKNOWN",
            "technique_name": "Unknown Technique",
            "tactic": "Unknown"
        }
    )