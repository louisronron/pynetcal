""" Provides helper functionality for 
IPv4 addresses, networks, and address classes such
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


class_b_masks = [
['NETBITS', 'MASK', 'SUBNETS', 'HOSTS'],
['16', '255.255.0.0', '0', '65534'],
['17', '255.255.128.0', '2', '32766'],
['18', '255.255.192.0', '4', '16382'],
['19', '255.255.224.0', '8', '8190'],
['20', '255.255.240.0', '16', '4094'],
['21', '255.255.248.0', '32', '2046'],
['22', '255.255.252.0', '64', '1022'],
['23', '255.255.254.0', '128', '510'],
['24', '255.255.255.0', '256', '254'],
['25', '255.255.255.128', '512', '126'],
['26', '255.255.255.192', '1024', '62'],
['27', '255.255.255.224', '2048', '30'],
['28', '255.255.255.240', '4096', '14'],
['29', '255.255.255.248', '8192', '6'],
['30', '255.255.255.252', '16384', '2']
]

class_c_masks = [
['NETBITS', 'MASK', 'SUBNETS', 'HOSTS'],
['24', '255.255.255.0', '0', '254'],
['25', '255.255.255.128', '2', '126'],
['26', '255.255.255.192', '4', '62'],
['27', '255.255.255.224', '8', '30'],
['28', '255.255.255.240', '16', '14'],
['29', '255.255.255.248', '32', '6'],
['30', '255.255.255.252', '64', '2'],
]


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

    # do some validation first
    if(not isinstance(ipv4_network, IPv4Network)):
        raise TypeError("IPv4 network must be of type IPv4Network")

    max_hosts = sum(1 for x in ipv4_network.hosts())
    return max_hosts



def max_subnets(ipv4_network, new_prefix):
    """Maximum number of subnets
    in a particular IPv4 network,
    Returns Integer.
    """
    # do some validation first
    if(not isinstance(ipv4_network, IPv4Network)):
        raise TypeError("IPv4 network must be of type IPv4Network")
    elif(not isinstance(new_prefix, int)):
        raise TypeError("New prefix must be of type int")

    net = ipv4_network
    subnets = net.subnets(new_prefix=new_prefix)
    max_subnets = sum(1 for x in subnets)
    return max_subnets



def containing_mask(netaddr, hosts, subnets, 
                    prioritizeHosts=True):
    """The mask that optimally produces
    hosts and subnets, Returns Dictionary object.
    """
    mask_table = None
    isClassA = is_class_A(netaddr)
    isClassB = is_class_B(netaddr)
    isClassC = is_class_C(netaddr)
    if(isClassA):
        mask_table = class_a_masks
    elif(isClassB):
        mask_table = class_b_masks
    elif(isClassC):
        mask_table = class_c_masks
    else:
        raise TypeError("Network address class not supported")
    mask_table = mask_table[1:]
    maskRow = None
    if(prioritizeHosts):
        mask_table.reverse()
        for i in range(len(mask_table)):
            if(hosts <= int(mask_table[i][3])):
                maskRow = mask_table[i]
                break
    else:
        for i in range(len(mask_table)):
            if(subnets <= int(mask_table[i][2])):
                maskRow = mask_table[i]
                break
    if(maskRow is None):
        raise ValueError("Specified number of hosts or subnets cannot be accommodated")
    else:
        return {"netbits": int(maskRow[0]), "mask": IPv4Address(maskRow[1]), 
        "subnets": int(maskRow[2]), "hosts": int(maskRow[3])}



def is_private(address):
    """Determines whether an IPv4 address is
    a private address or not, Returns Boolean.
    """
    if(not isinstance(address, IPv4Address)):
        raise TypeError("'ipv4address' must be of type ipaddress.IPv4Address")
    if(address >= IPv4Address("10.0.0.0") and address <= IPv4Address("10.255.255.255")):
        return True
    elif(address >= IPv4Address("172.16.0.0") and address <= IPv4Address("172.31.255.255")):
        return True
    elif(address >= IPv4Address("192.168.0.0") and address <= IPv4Address("192.168.255.255")):
        return True
    else:
        return False




def is_public(address):
    """Determines whether an IPv4 address is
    a public address or not, Returns Boolean.
    """
    if(not isinstance(address, IPv4Address)):
        raise TypeError("'ipv4address' must be of type ipaddress.IPv4Address")
    if(address >= IPv4Address("10.0.0.0") and address <= IPv4Address("10.255.255.255")):
        return False
    elif(address >= IPv4Address("172.16.0.0") and address <= IPv4Address("172.31.255.255")):
        return False
    elif(address >= IPv4Address("192.168.0.0") and address <= IPv4Address("192.168.255.255")):
        return False
    else:
        return True