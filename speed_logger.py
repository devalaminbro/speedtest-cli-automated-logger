```python
import speedtest
import csv
import time
import os
from datetime import datetime

# ============================================================
# ISP Uplink Quality Monitor (Speedtest Logger)
# Author: Sheikh Alamin Santo
# Description: Logs Bandwidth & Latency to CSV
# ============================================================

# Configuration
LOG_FILE = "speed_log.csv"
TEST_INTERVAL = 3600  # Run every 1 hour (in seconds)

def run_speedtest():
    print(f"[+] Starting Speedtest at {datetime.now()}...")
    
    try:
        st = speedtest.Speedtest()
        
        print(" -> Finding best server...")
        st.get_best_server()
        
        print(" -> Testing Download...")
        download_speed = st.download() / 1_000_000  # Convert bps to Mbps
        
        print(" -> Testing Upload...")
        upload_speed = st.upload() / 1_000_000  # Convert bps to Mbps
        
        ping = st.results.ping
        
        return download_speed, upload_speed, ping

    except Exception as e:
        print(f"[-] Speedtest Failed: {e}")
        return None, None, None

def save_to_csv(download, upload, ping):
    # Check if file exists to write header
    file_exists = os.path.isfile(LOG_FILE)
    
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write Header if new file
        if not file_exists:
            writer.writerow(["Timestamp", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])
        
        # Write Data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, round(download, 2), round(upload, 2), round(ping, 2)])
        
    print(f"[+] Data Logged: {download:.2f} Mbps / {upload:.2f} Mbps / {ping} ms\n")

def main():
    print("=========================================")
    print("   AUTOMATED SPEEDTEST LOGGER RUNNING    ")
    print("=========================================")
    
    while True:
        dl, ul, pg = run_speedtest()
        
        if dl is not None:
            save_to_csv(dl, ul, pg)
        
        print(f"Waiting {TEST_INTERVAL} seconds for next test...")
        time.sleep(TEST_INTERVAL)

if __name__ == "__main__":
    main()
