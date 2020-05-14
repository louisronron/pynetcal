from ipaddress import IPv4Address, IPv4Network

class IPv4SubnetMask:
    def __init__(self,mask):
        # first validate passed arguments
        validated=self.validate_args(mask)
        if(validated):
            self.mask = mask
            self.prefix = self.calculate_prefix()
            self.decimal = self.calculate_decimal()
            self.binary = self.calculate_binary()
            self.total_hosts = 0
            self.total_subnets = 0
            self.address_class = ""
    
    def validate_args(self, mask):
        if(not isinstance(mask, IPv4Address)):
            raise TypeError("'mask' should be of type ipaddress.IPv4Address")
        else:
            return True
    
    def calculate_prefix(self):
        mask_str = str(self.mask)
        count_1s = mask_str.count("1")
        return str(count_1s)


    def calculate_decimal(self):
        mask_str = str(self.mask)
        return mask_str

    def calculate_binary(self):
        mask_str = str(self.mask)
        o1,o2,o3,o4 = list(map(lambda x: int(x), mask_str.split(".")))
        o1 = bin(o1).replace("0b","")+"."
        o2 = bin(o2).replace("0b","")+"."
        o3 = bin(o3).replace("0b","")+"."
        o4 = bin(o4).replace("0b","")
        binary_str = o1+o2+o3+o4
        return binary_str
