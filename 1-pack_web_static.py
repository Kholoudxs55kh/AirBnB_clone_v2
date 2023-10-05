#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
using the function do_pack
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


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

