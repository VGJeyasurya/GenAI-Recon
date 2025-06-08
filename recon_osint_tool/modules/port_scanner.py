import socket
from typing import List
from tqdm import tqdm


def scan_ports(host: str, ports: List[int]) -> List[int]:
    """Scan a list of ports on the given host."""
    open_ports = []
    for port in tqdm(ports, desc=f"Port Scan {host}"):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect((host, port))
                open_ports.append(port)
            except Exception:
                continue
    return open_ports
