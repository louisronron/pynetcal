""" the program's main entry-point in this module """

from ipaddress import IPv4Address, IPv4Network
from ipv4subnetmask import IPv4SubnetMask
ip1 = IPv4SubnetMask(IPv4Address("255.255.0.0"))

print(ip1.mask)
print(ip1.prefix)
print(ip1.decimal)
print(ip1.binary)
