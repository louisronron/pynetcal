"""Tests for the ipv6pynetcal.py module """

import pytest
from ipaddress import IPv6Address, IPv6Network
import pynetcal.ipv6pynetcal as pynetcal



# Setup my fixture functions

@pytest.fixture
def ipv6_addresses_valid():
    """A random list of IPv6 addresses
    in their hex, decimal, and binary forms
    """
    return [
        {
            'hex': 'e83c:e7da:abe0:9d77:a805:3560:bec8:9d77',
            'dec': '59452:59354:44000:40311:43013:13664:48840:40311',
            'bin': '1110100000111100:1110011111011010:1010101111100000:1001110101110111:1010100000000101:0011010101100000:1011111011001000:1001110101110111'
        },

        {
            'hex': 'c7ad:9144:9e00:6ee8:413a:5878:ae17:1657',
            'dec': '51117:37188:40448:28392:16698:22648:44567:5719',
            'bin': '1100011110101101:1001000101000100:1001111000000000:0110111011101000:0100000100111010:0101100001111000:1010111000010111:0001011001010111'
        },
    ]



@pytest.fixture
def ipv6_networks_valid():
    """A random list of IPv6 network addresses
    along with their masks.
    """
    return [
        "ff0a:165a::/80",
        "::1080:f000/125",
        "fac1:cac3:90a5::1000:0000/100",
        "::/70",
        "ff0a:165a::0/100"
    ]






@pytest.fixture
def ipv6_networks_flsm():
    """A random list of IPv6 network addresses
    along with their masks, hosts, subnets, priorityHosts.
    """
    return [
        {"net": "ff0a:165a::/80", "hosts": 900, "subnets": 5, "priorityHosts": False, 
        "expected_subnets": [
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:0000:0000:0000/83"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:2000:0000:0000/83"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:4000:0000:0000/83"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:6000:0000:0000/83"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:8000:0000:0000/83"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:a000:0000:0000/83"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:c000:0000:0000/83"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:e000:0000:0000/83"),
        ]},

        {"net": "ff0a:165a::/80", "hosts": 900, "subnets": 2, "priorityHosts": False, 
        "expected_subnets": [
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:0000:0000:0000/81"),
            pynetcal.PyNIPv6Network("ff0a:165a::8000:0000:0000/81"),
        ]}
    ]






@pytest.fixture
def ipv6_networks_vlsm():
    """A random list of IPv6 network addresses
    along with their masks, hosts, subnets, priorityHosts.
    """
    return [
        {"net": "ff0a:165a::/80", "hosts": [70368744177664,
            70368744177664,70368744177664,70368744177664], 
        "expected_subnets": [
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:0000:0000:0000/82"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:4000:0000:0000/82"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:8000:0000:0000/82"),
            pynetcal.PyNIPv6Network("ff0a:165a:0000:0000:0000:c000:0000:0000/82"),
        ]}
    ]










def test_is_hex(ipv6_addresses_valid):
    """Tests for is_hex() function"""
    addresses = ipv6_addresses_valid
    for address in addresses:
        hexaddr = address["hex"]
        assert pynetcal.is_hex(hexaddr) == True






def test_is_bin(ipv6_addresses_valid):
    """Tests for is_bin() function"""
    addresses = ipv6_addresses_valid
    for address in addresses:
        binaddr = address["bin"]
        assert pynetcal.is_bin(binaddr) == True







def test_bin_to_hex(ipv6_addresses_valid):
    """Tests for bin_to_hex() function"""
    addresses = ipv6_addresses_valid
    for address in addresses:
        binaddr = address["bin"]
        hexaddr = address["hex"]
        result = pynetcal.bin_to_hex(binaddr)
        assert result == hexaddr 







def test_hex_to_bin(ipv6_addresses_valid):
    """Tests for hex_to_bin() function"""
    addresses = ipv6_addresses_valid
    for address in addresses:
        binaddr = address["bin"]
        hexaddr = address["hex"]
        result = pynetcal.hex_to_bin(hexaddr)
        assert result == binaddr 




def test_dec_to_hex(ipv6_addresses_valid):
    """Tests for dec_to_hex() function"""
    addresses = ipv6_addresses_valid
    for address in addresses:
        decaddr = address["dec"]
        hexaddr = address["hex"]
        result = pynetcal.dec_to_hex(decaddr)
        assert result == hexaddr 





