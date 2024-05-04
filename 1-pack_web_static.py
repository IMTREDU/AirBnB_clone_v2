#!/usr/bin/python3
"""
Fabric script for creating a tgz archive.
To execute, use: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Creates an archive within the web_static folder.
    """

    current_time = datetime.now()
    archive_name = 'web_static_' + current_time.strftime("%Y%m%d%H%M%S") + '.tgz'
    local('mkdir -p versions')
    creation_status = local('tar -cvzf versions/{} web_static'.format(archive_name))
    if creation_status.succeeded:
        return archive_name
    else:
        return None
