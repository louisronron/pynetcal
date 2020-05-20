"""contains IPv4SubnetMask class and supporting functionality"""

__all__ = ['IPv4SubnetMask']
__author__ = 'Louis Ronald'


from ipaddress import IPv4Address, IPv4Network
import re
import pynetcal.ipv4networkclasses as ipv4helper

class IPv4SubnetMask:
    """Represents a single and valid IPv4 
    subnet mask.
    """

    def __init__(self,mask):
        """Initializer creates IPv4SubnetMask object."""
        # first validate passed arguments
        validated=self.__validate_args(mask)
        if(validated):
            self.mask = mask
            self.prefix = self.__calculate_prefix(self.mask)
            self.decimal = self.__calculate_decimal(self.mask)
            self.binary = self.__calculate_binary(self.mask)
    
    def __validate_args(self, mask):
        """Validates arguments passed when 
        initializing the class, and return boolean.
        """
        def valid_mask(mask):
            binary_mask = self.__calculate_binary(mask)
            binary_mask = binary_mask.replace(".", "")
            try:
                marker = binary_mask.index("10")
                marker += 1
                if('1' in binary_mask[marker:]):
                    return False
                else:

                    return True
            except ValueError:
                # index couldn't find substring, so 
                # check if its all 1s.
                if(len(re.findall("1{32}",binary_mask))==1):
                    # then its 255.255.255.255, as 
                    # in all 1 bits
                    return True
                else:
                    return False
            except Exception:
                return False
        # ensure the mask is of correct type
        if(not isinstance(mask, IPv4Address)):
            raise TypeError("'mask' should be of type \
                ipaddress.IPv4Address")
        # ensure the mask is valid
        elif(not valid_mask(mask)):
            raise TypeError("'mask' is not a valid \
                subnet mask")
        else:
            return True
    
    def __calculate_prefix(self, mask):
        """Calculates the prefix integer of 
        a subnet mask, and return string.
        """
        mask_bin_str = self.__calculate_binary(mask)
        count_1s = mask_bin_str.count("1")
        return str(count_1s)

    def __calculate_decimal(self, mask):
        """Calculates the decimal-string 
        representation of a subnet mask,
        and return string.
        """
        mask_str = str(mask)
        return mask_str

    def __calculate_binary(self, mask):
        """Calculates the binary-string 
        representation of a subnet mask,
        and return string.
        """
        mask_str = str(mask)
        o1,o2,o3,o4 = list(map(lambda x: int(x), mask_str.split(".")))
        o1 = "{:0>8}.".format(bin(o1).replace("0b",""))
        o2 = "{:0>8}.".format(bin(o2).replace("0b",""))
        o3 = "{:0>8}.".format(bin(o3).replace("0b",""))
        o4 = "{:0>8}".format(bin(o4).replace("0b",""))
        binary=o1+o2+o3+o4
        return binary


    def __eq__(self, ipv4subnetmask):
        """Equality operator of IPv4SubnetMask,
        Returns Boolean
        """
        return self.mask == ipv4subnetmask.mask