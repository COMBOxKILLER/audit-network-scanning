import socket
import struct

def spoof_ip(source_ip, destination_ip):
    # Create a raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    # Set the IP header fields
    ip_header = struct.pack('!BBHHHBBH4s4s', 4 << 4, 0, 0, 0, 0, 255, socket.IPPROTO_TCP, 0, socket.inet_aton(source_ip), socket.inet_aton(destination_ip))

    # Send the spoofed IP packet
    s.sendto(ip_header, (destination_ip, 0))

# Usage example
source_ip = '192.168.0.100'  # Replace with your desired source IP address
destination_ip = '10.0.0.1'  # Replace with the target IP address

spoof_ip(source_ip, destination_ip)