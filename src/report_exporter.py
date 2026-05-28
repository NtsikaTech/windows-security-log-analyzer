import json
import os
from datetime import datetime


def export_soc_report(risk_score, status, alerts, incidents):
    """
    Exports SOC analysis results into a structured JSON report.
    """

    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "risk_score": risk_score,
        "risk_status": status,
        "summary": {
            "total_alerts": len(alerts),
            "total_incidents": len(incidents)
        },
        "alerts": alerts,
        "incidents": incidents
    }

    file_name = "reports/soc_report.json"

    with open(file_name, "w") as f:
        json.dump(report, f, indent=4)

    return file_name