import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning ports on {host}...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage
scan_ports("127.0.0.1", 1, 1000)