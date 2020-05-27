"""PyNetcal main module

Usage:
  pynetcal subnetter (--flsm|--vlsm) <network-address> ((<hosts> <subnets> [--priority=(hosts|subnets)])|<subnet-size>...)
  pynetcal <ip-address> [--to-binary|--to-decimal|--check]
  pynetcal (-h | --help)
  pynetcal --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --priority	Specifies whether to prioritize hosts or subnets in subnetting [default: hosts].
"""

from docopt import docopt
from ipaddress import IPv4Network, IPv4Address
import json

from pynetcal.ipv4.pynetcal import PyNetcalSubnetter, PyNetcalIPv4
import pynetcal.ipv4.ipv4clihelpers as helpers
import pynetcal.ipv4.validator as validator
import pynetcal.ipv4.ipv4helpers as ipv4helpers



# retrieve arguments from CLI
arguments = docopt(__doc__,version=None)


# perform an action based on the commands
# and options passed from the CLI.


if(arguments["--version"]):
	helpers.show_version()


elif(arguments['subnetter']):
	# do subnetting.
	if(arguments['--flsm']):
		# do FLSM subnetting

		# retrieve arguments passed
		network = arguments['<network-address>']
		hosts = arguments['<hosts>']
		subnets = arguments['<subnets>']

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
		if(arguments['--priority']=='hosts'):
			priorityHosts = True
		elif(arguments['--priority']=='subnets'):
			priorityHosts = False
		elif(arguments['--priority']==None):
			priorityHosts = True
		else:
			priorityHosts = True
		
		subnetList = PyNetcalSubnetter.ipv4_calculate_subnets_flsm(
		IPv4Network(network),
		int(hosts),
		int(subnets),
		priorityHosts)
		helpers.show_subnet_table(network, hosts, subnets, subnetList)

	elif(arguments['--vlsm']):
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
			helpers.show_subnet_table(network, hosts, len(hosts), subnetList)
		except ValueError:
			helpers.show_error("Specified number of hosts or \
				subnets cannot be accommodated")



elif(arguments['<ip-address>']):
	# do ipv4 manipulation tasks.
	# validation, and determine if ipv6 or ipv4
	

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
		print("Binary:",binary)
		print("Octet 1 => %s (%s)" %(octet1,address.split(".")[0]))
		print("Octet 2 => %s (%s)" %(octet1,address.split(".")[1]))
		print("Octet 3 => %s (%s)" %(octet1,address.split(".")[2]))
		print("Octet 4 => %s (%s)" %(octet1,address.split(".")[3]))

	elif(arguments["--to-decimal"]):
		# convert IPv4 binary address to decimal

		# fetch arguments to be used here.
		address = arguments['<ip-address>']
		
		# validation of arguments
		if(not validator.ipv4address_bin(address)):
			helpers.show_error("Binary IPv4 address is invalid.")
			exit(1)
		
		# else, all good, continue.
		converter = PyNetcalIPv4()
		print("Decimal address:", converter.to_decimal(address))
		boct1, boct2, boct3, boct4 = address.split(".")
		oct1, oct2, oct3, oct4 = converter.to_decimal(address).split(".")
		print(boct1,"=>",oct1)
		print(boct2,"=>",oct2)
		print(boct3,"=>",oct3)
		print(boct4,"=>",oct4)

	elif(arguments["--check"]):
		# check that an ip address is a valid ipv4 address

		# fetch arguments to be used here.
		address = arguments['<ip-address>']
		
		# validation of arguments
		if(not validator.ipv4address(address)):
			print("{} is an INVALID IPv4 Address".format(address))
		else:
			print("{} is a VALID IPv4 Address".format(address))

	else:
		# show IP address stats

		# fetch arguments to be used here.
		address = arguments['<ip-address>']
		
		# do some validation on the arguments
		if(not validator.ipv4address(address)):
			helpers.show_error("IPv4 address entered is invalid.")
			exit(1)
		
		# All good, show IP address information
		converter = PyNetcalIPv4()
		print("{:<20}=> {}".format("IP address",address))
		print("{:<20}=> {}".format("Binary form", converter.to_binary(address)))
		print("{:<20}=> {}".format("IP version","IPv4"))
		if(ipv4helpers.is_private(IPv4Address(address))):
			print("{:<20}=> {}".format("IP Type","Private Address"))
		else:
			print("{:<20}=> {}".format("IP Type","Public Address"))
		# determine and show class
		if(ipv4helpers.is_class_A(IPv4Address(address))):
			print("{:<20}=> {}".format("Class","Class A"))
		if(ipv4helpers.is_class_B(IPv4Address(address))):
			print("{:<20}=> {}".format("Class","Class B"))
		if(ipv4helpers.is_class_C(IPv4Address(address))):
			print("{:<20}=> {}".format("Class","Class C"))
		
		
