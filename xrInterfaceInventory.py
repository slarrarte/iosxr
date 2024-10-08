# xrInterfaceInventory.py
# The purpose of this script is to automate the obtaining of interface data for all nodes
# in your network (as many nodes as you list)
from netconfActions import netconfGet as get
from getpass import getpass
import xmltodict, csv

# Path to csv file
database_path = ''

# List all the router IPs that you'd like included in the data gathering
router_loopbacks = []

# For security purposes, username and password will be entered at user input prompt
enter_username = input('Username: \n')
enter_password = getpass('Password: \n')

# YANG-formatted filter for XML parsing
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

# List of interface data to be written to csv
interface_data_list = [
    ['Hostname', 'Interface', 'IP', 'Mask', 'VRF', 'Description']
]

# <get> each router in router_loopbacks
for router in router_loopbacks:
    # Exception handling for when a node is unreachable
    try:
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
        # Parsing per interface on router
        for interface in range(len(router_response['rpc-reply']['data']['interface-configurations']['interface-configuration'])):
            # Sub-list to be appended to interface_data_list
            host_list = []
            # Hostname will be added to host_list[0] only if this is the first interface of said host;
            # otherwise, host_list[0] will be empty.
            if interface == 0:
                host_list.append(router_response['rpc-reply']['data']['hostname']['system-network-name'])
            else:
                host_list.append('')
            # Interface
            host_list.append(
                router_response['rpc-reply']['data']['interface-configurations']['interface-configuration'][interface]['interface-name']
            )
            # IP
            try:
                host_list.append(
                    router_response['rpc-reply']['data']['interface-configurations']['interface-configuration'][interface]['ipv4-network']['addresses']['primary']['address']
                )
            except:
                host_list.append('')
            # Mask
            try:
                host_list.append(
                    router_response['rpc-reply']['data']['interface-configurations']['interface-configuration'][interface]['ipv4-network']['addresses']['primary']['netmask']
                )
            except:
                host_list.append('')
            # VRF
            try:
                host_list.append(
                    router_response['rpc-reply']['data']['interface-configurations']['interface-configuration'][interface]['vrf']['#text']
                )
            except:
                host_list.append('')
            # Description
            try:
                host_list.append(
                    router_response['rpc-reply']['data']['interface-configurations']['interface-configuration'][interface]['description']
                )
            except:
                host_list.append('')
            # Write sublist to interface_data_list
            interface_data_list.append(host_list)
    # Writes IP as hostname with blank arguments if router is unreachable
    except:
        interface_data_list.append([router, '', '', '', '', ''])
        continue

# Import csv file into program and modify it with gathered NETCONF data
with open(database_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(interface_data_list)
