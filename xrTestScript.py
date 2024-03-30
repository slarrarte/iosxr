import netconfActions
from pathlib import Path

# Script mainly for use in DEVNET Sandbox XR 8000 Notebooks lab environment

# Get Capabilities
netconfActions.netconfGetCapabilities(
        'sandbox-iosxr-1.cisco.com',
        '830',
        'admin',
        'C1sco12345',
        'iosxr'
)
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
