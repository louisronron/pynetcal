""" All tests for ipv4subnetmask.py module in here."""


import pytest
from ipaddress import IPv4Address
from pysubnetter.ipv4subnetmask import IPv4SubnetMask



# Tests for __init__ method

@pytest.mark.parametrize("mask,addr_class,prefix,\
    decimal,binary, total_hosts, total_subnets",
    [(
        IPv4Address("255.255.255.0"), "", "24", 
            "255.255.255.0",
            "11111111.11111111.11111111.00000000", 
            254,0),
        (IPv4Address("255.248.0.0"), "", "13", 
            "255.248.0.0",
            "11111111.11111000.00000000.00000000",
            524286,32),
        (IPv4Address("255.255.240.0"), "", "20", 
            "255.255.240.0",
            "11111111.11111111.11110000.00000000",
            4094,4096),

        (IPv4Address("255.255.255.0"), "", "24",
            "255.255.255.0",
            "11111111.11111111.11111111.00000000",
            254,256),

        (IPv4Address("255.255.255.128"), "", "25",
            "255.255.255.128",
            "11111111.11111111.11111111.10000000",
            126,512),

        (IPv4Address("255.255.255.252"), "", "30",
            "255.255.255.252",
            "11111111.11111111.11111111.11111100",
            2,64)
    ])
def test_init_with_valid_args(mask, addr_class, prefix,
                       decimal, binary, total_hosts, 
                       total_subnets):
    ''' Tests IPv4SubnetMask initialization 
    with valid args.
    '''
    ip1 = IPv4SubnetMask(mask)
    assert ip1.mask == mask
    assert ip1.address_class == addr_class
    assert ip1.prefix == prefix
    assert ip1.decimal == decimal
    assert ip1.binary == binary
    #assert ip1.total_hosts == total_hosts
    #assert ip1.total_subnets == total_subnets





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