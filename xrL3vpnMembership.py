# XR L3VPN MEMBERSHIP
# This script pulls all MPLS L3VPN memberships from a list of routers
# and creates/modifies a JSON-formatted database from it.
from netconfActions import netconfGet as get
from pathlib import Path
import xmltodict, json

# Path to document where vpnv4 data will be written to (JSON formatted)
database_path = Path.cwd()/'dataCollection/vpnv4Database.json'

# List all the router IPs that you'd like included in the data gathering
router_loopbacks = ['172.16.100.5', '172.16.100.6', '172.16.100.7', '172.16.100.8', '172.16.100.9']

# For security purposes, username and password will be entered at user input prompt
enter_username = input('Username: \n')
enter_password = input('Password: \n')

# YANG-formatted filter for XML parsing
xml_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <l3vpn xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-mpls-vpn-oper"/>
</filter>
"""

# Import interfaceDatabase.json into program as a dictionary to be modified
with open(database_path, 'r') as json_data:
    dict_data = json.load(json_data)

for router in router_loopbacks:
    router_response = xmltodict.parse(
        get(
            host=router,
            port="830",
            username=enter_username,
            password=enter_password,
            ios="iosxr",
            filter=xml_filter
        )
    )
    try:
        for vrf in router_response['rpc-reply']['data']['l3vpn']['vrfs']:
            for
            # dict_data[router] = router_response['rpc-reply']['data']['l3vpn']['vrfs']
    except:
        print(f'No VPNv4 data found on {router}\n')
        continue

database_doc = open(database_path, 'w')
database_doc.write(json.dumps(dict_data, indent=3))
database_doc.close()
