import configparser
from ncclient import manager

config = configparser.ConfigParser()
config.read('workshop-configuration.ini')
device=config['DEVICE']
print("Connecting to device..")
netconf_connection = manager.connect(host=device['Host'], 
                                     port=device['NCPort'],
                                     username=device['UserName'],
                                     password=device['Password'],
                                     hostkey_verify=False,
                                     device_params={'name':'iosxr'})

filter_payload = """
<filter>
 <telemetry-model-driven xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-telemetry-model-driven-cfg">
 </telemetry-model-driven>
</filter>
"""

config = netconf_connection.get_config(source='running', filter=filter_payload)
filter_payload = """
<filter>
 <telemetry-model-driven xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-telemetry-model-driven-oper">
 </telemetry-model-driven>
</filter>
"""
print(netconf_connection.get(filter=filter_payload))
