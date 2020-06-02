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

    # if(all_subnets.count()!=0):
    #     # smallest subnets
    #     smallest_subnets = all_subnets.smallest()
    #     print("Smallest Subnets: ", end="")
    #     for index in range(smallest_subnets.count()):
    #         if(index != (smallest_subnets.count()-1)):
    #             print("%s, " % (smallest_subnets.subnets[index].subnet_id),
    #                 end="")
    #         else:
    #             print("%s." % (smallest_subnets.subnets[index].subnet_id))
            

    #     # biggest subnets
    #     biggest_subnets = all_subnets.biggest()
    #     print("Biggest Subnets: ", end="")
    #     for index in range(biggest_subnets.count()):
    #         if(index != (biggest_subnets.count()-1)):
    #             print("%s, " % (biggest_subnets.subnets[index].subnet_id),
    #                 end="")
    #         else:
    #             print("%s." % (biggest_subnets.subnets[index].subnet_id))
    #     print()





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