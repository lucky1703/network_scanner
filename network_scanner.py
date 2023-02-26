#!/usr/bin/env python
import scapy.all as scapy
import optparse
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answered_list

def print_result(answer_list):
    print("IP\t\t\tMAC Address\n----------------------------------------")
    for answer in answer_list:
        print(answer[1].psrc + "\t\t" + answer[1].hwsrc)

def parse():
 parser=optparse.OptionParser()

 parser.add_option("-t", "--target", dest="target", help="The target and range of ip address to scan")
 (options , arguments) = parser.parse_args()
 if not options.target:
     parser.error("Please spacify a target ip.--help for more info")
 return options

#main
options=parse()
list=scan(options.target)
print_result(list)

