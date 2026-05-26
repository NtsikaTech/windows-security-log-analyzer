from src.log_reader import get_security_logs
from src.analyzer import detect_suspicious_activity
from src.risk_engine import calculate_risk_score
from src.incident_grouper import group_incidents
from src.report_exporter import export_soc_report
from src.ticket_system import create_ticket, get_all_tickets
from src.mitre_mapper import map_to_mitre

def run_soc_analysis():
    print("\n===== SOC ANALYST REPORT =====\n")

    logs = get_security_logs()

    alerts = detect_suspicious_activity(logs)
    risk_score = calculate_risk_score(logs)

    incidents = group_incidents(alerts)

    # Risk classification
    if risk_score < 30:
        status = "LOW RISK"
    elif risk_score < 70:
        status = "MEDIUM RISK"
    else:
        status = "HIGH RISK"

    print(f"Risk Score: {risk_score}")
    print(f"Status: {status}")

    print("\n===== INCIDENT GROUPS =====")

    tickets = []

    for inc in incidents:
        ticket = create_ticket(inc)
        tickets.append(ticket)

        mitre = map_to_mitre(ticket["title"])

        print(f"\n🚨 INCIDENT → {ticket['title']}")
        print(f"Ticket ID: {ticket['ticket_id']}")
        print(f"Severity: {ticket['severity']}")
        print(f"Status: {ticket['status']}")

        print("MITRE ATT&CK Mapping:")
        print(f"Technique ID: {mitre['technique_id']}")
        print(f"Technique Name: {mitre['technique_name']}")
        print(f"Tactic: {mitre['tactic']}")
        
    # ==========================
    # TICKET SUMMARY
    # ==========================

    print("\n===== SOC TICKETS =====")

    all_tickets = get_all_tickets()

    for t in all_tickets:
        print(f"\n🧾 Ticket ID: {t['ticket_id']}")
        print(f"Title: {t['title']}")
        print(f"Status: {t['status']}")
        print(f"Severity: {t['severity']}")

    # ==========================
    # EXPORT SOC REPORT
    # ==========================
    file_name = export_soc_report(
        risk_score,
        status,
        alerts,
        incidents
    )

    print("\n===== EXPORT COMPLETE =====")
    print(f"SOC report saved to: {file_name}")


if __name__ == "__main__":
    run_soc_analysis()