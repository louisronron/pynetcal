"""All tests for ipv4subnetmask.py module in here."""

import pytest
from ipaddress import IPv4Address
from pynetcal.ipv4subnetmask import IPv4SubnetMask


# Tests for __init__ method

@pytest.mark.parametrize("mask,prefix,decimal,binary",
    [(
        IPv4Address("255.255.255.0"), "24", 
            "255.255.255.0",
            "11111111.11111111.11111111.00000000"),
        (IPv4Address("255.248.0.0"), "13", 
            "255.248.0.0",
            "11111111.11111000.00000000.00000000"),
        (IPv4Address("255.255.240.0"), "20", 
            "255.255.240.0",
            "11111111.11111111.11110000.00000000"),

        (IPv4Address("255.255.255.0"), "24",
            "255.255.255.0",
            "11111111.11111111.11111111.00000000"),

        (IPv4Address("255.255.255.128"), "25",
            "255.255.255.128",
            "11111111.11111111.11111111.10000000"),

        (IPv4Address("255.255.255.252"), "30",
            "255.255.255.252",
            "11111111.11111111.11111111.11111100")
    ])
def test_init_with_valid_args(mask, prefix, decimal, binary):
    ''' Tests IPv4SubnetMask initialization 
    with valid args.
    '''
    ip1 = IPv4SubnetMask(mask)
    assert ip1.mask == mask
    assert ip1.prefix == prefix
    assert ip1.decimal == decimal
    assert ip1.binary == binary





@pytest.mark.parametrize("mask",
    [15, 
    "test", 
    True, 
    None, 
    list(), 
    {'test': 67},
    IPv4Address("192.168.0.0"), 
    IPv4Address("192.168.100.5"),
    IPv4Address("10.10.1.1")])
def test_init_with_invalid_args(mask):
    ''' Tests IPv4SubnetMask initialization 
    with invalid args.
    '''
    with pytest.raises(TypeError):
        IPv4SubnetMask(mask)