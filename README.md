![PySubnetter](res/header.png)

# PySubnetter

## 1.0. Introduction

**PySubnetter** is a lightweight, simple CLI tool for generating IPv4 subnets, and is written in Python. The program is on the standard `ipaddress` module to create a straightforward approach to subnetting. It is suitable for students studying networking such as CISCO CCNA, but may even be useful to the seasoned network professional. I dedicate this tool to the Divine Word University students from the *Mathematics and Computing Science (MCS)*, and *Information Systems (IS)* departments'; subnetting can be a little nerve-wrecking at first, but it gets easier. I hope this tool helps you a little. *Stap Ston Ol Pikinini Diwai!*

## 2.0. Feature Summary

- Supports IPv4 addresses of classes A, B, C.
- FLSM subnetting.
- VLSM subnetting.
- Basic IP Address stats (i.e. address class, network, binary form, etc.)
- Output subnet tables to `.txt` file.



## 3.0. Installation

There are two ways to install and use *PySubnetter*.

### 3.1. Binary

Binary versions are currently available for Windows and Linux (Ubuntu).

#### 3.1.1. Ubuntu (>= 16.0)

```shell
$ sudo apt-get install pysubnetter
```

#### 3.1.2. Windows

Download the executables from  https://www.sourceforge.com/pysubnetter

### 3.2. Build from Source

#### 3.2.1. Ubuntu

Build from source instructions for Ubuntu.

#### 3.2.2. Windows

Build from source instructions for Windows.

## 4.0. How to use

Here is a quick example to get you started with PySubnetter.

### 4.1. FLSM Subnetting

#### 4.1.1. Generate subnets by number of hosts

```
$ pysubnetter 
```

Sample Output:

```shell
Shell output here
```

#### 4.1.2. Generate subnets by specified number of subnets

```
$ pysubnetter
```

Sample Output:

```shell
Shell output here
```

### 4.2. VLSM Subnetting

Still writing



## 6.0. More Example Commands

```shell
$ pysubnetter 192.168.0.0/255.255.0.0 --subnets 10
$ pysubnetter 192.168.0.0/255.255.0.0 --hosts 780
$ pysubnetter 192.168.0.0/16 --hosts 950
$ pysubnetter 192.168.1.0/24 --hosts 40
```

# Licensed

The project is maintained by **Louis Ronald.**

This repository is distributed under [GPLv3 License](LICENSE).







