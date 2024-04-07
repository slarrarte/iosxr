import netconfActions, fuck
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
qwer = """
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
      <interface>
        <name>Loopback25</name>
        <config>
          <name>Loopback25</name>
          <type xmlns:idx="urn:ietf:params:xml:ns:yang:iana-if-type">idx:softwareLoopback</type>
          <enabled>true</enabled>
          <description>Test</description>
        </config>
        <subinterfaces>
          <subinterface>
            <index>0</index>
            <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
              <addresses>
                <address>
                  <ip>5.5.5.5</ip>
                  <config>
                    <ip>5.5.5.5</ip>
                    <prefix-length>32</prefix-length>
                  </config>
                </address>
              </addresses>
            </ipv4>
          </subinterface>
        </subinterfaces>
      </interface>
    </interfaces>
</config>
"""
# Create hostname
# print(
#     netconfActions.netconfEditConfig(
#         '10.10.20.48',
#         '830',
#         'developer',
#         'C1sco12345',
#         'iosxr',
#         filter=qwer,
#         datastore='running'
#     )
# )
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
