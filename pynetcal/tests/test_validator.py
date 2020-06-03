"""Tests for the validator.py module"""

import pytest
import pynetcal.validator as validator


# Tests for ipv4address function
@pytest.mark.parametrize("address, expected_result",
    [
        ["192.168.1.0", True],
        ["10.1.0.1", True], 
        ["100.10.6.125", True],

        ["500.6.7.6", False],
        ["104.4.4.1003", False],
        ["90.1.1.256", False]
    ]
)
def test_ipv4address(address, expected_result):
    result = validator.ipv4address(address)
    assert result == expected_result




# Tests for ipv6address function
@pytest.mark.parametrize("address, expected_result",
    [
        ["ffa0::0ac1", True],
        ["f0::", True], 
        ["::", True],
        ["::01a", True],
        ["ac1a:0ac:112::0ac1", True],

        ["xka::ac", False],
        ["90av::", False],
        ["902a::9a3::", False],
        ["ac12::091a:fc12a", False]
    ]
)
def test_ipv6address(address, expected_result):
    result = validator.ipv6address(address)
    assert result == expected_result








# Tests for ipv4network function
@pytest.mark.parametrize("network, expected_result",
    [
        ["192.168.1.0/24", True],
        ["192.168.0.0/20", True],
        ["10.1.0.0/20", True],
        ["217.0.0.0/255.255.0.0", True],
        
        ["180.168.1.0/90", False],
        ["105.60.1.0/255.254.0.0", False],
        ["165.1.1.251/255.255.255.254", False],
        ["1920.168.1.0/24", False]
    ]
)
def test_ipv4network(network, expected_result):
    result = validator.ipv4network(network)
    assert result == expected_result







# Tests for ipv6network function
@pytest.mark.parametrize("network, expected_result",
    [
        ["ffa0::/80", True],
        ["ffa0::/90", True],
        ["ffa0:15ac:1671:ac1::/100", True],
        ["1ca3:ac45::/80", True],

        ["ffa0::/130", False],
        ["::x901a:0000/124", False],
        ["::0ac:1::/2", False],
        ["192.168.ac.134f", False],
    ]
)
def test_ipv6network(network, expected_result):
    result = validator.ipv6network(network)
    assert result == expected_result





# Tests for integer function
@pytest.mark.parametrize("integer, expected_result",
    [
        ["67", True],
        ["109", True],
        ["10", True],
        [190, True],
        [12, True],

        ["109.3", False],
        ["10.4", False],
        ["109.28934", False],
        [103.87, False], 
        [10.34, False]
    ]
)
def test_integer(integer, expected_result):
    result = validator.integer(integer)
    assert result == expected_result