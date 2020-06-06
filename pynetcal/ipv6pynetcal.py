from ipaddress import IPv6Address, IPv6Network
import math


def is_hex(hexaddr):
    try:
        IPv6Address(hexaddr)
        return True
    except:
        return False


def is_bin(ipv6address):
    address = str(ipv6address)

    # check for special address cases
    if(address == '::'):
        return True

    # all characters must be a '1', '0', ':', or '::'.
    for char in address:
        if(char != '0' and char != '1' and char != ':'):
            return False

    
    # at most ONLY ONE '::' or ZERO
    dbl_colon_count = address.count("::")
    if(dbl_colon_count > 1):
        return False
    
    # Each segment must be between the binary values 
    # of 0000000000000000 and 1111111111111111 inclusively.
    # or 0000 and ffff
    binary_addr = ""
    if(dbl_colon_count == 0):
        # go ahead and convert binary to hex for each segment
        # divided by ':'
        segments = address.split(':')
        # check the validity of the value range of each segment
        for segment in segments:
            if(int(segment, base=2) < 0 or int(segment, base=2) > 65535):
                return False
        s1 = "{:0<4}".format(hex(int(segments[0], base=2)).replace("0x",""))
        s2 = "{:0<4}".format(hex(int(segments[1], base=2)).replace("0x",""))
        s3 = "{:0<4}".format(hex(int(segments[2], base=2)).replace("0x",""))
        s4 = "{:0<4}".format(hex(int(segments[3], base=2)).replace("0x",""))
        s5 = "{:0<4}".format(hex(int(segments[4], base=2)).replace("0x",""))
        s6 = "{:0<4}".format(hex(int(segments[5], base=2)).replace("0x",""))
        s7 = "{:0<4}".format(hex(int(segments[6], base=2)).replace("0x",""))
        s8 = "{:0<4}".format(hex(int(segments[7], base=2)).replace("0x",""))
        binary_addr = s1 + ":" + s2 + ":" + s3 + ":" + s4 + ":" + s5 + ":" + s6 + ":" + s7 + ":" + s8
    elif(dbl_colon_count == 1):
        # Split the binary address by '::' first, then do 
        # as if dbl_colon_count is 0 like above.
        left_dbl_colon, right_dbl_colon = address.split('::')
        left_binary_str = ""
        right_binary_str = ""

        # perform conversion on left-side of dbl colon first.
        if(left_dbl_colon != ''):
            segments = left_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x",""))
        else:
            left_binary_str = ""



        # perform conversion on right-side of dbl colon next.
        if(right_dbl_colon != ""):
            segments = right_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x",""))
        else:
            right_binary_str = ""            


        # combine both left and right to form final hex string
        binary_addr = left_binary_str + "::" + right_binary_str

    try:
        IPv6Address(binary_addr)
        return True
    except:
        return False
    
    
def is_dec(ipv6address):
    address = str(ipv6address)

    # check for special address cases
    if(address == '::'):
        return True

    # all characters must be either from 0-9 or a ':'
    for char in address:
        try:
            int(char)
        except:
            if(char != ':'):
                return False
    
    # at most ONLY ONE '::' or ZERO
    dbl_colon_count = address.count("::")
    if(dbl_colon_count > 1):
        return False
    
    # Each segment must be between the decimal values 
    # of 0 and 65535 inclusively.
    binary_addr = ""
    if(dbl_colon_count == 0):
        # go ahead and convert decimal to hex for each segment
        # divided by ':'
        segments = address.split(':')
        # check the validity of the value range of each segment
        for segment in segments:
            if(int(segment, base=10) < 0 or int(segment, base=10) > 65535):
                return False
        s1 = "{:0<4}".format(hex(int(segments[0], base=10)).replace("0x",""))
        s2 = "{:0<4}".format(hex(int(segments[1], base=10)).replace("0x",""))
        s3 = "{:0<4}".format(hex(int(segments[2], base=10)).replace("0x",""))
        s4 = "{:0<4}".format(hex(int(segments[3], base=10)).replace("0x",""))
        s5 = "{:0<4}".format(hex(int(segments[4], base=10)).replace("0x",""))
        s6 = "{:0<4}".format(hex(int(segments[5], base=10)).replace("0x",""))
        s7 = "{:0<4}".format(hex(int(segments[6], base=10)).replace("0x",""))
        s8 = "{:0<4}".format(hex(int(segments[7], base=10)).replace("0x",""))
        binary_addr = s1 + ":" + s2 + ":" + s3 + ":" + s4 + ":" + s5 + ":" + s6 + ":" + s7 + ":" + s8
    elif(dbl_colon_count == 1):
        # Split the binary address by '::' first, then do 
        # as if dbl_colon_count is 0 like above.
        left_dbl_colon, right_dbl_colon = address.split('::')
        left_binary_str = ""
        right_binary_str = ""

        # perform conversion on left-side of dbl colon first.
        if(left_dbl_colon != ''):
            segments = left_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x",""))
        else:
            left_binary_str = ""



        # perform conversion on right-side of dbl colon next.
        if(right_dbl_colon != ""):
            segments = right_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x",""))
        else:
            right_binary_str = ""            


        # combine both left and right to form final hex string
        binary_addr = left_binary_str + "::" + right_binary_str

    try:
        IPv6Address(binary_addr)
        return True
    except:
        return False
    

