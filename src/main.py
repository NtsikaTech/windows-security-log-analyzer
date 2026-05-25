from log_reader import get_security_logs
from analyzer import extract_events, detect_suspicious_activity


def main():
    logs = get_security_logs()

    successful_logins = extract_events(logs, 4624)
    logoffs = extract_events(logs, 4634)
    admin_sessions = extract_events(logs, 4672)
    explicit_creds = extract_events(logs, 4648)
    credential_access = extract_events(logs, 5379)

    print("\n===== WINDOWS SECURITY MONITOR =====\n")

    print(f"Successful Logins: {len(successful_logins)}")
    print(f"Logoffs: {len(logoffs)}")
    print(f"Admin Sessions: {len(admin_sessions)}")
    print(f"Explicit Credential Use: {len(explicit_creds)}")
    print(f"Credential Manager Access: {len(credential_access)}")

    print("\n===== SECURITY ALERTS =====\n")

    alerts = detect_suspicious_activity(logs)

    if not alerts:
        print("No suspicious activity detected (baseline normal behaviour)")
    else:
        for alert in alerts:
            print(f"[!] {alert}")


if __name__ == "__main__":
    main()