import netconfActions
from pathlib import Path

# Scripts used in various DevNet Sandbox environments

# Below code used in Cisco Crosswork sandbox

# Below for loop creates text files containing capabilities for each router in topology.
# capFileDir is the path to the directory for the Capabilities text files.
capFileDir = Path.home()/'pyProjects/projects/iosXrLab/crossworkNodesCapabilities'
for i in range(192, 200):
        try:
                capFile = open(capFileDir/f'{str(i)}.txt', 'a')
                capFile.write(f'********************\n{str(i)}\n********************\n')
                capFile.write(
                        netconfActions.netconfGetCapabilities(
                                f'10.10.20.{str(i)}',
                                '830',
                                'cisco',
                                'cisco',
                                'iosxr'
                        )
                )
                capFile.close()
        except:
                continue

#
# # Path to NETCONF Filter
# filterPath = Path.home()/'pyProjects'/'projects'/'iosXrLab'/'netconfFilter.xml'
#
# # Import filter into script
# xmlFilter = filterPath.read_text()
#
# # Get interface data
# print(
#     netconfActions.netconfGet(
#         'sandbox-iosxr-1.cisco.com',
#         '830',
#         'admin',
#         'C1sco12345',
#         'iosxe',
#         filter=xmlFilter
#     )
# )
