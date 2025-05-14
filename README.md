# 🔍 Port Scanner 🔒

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A simple TCP port scanner built with Python. It scans ports from 1 to 1024 on a specified target IP address and displays the open ports. Great for beginners in cybersecurity and ethical hacking.

---

## 🧠 Features

- Scans TCP ports 1–1024 on any given host
- Converts hostname to IPv4 address automatically
- Shows real-time scan timestamp
- Displays open ports only
- Uses `pyfiglet` for a cool ASCII art banner
- Lightweight, fast, and beginner-friendly

---

## 📸 Example Output

 ____            _     ____                                  
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                             

--------------------------------------------------
Scanning target 192.168.1.1
Time started: 2025-05-14 10:16:44.772313
--------------------------------------------------
Port 80:      Open
Port 443:      Open

---

## 📦 Installation

Clone the repository and install the required library:

```bash
git clone https://github.com/alperoztvrk/port-scanner.git
cd port-scanner
pip install -r requirements.txt

---

⚙️ Usage

python3 scanner.py <target-ip-or-hostname>

Example:

python3 scanner.py 192.168.1.1

---

⚠️ Disclaimer

This tool is intended for educational and ethical purposes only.
Never scan IPs you don’t own or don’t have explicit permission to scan.
Unauthorized scanning may be illegal depending on your jurisdiction.

---

📄 License

This project is licensed under the MIT License.

---

👨‍💻 Author

Alper Alexandru Ozturk
📧 alperoztvrk@gmail.com
