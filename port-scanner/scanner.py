import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        try:
            banner = sock.recv(1024).decode().strip()
        except:
            banner = "No banner"
        print(f"Port {port} is OPEN — {banner}")
    
    sock.close()

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print("\nScan complete.")