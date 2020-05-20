from ipaddress import IPv4Address, IPv4Network
import pysubnetter.ipv4networkclasses as ipv4helper
from pysubnetter.ipv4subnet import IPv4Subnet
from pysubnetter.ipv4subnetlist import IPv4SubnetList
from pysubnetter.ipv4subnetmask import IPv4SubnetMask

class PySubnetter:

    @classmethod
    def ipv4_calculate_subnets_flsm(self, ipv4network, hosts=None,
        subnets=None, prioritizeHosts=True):
        """Performs optimal FLSM subnetting on
        IPv4Network address passed, Returns IPv4SubnetList
        """
        container_mask = None
        # find the required block size for hosts
        if(prioritizeHosts):
            # find containing block size for hosts, and corresponding subnet
            container_mask = ipv4helper.containing_mask(ipv4network,
            hosts, subnets, prioritizeHosts=True)
        else:
            # find containing block size for subnet, and corresponding hosts
            container_mask = ipv4helper.containing_mask(ipv4network,
            hosts, subnets, prioritizeHosts=False)

        subnetList = IPv4SubnetList()
        new_prefix = container_mask["netbits"]
        for i in range(container_mask["subnets"]):
            subnet = list(ipv4network.subnets(new_prefix=new_prefix))[i]
            subnet = IPv4Subnet(i,subnet)
            subnetList.append(subnet)
        return subnetList

    
    @classmethod
    def ipv4_calculate_subnets_vlsm(self, network, hosts):
        """Performs optimal VLSM subnetting on
        IPv4Network address passed, Returns IPv4SubnetList
        """
        hosts_no = hosts
        hosts_no.sort()
        hosts_no.reverse()

        container_masks = list()
        subnet_list = IPv4SubnetList()

        #find the required containing masks for each hosts no.
        for i in range(len(hosts)):
            # find containing block size for current host no.
            container_mask = ipv4helper.containing_mask(network,
            hosts[i],1, prioritizeHosts=True)
            container_masks.append(container_mask)

        # generate subnets
        network_addr = network.network_address
        for i in range(len(container_masks)):
            container_mask = container_masks[i]
            net_incr = container_mask["hosts"]+2
            netbits = container_mask["netbits"]
            # generate net address for the curr subnet
            net_addr = str(network_addr)\
                +"/"\
                +str(netbits)
            subnet = IPv4Subnet(i,
                IPv4Network(net_addr))
            # add the subnet to subnet list
            subnet_list.append(subnet)
            network_addr += net_incr
        return subnet_list



            
