#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    """ This Script generates archive the contents of web_static """
    file_Name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file_Name))
        return "versions/web_static_{}.tgz".format(file_Name)

    except Exception as e:
        print("Exception occurred in the priocess of creating archive: ", e)
        return None
