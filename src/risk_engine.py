def calculate_risk_score(logs):
    score = 0

    events = logs.split("Event[")

    # Counters (not raw addition)
    admin_count = 0
    credential_count = 0
    login_count = 0

    for event in events:

        if "Event ID: 4672" in event:
            admin_count += 1

        if "Event ID: 4648" in event:
            credential_count += 1

        if "Event ID: 4624" in event:
            login_count += 1

    # NORMALISATION (this is the fix)

    if admin_count > 10:
        score += 40
    elif admin_count > 5:
        score += 20
    else:
        score += 5

    if credential_count > 10:
        score += 30
    elif credential_count > 5:
        score += 15
    else:
        score += 5

    if login_count > 50:
        score += 20
    else:
        score += 5

    # FINAL CAP (important)
    return min(score, 100)