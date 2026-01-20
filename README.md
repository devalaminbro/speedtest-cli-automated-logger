# 🚀 Automated Speedtest Logger & SLA Monitor

![Language](https://img.shields.io/badge/Language-Python%203-blue)
![Library](https://img.shields.io/badge/Library-Speedtest--CLI-orange)
![Data](https://img.shields.io/badge/Data-CSV%20Logging-green)

## 📖 Overview
For ISPs and Network Engineers, verifying if the Upstream Provider (IIG) is delivering the promised bandwidth is critical. Manual testing is inconsistent.

This repository contains a **Python Automation Tool** that performs scheduled bandwidth tests using the Ookla Speedtest network. It logs **Download Speed, Upload Speed, Ping, and Jitter** into a structured CSV file, allowing you to generate reports and hold providers accountable for SLA breaches.

## 🛠 Features
- 🕒 **Scheduled Testing:** Runs automatically at set intervals (e.g., every 1 hour).
- 📊 **CSV Export:** Saves data in `speed_log.csv` for easy analysis in Excel/Google Sheets.
- 📉 **Low Performance Alert:** Detects if speed drops below a threshold (Logic ready).
- 🖥️ **Lightweight:** Can run on a Raspberry Pi or any Linux Server background.

## ⚙️ Prerequisites
- Python 3.x
- `speedtest-cli` library

## 🚀 Usage Guide

### 1. Installation
Install the required library:
```bash
pip install speedtest-cli

2. Run the Logger
Clone the repo and start the script:
python3 speed_logger.py

3. Analyze Data
Open speed_log.csv to see the history:
Timestamp,Download(Mbps),Upload(Mbps),Ping(ms)
2026-01-22 10:00:00, 95.5, 92.1, 12.5
2026-01-22 11:00:00, 45.2, 88.0, 150.2

(Here you can clearly see a drop in download speed and high latency at 11:00 AM)

Author: Sheikh Alamin Santo
Cloud Infrastructure Specialist & Network Analyst
