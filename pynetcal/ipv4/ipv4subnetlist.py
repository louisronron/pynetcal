"""Provides subnet list functionalities especially
the IPv4SubnetList class, and helper methods
"""

from pynetcal.ipv4.ipv4subnet import IPv4Subnet

class IPv4SubnetList:
    """Represents a collection of 
    IPv4Subnet objects
    """

    def __init__(self, *args):
        """Initializes an IPv4SubnetList object"""
        if(self.__validate_args(args)):
            # add subnets to object subnets list
            self.subnets = list()
            for subnet in args:
                self.subnets.append(subnet)
    
    def __validate_args(self, list_of_args):
        """Validates all arguments 
        passed during initialization. Returns
        True if successful, or raises TypeError
        """
        args = list_of_args
        for arg in args:
            if(not isinstance(arg, IPv4Subnet)):
                raise TypeError("All 'arg' must be of type IPv4Subnet")
        return True

    
    def append(self, ipv4subnet):
        """Appends a subnet of type IPv4Subnet
        to the add of current list. Returns None,
        or raises TypeError
        """
        if(not isinstance(ipv4subnet, IPv4Subnet)):
            raise TypeError("'ipv4subnet' must be of type IPv4Subnet")
        self.subnets.append(ipv4subnet)


    def smallest(self):
        """All smallest subnets, Returns IPv4SubnetList"""
        try:
            allsubnets = self.subnets
            allsubnets.sort()
            smallSubnet = allsubnets[0]
            smallest = IPv4SubnetList()
            for net in allsubnets:
                if(net == smallSubnet):
                    smallest.append(net)
            return smallest
        except ValueError:
            return list()


    def biggest(self):
        """All biggest subnets, Returns IPv4SubnetList"""
        try:
            allsubnets = self.subnets
            allsubnets.sort()
            bigSubnet = allsubnets[-1]
            biggest = IPv4SubnetList()
            for net in allsubnets:
                if(net == bigSubnet):
                    biggest.append(net)
            return biggest
        except ValueError:
            return list()


    def count(self):
        """Counts total number of subnets in list,
        Returns Integer
        """
        return len(self.subnets)



    def __str__(self):
        """String representation of object"""
        final_str = "IPv4SubnetList("
        for i in range(len(self.subnets)):
            final_str += str(self.subnets[i])
            if(i!=(len(self.subnets)-1)):
                final_str += ", "
        final_str += ")"
        return final_str


    def __repr__(self):
        """Repr representation of object"""
        final_str = "IPv4SubnetList("
        for i in range(len(self.subnets)):
            final_str += str(self.subnets[i])
            if(i!=(len(self.subnets)-1)):
                final_str += ", "
        final_str += ")"
        return final_str


    def __eq__(self, ipv4subnetlist):
        """Equality operator for IPv4SubnetList"""
        list1 = self.subnets
        list2 = ipv4subnetlist.subnets
        if(len(list1)!=len(list2)):
            return False
        for i in range(len(list1)):
            if(list1[i]!=list2[i]):
                return False
        return True