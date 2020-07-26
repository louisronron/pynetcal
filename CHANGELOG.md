# Changelog
All notable changes to the official PyNetcal project will be documented in this file. The format of this log file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- GUI interface in `GUI.py`

## [1.0.0-beta] - 2020-06-03

### Added

- `pyrequirements.txt` file containing list of dependencies for installation through PIP.
- FLSM and VLSM subnetting calculator for IPv4 and IPv6.
- IPv4, IPv6 address validity check functionality
- IPv4, IPv6 address conversion between binary, hexadecimal, and decimal.
- IPv4, IPv6 address, and network information
- Added a CHANGELOG.md
- Tests modules `test_validator.py`, `test_ipv4pynetcal.py`, `test_ipv6pynetcal.py`.
- `--limit` parameter for subnetting to limit long outputs when subnetting and displaying a very long list of calculated subnets.

### Changed

- Cleaned up the README.md to be more concise and focused
- Fixed bug in the padding of IP addresses in hexadecimal and binary form, in `ipv4pynetcal.py`, in functions `dec_to_hex()` and `dec_to_bin()`.
- exit() to sys.exit() for platform independence.

### Removed
- Old test files from previous experimental versions, `test_ipv4helpers.py`, `test_ipv4subnetlist.py`, `test_ipv4subnet.py`, `test_pynetcal.py`, `test_validator.py`. 





