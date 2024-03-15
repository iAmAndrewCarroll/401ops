# Ops Challenge 42: Attack Tools Part 2 of 3

## Custom Nmap Scanner Using Python

# Create a Python script that uses the nmap module to perform a simple port scan on a target IP address and port range.
import nmap  # Import the nmap module
import sys

def simple_nmap_scan(target, ports):
    scanner = nmap.PortScanner()  # Instantiate a PortScanner object
    scanner.scan(target, ports)  # Perform the scan on the target and ports
    
    for host in scanner.all_hosts():  # Iterate through all hosts found in the scan
        print(f'Host: {host} ({scanner[host].hostname()})')
        print(f'State: {scanner[host].state()}')
        
        for proto in scanner[host].all_protocols():  # Iterate through all protocols
            print(f'Protocol: {proto}')
            
            lport = scanner[host][proto].keys()
            for port in lport:  # Iterate through all ports for the protocol
                print(f'Port: {port}\tState: {scanner[host][proto][port]["state"]}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 nmap_script.py <target> <ports>")
        sys.exit(1)

    target_ip = sys.argv[1]
    ports = sys.argv[2]
    
    simple_nmap_scan(target_ip, ports)
