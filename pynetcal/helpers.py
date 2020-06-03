"""Helper function handlers, contants, and helpers
that provide support to the CLI implementation in main
"""

import json
import os

class clicolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def show_ipv4_address_stats(pynipv4address):
    """Output some stats and information about
    the PyNIPv4Address object being passed.
    """
    # determine address class
    addrClass = ""
    if(pynipv4address.pn_is_class_a):
        addrClass = "Class A"
    elif(pynipv4address.pn_is_class_b):
        addrClass = "Class B"
    elif(pynipv4address.pn_is_class_c):
        addrClass = "Class C"
    elif(pynipv4address.pn_is_class_d):
        addrClass = "Class D"
    elif(pynipv4address.pn_is_class_e):
        addrClass = "Class E"

    # determine whether address is multicast
    isMulticast = "Yes" if pynipv4address.is_multicast else "No"

    # determine if address is private
    isPrivate = "Yes" if pynipv4address.is_private else "No"

    # determine if address is global
    isGlobal = "Yes" if pynipv4address.is_global else "No"
    
    # determine if address is reserved
    isReserved = "Yes" if pynipv4address.is_reserved else "No"
    
    # determine if address is loopback address
    isLoopback = "Yes" if pynipv4address.is_loopback else "No"
    
    # determine if address is link local
    isLinkLocal = "Yes" if pynipv4address.is_link_local else "No"
    
    
    formatStr = "{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n"
    print("\nAddress Information")
    print("========================================================>")
    print(formatStr.format(
    "IP Address:",pynipv4address.pn_decimal,
    "Binary:",pynipv4address.pn_binary,
    "Hex:",pynipv4address.pn_hexadecimal,
    "Version:", "IP version 4",
    "Class:", addrClass, 
    "Multicast:", isMulticast,
    "Private:", isPrivate,
    "Global:", isGlobal,
    "IETF Reserved:", isReserved,
    "Loopback:", isLoopback,
    "Link Local:", isLinkLocal))


def show_ipv6_address_stats(pynipv6address):
    """Output some stats and information about
    the PyNIPv6Address object being passed.
    """

    # determine whether address is multicast
    isMulticast = "Yes" if pynipv6address.is_multicast else "No"

    # determine if address is private
    isPrivate = "Yes" if pynipv6address.is_private else "No"

    # determine if address is global
    isGlobal = "Yes" if pynipv6address.is_global else "No"
    
    # determine if address is reserved
    isReserved = "Yes" if pynipv6address.is_reserved else "No"
    
    # determine if address is loopback address
    isLoopback = "Yes" if pynipv6address.is_loopback else "No"
    
    # determine if address is link local
    isLinkLocal = "Yes" if pynipv6address.is_link_local else "No"


    # breakup the ipv6 address into 8 segments
    bin_segment1 = pynipv6address.binary.split(':')[0]
    bin_segment2 = pynipv6address.binary.split(':')[1]
    bin_segment3 = pynipv6address.binary.split(':')[2]
    bin_segment4 = pynipv6address.binary.split(':')[3]
    bin_segment5 = pynipv6address.binary.split(':')[4]
    bin_segment6 = pynipv6address.binary.split(':')[5]
    bin_segment7 = pynipv6address.binary.split(':')[6]
    bin_segment8 = pynipv6address.binary.split(':')[7]
    
    
    formatStr = "{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n"
    print("\nAddress Information")
    print("========================================================>")
    print(formatStr.format(
    "IP Address:",pynipv6address.hexadecimal,
    "Decimal:",pynipv6address.decimal,
    "Shorthand", pynipv6address.compressed,
    "Version:", "IP version 6",
    "IPv4 Mapped", str(pynipv6address.ipv4_mapped),
    "Multicast:", isMulticast,
    "Private:", isPrivate,
    "Global:", isGlobal,
    "IETF Reserved:", isReserved,
    "Loopback:", isLoopback,
    "Link Local:", isLinkLocal,
    "Binary Segment 1:", bin_segment1,
    "Binary Segment 2:", bin_segment2,
    "Binary Segment 3:", bin_segment3,
    "Binary Segment 4:", bin_segment4,
    "Binary Segment 5:", bin_segment5,
    "Binary Segment 6:", bin_segment6,
    "Binary Segment 7:", bin_segment7,
    "Binary Segment 8:", bin_segment8))


