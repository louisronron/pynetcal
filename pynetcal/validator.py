"""All validators and helper functions for 
pynetcal
"""
import ipaddress

def ipv4address(address):
    """Validates that an IPv4Address
    passed is valid, returns Boolean
    """
    try:
        ipaddress.IPv4Address(str(address))
        return True
    except:
        return False


def ipv4address_bin(address):
    """Validates that a binary IPv4Address
    passed is valid, returns Boolean
    """
    # there must be 3 dots in the address.
    if(not (address.count(".") == 3)):
        return False
    
    # each octet must be 8 characters long
    oct1, oct2, oct3, oct4 = address.split(".")
    if(len(oct1) != 8):
        return False
    elif(len(oct2) != 8):
        return False
    elif(len(oct3) != 8):
        return False
    elif(len(oct4) != 8):
        return False

    # each octet must contain only 1s and 0s
    octets = [oct1, oct2, oct3, oct4]
    acceptable_ch = ['0', '1']
    for octet in octets:
        for ch in octet:
            if(ch not in acceptable_ch):
                return False
    
    # we're good.
    return True



def ipv4network(address):
    """Validates that an address is
    a valid network address, returns Boolean
    """
    try:
        ipaddress.IPv4Network(address)
        return True
    except:
        return False


def integer(n):
    """Validates that a value passed
    is a valid Integer, returns Boolean.
    """
    if(isinstance(n, int)):
        return True
    elif("." in str(n)):
        return False
    else:
        try:
            int(n)
            return True
        except:
            return False


