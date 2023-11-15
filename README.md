# Crazyflie - Autonomous Flight

This branch contains two files `closed_trajectory.py` and `random_trajectory.py`, that are used to test the autonomous flight of the Crazyflie via commands.

## Pre-requirements

- [Python 3](https://www.python.org/downloads/)
- [cflib](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/installation/install/)

## Hardware requirements
- The [Crazyflie 2.0](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/) fully assembled.
- The [Flow Deck V2](https://www.bitcraze.io/products/flow-deck-v2/) attached to the Crazyflie. 
- A [Crazyradio PA](https://www.bitcraze.io/products/crazyradio-pa/) to send the commands to the Crazyflie 2.0.

## Building and flashing

For more details about this instructions you can go to this [link](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/building-and-flashing/build/). Make sure to have the Crazyradio connected to your PC.

### 1. Install a toolchain

#### MacOS:

```shell
brew tap PX4/homebrew-px4
brew install gcc-arm-none-eabi
```

#### Ubuntu 20.04 or 22.04

```shell
sudo apt-get install make gcc-arm-none-eabi
```

#### Ubuntu 20.04 or 22.04

```shell
sudo add-apt-repository ppa:team-gcc-arm-embedded/ppa
sudo apt-get update
sudo apt install gcc-arm-embedded
```

#### Arch Linux

```shell
$ sudo pacman -S community/arm-none-eabi-gcc community/arm-none-eabi-gdb community/arm-none-eabi-newlib
```
#### Windows

The supported way to build the Crazyflie on Windows is to use the Windows Subsystem for Linux (WSL) on Windows 10+. This means that development happens in a Linux environment. Flashing is handled by installing Python and the Crazyflie client on Windows launched from linux.

To get started you need to enable WSL and install an Ubuntu system. This can be done by opening power shell as administrator and typing:

```shell
wsl --install
```

Then follow the install instruction for Ubuntu 20.04 above to install the required build dependencies.

For flashing you need to install Python (=>version 3.7) and the CFclient on Windows. When installing Python, the checkbox to add python to the Path should be checked and then the CFclient can be installed with pip in a powershell or cmd window:

```shell
pip.exe install cfclient
```

### 2. Clone the Crazyflie repository

This repository contains the latest versions of the firmware. To clone the repository use the following command:

```shell
git clone --recursive https://github.com/bitcraze/crazyflie-firmware.git
```

### 3. Build the default firmware

Go to the root of the crazyflie-firmware project (the one you cloned in the previous step), and run the following command:

### 4. Flashing

Writing a new binary to the Crazyflie is called flashing (writing it to the flash memory). The supported way to flash when developping for the Crazyflie is to use the Crazyradio and the radio bootloader.

#### Prerequisites

- A Crazyradio with drivers installed
- Crazyflie Client installed with Python’s pip (so not by Snap (Ubuntu) or the .exe (Windows))
- Note than when developing in WSL on Windows, the client needs to be installed on Windows. See the Windows build instruction above.
- The firmware has been built
- The current working directory is the root of the crazyflie-firmware project

#### Manually entering bootloader mode

- Turn the Crazyflie off
- Start the Crazyflie in bootloader mode by pressing the power button for 3 seconds. Both the blue LEDs will blink.
- In your terminal, run:

```shell
make cload
```

It will try to find a Crazyflie in bootloader mode and flash the binary to it.

**Warning:** if you have multiple Crazyflies, you must do this one by one.

## Open the Crazyflie client

To make sure that the building and flashing worked properly, you can open the [Crazyflie Client](https://www.bitcraze.io/2018/03/crazyflie-clients/) and do some test flights. To open the client run on the cmd or terminal:

```shell
python3 -m cfclient.gui
```

Some of the things you can do with the Crazyflie client are:
- Monitor the link quality between the Crazyflie and the Crazyradio
- Monitor the Crazyflie battery
- Modify the Crazyflie address
- Manually control the Crazyflie
- Modify flight parameters

## Run the autonomous flight programs

In this repository you have two programs to test the autonomous flight of the Crazyflie

### closed_trajectory.py

With this program, the Crazyflie will perform a square trajectory. You can modify the `URI`, `TARGET_HEIGHT`, `TARGET_VELOCITY` and `TRAVEL_DISTANCE` in the `closed_trajectory.py` file, to observe the behavior of the Crazyflie. To run this program run the following command:

```shell
python3 ./closed_trajectory.py
```

### random_trajectory.py

With this program, the Crazyflie will perform a square trajectory. You can modify the `URI`, `TARGET_HEIGHT` and `TARGET_VELOCITY` in the `random_trajectory.py` file, to observe the behavior of the Crazyflie. To run this program run the following command:

```shell
python3 ./random_trajectory.py
```