def show_ipv4_network_stats(pynipv4network):
    """Output some stats and information about
    the PyNIPv4Network object being passed.
    """

    # get ip address from network address
    pynipv4address = pynipv4network.pn_network_address

    # show the ip address information
    show_ipv4_address_stats(pynipv4address)

    # now show the network information
    formatStr = "{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n{:<19}{:<10}\n"
    
    print("\nNetwork Information")
    print("========================================================>")
    print(formatStr.format(
        "Network:", str(pynipv4network),
        "Broadcast", str(pynipv4network.broadcast_address),
        "Hostmask", str(pynipv4network.pn_hostmask),
        "Netmask", str(pynipv4network.pn_netmask),
        "Prefix", str(pynipv4network.prefixlen),
        "Total Addresses", str(pynipv4network.num_addresses),
        "Total Hosts", str(pynipv4network.pn_hosts),
        "Host Min", str(pynipv4network.pn_hostmin),
        "Host Max", str(pynipv4network.pn_hostmax),
        "Max Prefix Len", str(pynipv4network.max_prefixlen)))





def show_ipv4_subnet_table(netToSubnet, subnetSizes, num_of_subnets, all_subnets):
    """Given a IPv4SubnetList object, shows 
    formatted output of a subnet table in a CLI
    """

    # display some table general information
    print()
    print("Network: %s" % (netToSubnet))
    subnetSizes = str(subnetSizes)
    subnetSizes = subnetSizes.replace("[","")
    subnetSizes = subnetSizes.replace("]","")
    print("Specified number of hosts: %s" % (subnetSizes))
    print("Specified number of subnets: %s" % (num_of_subnets))
    print()
    # display subnet table.
    
    formatStr = "{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n"
    # print(clicolors.BOLD+formatStr.format("#","NETWORK","MASK","HOSTS","HOSTMIN","HOSTMAX",
    # 		      "BROADCAST")+clicolors.ENDC)
    i = 0
    for subnet in all_subnets:
        print("=====================================>")
        print(formatStr.format(
        "Subnet ID:",str(i),
        "Network:",str(subnet.pn_network_address),
        "Mask:",str(subnet.pn_netmask),
        "Total Hosts:",str(subnet.pn_hosts),
        "HostMin:",str(subnet.pn_hostmin),
        "HostMax:",str(subnet.pn_hostmax),
        "Broadcast:",str(subnet.broadcast_address)))
        i += 1
    # total subnets
    print()
    print("Total subnets: %d." %(len(all_subnets)))




def show_ipv6_subnet_table(netToSubnet, subnetSizes, num_of_subnets, all_subnets):
    """Given a IPv6SubnetList object, shows 
    formatted output of a subnet table in a CLI
    """

    # display some table general information
    print()
    print("Network: %s" % (netToSubnet))
    subnetSizes = str(subnetSizes)
    subnetSizes = subnetSizes.replace("[","")
    subnetSizes = subnetSizes.replace("]","")
    print("Specified number of hosts: %s" % (subnetSizes))
    print("Specified number of subnets: %s" % (num_of_subnets))
    print()
    # display subnet table.
    
    formatStr = "{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n"
    # print(clicolors.BOLD+formatStr.format("#","NETWORK","MASK","HOSTS","HOSTMIN","HOSTMAX",
    # 		      "BROADCAST")+clicolors.ENDC)
    i = 0
    for subnet in all_subnets:
        print("=====================================>")
        print(formatStr.format(
        "Subnet ID:",str(i),
        "Network:",str(subnet.pn_network_address),
        "Mask:",str(subnet.pn_netmask),
        "Total Hosts:",str(subnet.pn_hosts),
        "HostMin:",str(subnet.pn_hostmin),
        "HostMax:",str(subnet.pn_hostmax)))
        i += 1
    # total subnets
    print()
    print("Total subnets: %d." %(len(all_subnets)))




def show_version():
    header=r"""
  ____        _   _      _            _ 
 |  _ \ _   _| \ | | ___| |_ ___ __ _| |
 | |_) | | | |  \| |/ _ \ __/ __/ _` | |
 |  __/| |_| | |\  |  __/ || (_| (_| | |
 |_|    \__, |_| \_|\___|\__\___\__,_|_|
        |___/                           
    """
    """Shows the current version running"""
    # extract current version number from build.json file
    json_file = os.path.abspath(os.path.join("build.json"))
    buildJson = open(json_file)
    data = json.load(buildJson)
    # set the current version and display.
    version = data["version"]
    print(header)
    print(" PyNetcal, v%s" % (version))
    print(" Written by Louis Ronald, under GPLv3")
    print(" PyNetcal is a simple network calculator.")
    print(" Official source repo: https://github.com/louisronron/pynetcal")
    print()




def show_error(msg):
    """Shows error in standard format
    with passed message.
    """
    print("Error: %s" % (msg))