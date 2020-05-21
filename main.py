"""PyNetcal main module

Usage:
  pynetcal subnetter flsm <network-address> <hosts> <subnets> [--priority=(hosts|subnets)]
  pynetcal subnetter vlsm <network-address> <subnet-size>...
  pynetcal ipv4 <ip-address> (--to-binary|--to-decimal|--to-hex|--class|--hosts|--subnets)
  pynetcal (-h | --help)
  pynetcal --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
from ipaddress import IPv4Network
import json

from pynetcal.pynetcal import PyNetcal
import pynetcal.cli_helpers as helpers



# retrieve arguments from CLI
arguments = docopt(__doc__,version=None)
#print(arguments)

# perform an action based on the commands
# and options passed from the CLI.

if(arguments["--version"]):
	helpers.show_version()

elif(arguments['subnetter']):
	# do subnetting.
	if(arguments['flsm']):
		# do FLSM subnetting
		network = arguments['<network-address>']
		hosts = arguments['<hosts>']
		subnets = arguments['<subnets>']
		if(arguments['--priority'] is 'hosts'):
			priorityHosts = True
		else:
			priorityHosts = False
			subnetList = PyNetcal.ipv4_calculate_subnets_flsm(
			IPv4Network(network),
			int(hosts),
			int(subnets),
			priorityHosts)
		helpers.show_subnet_table(network, hosts, subnetList)
	elif(arguments['vlsm']):
		# do VLSM subnetting
		network = arguments['<network-address>']
		hosts = arguments['<subnet-size>']
		hosts = list(map(lambda i: int(i), hosts))
		try:
			subnetList = PyNetcal.ipv4_calculate_subnets_vlsm(
				IPv4Network(network), 
				hosts
			)
			helpers.show_subnet_table(network, hosts, subnetList)
		except ValueError:
			helpers.show_error("Specified number of hosts or subnets cannot be accommodated")
elif(arguments['ipv4']):
	# do ipconvert.
	print("Doing ipconvert")