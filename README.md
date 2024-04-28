# Mac Changer

MacChanger is a Python script for Linux systems that allows users to quickly and easily change the MAC address of a network interface. It provides a command-line interface to specify the network interface and the new MAC address to be set.

## Features

- Change MAC address of any network interface
- Command-line options for ease of use
- Current MAC address display
- Verification of MAC address change

## Prerequisites

Before using Mac Changer, make sure you have Python installed on your Linux system. This script utilizes the `subprocess` and `optparse` modules, which are included in the standard Python library.

## Usage

To use Mac Changer, clone this repository to your local machine and navigate to the project directory:

```sh
git clone https://github.com/yourusername/Mac_Changer.git
cd Mac_Changer
```
Run the script by specifying the interface and the new MAC address using the -i and -m flags:
```sh
sudo python main.py -i interface -m new_mac_address
```
Replace the interface with your network interface (e.g., `eth0` or `wlan0`) and `new_mac_address` with the desired MAC address.

## Command-line Options
- **-i or --interface**: The network interface whose MAC address you want to change.
- **-m or --mac**: The new MAC address you want to assign to the interface.
## How It Works
1. The script takes command-line arguments for the network interface and new MAC address.
2. It disables the network interface using ifconfig down.
3. The MAC address is changed using ifconfig hw ether.
4. The network interface is re-enabled using ifconfig up.
5. The script checks if the MAC address was successfully changed and displays the current MAC address.

## Examples
To change the MAC address of `eth0` to `00:11:22:33:44:55`, the command would be:
```sh
sudo python macchanger.py -i eth0 -m 00:11:22:33:44:55
```
## Disclaimer
This tool is for educational purposes and should be used only on devices and networks where you have permission to make such changes. Unauthorized use of this tool is not encouraged.
