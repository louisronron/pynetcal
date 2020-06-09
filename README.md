![PyNetcal](res/header.png)

# PyNetcal

## 1.0. Introduction

**PyNetcal** is a simple IPv4, IPv6 network calculator, written in Python for your CLI. So, once upon a time I decided to have some fun and explore networking tools, and then decided to experiment with a simple subnet calculator; one that's a little simpler than Sipcalc, which may seem a bit too advanced for users without subnetting experience. Enjoy!



## 2.0. Installation

### 2.1. Installers

- Download for Windows



### 2.2. Build from source

Building the project from source has been tested successfully in Ubuntu, and Windows.

1. Install the latest version of [Python](https://www.python.org/downloads/)

2. Install the latest version of [pip](https://pip.pypa.io/en/stable/installing/).

3. Open a terminal and clone this git repository

   ```shell
   $ git clone https://github.com/louisronron/pynetcal
   ```

   Alternatively, you can download source zip, and unzip it to a working location on your local machine.

4. We will need to install a couple of Python dependencies using pip. In the terminal, navigate to the root of the cloned repo, and go

   ```shell
   $ pip install -r pyrequirements.py
   ```

5. Then, initiate the build process using

   ```shell
   $ python build.py
   ```

   The build process generates a couple of things, among them two new directories `/dist` and `/build` in the root directory.

6. In the new `/dist` directory, copy the new `pynetcal` executable created to any location on your machine, and add that location to your environment's `PATH` variable.



## 3.0. Usage

Up to this point, you should have *PyNetcal* successfully installed. You're all set! See [Usage](https://google.com).  



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
  pynetcal subnetter flsm <network-address> <hosts> <subnets> [--priority=(hosts|subnets)] [--limit=<subnet-limit>]
  pynetcal subnetter vlsm <network-address> <subnet-size>...
  pynetcal ip <ip-address> [--dec-to-bin| --dec-to-hex| --bin-to-dec| --bin-to-hex| --hex-to-dec| --hex-to-bin| --check]
  pynetcal version
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


