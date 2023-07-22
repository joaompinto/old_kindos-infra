# KindOS Infra Setup

This repository provides all the necessary scripts to setup a KindOS infrastructure.

The deployment is done to the [Hetzner Cloud](https://www.hetzner.com/).

## Requirements

- Project created at https://console.hetzner.cloud/projects
    - Setup a SSH Key with name "Janito", create API TOKEN and set it on environment variable CLOUD_API_TOKEN

## Deploy
```bash
./create-server.py main-web-server
````
