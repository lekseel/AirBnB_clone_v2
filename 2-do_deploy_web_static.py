#!/usr/bin/python3
"""In the following example, the SSH key and the username used for accessing to the server are passed in the command line
"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['18.235.248.180', '18.215.160.220']
env.user = os.getenv('ubuntu')
env.key_filename = os.getenv('~/.ssh/id_rsa')

def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False

    put(archive_path, '/tmp/')

    archive_filename = os.path.basename(archive_path)
    archive_name = os.path.splitext(archive_filename)[0]

    run('mkdir -p /data/web_static/releases/{}'.format(archive_name))

    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(archive_filename, archive_name))

    run('rm /tmp/{}'.format(archive_filename))

    run('mv /data/web_static/releases/{}/web_static/* '
        '/data/web_static/releases/{}/'.format(archive_name, archive_name))

    run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_name))

    run('rm -f /data/web_static/current')

    run('ln -s /data/web_static/releases/{} /data/web_static/current'
        .format(archive_name))

    return True
