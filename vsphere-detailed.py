from __future__ import print_function
import pyVmomi
from vconnector.core import VConnector
client = VConnector(
     user='root',
     pwd='p4ssw0rd',
     host='vc01.example.org'
 )
client.connect()
datastores = client.get_datastore_view()
result = client.collect_properties(
     view_ref=datastores,
     obj_type=pyVmomi.vim.Datastore,
     path_set=['name', 'summary.capacity']
)
print(result)
client.disconnect()