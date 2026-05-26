# 🛡️ Windows Security Log Analyzer (SOC Simulation Project)

## 📌 Overview

The Windows Security Log Analyzer is a SOC (Security Operations Center) simulation project built in Python. It replicates core SOC analyst workflows by ingesting Windows Security logs, detecting suspicious activity, correlating incidents, assigning tickets, mapping attack techniques to MITRE ATT&CK, and generating structured security reports.

This project demonstrates practical SOC analyst skills including threat detection, incident response, and security event correlation.

---

## 🎯 Key Features

### 🔍 Log Ingestion
- Reads and processes Windows Security Event Logs
- Extracts authentication and system security events

### 🚨 Threat Detection Engine
Detects common attack patterns such as:
- Brute force login attempts
- Credential access activity
- Privilege escalation indicators
- Suspicious authentication behavior

---

### 🧠 Incident Correlation
- Groups related security alerts into structured incidents
- Reduces alert noise for SOC-style analysis
- Builds meaningful attack narratives from raw logs

---

### 🧾 SOC Ticketing System
- Converts incidents into SOC-style tickets
- Assigns unique ticket IDs
- Tracks status (OPEN / CLOSED)
- Classifies severity levels

---

### 🧭 MITRE ATT&CK Mapping
- Maps incidents to MITRE ATT&CK techniques
- Provides structured attack classification

Examples:
- T1110 → Brute Force
- T1078 → Valid Accounts
- T1068 → Privilege Escalation

---

### 📊 SOC Reporting Engine
- Generates structured JSON reports
- Includes:
  - Risk score
  - Alerts
  - Incidents
  - Tickets
  - MITRE mappings

---

## 🏗️ Project Architecture
Logs → Analyzer → Alerts → Incident Correlation → Ticket System → MITRE Mapping → Report Export


---

## 📁 Project Structure
windows-security-log-analyzer/
│
├── main.py # SOC workflow entry point
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── src/
│ ├── log_reader.py # Windows log ingestion
│ ├── analyzer.py # Detection engine
│ ├── risk_engine.py # Risk scoring system
│ ├── incident_grouper.py # Incident correlation logic
│ ├── ticket_system.py # SOC ticketing system
│ ├── mitre_mapper.py # MITRE ATT&CK mapping
│ └── report_exporter.py # JSON report generation
│
├── data/ # Input logs (optional/sample data)
├── reports/ # Generated SOC reports
└── utils/ # Helper utilities (optional)

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run the analyzer
python main.py

📊 Example Output
Risk Score: 78 (HIGH RISK)
Alerts detected
Grouped incidents
Generated SOC tickets
MITRE ATT&CK mapping per incident
Exported JSON report

🧠 SOC Skills Demonstrated
This project demonstrates:

Security log analysis
Threat detection engineering
Incident correlation
SOC ticket lifecycle management
MITRE ATT&CK framework usage
Security reporting and documentation

📌 Use Case
This project is designed for:

SOC Analyst portfolio development
Cybersecurity learning and practice
SIEM-style detection simulation
Interview demonstrations

⚠️ Disclaimer
This project is for educational and SOC training simulation purposes only. It does not interact with real production security systems.****
