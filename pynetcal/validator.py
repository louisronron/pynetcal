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


