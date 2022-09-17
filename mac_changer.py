#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to be changed") 
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Interface not specified. Use --help for more info")
    elif not options.new_mac:
        parser.error("[-] New MAC Address not specified. Use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC Address of " +interface +" to " +new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface ,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    new_result = subprocess.check_output(["ifconfig", interface])
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(new_result))
    if mac_address_result:
        return mac_address_result[0]
    else:
        print("[-] Failed to find MAC Address")

options = get_arguments()

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC Address is changed to " +str(current_mac))
else:
    print("[-] Failed to change MAC Address")

