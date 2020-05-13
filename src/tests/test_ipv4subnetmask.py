import pytest
from pysubnetter.ipv4subnetmask import IPv4SubnetMask

def test_no_arguments():
    with pytest.raises(TypeError):
        IPv4SubnetMask()


