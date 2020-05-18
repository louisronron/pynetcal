"""Provides subnet functionality, and 
defines the IPv4Subnet class
"""

from ipaddress import IPv4Network
from pysubnetter.ipv4subnetmask import IPv4SubnetMask

class IPv4Subnet:
    """Represents a single IPv4 subnet"""

    def __init__(self,subnet_id, ipv4_network):
        """Initializes IPv4Subnet object"""
        if(self.__validate_args(subnet_id, ipv4_network)):
            self.subnet_id = subnet_id
            self.network = ipv4_network
            self.mask = IPv4SubnetMask(ipv4_network.netmask)
            self.host_min = list(self.network.hosts())[0]
            self.host_max = list(self.network.hosts())[-1]
            self.broadcast = self.network.broadcast_address
            self.hosts = len(list(self.network.hosts()))

    def __validate_args(self, subnet_id, ipv4_network):
        """Validates arguments passed when 
        initializing the class, and return boolean.
        """
        # ensure the subnet_id is type Integer
        if(not isinstance(subnet_id, int)):
            raise TypeError("'subet_id' should be of type \
                Integer")
        # ensure the ipv4_network is type IPv4Network
        elif(not isinstance(ipv4_network, IPv4Network)):
            raise TypeError("'ipv4_network' should be of \
                type IPv4Network")
        else:
            return True



    def __eq__(self, ipv4subnet):
        """IPv4Subnet equality operator"""
        return self.hosts == ipv4subnet.hosts

    def __lt__(self, ipv4subnet):
        """IPv4Subnet less than operator"""
        return self.hosts < ipv4subnet.hosts
    
    def __gt__(self, ipv4subnet):
        """IPv4Subnet greater than operator"""
        return self.hosts > ipv4subnet.hosts
    
    def __le__(self, ipv4subnet):
        """IPv4Subnet less than or equal operator"""
        return self.hosts <= ipv4subnet.hosts
    
    def __ge__(self, ipv4subnet):
        """IPv4Subnet greater than or equal operator"""
        return self.hosts >= ipv4subnet.hosts

    def __str__(self):
        """String representation of object"""
        return "IPv4Subnet("\
        +str(self.network.network_address)\
        +"/"\
        +str(self.mask.decimal)\
        +")"


    def __repr__(self):
        """Repr representation of object"""
        return "IPv4Subnet("\
        +str(self.network.network_address)\
        +"/"\
        +str(self.mask.decimal)\
        +")"