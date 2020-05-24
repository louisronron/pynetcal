"""PyNetcal main module

Usage:
  pynetcal subnetter flsm <network-address> <hosts> <subnets> [--priority=(hosts|subnets)]
  pynetcal subnetter vlsm <network-address> <subnet-size>...
  pynetcal ipv4 <ip-address> (--to-binary|--to-decimal|--class|--hosts|--subnets)
  pynetcal (-h | --help)
  pynetcal --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
from ipaddress import IPv4Network, IPv4Address
import json

from pynetcal.pynetcal import PyNetcalSubnetter, PyNetcalIPv4
import pynetcal.cli_helpers as helpers
import pynetcal.validator as validator



# retrieve arguments from CLI
arguments = docopt(__doc__,version=None)


# perform an action based on the commands
# and options passed from the CLI.


if(arguments["--version"]):
	helpers.show_version()


elif(arguments['subnetter']):
	# do subnetting.
	
	if(arguments['flsm']):
		# do FLSM subnetting

		# retrieve arguments passed
		network = arguments['<network-address>']
		hosts = arguments['<hosts>']
		subnets = arguments['<subnets>']
		priorityCondition1 = arguments['--priority'] is 'hosts'
		priorityCondition2 = arguments['--priority'] is None

		# do some validation first
		if(not validator.ipv4network(network)):
			helpers.show_error("IPv4 network address you supplied is invalid.")
			exit(1)
		elif(not validator.integer(hosts)):
			helpers.show_error("number of <hosts> specified must be an integer.")
			exit(1)
		elif(not validator.integer(subnets)):
			helpers.show_error("number of <subnets> specified must be an integer.")
			exit(1)
		
		# all good continue with code.
		if(priorityCondition1 or priorityCondition2):
			priorityHosts = True
		else:
			priorityHosts = False
		subnetList = PyNetcalSubnetter.ipv4_calculate_subnets_flsm(
		IPv4Network(network),
		int(hosts),
		int(subnets),
		priorityHosts)
		helpers.show_subnet_table(network, hosts, subnetList)

	elif(arguments['vlsm']):
		# do VLSM subnetting

		# retrieve the arguments passed
		network = arguments['<network-address>']
		hosts = arguments['<subnet-size>']
		
		
		# do some validation on the arguments
		if(not validator.ipv4network(network)):
			pass
		for host in hosts:
			if(not validator.integer(host)):
				helpers.show_error("All <hosts> numbers must all be integers")
				exit(1)

		# Now, get to work on VLSM.
		hosts = list(map(lambda i: int(i), hosts))
		try:
			subnetList = PyNetcalSubnetter.ipv4_calculate_subnets_vlsm(
				IPv4Network(network), 
				hosts
			)
			helpers.show_subnet_table(network, hosts, subnetList)
		except ValueError:
			helpers.show_error("Specified number of hosts or \
				subnets cannot be accommodated")



elif(arguments['ipv4']):
	# do ipv4 manipulation tasks.

	if(arguments["--to-binary"]):
		# convert IPv4 address to binary

		# fetch arguments to be used here.
		address = arguments['<ip-address>']
		
		

		# do some validation on the arguments
		if(not validator.ipv4address(address)):
			helpers.show_error("IPv4 address entered is invalid.")
			exit(1)

		
		converter = PyNetcalIPv4()
		ipv4address = IPv4Address(address)
		binary = converter.to_binary(ipv4address)
		# display binary form with octets
		octet1 = binary.split(".")[0]
		octet2 = binary.split(".")[1]
		octet3 = binary.split(".")[2]
		octet4 = binary.split(".")[3]
		print("Original:",address)
		print("Binary:",binary)
		print("Octet 1:", octet1)
		print("Octet 2:", octet2)
		print("Octet 3:", octet3)
		print("Octet 4:", octet4)

	elif(arguments["--to-decimal"]):
		# convert IPv4 binary address to decimal

		# fetch arguments to be used here.
		address = arguments['<ip-address>']
		
		# validation of arguments
		if(not validator.ipv4address_bin(address)):
			helpers.show_error("Binary IPv4 address is invalid.")
			exit(1)
		
		# else, all good, continue.
		
		