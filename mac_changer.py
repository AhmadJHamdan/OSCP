#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to be changed")
    parser.add_option("-m", "--mac-address", dest="new_mac", help="New MAC Address")
    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error("[-] Interface not found. Use -i or --interface to specify an interface")
    elif not options.new_mac:
        parser.error("[-] MAC Address not found. Use -m or --mac-address to specify a new mac address")
    return options

def change_mac(interface, mac):
    print(f"Changing MAC Address @ interface {interface} to {mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
