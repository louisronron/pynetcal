"""Tests for the ipv4pynetcal.py module """

import pytest
from ipaddress import IPv4Address, IPv4Network
import pynetcal.ipv4pynetcal as pynetcal


# Tests for is_bin() function
@pytest.mark.parametrize("address,expected_result",
[
    ["10101101.10101111.10000000.00000000", True],
    ["10000000.1010.1000110.10101010", True],
    ["111110.100010.11110000.011", True],

    ["10000007.010101.100010.1001", False],
    ["11111111.11110101.1010101011.10100000", False],
    ["11111111.11110101.10101010", False],
    ["11111111.11110101..10101010", False],
]
)
def test_is_bin(address, expected_result):
    result = pynetcal.is_bin(address)
    assert result == expected_result






# Tests for is_hex() function
@pytest.mark.parametrize("address,expected_result",
[
    ["fa.1f.ac.00", True],
    ["fa.cc.10.10", True],
    ["01.01.01.10", True],
    ["1c.1c.ac.ac", True],

    ["0.1a.0.0", False],
    ["12.a.0a.c", False],
    ["90.ff.0f.5", False],
    ["67.14.111.0a", False]

]
)
def test_is_hex(address, expected_result):
    result = pynetcal.is_hex(address)
    assert result == expected_result





# Tests for is_dec() function
@pytest.mark.parametrize("address,expected_result",
[
    ["192.178.1.167", True],
    ["253.1.0.1", True],
    ["255.255.255.0", True], 
    ["127.0.0.1", True],
    ["0.0.0.0", True],

    ["108.1006.0.0", False], 
    ["109.10.10.0a", False],
    ["106.10.1.ff", False],
    ["1.1.255.256", False],
    ["256.1.1.1", False],
    ["192.168.700.6", False]
]
)
def test_is_dec(address, expected_result):
    result = pynetcal.is_dec(address)
    assert result == expected_result





# Tests for dec_to_bin() function
@pytest.mark.parametrize("address,expected_result",
[
    ["255.255.255.0", "11111111.11111111.11111111.00000000"],
    ["255.0.255.0", "11111111.00000000.11111111.00000000"],
    ["16.1.1.255", "00010000.00000001.00000001.11111111"],
    ["209.153.1.56", "11010001.10011001.00000001.00111000"],
]
)
def test_dec_to_bin(address, expected_result):
    result = pynetcal.dec_to_bin(address)
    assert result == expected_result







# Tests for dec_to_hex() function
@pytest.mark.parametrize("address,expected_result",
[
    ["255.255.255.0", "ff.ff.ff.00"],
    ["192.187.255.90", "c0.bb.ff.5a"],
    ["148.170.180.190", "94.aa.b4.be"],
    ["69.69.69.69", "45.45.45.45"],
    ["127.0.0.1", "7f.00.00.01"],
]
)
def test_dec_to_hex(address, expected_result):
    result = pynetcal.dec_to_hex(address)
    assert result == expected_result








# Tests for bin_to_dec() function
@pytest.mark.parametrize("address,expected_result",
[
    ["11111111.11111111.11111111.00000000", "255.255.255.0"],
    ["11111111.00000000.11111111.00000000", "255.0.255.0"],
    ["00010000.00000001.00000001.11111111", "16.1.1.255"],
    ["11010001.10011001.00000001.00111000", "209.153.1.56"],
]
)
def test_bin_to_dec(address, expected_result):
    result = pynetcal.bin_to_dec(address)
    assert result == expected_result





# Tests for hex_to_dec() function
@pytest.mark.parametrize("address,expected_result",
[
    ["ff.ff.ff.00", "255.255.255.0"],
    ["c0.bb.ff.5a", "192.187.255.90"],
    ["94.aa.b4.be", "148.170.180.190"],
    ["45.45.45.45", "69.69.69.69"],
    ["7f.00.00.01", "127.0.0.1"],

    
]
)
def test_hex_to_dec(address, expected_result):
    result = pynetcal.hex_to_dec(address)
    assert result == expected_result







# Tests for is_class_A function
@pytest.mark.parametrize("address,expected_result",
[
    [IPv4Address("10.1.1.15"), True],
    [IPv4Address("38.217.4.188"), True],
    [IPv4Address("15.35.164.249"), True],
    [IPv4Address("93.111.92.144"), True],
    [IPv4Address("114.119.185.154"), True],
    [IPv4Address("38.178.138.40"), True],
    [IPv4Address("2.94.136.169"), True],

    [IPv4Address("240.255.1.10"), False],
    [IPv4Address("249.160.95.209"), False],
    [IPv4Address("248.186.104.251"), False],
    [IPv4Address("249.185.204.100"), False],
    [IPv4Address("246.240.47.108"), False],
    [IPv4Address("244.196.71.250"), False],
    [IPv4Address("253.22.243.155"), False],

    [IPv4Address("190.127.8.90"), False],
    [IPv4Address("146.1.0.1"), False], 
    [IPv4Address("131.1.1.1"), False], 
    [IPv4Address("166.1.1.1"), False], 
    [IPv4Address("155.1.1.1"), False], 
    [IPv4Address("157.1.1.1"), False],


]
)
def test_is_class_A(address, expected_result):
    result = pynetcal.is_class_A(address)
    assert result == expected_result








