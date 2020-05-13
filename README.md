![PySubnetter](res/header.png)

# PySubnetter

## Introduction

**PySubnetter** is a lightweight, simple CLI tool for generating IPv4 subnets. It is open source, and written in Python. The program basically wraps the powerful Python IP and networking libraries to create a straightforward approach to subnetting. It is suitable for students studying networking such as CISCO CCNA, but may even be useful to the seasoned network professional. I dedicate this tool to the Divine Word University students from the *Mathematics and Computing Science (MCS)*, and *Information Systems (IS)* departments'; subnetting can be a little nerve-wrecking at first, but it gets easier. I hope this tool helps you a little. *Stap Ston Ol Pikinini Diwai!*

## Installation

### Windows

Instructions for how to install on Windows here.

### Ubuntu (Linux)

Instructions for how to install on Ubuntu here.

## Example

Here is a quick example to get you started with PySubnetter.

### a) Generate subnets by number of hosts

```
$ pysubnetter 192.168.0.0/255.255.0.0 --hosts 2800
```

Sample Output:

```shell
                            _                   _    _              
                           | |                 | |  | |             
  _ __   _   _  ___  _   _ | |__   _ __    ___ | |_ | |_  ___  _ __ 
 | '_ \ | | | |/ __|| | | || '_ \ | '_ \  / _ \| __|| __|/ _ \| '__|
 | |_) || |_| |\__ \| |_| || |_) || | | ||  __/| |_ | |_|  __/| |   
 | .__/  \__, ||___/ \__,_||_.__/ |_| |_| \___| \__| \__|\___||_|   
 | |      __/ |                                                     
 |_|     |___/                                                      

Developed by Louis Ronald, (C) 2020.
https://github.com/louisronron/pysubnetter	
Distributed under GPLv3


#     NETWORK             MASK                TOTAL HOSTS         HOSTMIN             HOSTMAX             BROADCAST           
0     192.168.0.0/20      255.255.240.0       4094                192.168.0.1         192.168.15.254      192.168.15.255      
1     192.168.16.0/20     255.255.240.0       4094                192.168.16.1        192.168.31.254      192.168.31.255      
2     192.168.32.0/20     255.255.240.0       4094                192.168.32.1        192.168.47.254      192.168.47.255      
3     192.168.48.0/20     255.255.240.0       4094                192.168.48.1        192.168.63.254      192.168.63.255      
4     192.168.64.0/20     255.255.240.0       4094                192.168.64.1        192.168.79.254      192.168.79.255      
5     192.168.80.0/20     255.255.240.0       4094                192.168.80.1        192.168.95.254      192.168.95.255      
6     192.168.96.0/20     255.255.240.0       4094                192.168.96.1        192.168.111.254     192.168.111.255     
7     192.168.112.0/20    255.255.240.0       4094                192.168.112.1       192.168.127.254     192.168.127.255     
8     192.168.128.0/20    255.255.240.0       4094                192.168.128.1       192.168.143.254     192.168.143.255     
9     192.168.144.0/20    255.255.240.0       4094                192.168.144.1       192.168.159.254     192.168.159.255     
10    192.168.160.0/20    255.255.240.0       4094                192.168.160.1       192.168.175.254     192.168.175.255     
11    192.168.176.0/20    255.255.240.0       4094                192.168.176.1       192.168.191.254     192.168.191.255     
12    192.168.192.0/20    255.255.240.0       4094                192.168.192.1       192.168.207.254     192.168.207.255     
13    192.168.208.0/20    255.255.240.0       4094                192.168.208.1       192.168.223.254     192.168.223.255     
14    192.168.224.0/20    255.255.240.0       4094                192.168.224.1       192.168.239.254     192.168.239.255     
15    192.168.240.0/20    255.255.240.0       4094                192.168.240.1       192.168.255.254     192.168.255.255     

```



### b) Generate subnets by specified number of subnets

```
$ pysubnetter 192.168.0.0/255.255.0.0 --subnets 5
```

Sample Output:

```shell
                            _                   _    _              
                           | |                 | |  | |             
  _ __   _   _  ___  _   _ | |__   _ __    ___ | |_ | |_  ___  _ __ 
 | '_ \ | | | |/ __|| | | || '_ \ | '_ \  / _ \| __|| __|/ _ \| '__|
 | |_) || |_| |\__ \| |_| || |_) || | | ||  __/| |_ | |_|  __/| |   
 | .__/  \__, ||___/ \__,_||_.__/ |_| |_| \___| \__| \__|\___||_|   
 | |      __/ |                                                     
 |_|     |___/                                                      

Developed by Louis Ronald, (C) 2020.
https://github.com/louisronron/pysubnetter	
Distributed under GPLv3


#     NETWORK             MASK                TOTAL HOSTS         HOSTMIN             HOSTMAX             BROADCAST           
0     192.168.0.0/19      255.255.224.0       8190                192.168.0.1         192.168.31.254      192.168.31.255      
1     192.168.32.0/19     255.255.224.0       8190                192.168.32.1        192.168.63.254      192.168.63.255      
2     192.168.64.0/19     255.255.224.0       8190                192.168.64.1        192.168.95.254      192.168.95.255      
3     192.168.96.0/19     255.255.224.0       8190                192.168.96.1        192.168.127.254     192.168.127.255     
4     192.168.128.0/19    255.255.224.0       8190                192.168.128.1       192.168.159.254     192.168.159.255     
5     192.168.160.0/19    255.255.224.0       8190                192.168.160.1       192.168.191.254     192.168.191.255     
6     192.168.192.0/19    255.255.224.0       8190                192.168.192.1       192.168.223.254     192.168.223.255     
7     192.168.224.0/19    255.255.224.0       8190                192.168.224.1       192.168.255.254     192.168.255.255    
```



### c) More Examples

```shell
$ pysubnetter 192.168.0.0/255.255.0.0 --subnets 10
$ pysubnetter 192.168.0.0/255.255.0.0 --hosts 780
$ pysubnetter 192.168.0.0/16 --hosts 950
$ pysubnetter 192.168.1.0/24 --hosts 40
```

# Licensed

The project is maintained by Louis Ronald, and developed under the [GPLv3 License](LICENSE).







