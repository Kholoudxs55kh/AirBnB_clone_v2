#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
using the function do_pack
"""

from fabric.api import *
from os.path import exists
from datetime import datetime
from os.path import isdir, exists

env.hosts = ['54.90.30.64', '52.90.15.99']  # <IP web-01>, <IP web-02>
env.user = 'ubuntu'  # username


def do_pack():
    """
    anything
    """
    date_ = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file_ = local("tar -cvzf versions/web_static_{}.tgz web_static"
                  .format(date_))
    if file_.failed:
        return None
    print(file_)
    return file_


def do_deploy(archive_path):
    """ distributes an archive to your  web servers
    """
    if exists(archive_path) is False:
        return False
    file_ = archive_path.split('/')[-1]
    tmp = "/tmp/" + file_
    archive_p = '/data/web_static/releases/' + "{}".format(file_.split('.')[0])

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(archive_p))
        run("sudo tar -xzf {} -C {}/".format(tmp, archive_p))
        run("sudo rm {}".format(tmp))
        run("sudo mv {}/web_static/* {}/".format(archive_p, archive_p))
        run("sudo rm -rf {}/web_static".format(archive_p))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(archive_p))
        return True
    except Exception as e:
        return False


def deploy():
    """ creates and distributes an archive to your web servers
    """
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    result = do_deploy(new_archive_path)
    return result
