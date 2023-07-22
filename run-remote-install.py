from subprocess import getstatusoutput
from hcloud_helper import get_server_ip
import os

server_ip = get_server_ip("main-web-server")
cmd = f"scp -r remote root@{server_ip}:/root"
os.system(cmd)
rc, output = getstatusoutput(cmd)
os.system(f"ssh root@{server_ip} bash /root/remote/install.sh")
