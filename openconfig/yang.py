#!/usr/bin/env python

from ncclient import manager
from getpass import getpass


connection_params = {
    "host": "sbx-iosxr-mgmt.cisco.com",
    "port": 10000,
    "username": input("username: "),
    "password": getpass("password: "),
    "hostkey_verify": False,
}


with manager.connect(**connection_params) as conn:
    config = conn.get_config(source="running")
    print(config)
