#!/usr/bin/python3
""" script distributes an archive to your web servers,
using the function do_deploy """


from fabric.api import *
from os.path import exists


env.hosts = ['54.90.30.64', '52.90.15.99']  # <IP web-01>, <IP web-02>
