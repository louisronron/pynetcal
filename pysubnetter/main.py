""" the program's main entry-point in this module """

from ipaddress import IPv4Address, IPv4Network
from ipv4subnetmask import IPv4SubnetMask
import ipv4networkclasses as ipv4help
ip1 = IPv4SubnetMask(IPv4Address("255.255.0.0"))

print(ip1.mask)
print(ip1.prefix)
print(ip1.decimal)
print(ip1.binary)
print(ipv4help.max_hosts(IPv4Network("192.168.0.0/17")))