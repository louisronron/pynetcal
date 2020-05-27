""" All tests for ipv4subnet.py 
module in here.
"""

import pytest
from ipaddress import IPv4Address, IPv4Network
from pynetcal.ipv4.ipv4subnet import IPv4Subnet
from pynetcal.ipv4.ipv4subnetmask import IPv4SubnetMask


# Test for IPv4Subnet.__init__()

@pytest.mark.parametrize(
    "network,subnet_id,mask,\
    host_min,host_max,broadcast,hosts",
    [
        (IPv4Network("192.168.0.0/16"),
        0,
        IPv4SubnetMask(IPv4Address("255.255.0.0")),
        IPv4Address("192.168.0.1"),
        IPv4Address("192.168.255.254"),
        IPv4Address("192.168.255.255"),
        65534),

        (IPv4Network("192.168.1.0/24"),
        1,
        IPv4SubnetMask(IPv4Address("255.255.255.0")),
        IPv4Address("192.168.1.1"),
        IPv4Address("192.168.1.254"),
        IPv4Address("192.168.1.255"),
        254),

        (IPv4Network("192.168.11.0/24"),
        2,
        IPv4SubnetMask(IPv4Address("255.255.255.0")),
        IPv4Address("192.168.11.1"),
        IPv4Address("192.168.11.254"),
        IPv4Address("192.168.11.255"),
        254),

        (IPv4Network("10.0.0.0/8"),
        2,
        IPv4SubnetMask(IPv4Address("255.0.0.0")),
        IPv4Address("10.0.0.1"),
        IPv4Address("10.255.255.254"),
        IPv4Address("10.255.255.255"),
        16777214),
    ]
)
def test_IPv4Subnet__init__withargs(
    network, subnet_id, mask, host_min,
    host_max, broadcast, hosts
    ):
    """Tests the IPv4Subnet.__init__()
    function, with valid args
    """
    ipv4subnet = IPv4Subnet(subnet_id,
        network)
    assert ipv4subnet.subnet_id == subnet_id
    assert ipv4subnet.network == network
    assert ipv4subnet.mask == mask
    assert ipv4subnet.host_min == host_min
    assert ipv4subnet.host_max == host_max
    assert ipv4subnet.broadcast == broadcast
    assert ipv4subnet.hosts == hosts




@pytest.mark.parametrize("subnet_id, mask",
    [(0,15), 
    ("id","test"), 
    (13,True), 
    ("l",None), 
    (12,list()), 
    (5,{'test': 67}),
    (list(),IPv4Address("192.168.0.0")), 
    ("test",IPv4Address("255.255.255.0")),
    (15,IPv4Address("10.10.1.1"))])
def test_IPv4Subnet___validate_args(subnet_id, mask):
    """ Tests IPv4SubnetMask initialization 
    with invalid args.
    """
    with pytest.raises(TypeError):
        IPv4Subnet(subnet_id, mask)


@pytest.mark.parametrize("network1, network2, isSubnet",
    [
        [IPv4Network("192.168.0.0/24"), IPv4Network("192.168.0.0/26"), True],
        [IPv4Network("192.168.0.0/24"), IPv4Network("192.168.0.0/27"), True],
        [IPv4Network("192.168.0.0/24"), IPv4Network("192.168.0.0/28"), True],
        [IPv4Network("192.168.0.0/24"), IPv4Network("192.168.0.0/29"), True],
        [IPv4Network("192.168.0.0/24"), IPv4Network("192.168.0.0/16"), False],
    ]
)

def test_IPv4Subnet_subnet_of(network1, network2, isSubnet):
    """Tests IPv4Subnet.subnet_of()
    method with valid arguments.
    """
    subnet1 = IPv4Subnet(0, network1)
    subnet2 = IPv4Subnet(1, network2)
    assert subnet2.subnet_of(subnet1) == isSubnet