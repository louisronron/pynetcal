"""All tests for pysubnetter.py module and 
functionality all in here.
"""
import pytest
from ipaddress import IPv4Address, IPv4Network
from pysubnetter.pysubnetter import PySubnetter
from pysubnetter.ipv4subnetlist import IPv4SubnetList
from pysubnetter.ipv4subnet import IPv4Subnet



@pytest.mark.parametrize("network, hosts, subnets, \
    prioritize_host, expected_result",
    [
        [IPv4Network("192.168.1.0/24"),
        45,
        10,
        True,
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("192.168.1.0/26")),
            IPv4Subnet(1,IPv4Network("192.168.1.64/26")),
            IPv4Subnet(2,IPv4Network("192.168.1.128/26")),
            IPv4Subnet(3,IPv4Network("192.168.1.192/26"))),
        ],

        [IPv4Network("10.0.0.0/8"),
        10,
        4,
        False,
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("10.0.0.0/10")),
            IPv4Subnet(1,IPv4Network("10.64.0.0/10")),
            IPv4Subnet(2,IPv4Network("10.128.0.0/10")),
            IPv4Subnet(3,IPv4Network("10.192.0.0/10")))
        ]

    ]
)
def test_PySubnetter_ipv4_calculate_subnets_flsm_validargs(
        network, hosts, subnets, prioritize_host,
        expected_result
    ):
    """Tests PySubnetter.ipv4_calculate_subnets_flsm()
    function for FLSM subnetting mode
    """
    subnetter = PySubnetter()
    the_result = subnetter.ipv4_calculate_subnets_flsm(
        network, hosts, subnets, prioritize_host
    )
    assert the_result == expected_result









@pytest.mark.parametrize("network, hosts, expected_result",
    [
        [IPv4Network("192.168.1.0/24"),
        [50,20,10],
        IPv4SubnetList(
            IPv4Subnet(0,IPv4Network("192.168.1.0/26")),
            IPv4Subnet(1,IPv4Network("192.168.1.64/27")),
            IPv4Subnet(2,IPv4Network("192.168.1.96/28"))),
        ],
    ]
)
def test_PySubnetter_ipv4_calculate_subnets_vlsm(network, hosts, expected_result):
    """Tests PySubnetter.ipv4_calculate_subnets_vlsm()
    function for VLSM subnetting mode
    """
    subnetter = PySubnetter()
    the_result = subnetter.ipv4_calculate_subnets_vlsm(network, hosts)
    assert the_result == expected_result

