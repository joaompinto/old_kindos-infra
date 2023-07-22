#!/bin/sh
set -eu

SCRIPT_DIR=$(dirname $(readlink -f "$0"))


apt install -y nginx python3-certbot-nginx supervisor python3.11-venv

# Create a new user called wwwkindos if it does not exist
[[ ! -d /home/wwwkindos ]] && useradd -m -s /bin/false wwwkindos && chmod 700 /home/wwwkindos

cp -vr ${SCRIPT_DIR}/etc /
cp -vr ${SCRIPT_DIR}/home /
chown -R wwwkindos:wwwkindos /home/wwwkindos
bash ${SCRIPT_DIR}/setup-venv.sh
rm -f /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/wwwkindos
ln -s /etc/nginx/sites-available/wwwkindos /etc/nginx/sites-enabled/wwwkindos
certbot --keep --nginx -d www.kindos.org --post-hook "/usr/sbin/service nginx restart"

supervisorctl reread
supervisorctl update

setfacl -m user:www-data:rx- /home/wwwkindos/ /home/wwwkindos/run
setfacl -Rdm user:www-data:r-- /home/wwwkindos/ /home/wwwkindos/run
setfacl -Rm user:www-data:r-- /home/wwwkindos/run/*