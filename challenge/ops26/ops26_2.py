import pandas as pd
from scapy.all import *
import platform
import os
import ipaddress
import logging

# Setup basic logging
logging.basicConfig(filename='ops26-2.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

def scan_port(ip, port):
    try:
        pkt = IP(dst=ip)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=2, verbose=0)

        if resp is None:
            logging.info(f"Port {port} on {ip} is filtered")
            return port, "Filtered"
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
                sr(IP(dst=ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
                logging.info(f"Port {port} on {ip} is open")
                return port, "Open"
            elif resp.getlayer(TCP).flags == 0x14:  # RST-ACK
                logging.info(f"Port {port} on {ip} is closed")
                return port, "Closed"
        return port, "Unknown"
    except KeyboardInterrupt:
        logging.warning(f"Port scanning interrupted by user at port {port}")
        print("\nScan interrupted by user.")
        return port, "Interrupted"

def export_results(scan_results, filename):
    df = pd.DataFrame(scan_results, columns=["Port", "Status"])
    try:
        if platform.system() == "Windows":
            df.to_excel(f"{filename}.xlsx", index=False)
        else:
            df.to_csv(f"{filename}.csv", index=False)
        logging.info(f"Scan results exported successfully to {filename}")
    except Exception as e:
        logging.error(f"Error exporting scan results: {str(e)}")
        print("Error occurred while exporting results.")

def generate_ip_range(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        logging.error(f"Invalid CIDR block: {str(e)}")
        return []

def icmp_ping_sweep(ip_list):
    online_hosts = 0
    for ip in ip_list:
        try:
            pkt = IP(dst=ip)/ICMP()
            resp = sr1(pkt, timeout=1, verbose=0)
            if resp is None:
                print(f"{ip} is down or not responding.")
                logging.info(f"{ip} is down or not responding")
            elif (resp.haslayer(ICMP) and
                  resp.getlayer(ICMP).type == 3 and
                  resp.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]):
                print(f"{ip} is actively blocking ICMP traffic.")
                logging.info(f"{ip} is blocking ICMP traffic")
            else:
                print(f"{ip} is responding.")
                logging.info(f"{ip} is responding")
                online_hosts += 1
        except Exception as e:
            logging.error(f"Error during ICMP ping sweep on {ip}: {str(e)}")

    print(f"\nTotal online hosts: {online_hosts}")
    logging.info(f"Total online hosts: {online_hosts}")

def scan_ip_and_ports(target_ip):
    try:
        scan_results = []

        for port in range(1, 1025):
            result = scan_port(target_ip, port)
            scan_results.append(result)
            if result[1] == "Interrupted":
                break

        export_results(scan_results, "scan_results")
        print("Scan results exported successfully.")
    except KeyboardInterrupt:
        logging.warning("Port scanning operation interrupted by user.")
        print("\nScan interrupted by user.")

def main():
    try:
        while True:
            print("1. Scan IP Address and Ports")
            print("2. ICMP Ping Sweep")
            print("3. Exit")
            choice = input("Select an option (1, 2, or 3): ")

            if choice == "1":
                target_ip = input("Enter target IP: ")
                icmp_response = sr1(IP(dst=target_ip)/ICMP(), timeout=1, verbose=0)
                if icmp_response is not None:
                    print(f"{target_ip} is responding to ICMP ping.")
                    logging.info(f"{target_ip} is responding to ICMP ping")
                    scan_ip_and_ports(target_ip)
                else:
                    print(f"{target_ip} is down or not responding to ICMP ping.")
                    logging.info(f"{target_ip} is down or not responding to ICMP ping")
            elif choice == "2":
                cidr = input("Enter network address (CIDR format, e.g., 192.168.1.0/24): ")
                ip_list = generate_ip_range(cidr)
                if ip_list:
                    icmp_ping_sweep(ip_list)
                else:
                    print("Invalid CIDR block. Please enter a valid CIDR.")
            elif choice == "3":
                logging.info("Program exited by user.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
                logging.warning("Invalid choice made in main menu.")

    except KeyboardInterrupt:
        logging.info("Operation cancelled by user.")
        print("\nOperation cancelled by user.")

if __name__ == "__main__":
    main()
