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


# def ipv4address_bin(address):
#     """Validates that a binary IPv4Address
#     passed is valid, returns Boolean
#     """
#     # there must be 3 dots in the address.
#     if(not (address.count(".") == 3)):
#         return False
    
#     # each octet must be 8 characters long
#     oct1, oct2, oct3, oct4 = address.split(".")
#     if(len(oct1) != 8):
#         return False
#     elif(len(oct2) != 8):
#         return False
#     elif(len(oct3) != 8):
#         return False
#     elif(len(oct4) != 8):
#         return False

#     # each octet must contain only 1s and 0s
#     octets = [oct1, oct2, oct3, oct4]
#     acceptable_ch = ['0', '1']
#     for octet in octets:
#         for ch in octet:
#             if(ch not in acceptable_ch):
#                 return False
    
#     # we're good.
#     return True


# def ipv6address_bin(address):
#     """Validates that a binary IPv6Address
#     passed is valid, returns Boolean
#     """

#     # length of binary string is 135
#     if(len(address)!=135):
#         return False
    
#     # there should be 7 colons ':' in the string.
#     if(address.count(':') != 7):
#         return False


#     # there should be 8 blocks
#     if(len(address.split(':')) != 8):
#         return False
    
#     # There should be 128 0s or 1s
#     ones = address.count('1')
#     zeroes = address.count('0')
#     if((ones+zeroes) != 128):
#         return False
    
#     # Each segment is 16 characters or bits long.
#     segments = address.split(':')
#     for segment in segments:
#         if(len(segment) != 16):
#             return False

#     # if all good, return True.
#     return True


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

