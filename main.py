"""PyNetcal main module

Usage:
  pynetcal subnetter --flsm <network-address> <hosts> <subnets> [--priority=(hosts|subnets)]
  pynetcal subnetter --vlsm <network-address> <subnet-size>...
  pynetcal <ip-address> [--dec-to-bin|--dec-to-hex|--bin-to-dec|--bin-to-hex|--hex-to-dec|--hex-to-bin|--check]
  pynetcal (-h | --help)
  pynetcal --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --priority	Specifies whether to prioritize hosts or subnets in subnetting [default: hosts].
"""

from docopt import docopt
import ipaddress
import json

from ipaddress import IPv4Network, IPv4Address, IPv6Network, IPv6Address
import pynetcal.helpers as helpers
import pynetcal.validator as validator
from pynetcal.ipv6pynetcal import PyNIPv6Address, PyNIPv6Network
from pynetcal.ipv4pynetcal import PyNIPv4Address, PyNIPv4Network

# retrieve arguments from CLI
arguments = docopt(__doc__,version=None)


# perform an action based on the commands
# and options passed from the CLI.


if(arguments["--version"]):
	# show the app version.
	header=r"""
  ____        _   _      _            _ 
 |  _ \ _   _| \ | | ___| |_ ___ __ _| |
 | |_) | | | |  \| |/ _ \ __/ __/ _` | |
 |  __/| |_| | |\  |  __/ || (_| (_| | |
 |_|    \__, |_| \_|\___|\__\___\__,_|_|
		|___/                           
	"""
	"""Shows the current version running"""
	# set the current version and display.
	version = "1.0.0"
	print(header)
	print(" PyNetcal, v%s" % (version))
	print(" Written by Louis Ronald, under GPLv3")
	print(" PyNetcal is a simple network calculator.")
	print(" Official source repo: https://github.com/louisronron/pynetcal")
	print()


elif(arguments['subnetter']):
	# do subnetting.
	if(arguments['--flsm']):
		# do FLSM subnetting

		# retrieve arguments passed
		network = arguments['<network-address>']
		hosts = arguments['<hosts>']
		subnets = arguments['<subnets>']

		# do some validation first
		if(not validator.ipv4network(network) and not validator.ipv6network(network)):
			helpers.show_error("IPv4/IPv6 network address you supplied is invalid.")
			exit(1)
		elif(not validator.integer(hosts)):
			helpers.show_error("number of <hosts> specified must be an integer.")
			exit(1)
		elif(not validator.integer(subnets)):
			helpers.show_error("number of <subnets> specified must be an integer.")
			exit(1)

		is_ipv4 = validator.ipv4network(network)
		is_ipv6 = validator.ipv6network(network)
		
		# all good continue with code.
		if(arguments['--priority']=='hosts'):
			priorityHosts = True
		elif(arguments['--priority']=='subnets'):
			priorityHosts = False
		elif(arguments['--priority']==None):
			priorityHosts = True
		else:
			priorityHosts = True
		
		subnetList = list()
		if(is_ipv4):
			subnetList = PyNIPv4Network(network).subnets_flsm(
			int(hosts),
			int(subnets),
			priorityHosts)
			helpers.show_ipv4_subnet_table(network, hosts, subnets, subnetList)
		if(is_ipv6):
			subnetList = PyNIPv6Network(network).subnets_flsm(
			int(hosts),
			int(subnets),
			priorityHosts)
			helpers.show_ipv6_subnet_table(network, hosts, subnets, subnetList)
		


	elif(arguments['--vlsm']):
		# do VLSM subnetting
		
		# retrieve the arguments passed
		network = arguments['<network-address>']
		hosts = arguments['<subnet-size>']
		
		
		# do some validation on the arguments
		if(not validator.ipv4network(network) and not validator.ipv6network(network)):
			helpers.show_error("IPv4/IPv6 network address you supplied is invalid.")
			exit(1)

		for host in hosts:
			if(not validator.integer(host)):
				helpers.show_error("All <hosts> numbers must all be integers")
				exit(1)

		is_ipv4 = validator.ipv4network(network)
		is_ipv6 = validator.ipv6network(network)


		# Now, get to work on VLSM.
		hosts = list(map(lambda i: int(i), hosts))
		try:
			if(is_ipv4):
				subnetList = PyNIPv4Network(network).subnets_vlsm(hosts)
				helpers.show_ipv4_subnet_table(network, hosts, len(hosts), subnetList)
			elif(is_ipv6):
				subnetList = PyNIPv6Network(network).subnets_vlsm(hosts)
				helpers.show_ipv6_subnet_table(network, hosts, len(hosts), subnetList)

		except ValueError:
			helpers.show_error("Specified number of hosts or \
				subnets cannot be accommodated")
			exit(1)
				





