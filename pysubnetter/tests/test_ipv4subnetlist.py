"""All tests for ipv4subnetlist.py module in here."""

import pytest
from ipaddress import IPv4Network
from pysubnetter.ipv4subnet import IPv4Subnet
from pysubnetter.ipv4subnetmask import IPv4SubnetMask
from pysubnetter.ipv4subnetlist import IPv4SubnetList


@pytest.fixture
def ipv4_subnet_list_1():
    """Fixture providing sample 
    subnet list of IPv4Subnet objects
    """
    subnets = list()
    subnets.append(IPv4Subnet(0, IPv4Network("192.168.1.0/26")))
    subnets.append(IPv4Subnet(1, IPv4Network("192.168.1.64/26")))
    subnets.append(IPv4Subnet(2, IPv4Network("192.168.1.128/26")))
    subnets.append(IPv4Subnet(3, IPv4Network("192.168.1.0/26")))
    subnets.append(IPv4Subnet(4, IPv4Network("192.168.1.64/26")))
    return subnets


@pytest.fixture
def ipv4_subnet_list_2():
    """Fixture providing sample
    subnet list of IPv4Subnet objects
    """
    subnets = list()
    subnets.append(IPv4Subnet(0, IPv4Network("192.168.2.0/26")))
    subnets.append(IPv4Subnet(1, IPv4Network("192.168.2.64/26")))
    subnets.append(IPv4Subnet(2, IPv4Network("192.168.2.128/26")))
    subnets.append(IPv4Subnet(3, IPv4Network("192.168.2.0/26")))
    subnets.append(IPv4Subnet(4, IPv4Network("192.168.2.64/26")))
    return subnets


@pytest.fixture
def ipv4_subnet_list_invalidargs_1():
    """Fixture providing sample
    subnet list of invalid, non-IPv4Subnet objects
    """
    subnets = list()
    subnets.append(10)
    subnets.append("subnet2")
    subnets.append(list())
    subnets.append(dict())
    subnets.append([1,2,3])
    return subnets


@pytest.fixture
def ipv4_subnet_list_withsizes1():
    """Fixture providing a list of subnets
    along with their respective sizes (by hosts)
    """
    subnets = list()
    subnets.append((IPv4Subnet(0, IPv4Network("192.168.2.0/26")),62))
    subnets.append((IPv4Subnet(1, IPv4Network("192.168.2.64/26")),62))
    subnets.append((IPv4Subnet(2, IPv4Network("192.168.2.128/26")),62))
    subnets.append((IPv4Subnet(3, IPv4Network("192.168.2.0/26")),62))
    subnets.append((IPv4Subnet(4, IPv4Network("192.168.2.64/26")),62))
    return subnets

@pytest.fixture
def ipv4_subnet_list_withsizes2():
    """Fixture providing a list of subnets
    along with their respective sizes (by hosts)
    """
    subnets = list()
    subnets.append((IPv4Subnet(0, IPv4Network("192.168.1.0/26")),62))
    subnets.append((IPv4Subnet(1, IPv4Network("192.168.1.64/27")),30))
    subnets.append((IPv4Subnet(2, IPv4Network("192.168.1.96/27")),30))
    subnets.append((IPv4Subnet(3, IPv4Network("192.168.1.128/27")),30))
    subnets.append((IPv4Subnet(4, IPv4Network("192.168.1.160/28")),14))
    subnets.append((IPv4Subnet(5, IPv4Network("192.168.1.176/28")),14))
    return subnets




def test_IPv4SubnetList_init_validargs(ipv4_subnet_list_1):
    """Tests IPv4SubnetList.__init__() function
    with valid arguments
    """
    subnets = ipv4_subnet_list_1
    # try two args
    sl = IPv4SubnetList(subnets[0], subnets[1])
    assert sl.subnets[0] == subnets[0]
    assert sl.subnets[1] == subnets[1]
    # try three args
    sl = IPv4SubnetList(subnets[0], subnets[1],
                        subnets[2])
    assert sl.subnets[0] == subnets[0]
    assert sl.subnets[1] == subnets[1]
    assert sl.subnets[2] == subnets[2]
    # try four arguments
    sl = IPv4SubnetList(subnets[0], subnets[1],
                        subnets[2], subnets[3])
    assert sl.subnets[0] == subnets[0]
    assert sl.subnets[1] == subnets[1]
    assert sl.subnets[2] == subnets[2]
    assert sl.subnets[3] == subnets[3]


def test_IPv4SubnetList_init_invalidargs(ipv4_subnet_list_invalidargs_1,
                                        ipv4_subnet_list_2):
    """Tests IPv4SubnetList.__init__() function
    with valid arguments
    """
    valid_args = ipv4_subnet_list_2
    invalid_args = ipv4_subnet_list_invalidargs_1
    # try two args
    with pytest.raises(TypeError):
        IPv4SubnetList(valid_args[0], invalid_args[0])
    # try three args
    with pytest.raises(TypeError):
        IPv4SubnetList(valid_args[0], valid_args[1], invalid_args[0])
    # try four args
    with pytest.raises(TypeError):
        IPv4SubnetList(valid_args[0], valid_args[1],
            valid_args[2], invalid_args[3])



