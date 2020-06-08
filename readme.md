## Terminology

YANG is a data modeling language used to model configuration and state data manipulated by the NETCONF protocol. YANG was published as RFC 6020 in September, 2010. YANG relates to the content and operations layers in NETCONF. (https://www.tail-f.com/what-is-yang/)

NETCONF is a protocol defined by the IETF to “install, manipulate, and delete the configuration of network devices”. NETCONF operations are realized on top of a Remote Procedure Call (RPC) layer using an XML encoding and provides a basic set of operations to edit and query configuration on a network device. (https://www.tail-f.com/what-is-netconf/)

pyang is a YANG validator, transformator and code generator, written in python. It can be used to validate YANG modules for correctness, to transform YANG modules into other formats, and to generate code from the modules.
(https://github.com/mbj4668/pyang)

OpenConfig is a collaborative effort by network operators to develop programmatic interfaces and tools for managing networks in a dynamic, vendor-neutral way. OpenConfig’s initial focus is on compiling a consistent set of vendor-neutral data models (written in YANG) based on actual operational needs from use cases and requirements from multiple network operators. (https://github.com/openconfig/public)

ncclient is a Python library that facilitates client-side scripting and application development around the NETCONF protocol. (https://github.com/ncclient/ncclient)

## Sites

http://www.openconfig.net/

## Demo

* Install pyang and ncclient
```
pip install pyang ncclient
```

* Clone openconfig yang modules
```
git clone git@github.com:openconfig/public.git yang_oc
```

* Use pyang to build an interfaces tree from the OpenConfig YANG module
```
mkdir data_ref
pyang --verbose --format tree --path yang_oc \
yang_oc/release/models/interfaces/openconfig-interfaces.yang > data_ref/oc_intf.txt
pyang --verbose --format tree --path yang_oc \
yang_oc/release/models/interfaces/openconfig-if-ethernet.yang > data_ref/oc_eth.txt
pyang --verbose --format tree --path yang_oc \
yang_oc/release/models/vlan/openconfig-vlan.yang > data_ref/oc_vlan.txt
```

* Use an always-on devnet sandbox from https://developer.cisco.com. They have a number of always on routers and switches to choose from. I'm using the 'IOS XR Programmability' sandbox. Below is a basic script to test NETCONF connectivity.

```
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
```
You should see an XML output representing the running config of the device.