def bin_to_hex(ipv6address):
    address = ipv6address

    # check for special address cases
    if(address == '::'):
        return address


    # all characters must be a '1', '0', ':', or '::'.
    for char in address:
        if(char != '0' and char != '1' and char != ':'):
            raise TypeError("Invalid IPv6 binary address passed")

    
    # at most ONLY ONE '::' or ZERO
    dbl_colon_count = address.count("::")
    if(dbl_colon_count > 1):
        raise TypeError("Invalid IPv6 binary address passed")
    
    # Each segment must be between the binary values 
    # of 0000000000000000 and 1111111111111111 inclusively.
    # or 0000 and ffff
    binary_addr = ""
    if(dbl_colon_count == 0):
        # go ahead and convert binary to hex for each segment
        # divided by ':'
        segments = address.split(':')
        # check the validity of the value range of each segment
        for segment in segments:
            if(int(segment, base=2) < 0 or int(segment, base=2) > 65535):
                raise TypeError("Invalid IPv6 binary address passed")
        s1 = "{:0<4}".format(hex(int(segments[0], base=2)).replace("0x",""))
        s2 = "{:0<4}".format(hex(int(segments[1], base=2)).replace("0x",""))
        s3 = "{:0<4}".format(hex(int(segments[2], base=2)).replace("0x",""))
        s4 = "{:0<4}".format(hex(int(segments[3], base=2)).replace("0x",""))
        s5 = "{:0<4}".format(hex(int(segments[4], base=2)).replace("0x",""))
        s6 = "{:0<4}".format(hex(int(segments[5], base=2)).replace("0x",""))
        s7 = "{:0<4}".format(hex(int(segments[6], base=2)).replace("0x",""))
        s8 = "{:0<4}".format(hex(int(segments[7], base=2)).replace("0x",""))
        binary_addr = s1 + ":" + s2 + ":" + s3 + ":" + s4 + ":" + s5 + ":" + s6 + ":" + s7 + ":" + s8
    elif(dbl_colon_count == 1):
        # Split the binary address by '::' first, then do 
        # as if dbl_colon_count is 0 like above.
        left_dbl_colon, right_dbl_colon = address.split('::')
        left_binary_str = ""
        right_binary_str = ""

        # perform conversion on left-side of dbl colon first.
        if(left_dbl_colon != ''):
            segments = left_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x",""))
        else:
            left_binary_str = ""



        # perform conversion on right-side of dbl colon next.
        if(right_dbl_colon != ""):
            segments = right_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=2)).replace("0x",""))
        else:
            right_binary_str = ""            


        # combine both left and right to form final hex string
        binary_addr = left_binary_str + "::" + right_binary_str

    try:
        IPv6Address(binary_addr)
        return binary_addr
    except:
        raise TypeError("Invalid IPv6 binary address passed")


