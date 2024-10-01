from ncclient import manager
import xml.dom.minidom

# XML handling function to be called as decorator in subsequent functions
def readable_xml(func):
    def wrapper(*args, **kwargs):
        xml_result = func(*args, **kwargs)
        temp = xml.dom.minidom.parseString(str(xml_result))
        new_xml = temp.toprettyxml(indent=" ", newl="")
        return new_xml
    return wrapper

# Get Capabilities function (aka <hello> rpc)
def netconfGetCapabilities(
        host,
        port,
        username,
        password,
        ios
):
    capabilities = []
    with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            device_params={'name': ios},
            timeout=10
    ) as m:
        for capability in m.server_capabilities:
            capabilities.append(capability)
        capabilities.sort()
        capabilities_str = '\n'.join(capabilities)
        return capabilities_str

# <get> (Only targets running datastore)
@readable_xml
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
            device_params={'name': ios},
            timeout=10
    ) as m:
        return m.get(filter).xml

# <get-config> (Targets any specified datastore)
@readable_xml
def netconfGetConfig(
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
            device_params={'name': ios},
            timeout=10
    ) as m:
        return m.get_config(
            filter=filter,
            source='running'
        ).xml

# <edit-config>
@readable_xml
def netconfEditConfig(
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
            device_params={'name': ios},
            timeout=10
    ) as m:
        return m.edit_config(
            target='running',
            config=filter
        ).xml
