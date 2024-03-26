from ncclient import manager
import xml.dom.minidom

# Get Capabilities function
def netconfGetCapabilities(
        host,
        port,
        username,
        password,
        ios
):
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': ios}
    ) as m:
        for capability in m.server_capabilities:
            print(capability)

# Get config (State data only, and only targeting running datastore)
def netconfGet(
        host,
        port,
        username,
        password,
        ios,
        filter
):
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': ios}
    ) as m:
        netconfReply = m.get(filter)
        # Make returned XML data more human-readable
        temp = xml.dom.minidom.parseString(str(netconfReply.xml))
        new_xml = temp.toprettyxml()
        print(new_xml)
