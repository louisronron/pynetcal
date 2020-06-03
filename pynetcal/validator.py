"""All validators and helper functions for 
pynetcal
"""
import ipaddress
from pynetcal.ipv6pynetcal import PyNIPv6Address, PyNIPv6Network
from pynetcal.ipv4pynetcal import PyNIPv4Address, PyNIPv4Network



def ipv4address(address):
    """Validates that an IPv4Address
    passed is valid, returns Boolean
    """
    try:
        PyNIPv4Address(str(address))
        return True
    except:
        return False


def ipv6address(address):
    """Validates that an IPv6Address
    passed is valid, returns Boolean
    """
    try:
        PyNIPv6Address(str(address))
        return True
    except:
        return False


def ipv4network(address):
    """Validates that an address is
    a valid IPv4 network address, returns Boolean
    """
    try:
        PyNIPv4Network(address)
        return True
    except:
        return False


def ipv6network(address):
    """Validates that an address is
    a valid IPv6 network address, returns Boolean
    """
    try:
        PyNIPv6Network(address)
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

