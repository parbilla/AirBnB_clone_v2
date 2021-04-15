#!/usr/bin/python3
"""Script that distributes an archive to your web servers,
 using the function do_deploy"""
import fabric.api
import os

env.hosts = ['35.229.57.233', '34.75.232.226']
env.user = ubuntu


def do_deploy(archive_path):
    """Function to distribute archives"""
    if not (path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        name = (archive_path.split('/')[1]).split(.)[0]
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xvzf /tmp/{}.tgz -C /home/data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("ln -sf /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False
