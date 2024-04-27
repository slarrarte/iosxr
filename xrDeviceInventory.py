# deviceInventory.py
# The purpose of this script is to automate the obtaining of interface data for all nodes
# in your network (as many nodes as you list)
from netconfActions import netconfGet as get
from getpass import getpass

# List all the router IPs that you'd like included in the data gathering
router_loopbacks = []

# For security purposes, username and password will be entered at user input prompt
enter_username = input('Please enter username: \n')
enter_password = getpass('Please enter password: \n')

hostname_filter = """
<hostname xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-um-hostname-cfg">
    <system-network-name/>
</hostname>
"""

interfaces_filter = """
<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
    <interface-configuration/>
</interface-configurations>
"""

for router in router_loopbacks:
    get(
        host=router,
        port="830",
        username=enter_username,
        password=enter_password,
        ios="iosxr",
        filter=interfaces_filter
    )