def test_IPv4SubnetList_append_validargs(ipv4_subnet_list_1):
    """Test IPv4SubnetList.append() method
    with valid arguments
    """
    subnets = ipv4_subnet_list_1
    subnet1 = subnets[0]
    subnet2 = subnets[1]
    subnet3 = subnets[2]
    subnet4 = subnets[3]

    # test append 1 argument
    sl = IPv4SubnetList(subnet1)
    sl.append(subnet2)
    assert sl.subnets == [subnet1, subnet2]

    # test append 2 arguments
    sl = IPv4SubnetList(subnet1, subnet2)
    sl.append(subnet3)
    sl.append(subnet4)
    assert sl.subnets == [subnet1, subnet2, subnet3, subnet4]

    # test append 3 arguments
    sl = IPv4SubnetList(subnet1)
    sl.append(subnet2)
    sl.append(subnet3)
    sl.append(subnet4)
    assert sl.subnets == [subnet1, subnet2, subnet3, subnet4]


def test_IPv4SubnetList_append_invalidargs(ipv4_subnet_list_invalidargs_1,
                                            ipv4_subnet_list_1):
    """Test IPv4SubnetList.append() method
    with invalid arguments
    """
    invalid_args = ipv4_subnet_list_invalidargs_1
    subnets = ipv4_subnet_list_1
    subnet1 = subnets[0]

    # test invalid argument 1
    sl = IPv4SubnetList(subnet1)
    with pytest.raises(TypeError):
        sl.append(invalid_args[0])
    
    # test invalid argument 1
    sl = IPv4SubnetList(subnet1)
    with pytest.raises(TypeError):
        sl.append(invalid_args[2])

    # test invalid argument 1
    sl = IPv4SubnetList(subnet1)
    with pytest.raises(TypeError):
        sl.append(invalid_args[3])

    # test invalid argument 1
    sl = IPv4SubnetList(subnet1)
    with pytest.raises(TypeError):
        sl.append(invalid_args[4])





def test_IPv4SubnetList_smallest_1(ipv4_subnet_list_withsizes1):
    """Tests the IPv4SubnetList.smallest() function"""
    subnet_list_obj = IPv4SubnetList()
    subnets_list = list(map(lambda s: s[0], ipv4_subnet_list_withsizes1))
    for subnet in subnets_list:
        subnet_list_obj.append(subnet)
    smallest_subnets = [subnets_list[0],subnets_list[1],subnets_list[2],
                        subnets_list[3], subnets_list[4]]
    calculated_smallest = subnet_list_obj.smallest().subnets
    assert calculated_smallest == smallest_subnets


def test_IPv4SubnetList_smallest_2(ipv4_subnet_list_withsizes2):
    """Tests the IPv4SubnetList.smallest() function"""
    subnet_list_obj = IPv4SubnetList()
    subnets_list = list(map(lambda s: s[0], ipv4_subnet_list_withsizes2))
    for subnet in subnets_list:
        subnet_list_obj.append(subnet)
    smallest_subnets = [subnets_list[4], subnets_list[5]]
    calculated_smallest = subnet_list_obj.smallest().subnets
    assert calculated_smallest == smallest_subnets







def test_IPv4SubnetList_biggest_1(ipv4_subnet_list_withsizes1):
    """Tests the IPv4SubnetList.biggest() function"""
    subnet_list_obj = IPv4SubnetList()
    subnets_list = list(map(lambda s: s[0], ipv4_subnet_list_withsizes1))
    for subnet in subnets_list:
        subnet_list_obj.append(subnet)
    biggest_subnets = [subnets_list[0],subnets_list[1],subnets_list[2],
                        subnets_list[3], subnets_list[4]]
    calculated_biggest = subnet_list_obj.biggest().subnets
    assert calculated_biggest == biggest_subnets



def test_IPv4SubnetList_biggest_2(ipv4_subnet_list_withsizes2):
    """Tests the IPv4SubnetList.biggest() function"""
    subnet_list_obj = IPv4SubnetList()
    subnets_list = list(map(lambda s: s[0], ipv4_subnet_list_withsizes2))
    for subnet in subnets_list:
        subnet_list_obj.append(subnet)
    biggest_subnets = [subnets_list[0]]
    calculated_biggest = subnet_list_obj.biggest().subnets
    assert calculated_biggest == biggest_subnets



def test_IPv4SubnetList_count_1(ipv4_subnet_list_withsizes1):
    """Tests the IPv4SubnetList.count() function"""
    subnet_list_obj = IPv4SubnetList()
    subnets_list = list(map(lambda s: s[0], ipv4_subnet_list_withsizes1))
    for subnet in subnets_list:
        subnet_list_obj.append(subnet)
    assert subnet_list_obj.count() == 5


def test_IPv4SubnetList_count_2(ipv4_subnet_list_withsizes2):
    """Tests the IPv4SubnetList.count() function"""
    subnet_list_obj = IPv4SubnetList()
    subnets_list = list(map(lambda s: s[0], ipv4_subnet_list_withsizes2))
    for subnet in subnets_list:
        subnet_list_obj.append(subnet)
    assert subnet_list_obj.count() == 6