def hex_to_bin(ipv6address):
    address = ipv6address

    # check for special address cases
    if(address == '::'):
        return address


    # all characters must be either from 0-f or ':'
    try:
        IPv6Address(address)
    except:
        raise TypeError("Invalid IPv6 hex address passed")

    
    # at most ONLY ONE '::' or ZERO
    dbl_colon_count = address.count("::")
    if(dbl_colon_count > 1):
        raise TypeError("Invalid IPv6 hex address passed")
    
    # Each segment must be between the hex values
    # of 0000 and ffff inclusively.
    binary_addr = ""
    if(dbl_colon_count == 0):
        # go ahead and convert hex to binary for each segment
        # divided by ':'
        segments = address.split(':')
        # check the validity of the value range of each segment
        for segment in segments:
            if(int(segment, base=16) < 0 or int(segment, base=16) > 65535):
                raise TypeError("Invalid IPv6 hex address passed")
        s1 = "{:0>16}".format(bin(int(segments[0], base=16)).replace("0b",""))
        s2 = "{:0>16}".format(bin(int(segments[1], base=16)).replace("0b",""))
        s3 = "{:0>16}".format(bin(int(segments[2], base=16)).replace("0b",""))
        s4 = "{:0>16}".format(bin(int(segments[3], base=16)).replace("0b",""))
        s5 = "{:0>16}".format(bin(int(segments[4], base=16)).replace("0b",""))
        s6 = "{:0>16}".format(bin(int(segments[5], base=16)).replace("0b",""))
        s7 = "{:0>16}".format(bin(int(segments[6], base=16)).replace("0b",""))
        s8 = "{:0>16}".format(bin(int(segments[7], base=16)).replace("0b",""))
        binary_addr = s1 + ":" + s2 + ":" + s3 + ":" + s4 + ":" + s5 + ":" + s6 + ":" + s7 + ":" + s8
    elif(dbl_colon_count == 1):
        # Split the binary address by '::' first, then do 
        # as if dbl_colon_count is 0 like above.
        left_dbl_colon, right_dbl_colon = address.split('::')
        left_binary_str = ""
        right_binary_str = ""

        # perform conversion on left-side of dbl colon first.
        if(left_dbl_colon != ''):
            segments = left_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    left_binary_str += "{:0<4}".format(bin(int(segments[i], base=16)).replace("0b","") + ":")

                else:
                    # if it's at the end of list.
                    left_binary_str += "{:0<4}".format(bin(int(segments[i], base=16)).replace("0b",""))
        else:
            left_binary_str = ""



        # perform conversion on right-side of dbl colon next.
        if(right_dbl_colon != ""):
            segments = right_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    right_binary_str += "{:0<4}".format(bin(int(segments[i], base=16)).replace("0b","") + ":")

                else:
                    # if it's at the end of list.
                    right_binary_str += "{:0<4}".format(bin(int(segments[i], base=16)).replace("0b",""))
        else:
            right_binary_str = ""            


        # combine both left and right to form final hex string
        binary_addr = left_binary_str + "::" + right_binary_str


    return binary_addr


def dec_to_hex(ipv6address):
    address = ipv6address

    # check for special address cases
    if(address == '::'):
        return address

    # all characters must be either from 0-9 or a ':'
    for char in address:
        try:
            int(char)
        except:
            if(char != ':'):
                raise TypeError("Invalid IPv6 decimal address passed")
    
    # at most ONLY ONE '::' or ZERO
    dbl_colon_count = address.count("::")
    if(dbl_colon_count > 1):
        raise TypeError("Invalid IPv6 decimal address passed")
    
    # Each segment must be between the decimal values 
    # of 0 and 65535 inclusively.
    binary_addr = ""
    if(dbl_colon_count == 0):
        # go ahead and convert decimal to hex for each segment
        # divided by ':'
        segments = address.split(':')
        # check the validity of the value range of each segment
        for segment in segments:
            if(int(segment, base=10) < 0 or int(segment, base=10) > 65535):
                raise TypeError("Invalid IPv6 decimal address passed")
        s1 = "{:0<4}".format(hex(int(segments[0], base=10)).replace("0x",""))
        s2 = "{:0<4}".format(hex(int(segments[1], base=10)).replace("0x",""))
        s3 = "{:0<4}".format(hex(int(segments[2], base=10)).replace("0x",""))
        s4 = "{:0<4}".format(hex(int(segments[3], base=10)).replace("0x",""))
        s5 = "{:0<4}".format(hex(int(segments[4], base=10)).replace("0x",""))
        s6 = "{:0<4}".format(hex(int(segments[5], base=10)).replace("0x",""))
        s7 = "{:0<4}".format(hex(int(segments[6], base=10)).replace("0x",""))
        s8 = "{:0<4}".format(hex(int(segments[7], base=10)).replace("0x",""))
        binary_addr = s1 + ":" + s2 + ":" + s3 + ":" + s4 + ":" + s5 + ":" + s6 + ":" + s7 + ":" + s8
    elif(dbl_colon_count == 1):
        # Split the binary address by '::' first, then do 
        # as if dbl_colon_count is 0 like above.
        left_dbl_colon, right_dbl_colon = address.split('::')
        left_binary_str = ""
        right_binary_str = ""

        # perform conversion on left-side of dbl colon first.
        if(left_dbl_colon != ''):
            segments = left_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    left_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x",""))
        else:
            left_binary_str = ""



        # perform conversion on right-side of dbl colon next.
        if(right_dbl_colon != ""):
            segments = right_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x","") + ":")

                else:
                    # if it's at the end of list.
                    right_binary_str += "{:0<4}".format(hex(int(segments[i], base=10)).replace("0x",""))
        else:
            right_binary_str = ""            


        # combine both left and right to form final hex string
        binary_addr = left_binary_str + "::" + right_binary_str

    try:
        IPv6Address(binary_addr)
        return binary_addr
    except:
        raise TypeError("Invalid IPv6 decimal address passed")


