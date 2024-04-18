import netconfActions
from pathlib import Path

# Scripts used in various DevNet Sandbox environments

# Below code to be used in XR Programmability Always-On Lab Env

# Path to NETCONF Filter
filterPath = Path.home()/'pyProjects'/'projects'/'iosXrLab'/'netconfFilter.xml'

# Import filter into script
xmlFilter = filterPath.read_text()

# print(
#     netconfActions.netconfGetCapabilities(
#         'sandbox-iosxr-1.cisco.com',
#         '830',
#         'admin',
#         'C1sco12345',
#         'iosxr'
#     )
# )
#
# print(
#     netconfActions.netconfGetConfig(
#         '10.10.20.35',
#         '830',
#         'developer',
#         'C1sco12345',
#         'iosxr',
#         filter=xmlFilter,
#         datastore='running'
#     )
# )

# Create hostname
print(
    netconfActions.netconfEditConfig(
        '172.16.100.5',
        '830',
        'developer',
        'C1sco12345',
        'iosxr',
        filter=xmlFilter,
        datastore='running'
    )
)
############################################################################################

# Below code used in Cisco Crosswork sandbox

# Below for loop creates text files containing capabilities for each router in topology.
# capFileDir is the path to the directory for the Capabilities text files.
# capFileDir = Path.home()/'pyProjects/projects/iosXrLab/crossworkNodesCapabilities'
# for i in range(192, 200):
#         try:
#                 capFile = open(capFileDir/f'{str(i)}.txt', 'a')
#                 capFile.write(f'********************\n{str(i)}\n********************\n')
#                 capFile.write(
#                         netconfActions.netconfGetCapabilities(
#                                 f'10.10.20.{str(i)}',
#                                 '830',
#                                 'cisco',
#                                 'cisco',
#                                 'iosxr'
#                         )
#                 )
#                 capFile.close()
#         except:
#                 continue
#
#
# # Path to NETCONF Filter
# filterPath = Path.home()/'pyProjects'/'projects'/'iosXrLab'/'netconfFilter.xml'
#
# # Import filter into script
# xmlFilter = filterPath.read_text()

# # Get interface data
# print(
#     netconfActions.netconfGetConfig(
#         '10.10.20.194',
#         '830',
#         'cisco',
#         'cisco',
#         'iosxr',
#         filter=xmlFilter,
#         datastore='running'
#     )
# )

# # Create Loopback69
# print(
#     netconfActions.netconfEditConfig(
#         'sandbox-iosxr-1.cisco.com',
#         '830',
#         'admin',
#         'C1sco12345',
#         'iosxr',
#         filter=xmlFilter,
#         datastore='running'
#     )
# )
