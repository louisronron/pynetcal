![PyNetcal](res/header.png)

# PyNetcal



## 1.0. Introduction

**PyNetcal** is a simple IPv4, IPv6 network calculator, written in Python for your CLI. So, once upon a time I decided to have some fun and explore networking tools, and then decided to experiment with a simple subnet calculator; one that's a little simpler than Sipcalc, which may seem a bit too advanced for users without subnetting experience. Enjoy!



## 2.0. Feature Summary

- IPv4, IPv6 support
- Subnet calculator, supports FLSM and VLSM, with output limiting.
- IP address, and network information.
- IP address conversion between decimal, hexadecimal, and binary.



## 3.0. Installation

### 3.1. Installers

- Download Windows Installer

  

### 3.2. Build from source

#### Requirements

- Python 3.5+
- docopt 0.6.2+
- PyInstaller 3.6+

#### Steps

Building the project from source has been tested successfully in Ubuntu, and Windows.

1. Install the latest version of [Python](https://www.python.org/downloads/)

2. Install the latest version of [pip](https://pip.pypa.io/en/stable/installing/).

3. Open a terminal and clone the git repository

   ```shell
   $ git clone https://github.com/louisronron/pynetcal
   ```

   Alternatively, you can download source zip, and unzip it to a working location on your local machine.

4. We will need to install a couple of Python dependencies using pip. Luckily, all the dependencies are pre-written in the `pyrequirements.txt` file so not much typing for you to do here. In the terminal, navigate to the root of the cloned repo, and enter

   ```shell
   $ pip install -r pyrequirements.txt
   ```

5. Then, initiate the build process using

   ```shell
   $ python build.py
   ```

   The build process generates a couple of things, among them two new directories `/dist` and `/build` in the root directory.

6. In the new `/dist` directory, copy the new `pynetcal` executable created to any location on your machine, and add that location to your environment's `PATH` variable.

You're all set!

To confirm that you've done things correctly, open a new terminal and enter

```shell
$ pynetcal version
```



## 4.0. Usage

Up to this point, you should have *PyNetcal* successfully installed! 

Head over to [Usage](USAGE.md) for all the "how to use *PyNetcal*" content :)



## 5.0. I Love My Coffee <3 

I love my coffee when I am writing code. If you found my project useful, and you're looking for the best way to say thanks, then feel free to help me keep my coffee pot full lol.