def hex_to_dec(ipv6address):
    address = ipv6address

    # check for special address cases
    if(address == '::'):
        return address


    # all characters must be either from 0-f or ':'
    try:
        IPv6Address(address)
    except:
        raise TypeError("Invalid IPv6 hex address passed")

    
    # at most ONLY ONE '::' or ZERO
    dbl_colon_count = address.count("::")
    if(dbl_colon_count > 1):
        raise TypeError("Invalid IPv6 hex address passed")
    
    # Each segment must be between the hex values
    # of 0000 and ffff inclusively.
    binary_addr = ""
    if(dbl_colon_count == 0):
        # go ahead and convert hex to binary for each segment
        # divided by ':'
        segments = address.split(':')
        # check the validity of the value range of each segment
        for segment in segments:
            if(int(segment, base=16) < 0 or int(segment, base=16) > 65535):
                raise TypeError("Invalid IPv6 hex address passed")
        s1 = "{:0<4}".format(int(segments[0], base=16))
        s2 = "{:0<4}".format(int(segments[1], base=16))
        s3 = "{:0<4}".format(int(segments[2], base=16))
        s4 = "{:0<4}".format(int(segments[3], base=16))
        s5 = "{:0<4}".format(int(segments[4], base=16))
        s6 = "{:0<4}".format(int(segments[5], base=16))
        s7 = "{:0<4}".format(int(segments[6], base=16))
        s8 = "{:0<4}".format(int(segments[7], base=16))
        binary_addr = s1 + ":" + s2 + ":" + s3 + ":" + s4 + ":" + s5 + ":" + s6 + ":" + s7 + ":" + s8
    elif(dbl_colon_count == 1):
        # Split the binary address by '::' first, then do 
        # as if dbl_colon_count is 0 like above.
        left_dbl_colon, right_dbl_colon = address.split('::')
        left_binary_str = ""
        right_binary_str = ""

        # perform conversion on left-side of dbl colon first.
        if(left_dbl_colon != ''):
            segments = left_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    left_binary_str += "{:0<4}".format(int(segments[i], base=16) + ":")

                else:
                    # if it's at the end of list.
                    left_binary_str += "{:0<4}".format(int(segments[i], base=16))
        else:
            left_binary_str = ""



        # perform conversion on right-side of dbl colon next.
        if(right_dbl_colon != ""):
            segments = right_dbl_colon.split(':')
            for i in range(len(segments)):
                if(i != len(segments) - 1):
                    # if it's not at the end of list.
                    right_binary_str += "{:0<4}".format(int(segments[i], base=16) + ":")

                else:
                    # if it's at the end of list.
                    right_binary_str += "{:0<4}".format(int(segments[i], base=16))
        else:
            right_binary_str = ""            


        # combine both left and right to form final hex string
        binary_addr = left_binary_str + "::" + right_binary_str


    return binary_addr



class PyNIPv6Address(IPv6Address):

    def __init__(self, address):
        
        # do some validation
        address = self.__validation(address)

        # go ahead call parent init
        IPv6Address.__init__(self, address)

        # set object variables.
        self.hexadecimal = self.exploded
        self.binary = hex_to_bin(self.hexadecimal)
        self.decimal = hex_to_dec(self.hexadecimal)

    def __validation(self, address):
        # check for special case
        if(str(address)=="::"):
            address = "::"

        # do some validation
        elif(is_dec(address)):
            # leave in decimal form
            address = dec_to_hex(address)

        elif(is_bin(address)):
            # convert from bin-to-decimal form
            address = bin_to_hex(address)
        
        elif(is_hex(address)):
            # convert from hex-to-decimal form
            pass
        
        else:
            # invalid address passed.
            raise TypeError("address must be a valid IPv6 address")

        return address



