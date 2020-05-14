import pytest
from ipaddress import IPv4Address
from pysubnetter.IPv4SubnetMask import IPv4SubnetMask







# Tests for __init__ method

# def test_init_noargs():
#     ''' tests that initializing IPv4SubnetMask without 
#     args raises TypeError '''
#     assert pytest.raises(TypeError, IPv4SubnetMask())






@pytest.mark.parameterize("mask,addr_class,prefix,\
    decimal,binary, total_hosts, total_subnets",
    [
        (IPv4Address("255.255.255.0"), "",24,"255.255.255.0",
        "11111111.11111111.11111111.00000000",254,0),

        (IPv4Address("255.248.0.0"), "",13,"255.248.0.0",
        "11111111.11111000.00000000.00000000",524286,32),

        (IPv4Address("255.255.240.0"), "",20,"255.255.240.0",
        "11111111.11111000.00000000.00000000",4094,4096),

        (IPv4Address("255.255.255.0"), "",24,"255.255.255.0",
        "11111111.11111000.00000000.00000000",254,256),

        (IPv4Address("255.255.255.128"), "",25,"255.255.255.0",
        "11111111.11111000.00000000.00000000",126,512),

        (IPv4Address("255.255.255.252"), "",30,"255.255.255.252",
        "11111111.11111000.00000000.00000000",2,64)
    ])
def test_init_withargs(mask, addr_class, prefix,
    decimal, binary, total_hosts, total_subnets):
    ''' tests passing args to IPv4SubnetMask init '''
    ip1 = IPv4SubnetMask(mask)
    assert ip1.mask == mask
    assert ip1.address_class == addr_class
    assert ip1.prefix == prefix
    assert ip1.decimal == decimal
    assert ip1.binary == binary
    assert ip1.total_hosts == total_hosts
    assert ip1.total_subnets == total_subnets





# Test for the validate_args() method

@pytest.mark.parameterize("mask",
    [15, "test", True, None, list(), {'test': 67},
    IPv4Address("192.168.0.0"), IPv4Address("192.168.100.5"),
    IPv4Address("10.10.1.1")])
def test_fail_validate_args_with_args(mask):
    ''' tests that validate_args fails with 
    invalid arguments passed '''
    assert pytest.raises(TypeError, IPv4SubnetMask(mask))

@pytest.mark.parameterize("mask",
    [IPv4Address("255.0.0.0"), 
    IPv4Address("255.255.0.0"),
    IPv4Address("255.255.255.0"),
    IPv4Address("255.255.255.255"),
    IPv4Address("255.255.240.0"),
    IPv4Address("255.255.192.0"),
    IPv4Address("255.255.255.248")])
def test_success_validate_args_with_args(mask):
    ''' tests that validate_args succeeds with
    valid subnet masks passed as arguments '''
    assert isinstance(mask, IPv4Address) is True






# Tests for the calculate_prefix() method
@pytest.mark.parameterize("ipv4subnetmask,prefix",
    [(IPv4SubnetMask("255.0.0.0"),"8"), 
    (IPv4SubnetMask("255.255.0.0"),"16"),
    (IPv4SubnetMask("255.255.255.0"),"24"),
    (IPv4SubnetMask("255.255.255.255"),"32"),
    (IPv4SubnetMask("255.255.240.0"),"20"),
    (IPv4SubnetMask("255.192.0.0"),"10"),
    (IPv4SubnetMask("255.255.255.248"),"27")])
def test_calculate_prefix(ipv4subnetmask,prefix):
    assert ipv4subnetmask.calculate_prefix() == prefix





# Tests for the calculate_decimal() method
@pytest.mark.parameterize("ipv4subnetmask,decimal",
    [(IPv4SubnetMask("255.0.0.0"),"255.0.0.0"), 
    (IPv4SubnetMask("255.255.0.0"),"255.255.0.0"),
    (IPv4SubnetMask("255.255.255.0"),"255.255.255.0"),
    (IPv4SubnetMask("255.255.255.255"),"255.255.255.255"),
    (IPv4SubnetMask("255.255.240.0"),"255.255.240.0"),
    (IPv4SubnetMask("255.192.0.0"),"255.192.0.0"),
    (IPv4SubnetMask("255.255.255.248"),"255.255.255.248")])
def test_calculate_decimal(ipv4subnetmask,decimal):
    assert ipv4subnetmask.calculate_decimal() == decimal





# Tests for the calculate_binary() method
@pytest.mark.parameterize("ipv4subnetmask,binary",
    [(IPv4SubnetMask("255.0.0.0"),
    "11111111.00000000.00000000.00000000"), 
    (IPv4SubnetMask("255.255.0.0"),
    "11111111.11111111.00000000.00000000"),
    (IPv4SubnetMask("255.255.255.0"),
    "11111111.11111111.11111111.00000000"),
    (IPv4SubnetMask("255.255.255.255"),
    "11111111.11111111.11111111.11111111"),
    (IPv4SubnetMask("255.255.240.0"),
    "11111111.11111111.11110000.00000000"),
    (IPv4SubnetMask("255.192.0.0"),
    "11111111.11000000.00000000.00000000"),
    (IPv4SubnetMask("255.255.255.248"),
    "11111111.11111111.11111111.11111000")])
def test_calculate_binary(ipv4subnetmask,binary):
    assert ipv4subnetmask.calculate_binary() == binary