#!/usr/bin/env python

import scapy.all as scapy
import optparse

                                            ## Discover Devices on the Network ##

def parse_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip_address", help="IP Address or IP Range")
    options, arguments = parser.parse_args()
    return options.ip_address

# create arp request send for broadcast mac to get ips
# send packet and recieve response
# Parse response

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_broadcast_request = broadcast/arp_request
    # print(arp_broadcast_request.summary())
    # scapy.ls(scapy.ARP())
    answered_list = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

# print result

def print_results(result_list):
    print("\n=========================================\nIP\t\t\tMAC\n=========================================")
    for client in result_list:
        print(client["ip"] +"\t\t" + client["mac"])

# run

ip = parse_arg()
scan_result = scan(ip)
print_results(scan_result)
