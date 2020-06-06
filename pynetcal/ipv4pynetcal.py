"""Contains classes and supporting functions for
IPv4 network and address manipulation.
"""


from ipaddress import IPv4Address, IPv4Network
import math


    
def is_bin(address):
    """Validates that a binary IPv4Address
    passed is valid, returns Boolean
    """
    # there must be 3 dots in the address.
    if(not (address.count(".") == 3)):
        return False
    

    # each octet must contain only 1s and 0s
    oct1, oct2, oct3, oct4 = address.split(".")
    octets = [oct1, oct2, oct3, oct4]
    acceptable_ch = ['0', '1']
    for octet in octets:

        # length of each octet should not be >8 or be <=0
        if(len(octet)<=0 or len(octet)>8):
            return False

        for ch in octet:
            if(ch not in acceptable_ch):
                return False
    
    # we're good.
    return True
    

def is_hex(hexaddr):
    """Validates that a hex IPv4Address
    passed is valid, returns Boolean
    """
    # length of string must be 11
    if(len(hexaddr) != 11):
        return False

    # 3 dots
    if(hexaddr.count('.') != 3):
        return False

    # 4 blocks
    if(len(hexaddr.split('.')) != 4):
        return False

    return True


def is_dec(decaddr):
    """Validates that a decimal IPv4Address
    passed is valid, returns Boolean
    """
    try:
        IPv4Address(decaddr)
        return True
    except:
        return False


def dec_to_bin(decaddr):
    """Converts an IPv4 address from its 
    decimal form to binary form.
    """
    oct1, oct2, oct3, oct4 = decaddr.split('.')
    return "{:0>8}.{:0>8}.{:0>8}.{:0>8}".format(
        bin(int(oct1)).replace("0b",""),
        bin(int(oct2)).replace("0b",""), 
        bin(int(oct3)).replace("0b",""),
        bin(int(oct4)).replace("0b",""))


def dec_to_hex(decaddr):
    """Converts an IPv4 address from its 
    decimal form to hexadecimal form
    """
    oct1, oct2, oct3, oct4 = decaddr.split('.')
    return "{:0>2}.{:0>2}.{:0>2}.{:0>2}".format(
        hex(int(oct1)).replace("0x",""),
        hex(int(oct2)).replace("0x",""), 
        hex(int(oct3)).replace("0x",""),
        hex(int(oct4)).replace("0x",""))


def bin_to_dec(binaddr):
    """ Converts a binary IPv4 address 
    into decimal form, and Returns it
    """
    oct1, oct2, oct3, oct4 = binaddr.split(".")
    return "{}.{}.{}.{}".format(
        int(oct1, base=2), 
        int(oct2, base=2), 
        int(oct3, base=2), 
        int(oct4, base=2))


def hex_to_dec(hexaddr):
    """Converts an IPv4 address from its 
    hexadecimal form, to its decimal form
    """
    oct1, oct2, oct3, oct4 = hexaddr.split('.')
    oct1 = int(oct1, base=16)
    oct2 = int(oct2, base=16)
    oct3 = int(oct3, base=16)
    oct4 = int(oct4, base=16)
    print("{}.{}.{}.{}".format(
        oct1, 
        oct2, 
        oct3, 
        oct4))
    return "{}.{}.{}.{}".format(
        oct1, 
        oct2, 
        oct3, 
        oct4)


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



def is_class_D(ipv4_address):
    """Determines if an IPv4Address or
    IPv4Network is a valid Class D address,
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

    start = IPv4Address("224.0.0.0")
    end = IPv4Address("239.255.255.255")
    if(addr >= start and addr <= end):
        return True
    else:
        return False



def is_class_E(ipv4_address):
    """Determines if an IPv4Address or
    IPv4Network is a valid Class E address,
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

    start = IPv4Address("240.0.0.0")
    end = IPv4Address("254.255.255.254")
    if(addr >= start and addr <= end):
        return True
    else:
        return False



class PyNIPv4Address(IPv4Address):

    def __init__(self, address):
        """Initializer"""

        # do some validation
        address = self.__validation(address)

        # go ahead call parent init
        IPv4Address.__init__(self, address)

        # set object variables.
        self.pn_decimal = self.exploded
        self.pn_hexadecimal = dec_to_hex(self.pn_decimal)
        self.pn_binary = dec_to_bin(self.pn_decimal)
        self.pn_is_class_a = is_class_A(IPv4Address(self.pn_decimal))
        self.pn_is_class_b = is_class_B(IPv4Address(self.pn_decimal))
        self.pn_is_class_c = is_class_C(IPv4Address(self.pn_decimal))
        self.pn_is_class_d = is_class_D(IPv4Address(self.pn_decimal))
        self.pn_is_class_e = is_class_E(IPv4Address(self.pn_decimal))


    def __validation(self, address):
        """Validates the arguments passed
        to the initializer
        """
        # do some validation
        if(is_dec(address)):
            # leave in decimal form
            pass

        elif(is_bin(address)):
            # convert from bin-to-decimal form
            address = bin_to_dec(address)
        
        elif(is_hex(address)):
            # convert from hex-to-decimal form
            print("Hex to Dec")
            address = hex_to_dec(address)
        
        else:
            # invalid address passed.
            raise TypeError("address must be a valid IPv4 address")
        return address



