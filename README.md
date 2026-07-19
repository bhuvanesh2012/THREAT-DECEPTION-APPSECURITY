# 🛡️ Threat Deception (Honeypot) & Secure Software Engineering

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-red.svg)](https://flask.palletsprojects.com/)
[![Security](https://img.shields.io/badge/Security-AppSec%20%7C%20Honeypot-success.svg)](#)

This repository demonstrates two complementary pillars of modern application security: proactive defense through **Secure Software Engineering** (AppSec) and active defense through **Threat Deception** (Honeypots).

---

## 📋 Overview

Modern cybersecurity requires protecting legitimate services while actively identifying malicious actors. This project showcases this dual approach:
1. **Secure Software Engineering** — A robust, production-ready web application built using industry-standard secure coding guidelines.
2. **Threat Deception (Honeypot)** — A decoy administrative system designed to lure, slow down, and log unauthorized scanners and attackers.

---

## 🗺️ Project Overview & Architecture

This project is divided into two operational environments to demonstrate defensive depth:
```
              ┌────────────────────────┐
              │   Incoming Traffic     │
              └───────────┬────────────┘
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
[ Port 5000: Real App ]           [ Port 5001: Honeypot ]
┌─────────────────────┐           ┌─────────────────────┐
│  • Secure Auth      │           │  • Fake Admin UI    │
│  • Bcrypt Hashing   │           │  • 100% Rejection   │
│  • SQLAlchemy ORM   │           │  • Intruder Logging │
│  • Hardened Sessions│           │  • Alarm Telemetry  │
└──────────┬──────────┘           └──────────┬──────────┘
           ▼                                 ▼
 [ secure_users.db ]               [ honeypot_log.txt ]
  (Legitimate DB)                   (Forensic Registry)
```

---

## 📂 Project Directory Tree

```text
threat-deception-appsec-project/
│
├── secure-app/                   # Hardened Web Application
│   ├── app.py                    # Main Flask application with AppSec controls
│   ├── models.py                 # SQLAlchemy relational schema
│   ├── forms.py                  # Input validation logic
│   ├── secure_users.db           # SQLite local production database
│   └── templates/                # Secure template files
│       ├── base.html             # Base layout template
│       ├── login.html            # Login screen
│       └── register.html         # User registration
│
├── honeypot/                     # Threat Deception Decoy
│   ├── app.py                    # Lightweight, non-blocking telemetry server
│   ├── honeypot_log.txt          # File-based logging registry
│   └── templates/
│       └── admin_login.html      # Highly enticing fake portal
│
├── requirements.txt              # Standardized dependency index
└── README.md                     # Technical project documentation
