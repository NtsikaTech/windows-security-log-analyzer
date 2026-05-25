import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, jsonify, request
from src.log_reader import get_security_logs
from src.risk_engine import calculate_risk_score
from src.analyzer import detect_suspicious_activity

app = Flask(__name__)

# =========================
# GLOBAL STATE
# =========================

risk_history = []

attack_simulation = {
    "active": False,
    "type": "brute_force",
    "severity": "medium"
}


# =========================
# ATTACK CONTROLS
# =========================

@app.route("/api/set-attack", methods=["POST"])
def set_attack():
    data = request.get_json()

    attack_simulation["active"] = True
    attack_simulation["type"] = data.get("type", "brute_force")
    attack_simulation["severity"] = data.get("severity", "medium")

    return jsonify({
        "status": "Attack configured",
        "type": attack_simulation["type"],
        "severity": attack_simulation["severity"]
    })


@app.route("/api/stop-attack")
def stop_attack():
    attack_simulation["active"] = False
    return jsonify({"status": "Attack stopped"})


# =========================
# DASHBOARD PAGE
# =========================

@app.route("/")
def home():
    logs = get_security_logs()

    risk_score = calculate_risk_score(logs)
    alerts = detect_suspicious_activity(logs)

    if risk_score < 30:
        status = "LOW RISK"
        level = "low"
    elif risk_score < 70:
        status = "MEDIUM RISK"
        level = "medium"
    else:
        status = "HIGH RISK"
        level = "high"

    return render_template(
        "index.html",
        risk_score=risk_score,
        status=status,
        level=level,
        alerts=alerts
    )


# =========================
# LIVE SOC FEED
# =========================

@app.route("/api/live")
def live_data():
    global risk_history

    logs = get_security_logs()

    risk_score = calculate_risk_score(logs)
    alerts = detect_suspicious_activity(logs)

    # =========================
    # ATTACK SIMULATION ENGINE
    # =========================
    if attack_simulation["active"]:

        attack_type = attack_simulation["type"]
        severity = attack_simulation["severity"]

        multiplier_map = {
            "low": 10,
            "medium": 25,
            "high": 45,
            "critical": 70
        }

        multiplier = multiplier_map.get(severity, 25)

        if attack_type == "brute_force":
            risk_score = min(risk_score + multiplier, 100)
            alerts.append("🚨 Brute-force login attempts detected")

        elif attack_type == "credential_stuffing":
            risk_score = min(risk_score + multiplier + 10, 100)
            alerts.append("🚨 Credential stuffing attack detected")

        elif attack_type == "privilege_escalation":
            risk_score = min(risk_score + multiplier + 20, 100)
            alerts.append("🚨 Privilege escalation attempt detected")

        elif attack_type == "mixed":
            risk_score = min(risk_score + multiplier + 30, 100)
            alerts.append("🚨 Multi-stage attack pattern detected")

    # =========================
    # RISK CLASSIFICATION
    # =========================
    if risk_score < 30:
        status = "LOW RISK"
    elif risk_score < 70:
        status = "MEDIUM RISK"
    else:
        status = "HIGH RISK"

    # =========================
    # HISTORY TRACKING
    # =========================
    risk_history.append(risk_score)
    risk_history = risk_history[-10:]

    return jsonify({
        "risk_score": risk_score,
        "status": status,
        "alerts": alerts,
        "history": risk_history,
        "attack_mode": attack_simulation["active"],
        "attack_type": attack_simulation["type"],
        "severity": attack_simulation["severity"]
    })


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)