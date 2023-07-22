# Install the Python Requests library:
# `pip install requests`

from hcloud_helper import create_dns_record, get_server_ip

server_ip = get_server_ip("main-web-server")
create_dns_record("www", "A", str(server_ip))
