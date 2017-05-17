from __future__ import print_function
from vconnector.core import VConnector
client = VConnector(
     user='root',
     pwd='p4ssw0rd',
     host='vc01.example.org'
)
client.connect()
vms = client.get_vm_view()
print(vms.view)
client.disconnect()