elif(arguments['<ip-address>']):
	# do ipv4 manipulation tasks.
	# # validation, and determine if ipv6 or ipv4
	

	if(arguments["--dec-to-bin"]):
		address = arguments['<ip-address>']
		#do some validation on the arguments
		is_ipv4, is_ipv6 = False, False
		try:
			PyNIPv6Address(address)
			is_ipv6 = True
		except:
			is_ipv6 = False
		try:
			PyNIPv4Address(address)
			is_ipv4 = True
		except:
			is_ipv4 = False
		# go ahead for either ipv4 or ipv6
		if(is_ipv4):
			print(PyNIPv4Address(address).pn_binary)
		elif(is_ipv6):
			print(PyNIPv6Address(address).binary)
		else:
			helpers.show_error("IP address entered is not a valid IPv6 or IPv4 address")
			exit(1)


	elif(arguments["--dec-to-hex"]):
		address = arguments['<ip-address>']
		#do some validation on the arguments
		is_ipv4, is_ipv6 = False, False
		try:
			PyNIPv6Address(address)
			is_ipv6 = True
		except:
			is_ipv6 = False
		try:
			PyNIPv4Address(address)
			is_ipv4 = True
		except:
			is_ipv4 = False
		# go ahead for either ipv4 or ipv6
		if(is_ipv4):
			print(PyNIPv4Address(address).pn_hexadecimal)
		elif(is_ipv6):
			print(PyNIPv6Address(address).hexadecimal)
		else:
			helpers.show_error("IP address entered is not a valid IPv6 or IPv4 address")
			exit(1)


	elif(arguments["--bin-to-dec"]):
		address = arguments['<ip-address>']
		#do some validation on the arguments
		is_ipv4, is_ipv6 = False, False
		try:
			PyNIPv6Address(address)
			is_ipv6 = True
		except:
			is_ipv6 = False
		try:
			PyNIPv4Address(address)
			is_ipv4 = True
		except:
			is_ipv4 = False
		# go ahead for either ipv4 or ipv6
		if(is_ipv4):
			print(PyNIPv4Address(address).pn_decimal)
		elif(is_ipv6):
			print(PyNIPv6Address(address).decimal)
		else:
			helpers.show_error("IP address entered is not a valid IPv6 or IPv4 address")
			exit(1)


	elif(arguments["--bin-to-hex"]):
		address = arguments['<ip-address>']
		#do some validation on the arguments
		is_ipv4, is_ipv6 = False, False
		try:
			PyNIPv6Address(address)
			is_ipv6 = True
		except:
			is_ipv6 = False
		try:
			PyNIPv4Address(address)
			is_ipv4 = True
		except:
			is_ipv4 = False
		# go ahead for either ipv4 or ipv6
		if(is_ipv4):
			print(PyNIPv4Address(address).pn_hexadecimal)
		elif(is_ipv6):
			print(PyNIPv6Address(address).hexadecimal)
		else:
			helpers.show_error("IP address entered is not a valid IPv6 or IPv4 address")
			exit(1)


	elif(arguments["--hex-to-dec"]):
		address = arguments['<ip-address>']
		#do some validation on the arguments
		is_ipv4, is_ipv6 = False, False
		try:
			PyNIPv6Address(address)
			is_ipv6 = True
		except:
			is_ipv6 = False
		try:
			PyNIPv4Address(address)
			is_ipv4 = True
		except:
			is_ipv4 = False
		# go ahead for either ipv4 or ipv6
		if(is_ipv4):
			print(PyNIPv4Address(address).pn_decimal)
		elif(is_ipv6):
			print(PyNIPv6Address(address).decimal)
		else:
			helpers.show_error("IP address entered is not a valid IPv6 or IPv4 address")
			exit(1)


	elif(arguments["--hex-to-bin"]):
		address = arguments['<ip-address>']
		#do some validation on the arguments
		is_ipv4, is_ipv6 = False, False
		try:
			PyNIPv6Address(address)
			is_ipv6 = True
		except:
			is_ipv6 = False
		try:
			PyNIPv4Address(address)
			is_ipv4 = True
		except:
			is_ipv4 = False
		# go ahead for either ipv4 or ipv6
		if(is_ipv4):
			print(PyNIPv4Address(address).pn_binary)
		elif(is_ipv6):
			print(PyNIPv6Address(address).binary)
		else:
			helpers.show_error("IP address entered is not a valid IPv6 or IPv4 address")
			exit(1)


	elif(arguments["--check"]):
		# check that an ip address is a valid ipv4 address

		# fetch arguments to be used here.
		address = arguments['<ip-address>']
		
		# validation of arguments
		if(not validator.ipv4address(address) and
			not validator.ipv6address(address)):
			print("{} is an INVALID IPv4/IPv6 Address".format(address))
		elif(validator.ipv4address(address)):
			print("{} is a VALID IPv4 Address".format(address))
		elif(validator.ipv6address(address)):
			print("{} is a VALID IPv6 Address".format(address))
			

	else:
		# show IP address stats

		# fetch arguments to be used here.
		address = arguments['<ip-address>']
		
		# do some validation on the arguments
		if(not validator.ipv4address(address) and
			not validator.ipv6address(address)):
			helpers.show_error("IPv4/IPv6 address entered is invalid.")
			exit(1)

		# identify whether it is an ipv4 or ipv6
		ip_address = ipaddress.ip_address(address)
		is_ipv4 = isinstance(ip_address, IPv4Address)
		is_ipv6 = isinstance(ip_address, IPv6Address)