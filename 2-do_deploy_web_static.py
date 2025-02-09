#!/usr/bin/python3
"""Script that distributes an archive to your web servers,
 using the function do_deploy"""
from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['35.229.57.233', '34.75.232.226']


def do_deploy(archive_path):
    """Function that decompress and deploy functions in the serv"""
    if path.exists(archive_path):
        absFilePath = path.abspath(archive_path)
        filepath, filename = path.split(absFilePath)
        local = "{}".format(archive_path)
        dest = "/tmp/{}".format(filename)
        if put(local, dest).failed:
            return False
        folder = filename[:-4]
        releases = "/data/web_static/releases"
        if run('mkdir -p {}/{}'.format(releases, folder)).failed:
            return False
        if run('tar -xzf /tmp/{} -C {}/{}'.
               format(filename, releases, folder)).failed:
            return False
        if run('rm /tmp/{}'.format(filename)).failed:
            return False
        if run('mv {}/{}/web_static/* {}/{}/'.
               format(releases, folder, releases, folder)).failed:
            return False
        if run('rm -rf {}/web_static'.format(releases)).failed:
            return False
        if run('rm -rf /data/web_static/current').failed:
            return False
        if run('ln -s {}/{}/ /data/web_static/current'.
               format(releases, folder)).failed:
            return False
        return True
    else:
        return False
