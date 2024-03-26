import netconfActions
from pathlib import Path

# # Get Capabilities
# netconfActions.netconfGetCapabilities(
#         'sandbox-iosxr-1.cisco.com',
#         '830',
#         'admin',
#         'C1sco12345',
#         'iosxr'
# )

# Path to NETCONF Filter
filterPath = Path.home()/'pyProjects'/'projects'/'iosXrLab'/'netconfFilter.xml'

# Import filter into script
xmlFilter = filterPath.read_text()

# Get interface data
print(
    netconfActions.netconfGet(
        '10.10.20.48',
        '830',
        'developer',
        'C1sco12345',
        'iosxe',
        filter=xmlFilter
    )
)
