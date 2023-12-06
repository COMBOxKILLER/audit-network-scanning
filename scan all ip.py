import socket

def scan_ips(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))

    # Convert the IP range to a list of IP addresses
    ip_range = [start]
    while ip_range[-1] != end:
        next_ip = ip_range[-1].copy()
        for i in range(3, -1, -1):
            if next_ip[i] < 255:
                next_ip[i] += 1
                break
            else:
                next_ip[i] = 0
        ip_range.append(next_ip)

    # Scan each IP address in the range
    for ip in ip_range:
        ip_str = '.'.join(str(x) for x in ip)
        try:
            hostname = socket.gethostbyaddr(ip_str)[0]
            print(f"IP: {ip_str}\tHostname: {hostname}")
        except socket.herror:
            print(f"IP: {ip_str}\tHostname not found")

# Example usage
start_ip = '192.168.0.1'
end_ip = '192.168.0.10'
scan_ips(start_ip, end_ip)