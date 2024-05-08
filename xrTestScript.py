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
print(
    netconfActions.netconfGet(
        '172.16.100.5',
        '830',
        'developer',
        'C1sco12345',
        'iosxr',
        xmlFilter
    )
)

# Create hostname
# print(
#     netconfActions.netconfEditConfig(
#         '172.16.100.5',
#         '830',
#         'developer',
#         'C1sco12345',
#         'iosxr',
#         filter=xmlFilter
#     )
# )
############################################################################################

# Below code used in Cisco Crosswork sandbox

# Below for loop creates text files containing capabilities for each router in topology.
# capFileDir is the path to the directory for the Capabilities text files.
# capFileDir = Path.home()/'pyProjects/projects/iosXrLab/crossworkNodesCapabilities'
# for router in ['172.16.100.5', '172.16.100.6','172.16.100.7', '172.16.100.8', '172.16.100.9']:
#     capFile = open(capFileDir/f'{router}.txt', 'w')
#     capFile.write(
#             netconfActions.netconfGetCapabilities(
#                     f'{router}',
#                     '830',
#                     'developer',
#                     'C1sco12345',
#                     'iosxr'
#             )
#     )
#     capFile.close()

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
#         '10.10.20.35',
#         '830',
#         'developer',
#         'C1sco12345',
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
