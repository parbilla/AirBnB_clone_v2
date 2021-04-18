#!/usr/bin/python3
"""Script that deletes out-of-date archives"""
from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['35.229.57.233', '34.75.232.226']
env.user = "ubuntu"


def do_clean(number=0):
    """Function to clean trash files"""
    number = int(number)
    number += 1
    if (number == 1):
        local('cd versions; ls -t | tail -n +2 | xargs rm -rf')
        run('cd /data/web_static/releases; ls -t | tail -n +2 | xargs rm -rf')
    else:
        local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.
              format(number))
        run('cd /data/web_static/releases; ls -t | tail -n +{} | xargs rm -rf'.
            format(number))