# Tests for is_class_B function
@pytest.mark.parametrize("address,expected_result",
[
    [IPv4Address("190.127.8.90"), True],
    [IPv4Address("146.1.0.1"), True], 
    [IPv4Address("131.1.1.1"), True], 
    [IPv4Address("166.1.1.1"), True], 
    [IPv4Address("155.1.1.1"), True], 
    [IPv4Address("157.1.1.1"), True],
    [IPv4Address("179.1.1.1"), True],

    [IPv4Address("10.1.1.15"), False],
    [IPv4Address("38.217.4.188"), False],
    [IPv4Address("15.35.164.249"), False],
    [IPv4Address("93.111.92.144"), False],
    [IPv4Address("114.119.185.154"), False],
    [IPv4Address("38.178.138.40"), False],
    [IPv4Address("2.94.136.169"), False],

    [IPv4Address("240.255.1.10"), False],
    [IPv4Address("249.160.95.209"), False],
    [IPv4Address("248.186.104.251"), False],
    [IPv4Address("249.185.204.100"), False],
    [IPv4Address("246.240.47.108"), False],
    [IPv4Address("244.196.71.250"), False],
    [IPv4Address("253.22.243.155"), False],


]
)
def test_is_class_B(address, expected_result):
    result = pynetcal.is_class_B(address)
    assert result == expected_result








# Tests for is_class_C function
@pytest.mark.parametrize("address,expected_result",
[
    [IPv4Address("192.168.100.67"), True],
    [IPv4Address("213.253.156.85"), True],
    [IPv4Address("199.216.167.70"), True],
    [IPv4Address("211.243.214.185"), True], 
    [IPv4Address("214.74.231.247"), True], 
    [IPv4Address("220.41.240.244"), True], 
    [IPv4Address("196.138.106.119"), True],

    [IPv4Address("190.127.8.90"), False],
    [IPv4Address("146.1.0.1"), False], 
    [IPv4Address("131.1.1.1"), False], 
    [IPv4Address("166.1.1.1"), False], 
    [IPv4Address("155.1.1.1"), False], 
    [IPv4Address("157.1.1.1"), False],
    [IPv4Address("179.1.1.1"), False],

    [IPv4Address("10.1.1.15"), False],
    [IPv4Address("38.217.4.188"), False],
    [IPv4Address("15.35.164.249"), False],
    [IPv4Address("93.111.92.144"), False],
    [IPv4Address("114.119.185.154"), False],
    [IPv4Address("38.178.138.40"), False],
    [IPv4Address("2.94.136.169"), False],

]
)
def test_is_class_C(address, expected_result):
    result = pynetcal.is_class_C(address)
    assert result == expected_result







# Tests for is_class_D function
@pytest.mark.parametrize("address,expected_result",
[
    [IPv4Address("225.239.180.176"), True],
    [IPv4Address("238.133.56.174"), True], 
    [IPv4Address("236.8.16.193"), True],
    [IPv4Address("238.48.203.103"), True],
    [IPv4Address("234.6.49.219"), True],
    [IPv4Address("224.55.94.89"), True],

    [IPv4Address("190.127.8.90"), False],
    [IPv4Address("146.1.0.1"), False], 
    [IPv4Address("131.1.1.1"), False], 
    [IPv4Address("166.1.1.1"), False], 
    [IPv4Address("155.1.1.1"), False], 
    [IPv4Address("157.1.1.1"), False],
    [IPv4Address("179.1.1.1"), False],

    [IPv4Address("10.1.1.15"), False],
    [IPv4Address("38.217.4.188"), False],
    [IPv4Address("15.35.164.249"), False],
    [IPv4Address("93.111.92.144"), False],
    [IPv4Address("114.119.185.154"), False],
    [IPv4Address("38.178.138.40"), False],
    [IPv4Address("2.94.136.169"), False],

]
)
def test_is_class_D(address, expected_result):
    result = pynetcal.is_class_D(address)
    assert result == expected_result






