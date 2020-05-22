![PyNetcal](res/header.png)

# PyNetcal

## 1.0. Introduction

**PyNetcal** is a simple IP network calculator, written in Python for your CLI. It is suitable for students studying networking such as CISCO CCNA, but may even be useful to the seasoned network professional. I dedicate this tool to the Divine Word University students from the *Mathematics and Computing Science (MCS)*, and *Information Systems (IS)* departments'; subnetting can be a little nerve-wrecking at first, but it gets easier. I hope this tool helps you a little. *Stap Ston Ol Pikinini Diwai!*

## 2.0. Feature Summary

- Supports IPv4 addresses, classes A, B, C.
- Subnetting calculator `pynetcal subnetter` for both FLSM, VLSM.
- IPv4 address formatter to decimal, binary, hex using `pynetcal ipv4`

## 3.0. Installation

There are two ways to install and use *PyNetcal*.

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

## 4.0. How to use

Assuming you've successfully installed PyNetcal on your machine, here are some quick example commands you can try that showcases the main features of PyNetcal.

### 4.1. Network Subnetting



#### 4.1.1. FLSM subnetting by host and subnet, prioritizing required hosts.

```shell
$ pynetcal subnetter 192.168.1.0/24 --hosts 15 --subnets 20 --priority hosts
```

#### 4.1.2. FLSM subnetting by host and subnet, prioritizing required subnets.

```shell
$ pynetcal subnetter 192.168.1.0/24 --hosts 15 --subnets 20 --priority subnets
```

#### 4.1.3. VLSM subnetting

```shell
$ pynetcal subnetter 192.168.1.0/24 --hosts 60 53 14 5
```



### 4.2. Address Arithmetic

```shell
$ pynetcal calculator 192.168.1.0 10 --add
```

```shell
$ pynetcal calculator 192.168.0.0 0.0.255.255 --add
```



### 4.3. Address Conversion

#### 4.3.1 IP Address to binary conversion

```shell
$ pynetcal dec2bin 192.168.9.10
```



#### 4.3.2 IP Address to 



## 5.0. Support us with a small donation?

PyNetcal is maintained by **Louis Ronald**, and is intended to be absolutely free for you to use and do whatever, of course, under the [GPLv3 License](LICENSE.md). On the other hand, continuous development does cost, along with administrative expenses. So, I do welcome donations via *PayPal* or *BitCoin* to help continue the project.









