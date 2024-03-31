import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    # parse command line arguments
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    # if interface or mac address is not provided, show error
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


option = get_arguments()
ifconfig_result = subprocess.check_output(["ifconfig", option.interface])
# search for MAC address in ifconfig_result
mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))
if mac_search_result:
    current_mac = mac_search_result.group(0)
    print("[+] Current MAC address: " + current_mac)
else:
    print("[-] Could not read MAC address.")
    
change_mac(option.interface, option.new_mac)
