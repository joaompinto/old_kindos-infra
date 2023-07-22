# KindOS Infra Setup

This repository provides all the necessary scripts to setup a KindOS infrastructure.

The deployment is done to the [Hetzner Cloud](https://www.hetzner.com/).

## Requirements

- Project created at https://console.hetzner.cloud/projects
    - Setup Security SSH Keys, create API TOKEN and set it on environment variable CLOUD_API_TOKEN


```bash
./create-server.py main-web-server
````
