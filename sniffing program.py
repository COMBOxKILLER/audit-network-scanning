from scapy.all import *

def sniff_packets(packet):
    if packet.haslayer(ICMP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        ether_src = packet[Ether].src
        ether_dst = packet[Ether].dst

        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Source Ethernet Address: {ether_src}")
        print(f"Destination Ethernet Address: {ether_dst}")

sniff(filter="icmp", prn=sniff_packets)