# Tests for is_class_E function
@pytest.mark.parametrize("address,expected_result",
[
    [IPv4Address("240.255.1.10"), True],
    [IPv4Address("249.160.95.209"), True],
    [IPv4Address("248.186.104.251"), True],
    [IPv4Address("249.185.204.100"), True],
    [IPv4Address("246.240.47.108"), True],
    [IPv4Address("244.196.71.250"), True],
    [IPv4Address("253.22.243.155"), True],

    [IPv4Address("10.1.1.15"), False],
    [IPv4Address("38.217.4.188"), False],
    [IPv4Address("15.35.164.249"), False],
    [IPv4Address("93.111.92.144"), False],
    [IPv4Address("114.119.185.154"), False],
    [IPv4Address("38.178.138.40"), False],
    [IPv4Address("2.94.136.169"), False],
    [IPv4Address("225.239.180.176"), False],
    [IPv4Address("238.133.56.174"), False], 
    [IPv4Address("236.8.16.193"), False],
    [IPv4Address("238.48.203.103"), False],
    [IPv4Address("234.6.49.219"), False],
    [IPv4Address("224.55.94.89"), False],


]
)
def test_is_class_E(address, expected_result):
    result = pynetcal.is_class_E(address)
    assert result == expected_result


















# Tests for the PyNIPv4Address class ===================


# Tests for __init__() of PyNIPv4Address
@pytest.mark.parametrize("address, deci, hexa, bina, isClassA, isClassB, isClassC, isClassD, isClassE",
    [
        ["192.168.1.0", "192.168.1.0", "c0.a8.01.00", "11000000.10101000.00000001.00000000", False, False, True, False, False],
    ]
)
def test_pynipv4address___init__valid_args(address, deci, hexa, bina, isClassA, isClassB, isClassC, isClassD, isClassE):
    address = pynetcal.PyNIPv4Address(address)
    assert address.pn_decimal == deci
    assert address.pn_hexadecimal == hexa
    assert address.pn_binary == bina
    assert address.pn_is_class_a == isClassA
    assert address.pn_is_class_b == isClassB
    assert address.pn_is_class_c == isClassC
    assert address.pn_is_class_d == isClassD
    assert address.pn_is_class_e == isClassE











# Tests for the PyNIPv4Network class ===================




# Tests for __init__() of PyNIPv4Network
@pytest.mark.parametrize("network, ipv4network, net_addr, hostmask, netmask, hosts, hostmin, hostmax",
    [
        ["192.168.1.0/24", IPv4Network("192.168.1.0/24"), pynetcal.PyNIPv4Address("192.168.1.0"), pynetcal.PyNIPv4Address("0.0.0.255"), pynetcal.PyNIPv4Address("255.255.255.0"), 254, pynetcal.PyNIPv4Address("192.168.1.1"), pynetcal.PyNIPv4Address("192.168.1.254")],
    ]
)
def test_pynipv4network___init__valid_args(network, ipv4network, net_addr, hostmask, netmask, hosts, hostmin, hostmax):
    network = pynetcal.PyNIPv4Network(network)
    assert network.pn_network == ipv4network
    assert network.pn_network_address == net_addr
    assert network.pn_hostmask == hostmask
    assert network.pn_netmask == netmask
    assert network.pn_hosts == hosts
    assert network.pn_hostmin == hostmin
    assert network.pn_hostmax == hostmax




# Tests for subnets_flsm() of PyNIPv4Network
@pytest.mark.parametrize("network, hosts, subnets, prioritizeHosts, expectedResult",
    [
        [pynetcal.PyNIPv4Network("192.168.1.0/24"), 64, 5, True,
            [
                pynetcal.PyNIPv4Network("192.168.1.0/25"),
                pynetcal.PyNIPv4Network("192.168.1.128/25"),
            ]
        ],
    ]
)
def test_pynipv4network_subnets_flsm(network, hosts, subnets, prioritizeHosts, expectedResult):
    result = network.subnets_flsm(hosts, subnets, prioritizeHosts)
    assert result == expectedResult







# Tests for subnets_vlsm() of PyNIPv4Network
@pytest.mark.parametrize("network, hosts, expectedResult",
    [
        [pynetcal.PyNIPv4Network("192.168.1.0/24"), [100, 10, 23, 40],
            [
                pynetcal.PyNIPv4Network("192.168.1.0/25"),
                pynetcal.PyNIPv4Network("192.168.1.128/26"),
                pynetcal.PyNIPv4Network("192.168.1.192/27"),
                pynetcal.PyNIPv4Network("192.168.1.224/28"),
            ]
        ],
    ]
)
def test_pynipv4network_subnets_vlsm(network, hosts, expectedResult):
    result = network.subnets_vlsm(hosts)
    assert result == expectedResult
