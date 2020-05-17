""" Provides helper functionality for 
IPv4 network and address classes such
as Class A, Class B, Class C IPv4 
addresses.
"""

from ipaddress import IPv4Address, IPv4Network


class_a_masks = [
['NETBITS', 'MASK', 'SUBNETS', 'HOSTS'],
['8', '255.0.0.0', '0', '16777214'],
['9', '255.128.0.0', '2', '8388606'],
['10', '255.192.0.0', '4', '4194302'],
['11', '255.224.0.0', '8', '2097150'],
['12', '255.240.0.0', '16', '1048574'],
['13', '255.248.0.0', '32', '524286'],
['14', '255.252.0.0', '64', '262142'],
['15', '255.254.0.0', '128', '131070'],
['16', '255.255.0.0', '256', '65534'],
['17', '255.255.128.0', '512', '32766'],
['18', '255.255.192.0', '1024', '16382'],
['19', '255.255.224.0', '2048', '8190'],
['20', '255.255.240.0', '4096', '4094'],
['21', '255.255.248.0', '8192', '2046'],
['22', '255.255.252.0', '16384', '1022'],
['23', '255.255.254.0', '32768', '510'],
['24', '255.255.255.0', '65536', '254'],
['25', '255.255.255.128', '131072', '126'],
['26', '255.255.255.192', '262144', '62'],
['27', '255.255.255.224', '524288', '30'],
['28', '255.255.255.240', '1048576', '14'],
['29', '255.255.255.248', '2097152', '6'],
['30', '255.255.255.252', '4194304', '2']]


def is_class_A(ipv4_address):
    """Determines if an IPv4Address or
    IPv4Network is a valid Class A address,
    returns a Boolean
    """
    addr = ipv4_address
    if(isinstance(addr, IPv4Address)):
        addr = addr

    elif(isinstance(ipv4_address, IPv4Network)):
        addr = ipv4_address.network_address
    else:
        raise TypeError("IPv4 address must be of\
            type IPv4Address or IPv4Network")

    start = IPv4Address("1.0.0.1")
    end = IPv4Address("126.255.255.254")
    if(addr >= start and addr <= end):
        return True
    else:
        return False


def is_class_B(ipv4_address):
    """Determines if an IPv4Address or
    IPv4Network is a valid Class B address,
    returns a Boolean
    """
    addr = ipv4_address
    if(isinstance(addr, IPv4Address)):
        addr = addr

    elif(isinstance(ipv4_address, IPv4Network)):
        addr = ipv4_address.network_address
    else:
        raise TypeError("IPv4 address must be of\
            type IPv4Address or IPv4Network")

    start = IPv4Address("128.1.0.1")
    end = IPv4Address("191.255.255.254")
    if(addr >= start and addr <= end):
        return True
    else:
        return False




def is_class_C(ipv4_address):
    """Determines if an IPv4Address or
    IPv4Network is a valid Class C address,
    returns a Boolean
    """
    addr = ipv4_address
    if(isinstance(addr, IPv4Address)):
        addr = addr

    elif(isinstance(ipv4_address, IPv4Network)):
        addr = ipv4_address.network_address
    else:
        raise TypeError("IPv4 address must be of\
            type IPv4Address or IPv4Network")

    start = IPv4Address("192.0.1.1")
    end = IPv4Address("223.255.254.254")
    if(addr >= start and addr <= end):
        return True
    else:
        return False




def max_hosts(ipv4_network):
    """Maximum number of hosts
    in a particular IPv4 network,
    Returns Integer.
    """
    net = ipv4_network
    hosts = list(net.hosts())
    max_hosts = len(hosts)
    return max_hosts



def max_subnets(ipv4_network, new_prefix):
    """Maximum number of subnets
    in a particular IPv4 network,
    Returns Integer.
    """
    net = ipv4_network
    subnets = list(net.subnets(
        new_prefix=new_prefix))
    max_subnets = len(subnets)
    return max_subnets