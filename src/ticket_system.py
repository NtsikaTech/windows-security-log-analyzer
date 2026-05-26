import uuid
from datetime import datetime

# Simple in-memory SOC ticket store
TICKETS = []


def create_ticket(incident):
    """
    Converts a grouped SOC incident into a ticket.
    """

    ticket = {
        "ticket_id": str(uuid.uuid4())[:8],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "OPEN",
        "severity": incident["severity"],
        "title": incident["incident_type"],
        "description": f"{incident['event_count']} related security events detected",
        "alerts": incident["alerts"]
    }

    TICKETS.append(ticket)

    return ticket


def get_all_tickets():
    """
    Returns all SOC tickets.
    """
    return TICKETS


def close_ticket(ticket_id):
    """
    Closes a SOC ticket by ticket ID.
    """

    for ticket in TICKETS:
        if ticket["ticket_id"] == ticket_id:
            ticket["status"] = "CLOSED"
            ticket["closed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            return ticket

    return None