# XR Template For Deployment of New Nodes
# Make sure to enable NETCONF on the nodes with the following CLI commands:
# ssh server v2
# ssh server netconf
# netconf agent tty
# netconf-yang agent ssh
# Todo: Run show run | xml on one of the lab XR nodes to see all YANG models involved
import netconfActions

# Variables
router_hostname = ""
username = ""
password_hash = ""
domain = ""


