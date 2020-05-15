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









# Tests for the calculate_prefix() method

@pytest.mark.parametrize("mask_addr,prefix",
    [(IPv4Address("255.0.0.0"),"8"), 
    (IPv4Address("255.255.0.0"),"16"),
    (IPv4Address("255.255.255.0"),"24"),
    (IPv4Address("255.255.255.255"),"32"),
    (IPv4Address("255.255.240.0"),"20"),
    (IPv4Address("255.192.0.0"),"10"),
    (IPv4Address("255.255.255.248"),"29")])
def test_calculate_prefix(mask_addr,prefix):
    """Tests IPv4SubnetMask.calculate_prefix() 
    with args.
    """
    ipSubMask = IPv4SubnetMask(mask_addr)
    calculated_prefix = ipSubMask.calculate_prefix(
        str(mask_addr))
    assert calculated_prefix == prefix







# Tests for the calculate_decimal() method

@pytest.mark.parametrize("mask_addr,decimal",
    [(IPv4Address("255.0.0.0"),"255.0.0.0"), 
    (IPv4Address("255.255.0.0"),"255.255.0.0"),
    (IPv4Address("255.255.255.0"),"255.255.255.0"),
    (IPv4Address("255.255.255.255"),"255.255.255.255"),
    (IPv4Address("255.255.240.0"),"255.255.240.0"),
    (IPv4Address("255.192.0.0"),"255.192.0.0"),
    (IPv4Address("255.255.255.248"),"255.255.255.248")])
def test_calculate_decimal(mask_addr,decimal):
    """Tests IPv4SubnetMask.calculate_decimal() 
    with args.
    """
    ipSubMask = IPv4SubnetMask(mask_addr)
    calculated_dec = ipSubMask.calculate_decimal(
        str(mask_addr))
    assert calculated_dec == decimal








# Tests for the calculate_binary() method

@pytest.mark.parametrize("mask_addr,binary",
    [(IPv4Address("255.0.0.0"),
    "11111111.00000000.00000000.00000000"), 
    (IPv4Address("255.255.0.0"),
    "11111111.11111111.00000000.00000000"),
    (IPv4Address("255.255.255.0"),
    "11111111.11111111.11111111.00000000"),
    (IPv4Address("255.255.255.255"),
    "11111111.11111111.11111111.11111111"),
    (IPv4Address("255.255.240.0"),
    "11111111.11111111.11110000.00000000"),
    (IPv4Address("255.192.0.0"),
    "11111111.11000000.00000000.00000000"),
    (IPv4Address("255.255.255.248"),
    "11111111.11111111.11111111.11111000")])
def test_calculate_binary(mask_addr,binary):
    """Tests IPv4SubnetMask.calculate_binary() 
    with args.
    """
    ipSubMask = IPv4SubnetMask(mask_addr)
    calculated_bin = ipSubMask.calculate_binary(
        str(mask_addr))
    assert calculated_bin == binary