# CAKWN-LEAKCHECK-EMAIL-CLI
**Email Breach Intelligence and Exposure Detection Framework**

A modern, fast, and lightweight CLI tool to check whether an email has appeared in data breaches. It analyzes risk levels, generates executive reports, and provides security recommendations.

Designed to feel like a powerful combination of Have I Been Pwned, LeakCheck, IntelX, DeHashed, and Snusbase.

## 🚀 Key Features
- **Comprehensive Email Check:** View exposure status, number of breaches, risk level, and compromised data types.
- **Risk Level Engine:** Intelligent scoring (LOW, MEDIUM, HIGH, CRITICAL) based on recency and data sensitivity.
- **Multi-Provider Support:** Integrates with HIBP, LeakCheck, IntelX, DeHashed, and custom APIs.
- **Batch & Domain Modes:** Multi-threaded analysis for bulk emails and domain-wide exposure tracking.
- **Report Generator:** Export findings to PDF, HTML, JSON, YAML, or CSV.
- **Local History & Caching:** Privacy-aware local SQLite database with TTL caching to prevent duplicate API queries.

## 📦 Installation
```bash
git clone https://github.com/wongpusatbolo/cakwn-leakcheck-email-cli.git
cd cakwn-leakcheck-email-cli
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🛠️ Usage
```bash
python3 main.py email user@example.com
python3 main.py domain example.com
python3 main.py batch emails.txt
python3 main.py stats
```
