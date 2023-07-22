#/bin/sh

set -eu

su - wwwkindos -s /bin/bash << _EOF_
set -eu
cd /home/wwwkindos
python3.11 -m venv .venv
source .venv/bin/activate
pip install gunicorn uvicorn fastapi
mkdir -p /home/wwwkindos/logs /home/wwwkindos/run
_EOF_
