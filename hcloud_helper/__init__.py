from hcloud import Client
from os import environ
import requests
import json

client = Client(token=environ["CLOUD_API_TOKEN"])


def get_server_ip(server_name):
    server = client.servers.get_by_name(server_name)
    return server.public_net.ipv4.ip


def create_dns_record(
    record_name: str,
    record_type: str,
    record_value: str,
    zone_id: str = environ["DNS_ZONE_ID"],
    ttl=3600,
):
    response = requests.post(
        url="https://dns.hetzner.com/api/v1/records",
        headers={
            "Content-Type": "application/json",
            "Auth-API-Token": environ["DNS_API_TOKEN"],
        },
        data=json.dumps(
            {
                "value": record_value,
                "ttl": ttl,
                "type": record_type,
                "name": record_name,
                "zone_id": zone_id,
            }
        ),
    )
    print(
        "Response HTTP Status Code: {status_code}".format(
            status_code=response.status_code
        )
    )
    print("Response HTTP Response Body: {content}".format(content=response.content))
    response.raise_for_status()
    return response.json()
