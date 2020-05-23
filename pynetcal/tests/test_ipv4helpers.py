""" All tests for ipv4helpers.py 
module in here.
"""


import pytest
from ipaddress import IPv4Network, IPv4Address
import pynetcal.ipv4helpers as ipv4nets



# Tests for ipv4helpers.is_class_A()

@pytest.mark.parametrize("net, isClassA",
[
    
    (IPv4Network("14.0.1.8/30"), True),
    (IPv4Network("14.0.1.20/30"), True),
    (IPv4Network("14.15.0.48/30"), True),
    (IPv4Network("14.15.0.72/30"), True),
    (IPv4Network("14.15.0.80/30"), True),

    (IPv4Address("10.0.0.100"), True),
    (IPv4Address("10.20.1.25"), True),
    (IPv4Address("1.0.25.4"), True),
    (IPv4Address("100.89.1.130"), True),
    (IPv4Address("124.124.23.13"), True),

    (IPv4Address("150.0.0.100"), False),
    (IPv4Address("134.4.2.102"), False),
    (IPv4Address("127.45.4.27"), False),
    (IPv4Address("246.1.16.16"), False),
    (IPv4Address("163.13.13.11"), False),

    (IPv4Network("192.168.0.0/24"), False),
    (IPv4Network("192.168.0.32/28"), False),
    (IPv4Network("192.168.0.48/28"), False),
    (IPv4Network("192.168.15.0/24"), False),
    (IPv4Network("192.168.15.8/30"), False)
])
def test_is_class_a(net, isClassA):
    """Tests that that an IPv4Network
    is of type Class A.
    """
    isValidClassA = ipv4nets.is_class_A(net)
    assert isValidClassA == isClassA






# Tests for ipv4helpers.is_class_B()

@pytest.mark.parametrize("net, isClassB",
[
    (IPv4Network("128.1.80.0/20"), True),
    (IPv4Network("128.1.128.0/20"), True),
    (IPv4Network("170.1.0.0/17"), True),
    (IPv4Network("170.1.128.0/17"), True),

    (IPv4Address("164.13.170.138"), True),
    (IPv4Address("178.153.147.194"), True),
    (IPv4Address("188.62.18.172"), True),
    (IPv4Address("173.164.116.187"), True),
    (IPv4Address("173.145.115.21"), True),

    (IPv4Address("39.24.223.203"), False),
    (IPv4Address("26.25.11.227"), False),
    (IPv4Address("89.108.32.44"), False),
    (IPv4Address("120.9.159.251"), False),
    (IPv4Address("14.81.239.24"), False),

    (IPv4Network("14.15.0.64/30"), False),
    (IPv4Network("14.15.0.76/30"), False),
    (IPv4Network("14.15.0.40/30"), False),
    (IPv4Network("14.12.0.28/30"), False),
])
def test_is_class_b(net, isClassB):
    """Tests that that an IPv4Network
    is of type Class B.
    """
    isValidClassB = ipv4nets.is_class_B(net)
    assert isValidClassB == isClassB






# Tests for ipv4helpers.is_class_C()

@pytest.mark.parametrize("net, isClassC",
[
    (IPv4Address("192.168.1.1"), True),
    (IPv4Address("192.168.10.11"), True),
    (IPv4Address("199.17.16.11"), True),
    (IPv4Address("200.100.10.13"), True),

    (IPv4Network("192.168.1.0/24"), True),
    (IPv4Network("192.168.3.0/24"), True),
    (IPv4Network("192.168.5.0/24"), True),
    (IPv4Network("192.168.20.64/26"), True),
    (IPv4Network("192.168.20.192/26"), True),

    (IPv4Address("164.13.170.138"), False),
    (IPv4Address("178.153.147.194"), False),
    (IPv4Address("188.62.18.172"), False),
    (IPv4Address("173.164.116.187"), False),
    (IPv4Address("173.145.115.21"), False),

    (IPv4Network("128.1.80.0/20"), False),
    (IPv4Network("128.1.128.0/20"), False),
    (IPv4Network("170.1.0.0/17"), False),
    (IPv4Network("170.1.128.0/17"), False),
    (IPv4Network("14.15.0.64/30"), False),
    (IPv4Network("14.15.0.76/30"), False),
    (IPv4Network("14.15.0.40/30"), False),
    (IPv4Network("14.12.0.28/30"), False)
])
def test_is_class_c(net, isClassC):
    """Tests that that an IPv4Network
    is of type Class C.
    """
    isValidClassC = ipv4nets.is_class_C(net)
    assert isValidClassC == isClassC





# Tests for ipv4helpers.max_hosts()
@pytest.mark.parametrize("ipv4network, maxHosts",
[
    (IPv4Network("10.0.0.0/24"),254),
    (IPv4Network("192.168.0.0/255.255.0.0"),65534),
    (IPv4Network("198.174.1.0/255.255.255.128"),126),
    (IPv4Network("200.168.70.0/255.255.255.240"),14),
    (IPv4Network("173.100.0.0/15"),131070),
])
def test_max_hosts(ipv4network, maxHosts):
    """Tests that an IPv4Network has
    the specified number of maximum
    hosts.
    """
    calculatedMaxHosts = ipv4nets.max_hosts(
        ipv4network)
    assert calculatedMaxHosts == maxHosts





# Tests for ipv4helpers.max_subnents()
@pytest.mark.parametrize("ipv4network, newPrefix, maxSubnets",
[
    (IPv4Network("192.0.0.0/255.0.0.0"),15,128),
    (IPv4Network("192.168.20.0/24"),26,4),
    (IPv4Network("172.168.0.0/16"),20,16),
    (IPv4Network("192.168.0.0/24"),24,1),
    (IPv4Network("192.168.0.0/24"),25,2),
])
def test_max_subnets(ipv4network, newPrefix, maxSubnets):
    """Tests that a specific IPv4Network,
    when given a new prefix, can have a
    specified number of maximum subnets.
    """
    calculatedMaxSubnets = ipv4nets.max_subnets(
        ipv4network, newPrefix)
    assert calculatedMaxSubnets == maxSubnets



@pytest.mark.parametrize("net_addr,hosts,subnets,prioritizeHosts,\
                        containingMask",
    [
        [IPv4Network("192.168.1.0/24"), 26, 4, True, 
        {"netbits": 27, "mask": IPv4Address("255.255.255.224"), 
        "subnets": 8, "hosts": 30}],

        [IPv4Network("10.0.0.0/255.0.0.0"), 50, 8, False, 
        {"netbits": 11, "mask": IPv4Address("255.224.0.0"), 
        "subnets": 8, "hosts": 2097150}],

        [IPv4Network("192.168.0.0/24"), 26, 4, True, 
        {"netbits": 27, "mask": IPv4Address("255.255.255.224"), 
        "subnets": 8, "hosts": 30}],

        [IPv4Network("10.0.0.0/255.0.0.0"), 100, 35, False, 
        {"netbits": 14, "mask": IPv4Address("255.252.0.0"), 
        "subnets": 64, "hosts": 262142}],
    ]
)
def test_containing_mask(net_addr, hosts, subnets, 
                        prioritizeHosts, containingMask):
    """Tests the optimum subnet
    mask that can contain a certain
    number of hosts and subnets.
    """
    containing_masks = ipv4nets.containing_mask(net_addr, hosts, subnets, 
        prioritizeHosts)
    assert containing_masks == containingMask
    

