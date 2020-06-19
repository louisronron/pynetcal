![PyNetcal](res/header.png)

# Usage



## 1.0. Command Syntax

```shell
$ pynetcal subnetter flsm <network-address> <hosts> <subnets> [--priority=(hosts|subnets)] [--limit=<subnet-limit>]
$ pynetcal subnetter vlsm <network-address> <subnet-size>...
$ pynetcal ip <ip-address> [--dec-to-bin| --dec-to-hex| --bin-to-dec| --bin-to-hex| --hex-to-dec| --hex-to-bin| --check]
$ pynetcal version
```



## 2.0. Subnetter Tool

The `subnetter` command allows you to create subnets via both FLSM and VLSM. The tool supports IPv4 and IPv6.

### 2.1. Commands

- `subnetter`

### 2.2. Sub-commands

- `flsm`
- `vlsm`

### 2.3. Arguments

- `<network-address` is an IPv4 or IPv6 network address with its network mask in CIDR or full-form. Examples: *192.168.1.0/24, 192.168.0.0/255.255.0.0, ff0a::/90*, etc.
- `<hosts>` the number of hosts.
- `<subnets>` the number of subnets.

### 2.4. Options

- `--priority` can be specified as either `hosts` or `subnets`. If not specified, the default is `hosts`.
- `--limit` allows you to specify the maximum subnets to display when subnetting a network into multiple smaller networks. If not specified, all the subnets are shown.

### 2.5. Examples

```shell
$ pynetcal subnetter flsm 192.168.1.0/24 17 5 --priority=hosts
$ pynetcal subnetter flsm 10.0.0.0/20 500 7 --priority=subnets
$ pynetcal subnetter vlsm 192.168.1.0/24 70 40 10
$ pynetcal subnetter vlsm 10.0.0.0/20 200 6 70 5
$ pynetcal subnetter flsm fa05::/105 10000 8 --priority=subnets
$ pynetcal subnetter vlsm fa05::/105 100000 54000 1000 2345
$ pynetcal subnetter flsm f0ac::/90 2 100 --limit=6
```





## 3.0. IP Tool

The `ip` command allows for general IP address, and network manipulation such as conversions, and validity checks.

### 3.1. Commands

- `ip`

### 3.2. Arguments

- `<ip-address>` is an IPv4 or IPv6 address.

### 3.3. Options

- `--check` checks the validity of an IP address.
- `--dec-to-bin` converts an IP address from decimal to binary form.
- `--dec-to-hex` converts an IP address from decimal to hexadecimal form.
- `--bin-to-dec` converts an IP address from binary to decimal form.
- `--bin-to-hex` converts an IP address from binary to hexadecimal form.
- `--bin-to-hex` converts an IP address from binary to hexadecimal form.
- `--hex-to-dec` converts an IP address from hexadecimal to decimal form.
- `--hex-to-bin` converts an IP address from hexadecimal to binary form.

### 3.4. Examples

IP address, network information;

```shell
$ pynetcal ip 192.168.1.0
$ pynetcal ip 10.1.0.0/20
$ pynetcal ip ff00::
$ pynetcal ip ::01ac:109c
$ pynetcal ip ac1:fac1:908f::/100
```

IP address conversion;

```shell
$ pynetcal ip 192.168.1.16 --dec-to-bin
$ pynetcal ip 172.17.16.67 --dec-to-hex
$ pynetcal ip 10.5.67.1 --dec-to-bin
$ pynetcal ip ff.ff.ff.00 --hex-to-dec
$ pynetcal ip 10101111.10000000.10101111.10111100 --bin-to-dec

$ pynetcal ip f0ac:: --hex-to-dec
$ pynetcal ip ::09ac:1045:a000 --hex-to-bin
$ pynetcal ip 1456::9081:1718 --dec-to-hex
$ pynetcal ip 1000000000000001::1111000010101100 --bin-to-hex
```