def test_hex_to_dec(ipv6_addresses_valid):
    """Tests for hex_to_dec() function"""
    addresses = ipv6_addresses_valid
    for address in addresses:
        decaddr = address["dec"]
        hexaddr = address["hex"]
        result = pynetcal.hex_to_dec(hexaddr)
        assert result == decaddr 







# Tests for the PyNIPv6Address class ===================





def test_pynipv6address___init__(ipv6_addresses_valid):
    """Tests for the __init__() function"""
    for address in ipv6_addresses_valid:
        ipv6address = pynetcal.PyNIPv6Address(address["hex"])
        assert ipv6address.hexadecimal == address["hex"]
        assert ipv6address.binary == address["bin"]
        assert ipv6address.decimal == address["dec"]






# Tests for the PyNIPv6Network class ===================




def test_pynipv6network___init__(ipv6_networks_valid):
    """Tests for the __init__() function"""
    for netaddress in ipv6_networks_valid:
        # create a network object.
        pynipv6network = pynetcal.PyNIPv6Network(netaddress)
        # calculate the expected results.
        expected_network = IPv6Network(netaddress)
        expected_network_address = pynetcal.PyNIPv6Address(
            IPv6Network(netaddress).network_address)
        expected_hostmask = pynetcal.PyNIPv6Address(
            IPv6Network(netaddress).hostmask.exploded)
        expected_netmask = pynetcal.PyNIPv6Address(
            IPv6Network(netaddress).netmask.exploded)
        expected_hosts = IPv6Network(netaddress).num_addresses
        expected_hostmin = pynetcal.PyNIPv6Address(
            IPv6Network(netaddress).network_address)
        expected_hostmax = pynetcal.PyNIPv6Address(
            IPv6Network(netaddress).network_address + \
                IPv6Network(netaddress).num_addresses - 1)
        # perform assertion.
        assert pynipv6network.pn_network == expected_network
        assert pynipv6network.pn_network_address == expected_network_address
        assert pynipv6network.pn_hostmask == expected_hostmask
        assert pynipv6network.pn_netmask == expected_netmask
        assert pynipv6network.pn_hosts == expected_hosts
        assert pynipv6network.pn_hostmin == expected_hostmin
        assert pynipv6network.pn_hostmax == expected_hostmax





def test_subnets_flsm(ipv6_networks_flsm):
    """Tests for subnets_flsm() function"""
    for network in ipv6_networks_flsm:
        expected_result = network["expected_subnets"]
        netaddr = network["net"]
        hosts = network["hosts"]
        subnets = network["subnets"]
        priority = network["priorityHosts"]
        pynipv6net = pynetcal.PyNIPv6Network(netaddr)
        result_gen = pynipv6net.subnets_flsm(hosts, subnets, priority)
        i = 0
        for result in result_gen:
            assert result == expected_result[i]
            i = i + 1









def test_subnets_vlsm(ipv6_networks_vlsm):
    """Tests for subnets_vlsm() function"""
    for network in ipv6_networks_vlsm:
        expected_result = network["expected_subnets"]
        netaddr = network["net"]
        hosts = network["hosts"]
        pynipv6net = pynetcal.PyNIPv6Network(netaddr)
        result = pynipv6net.subnets_vlsm(hosts)
        assert result == expected_result





@pytest.mark.parametrize("net, hosts, subnets, prioritizeHosts, expected_result",
[
    [pynetcal.PyNIPv6Network("ff0a::/119"), 100, 2, False, 2],
    [pynetcal.PyNIPv6Network("ff0a::/119"), 100, 3, False, 4],
    [pynetcal.PyNIPv6Network("ff0a::/119"), 100901, 63, False, 64],
    [pynetcal.PyNIPv6Network("ff0a::/119"), 16, 98, True, 16],
    [pynetcal.PyNIPv6Network("ff0a::/119"), 7, 105, True, 32],
])
def test_num_of_subnets(net, hosts, subnets, prioritizeHosts, expected_result):
    """Tests num_of_subnets() method of PyNIPv6Network"""
    assert net.num_of_subnets(hosts, subnets, prioritizeHosts) == expected_result