class PyNIPv6Network(IPv6Network):

    def __init__(self, address):
        """Initializer"""
        
        # validate the arguments passed
        self.__validate(address)

        # call the parent initializer
        IPv6Network.__init__(self, address)

        # set some object variables
        self.pn_network = IPv6Network(address)
        self.pn_network_address = PyNIPv6Address(self.network_address)
        self.pn_hostmask = PyNIPv6Address(self.hostmask.exploded)
        self.pn_netmask = PyNIPv6Address(self.netmask.exploded)
        self.pn_hosts = self.num_addresses

        self.pn_hostmin = PyNIPv6Address(self.pn_network_address)
        self.pn_hostmax = PyNIPv6Address(self.broadcast_address)


    def __validate(self, address):
        """Validates that the arguments passed
        in the initializer are valid
        """
        try:
            IPv6Network(address)
            return True
        except:
            raise TypeError("Invalid IPv6 network address passed")


    def subnets_flsm(self, hosts=None, subnets=None,
        prioritizeHosts=True):
        """Performs optimal FLSM subnetting on
        PyNIPv6Network address passed, Returns list of 
        PyNIPv6Network objects.
        """
        network = self.pn_network
        
        # validate parameters passed.
        if(prioritizeHosts and hosts is None):
            raise TypeError("Number of desired hosts must be set, because priority set for hosts")
        if(not prioritizeHosts and subnets is None):
            raise TypeError("Number of desired subnets must be set, because priority set for subnets")
        
        subnetList = list()

        # start subnetting
        if(prioritizeHosts):
            # subnet by number of hosts
            new_prefix = 128 - math.ceil(math.log2(hosts))
            if(hosts > self.pn_hosts):
                raise TypeError("Number of hosts you specified exceeds available addresses")
            num_networks = math.pow(2,(new_prefix - self.prefixlen))
            num_networks = int(num_networks)
            baseNetAddress = str(network.network_address.exploded)+"/"+str(int(new_prefix))
            for i in range(num_networks):
                baseNetwork = PyNIPv6Network(baseNetAddress)
                subnetList.append(baseNetwork)
                baseNetAddress = str(baseNetwork.network_address + baseNetwork.num_addresses)+"/"+str(int(new_prefix))


        else:
            # subnet by number of subnets
            new_prefix = self.prefixlen + int(math.ceil(math.log2(subnets)))
            num_hosts = math.pow(2, 128 - new_prefix)
            if(num_hosts > self.pn_hosts):
                raise TypeError("Number of hosts you specified exceeds available addresses")
            num_networks = math.pow(2,(new_prefix - self.prefixlen))
            num_networks = int(num_networks)
            baseNetAddress = str(network.network_address.exploded)+"/"+str(int(new_prefix))
            for i in range(num_networks):
                baseNetwork = PyNIPv6Network(baseNetAddress)
                subnetList.append(baseNetwork)
                baseNetAddress = str(baseNetwork.network_address + baseNetwork.num_addresses)+"/"+str(int(new_prefix))


        return subnetList


    def subnets_vlsm(self, hosts):
        """Performs optimal VLSM subnetting on
        PyNIPv6Network address passed, Returns list of 
        PyNIPv6Network objects.
        """
        network = self.pn_network
        subnetList = list()

        # first check if total hosts
        # exceed available number of addresses
        # in the network.
        subnet_hosts = list()
        for host_count in hosts:
            hostbits = math.ceil(math.log2(host_count))
            block_size = math.pow(2, int(hostbits))
            subnet_hosts.append(int(block_size))
        
        if(sum(subnet_hosts) > network.num_addresses):
            raise TypeError("Total hosts you specified exceeds address space available")

        # remove any zeroes '0' in the subnet list
        try:
            subnet_hosts.remove(0)
        except:
            pass

        # sort the subnets in ascending order
        subnet_hosts.sort()
        subnet_hosts.reverse()

        # start subnetting
        startAddress = self.pn_network_address
        for i in range(len(subnet_hosts)):
            prefix = 128 - math.ceil(math.log2(subnet_hosts[i]))
            net_addr = str(startAddress) + "/" + str(prefix)
            net = PyNIPv6Network(net_addr)
            subnetList.append(net)
            startAddress = startAddress + subnet_hosts[i]
            
        # return subnet list
        return subnetList

