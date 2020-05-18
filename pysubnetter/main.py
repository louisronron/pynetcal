""" the program's main entry-point in this module """

from ipaddress import IPv4Address, IPv4Network
from ipv4subnetmask import IPv4SubnetMask
from ipv4subnet import IPv4Subnet
from ipv4subnetlist import IPv4SubnetList
import ipv4networkclasses as ipv4help


subnets = IPv4SubnetList()
# subnets.append((IPv4Subnet(0, IPv4Network("192.168.2.0/26")),62))
# subnets.append((IPv4Subnet(1, IPv4Network("192.168.2.64/26")),62))
# subnets.append((IPv4Subnet(2, IPv4Network("192.168.2.128/26")),62))
# subnets.append((IPv4Subnet(3, IPv4Network("192.168.2.0/26")),62))
# subnets.append((IPv4Subnet(4, IPv4Network("192.168.2.64/26")),254))
subnets.append((IPv4Subnet(0, IPv4Network("192.168.2.0/26"))))
subnets.append((IPv4Subnet(1, IPv4Network("192.168.2.64/26"))))
subnets.append((IPv4Subnet(2, IPv4Network("192.168.2.128/26"))))
subnets.append((IPv4Subnet(3, IPv4Network("192.168.2.0/26"))))
subnets.append((IPv4Subnet(4, IPv4Network("192.168.2.64/26"))))

print(subnets)