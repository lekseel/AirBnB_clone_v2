#!/usr/bin/env python3
from fabric.api import env, put, run, sudo, local
import os
"""creates an ditribut an archive to your web
"""
env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = os.getenv('SSH_USER')
env.key_filename = os.getenv('SSH_KEY_FILE')

def do_pack():
    local("mkdir -p versions")
    date_time = local("date +%Y%m%d%H%M%S", capture=True)
    tar_path = "versions/web_static_{}.tgz".format(date_time)
    local("tar -czvf {} web_static".format(tar_path))
    if os.path.exists(tar_path):
        return tar_path
    return None

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


def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
