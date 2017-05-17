from vconnector.core import VConnector
client = VConnector(
     user='root',
     pwd='p4ssw0rd',
     host='vc01.example.org'
)
client.connect()