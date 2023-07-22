#!/usr/bin/env python
from hcloud.images.domain import Image
from hcloud.server_types.domain import ServerType
from hcloud_helper import client
import typer
import time

def create_server(name: str):
    # Create a server named my-server
    response = client.servers.create(
        name,
        server_type=ServerType(name="cax21"),
        image=Image(name="debian-12"),
        ssh_keys=[client.ssh_keys.get_by_name("janito")],
        location=client.locations.get_by_name("fsn1"),
    )

    server = response.server
    print("Waiting for server to become available ", end="", flush=True)
    while server.status != "running":
        print(".", end="", flush=True)
        server = client.servers.get_by_id(server.id)
        time.sleep(1)
    print("done\n")
    print("You can now")
    print("  ssh root@{}".format(server.public_net.ipv4.ip))


if __name__ == "__main__":
    typer.run(create_server)