class PyNIPv4Network(IPv4Network):

    def __init__(self, address):
        """Initializer"""

        # validate the arguments passed
        self.__validate(address)

        # call the parent initializer
        IPv4Network.__init__(self, address)

        # set some object variables
        self.pn_network = IPv4Network(address)
        ######################################## originally IPv4Address(self.network_address)
        self.pn_network_address = PyNIPv4Address(self.network_address)
        self.pn_hostmask = PyNIPv4Address(self.hostmask)
        self.pn_netmask = PyNIPv4Address(self.netmask)
        self.pn_hosts = sum(1 for x in self.hosts())
        self.pn_hostmin = PyNIPv4Address(self.pn_network_address+1)
        self.pn_hostmax = PyNIPv4Address(self.broadcast_address-1)


    def __validate(self, address):
        """Validates that the arguments passed
        in the initializer are valid
        """
        try:
            IPv4Network(address)
            return True
        except:
            raise TypeError("Invalid IPv4 network address passed")


    def subnets_flsm(self, hosts=None,
        subnets=None, prioritizeHosts=True):
        """Performs optimal FLSM subnetting on
        PyNIPv4Network address passed, Returns list of PyNIPv4Network
        """
        ipv4network = self.pn_network
        address_space_size = ipv4network.num_addresses
        new_prefix = 0
        nhost_bits = 0
        nsubnets = 0

        # find the required block size for specific hosts or subnets.
        if(prioritizeHosts):
            # find containing block size for hosts, and corresponding subnet
            nhost_bits = math.log2(hosts+2)
            nhost_bits = math.ceil(nhost_bits)
            new_prefix = 32 - nhost_bits
            nsubnets = math.pow(2, 32 - new_prefix)
        else:
            # find containing block size for subnet, and corresponding hosts
            nhost_bits = math.log2(address_space_size/subnets)
            nhost_bits = math.floor(nhost_bits)
            new_prefix = 32 - nhost_bits
            nsubnets = math.pow(2, 32 - new_prefix)

        baseNetwork = PyNIPv4Network(str(ipv4network.network_address)+"/"+str(new_prefix))

        for i in range(math.floor(address_space_size/baseNetwork.num_addresses)):
            # subnet = list(ipv4network.subnets(new_prefix=new_prefix))[i]
            yield baseNetwork
            #subnetList.append(baseNetwork)
            baseNetwork = PyNIPv4Network(str(baseNetwork.network_address+baseNetwork.num_addresses)+"/"+str(new_prefix))
            address_space_size -= baseNetwork.num_addresses


    def subnets_vlsm(self, hosts):
        """Performs optimal VLSM subnetting on
        PyNIPv4Network address passed, Returns list of PyNIPv4Network
        """
        
        # size of address space (inclusive of net, broad addresses)
        network = self.pn_network
        network_size = network.num_addresses

        hosts_no = hosts
        hosts_no.sort()
        hosts_no.reverse()

        container_masks = list()
        subnet_list = list()

        #find the required containing masks for each hosts no.
        for i in range(len(hosts)):
            # find containing block size for current host no.
            nhost_bits = math.ceil(math.log2(hosts[i]+2))
            container_mask = {'hosts': math.pow(2,nhost_bits)-2, 'netbits': 32 - nhost_bits}
            container_masks.append(container_mask)


        # generate subnets
        network_addr = network.network_address
        for i in range(len(container_masks)):
            container_mask = container_masks[i]
            net_incr = container_mask["hosts"]+2
            net_incr = int(net_incr)
            netbits = container_mask["netbits"]
            # generate net address for the curr subnet
            net_addr = str(network_addr)\
                +"/"\
                +str(netbits)
            subnet = PyNIPv4Network(net_addr)

            # check if there's sufficient space
            # to add another full subnet.
            if(subnet.num_addresses <= network_size):
                # add the subnet to subnet list
                subnet_list.append(subnet)
                network_addr += net_incr
                network_size -= subnet.num_addresses
            else:
                return subnet_list

        return subnet_list


    def num_of_subnets(self, hosts=None,
        subnets=None, prioritizeHosts=True):
        """Gets the number of possible subnets,
        Returns Integer.
        """
        ipv4network = self.pn_network
        address_space_size = ipv4network.num_addresses
        nhost_bits = 0
        new_prefix = 0
        nsubnets = 0
        # find the required block size for specific hosts or subnets.
        if(prioritizeHosts):
            # find containing block size for hosts, and corresponding subnet
            nhost_bits = math.log2(hosts+2)
            nhost_bits = math.ceil(nhost_bits)
            new_prefix = 32 - nhost_bits
            nsubnets = math.pow(2, new_prefix - self.prefixlen)
        else:
            # find containing block size for subnet, and corresponding hosts
            nhost_bits = math.log2(address_space_size/subnets)
            nhost_bits = math.floor(nhost_bits)
            new_prefix = 32 - nhost_bits
            nsubnets = math.pow(2, new_prefix - self.prefixlen)
        return nsubnets