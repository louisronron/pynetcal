"""The program's main entry-point in this module.


Subnetting FLSM
$ pynetcal 192.168.1.0/24 --hosts 40 --subnets 10

Subnetting VLSM
$ pynetcal 192.168.1.0/24 --hosts 104 5 10 45




"""
from pynetcal.pynetcal import PyNetcal
from ipaddress import IPv4Network

import argparse

# initiate the parser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('network', type=str,
                    help='A valid IPv4 network address and mask.')
parser.add_argument('--hosts', nargs='+', 
    type=int, required=True)
parser.add_argument('--subnets', type=int)
parser.add_argument('--priority', type=str, choices=['hosts', 'subnets'], default='hosts', required=False)
args = parser.parse_args()

# determine mode of subnetting
modeIsFlsm = len(args.hosts)==1
modeIsVlsm = len(args.hosts)!=1

# determine priority parameter (hosts or subnets?)
prioritizeHosts = args.priority == "hosts"

# create the subnetting object
subnetter = PyNetcal()








# format the output to a table of subnets
def output_subnet_table(all_subnets):

	class bcolors:
	    HEADER = '\033[95m'
	    OKBLUE = '\033[94m'
	    OKGREEN = '\033[92m'
	    WARNING = '\033[93m'
	    FAIL = '\033[91m'
	    ENDC = '\033[0m'
	    BOLD = '\033[1m'
	    UNDERLINE = '\033[4m'


	header = r"""
                           _                   _    _              
                          | |                 | |  | |             
 _ __   _   _  ___  _   _ | |__   _ __    ___ | |_ | |_  ___  _ __ 
| '_ \ | | | |/ __|| | | || '_ \ | '_ \  / _ \| __|| __|/ _ \| '__|
| |_) || |_| |\__ \| |_| || |_) || | | ||  __/| |_ | |_|  __/| |   
| .__/  \__, ||___/ \__,_||_.__/ |_| |_| \___| \__| \__|\___||_|   
| |      __/ |                                                     
|_|     |___/                                                      

Developed by Louis Ronald, (C) 2020.
https://github.com/louisronron/pynetcal	
Distributed under GPLv3

"""


	print(header)
	formatStr = "{: <5}{: <18}{: <17}{: <10}{: <18}{: <18}{: <18}"
	print(bcolors.BOLD+formatStr.format("#","NETWORK","MASK","HOSTS","HOSTMIN","HOSTMAX",
			      "BROADCAST")+bcolors.ENDC)
	for subnet in all_subnets.subnets:
		print(formatStr.format(
			str(subnet.subnet_id), #subnet number
			str(subnet.network.network_address), #subnet address
			str(subnet.mask.decimal), #subnet mask
			str(subnet.hosts), # total hosts
			str(subnet.host_min), #host min
			str(subnet.host_max),#host max
			str(subnet.broadcast)))#broadcast
	print()







if(modeIsFlsm):
    # do FLSM subnet
    subnets = subnetter.ipv4_calculate_subnets_flsm(
        IPv4Network(args.network), hosts=args.hosts[0], 
        subnets=args.subnets, prioritizeHosts=prioritizeHosts
    )
    output_subnet_table(subnets)

elif(modeIsVlsm):
    # do VLSM subnetting
    subnets = subnetter.ipv4_calculate_subnets_vlsm(
        IPv4Network(args.network), hosts=args.hosts)
    output_subnet_table(subnets)