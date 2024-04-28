# deviceInventory.py
# The purpose of this script is to automate the obtaining of interface data for all nodes
# in your network (as many nodes as you list)
from netconfActions import netconfGet as get
from getpass import getpass
import xmltodict, json

# Path to document where inventory data will be written to (JSON formatted)
database_path = '/Users/santiagolarrarte/pyProjects/projects/iosXrLab/interfaceDatabase.json'

# List all the router IPs that you'd like included in the data gathering
router_loopbacks = ['172.16.100.5']

# For security purposes, username and password will be entered at user input prompt
enter_username = input('Username: \n')
enter_password = getpass()

xml_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <hostname xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-um-hostname-cfg">
        <system-network-name/>
    </hostname>
    <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
        <interface-configuration/>
    </interface-configurations>
</filter>
"""

jsonData = {}

# Open database document and write data
database_doc = open(database_path, 'a')

for router in router_loopbacks:
    dictData = xmltodict.parse(
        get(
            host=router,
            port="830",
            username=enter_username,
            password=enter_password,
            ios="iosxr",
            filter=xml_filter
        )
    )
    jsonData[dictData['rpc-reply']['data']['hostname']['system-network-name']] = dictData['rpc-reply']['data']['interface-configurations']['interface-configuration']
    database_doc.write(
        json.dumps(jsonData, indent=3)
    )
database_doc.close()
