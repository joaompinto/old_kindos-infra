from hcloud.images.domain import Image
from hcloud.server_types.domain import ServerType

from hcloud_helper import client


# Create a server named my-server
response = client.servers.create(
    name="main-web-server",
    server_type=ServerType(name="cax21"),
    image=Image(name="debian-12"),
    ssh_keys=[client.ssh_keys.get_by_name("janito")],
    location=client.locations.get_by_name("fsn1"),
)

server = response.server
print(f"{server.id=} {server.name=} {server.status=}")
