![PyNetcal](res/header.png)

# PyNetcal

## 1.0. Introduction

**PyNetcal** is a simple IPv4, IPv6 network calculator, written in Python for your CLI. So, once upon a time I decided to have some fun and explore networking tools, and then decided to experiment with a simple subnet calculator; one that's a little simpler than Sipcalc, which may seem a bit too advanced for users without subnetting experience. Enjoy!

## 2.0. Installation

### 3.1. Binary

Binary versions are currently available for Windows and Linux (Ubuntu).

#### 3.1.1. Ubuntu (>= 16.0)

```shell
$ sudo apt-get install pynetcal
```

#### 3.1.2. Windows

Download the executables from  https://www.sourceforge.com/pynetcal

### 3.2. Build from Source

#### 3.2.1. Ubuntu

Build from source instructions for Ubuntu.

#### 3.2.2. Windows

Build from source instructions for Windows.

## 3.0. Usage

First confirm that PyNetcal is installed by opening up a terminal and entering:

```shell
$ pynetcal --version
```

You should get output similar to the following showing version, license, and other information:

```shell
  ____        _   _      _            _ 
 |  _ \ _   _| \ | | ___| |_ ___ __ _| |
 | |_) | | | |  \| |/ _ \ __/ __/ _` | |
 |  __/| |_| | |\  |  __/ || (_| (_| | |
 |_|    \__, |_| \_|\___|\__\___\__,_|_|
        |___/                           
    
...
...
```

### 3.1. Commands syntax

For usage information and commands, open a terminal and enter `$ pynetcal` which should give you something that looks like this;

```shell
Usage:
  pynetcal subnetter --flsm <network-address> <hosts> <subnets> [--priority=(hosts|subnets)]
  pynetcal subnetter --vlsm <network-address> <subnet-size>...
  pynetcal <ip-address> [--dec-to-bin|--dec-to-hex|--bin-to-dec|--bin-to-hex|--hex-to-dec|--hex-to-bin|--check]
  pynetcal (-h | --help)
  pynetcal --version

```

Okay, in the same terminal, let's experiment with some commands!

### 3.2. IP network, and address information

Network and address information is what it is. *PyNetcal* shows you general information about an IP address or even a network address in your terminal.

```shell
$ pynetcal 192.168.1.0
$ pynetcal 10.1.0.0/20
$ pynetcal ff00::
$ pynetcal ::01ac:109c
$ pynetcal ac1:fac1:908f::/100
```

### 3.3. IP address Conversion

Use *PyNetcal* to easily convert IP addresses both IPv4, IPv6 into a binary, decimal, and hexadecimal forms.

```shell
$ pynetcal 192.168.1.16 --dec-to-bin
$ pynetcal 172.17.16.67 --dec-to-hex
$ pynetcal 10.5.67.1 --dec-to-bin
$ pynetcal ff.ff.ff.00 --hex-to-dec
$ pynetcal 10101111.10000000.10101111.10111100 --bin-to-dec

$ pynetcal f0ac:: --hex-to-dec
$ pynetcal ::09ac:1045:a000 --hex-to-bin
$ pynetcal 1456::9081:1718 --dec-to-hex
$ pynetcal 1000000000000001::1111000010101100 --bin-to-hex
```

### 3.4. Network Subnetting

Perform subnetting for both IPv4 or IPv6 networks, either using the FLSM or VLSM mode. Since network block sizes are essentially powers of two, *PyNetcal* also uses what you specify as `--priority` ("hosts" or "subnets") to determine whether to break a network up by number of hosts or number of subnets.

**Syntax for FLSM;**

```shell
$ pynetcal subnetter --flsm <network-address> <number of hosts> <number of subnets> [--priority=(hosts|subnets)]
```

**Syntax for VLSM;**

```shell
$ pynetcal subnetter --vlsm <network-address> <subnet host sizes>...
```

**Examples;**

```shell
$ pynetcal subnetter --flsm 192.168.1.0/24 17 5 --priority=hosts
$ pynetcal subnetter --flsm 10.0.0.0/20 500 7 --priority=subnets

$ pynetcal subnetter --vlsm 192.168.1.0/24 70 40 10
$ pynetcal subnetter --vlsm 10.0.0.0/20 200 6 70 5

$ pynetcal subnetter --flsm fa05::/105 10000 8 --priority=subnets
$ pynetcal subnetter --vlsm fa05::/105 100000 54000 1000 2345
```



## 4.0. Help keep my coffee pot full?

I don't like to beg, but I do like coffee while writing code. If you found my project helpful and want to give me all of your money lol, consider making a donation...if for anything, to help keep my coffee pot full lol!