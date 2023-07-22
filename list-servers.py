#!/bin/env python
from hcloud_helper import client

servers = client.servers.get_all()
for server in servers:
    print(server.name, server.public_net.ipv4.ip)
