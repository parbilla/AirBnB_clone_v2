#!/usr/bin/python3
"""Script that distributes an archive to your web servers,
 using the function do_deploy"""
from fabric.api import run, env, put
from os import path

env.hosts = ['35.229.57.233', '34.75.232.226']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Function to distribute archives"""
    if not (path.exists(archive_path)):
        return False
        result = put(archive_path, "/tmp/")
        if result.failed:
            return False
        name = (archive_path.split('/')[1]).split('.')[0]
        result = run("mkdir -p /data/web_static/releases/{}".format(name))
        if result.failed:
            return False
        result = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
                     .format(name, name))
        if result.failed:
            return False
        result = run("rm /tmp/{}.tgz".format(name))
        if result.failed:
            return False
        result = run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(name, name))
        if result.failed:
            return False
        result = run("rm -rf /data/web_static/releases/{}/web_static"
                     .format(name))
        if result.failed:
            return False
        result = run("ln - sf / data/web_static/releases/{}\
                     /data/web_static/current".format(name))
        if result.failed:
            return False
        return True
