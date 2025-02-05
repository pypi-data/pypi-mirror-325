import socket

def ip_scanner(network: str) -> list:
    return [f"{network}.{i}" for i in range(1, 256)]

def port_scanner(target_ip: str) -> list:
    open_ports = []
    for port in range(1, 1025):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports
