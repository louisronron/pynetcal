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




# class IPv4SubnetTableOutput:
#     """An screen output render class for
#     an IPv4 Subnet table.
#     """

#     def __init__(self, network, subnet_list, table_options):
#         self.subnet_list = subnet_list
#         self.table_options = table_options
#     ############### Work yet to be done here...


def show_subnet_table(netToSubnet, subnetSizes, all_subnets):
    """Given a IPv4SubnetList object, shows 
    formatted output of a subnet table in a CLI
    """

    # display some table general information
    print()
    print("Network: %s" % (netToSubnet))
    subnetSizes = str(subnetSizes)
    subnetSizes = subnetSizes.replace("[","")
    subnetSizes = subnetSizes.replace("]","")
    print("Subnet sizes you specified (hosts): %s" % (subnetSizes))
    print()
    # display subnet table.
    
    formatStr = "{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n{:<14}{:<10}\n"
    # print(clicolors.BOLD+formatStr.format("#","NETWORK","MASK","HOSTS","HOSTMIN","HOSTMAX",
    # 		      "BROADCAST")+clicolors.ENDC)
    for subnet in all_subnets.subnets:
        print("=====================================>")
        print(formatStr.format(
        "Subnet ID:",str(subnet.subnet_id),
        "Network:",str(subnet.network.network_address),
        "Mask:",str(subnet.mask.decimal),
        "Total Hosts:",str(subnet.hosts),
        "HostMin:",str(subnet.host_min),
        "HostMax:",str(subnet.host_max),
        "Broadcast:",str(subnet.broadcast)))

    # total subnets
    print()
    print("Total subnets: %d." %(all_subnets.count()))

    if(all_subnets.count()!=0):
        # smallest subnets
        smallest_subnets = all_subnets.smallest()
        print("Smallest Subnets: ", end="")
        for index in range(smallest_subnets.count()):
            if(index != (smallest_subnets.count()-1)):
                print("Subnet #%s, " % (smallest_subnets.subnets[index].subnet_id),
                    end="")
            else:
                print("Subnet #%s." % (smallest_subnets.subnets[index].subnet_id))
            

        # biggest subnets
        biggest_subnets = all_subnets.biggest()
        print("Biggest Subnets: ", end="")
        for index in range(biggest_subnets.count()):
            if(index != (biggest_subnets.count()-1)):
                print("Subnet #%s, " % (biggest_subnets.subnets[index].subnet_id),
                    end="")
            else:
                print("Subnet #%s." % (biggest_subnets.subnets[index].subnet_id))
        print()











# def show_subnet_table(netToSubnet, subnetSizes, all_subnets):
#     """Given a IPv4SubnetList object, shows 
#     formatted output of a subnet table in a CLI
#     """

#     header = """
# PyNetcal - A super-simple network calculator (GPLv3)
# ===================================================="""

#     print(header)

#     # display some table general information
#     print()
#     print("Network: %s" % (netToSubnet))
#     subnetSizes = str(subnetSizes)
#     subnetSizes = subnetSizes.replace("[","")
#     subnetSizes = subnetSizes.replace("]","")
#     print("Subnet sizes you specified (hosts): %s" % (subnetSizes))
#     print()
#     # display subnet table.
#     formatStr = "{: <5}{: <18}{: <17}{: <10}{: <18}{: <18}{: <18}"
#     print(clicolors.BOLD+formatStr.format("#","NETWORK","MASK","HOSTS","HOSTMIN","HOSTMAX",
#     		      "BROADCAST")+clicolors.ENDC)
#     for subnet in all_subnets.subnets:
#     	print(formatStr.format(
#     		str(subnet.subnet_id),
#     		str(subnet.network.network_address),
# 			str(subnet.mask.decimal),
# 			str(subnet.hosts),
# 			str(subnet.host_min),
# 			str(subnet.host_max),
# 			str(subnet.broadcast)))

#     # total subnets
#     print()
#     print("Total subnets: %d." %(all_subnets.count()))

#     if(all_subnets.count()!=0):
#         # smallest subnets
#         smallest_subnets = all_subnets.smallest()
#         print("Smallest Subnets: ", end="")
#         for index in range(smallest_subnets.count()):
#             if(index != (smallest_subnets.count()-1)):
#                 print("Subnet #%s, " % (smallest_subnets.subnets[index].subnet_id),
#                     end="")
#             else:
#                 print("Subnet #%s." % (smallest_subnets.subnets[index].subnet_id))
            

#         # biggest subnets
#         biggest_subnets = all_subnets.biggest()
#         print("Biggest Subnets: ", end="")
#         for index in range(biggest_subnets.count()):
#             if(index != (biggest_subnets.count()-1)):
#                 print("Subnet #%s, " % (biggest_subnets.subnets[index].subnet_id),
#                     end="")
#             else:
#                 print("Subnet #%s." % (biggest_subnets.subnets[index].subnet_id))
#         print()















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