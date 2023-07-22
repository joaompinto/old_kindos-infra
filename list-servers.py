#!/bin/env python3
from hcloud_helper import client

servers = client.servers.get_all()
for server in servers:
    print(str(server))
