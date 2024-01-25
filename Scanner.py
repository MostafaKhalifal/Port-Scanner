import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_host, port):
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.settimeout(1)
            s.connect((target_host, port))
            print(f"Port {port} is open")
    except (socket.timeout, socket.error):
        pass

def port_scanner(target_host, start_port, end_port, num_threads):
    print(f"Scanning ports on {target_host}...")
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_host, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    
    parser.add_argument("target_host", help="Target host to scan")
    parser.add_argument("start_port", type=int, help="Start port of the scan range")
    parser.add_argument("end_port", type=int, help="End port of the scan range")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads for concurrent scanning")

    args = parser.parse_args()

    port_scanner(args.target_host, args.start_port, args.end_port, args.threads)
