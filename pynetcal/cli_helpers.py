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




def show_subnet_table(all_subnets):
    """Given a IPv4SubnetList object, shows 
    formatted output of a subnet table in a CLI
    """



    header = """
PyNetcal - A super-simple network calculator
Written by Louis Ronald, GPLv3
==========================================================================
"""


    print(header)
    formatStr = "{: <5}{: <18}{: <17}{: <10}{: <18}{: <18}{: <18}"
    print(clicolors.BOLD+formatStr.format("#","NETWORK","MASK","HOSTS","HOSTMIN","HOSTMAX",
    		      "BROADCAST")+clicolors.ENDC)
    for subnet in all_subnets.subnets:
    	print(formatStr.format(
    		str(subnet.subnet_id),
    		str(subnet.network.network_address),
			str(subnet.mask.decimal),
			str(subnet.hosts),
			str(subnet.host_min),
			str(subnet.host_max),
			str(subnet.broadcast)))

    # total subnets
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



def show_version():
    """Shows the current version running"""
    # extract current version number from build.json file
    json_file = os.path.abspath(os.path.join("build.json"))
    buildJson = open(json_file)
    data = json.load(buildJson)
    # set the current version and display.
    version = data["version"]
    print("PyNetcal, v%s" % (version))