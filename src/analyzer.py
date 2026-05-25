def extract_events(log_data, event_id):
    events = log_data.split("Event[")
    matched = []

    for event in events:
        if f"Event ID: {event_id}" in event:
            matched.append(event)

    return matched


def detect_suspicious_activity(log_data):
    alerts = []

    admin_logins = extract_events(log_data, 4672)
    explicit_creds = extract_events(log_data, 4648)
    credential_access = extract_events(log_data, 5379)
    logins = extract_events(log_data, 4624)

    # Normalize behaviour instead of raw counts
    admin_ratio = len(admin_logins) / max(len(logins), 1)
    credential_ratio = len(credential_access) / max(len(logins), 1)

    if admin_ratio > 1.5:
        alerts.append("Unusual privilege escalation pattern detected")

    if credential_ratio > 5:
        alerts.append("Abnormally high credential manager activity")

    if len(explicit_creds) > 5:
        alerts.append("Multiple explicit credential authentications detected")

    if len(logins) > 50:
        alerts.append("High authentication volume detected (possible automation or service activity)")

    return alerts