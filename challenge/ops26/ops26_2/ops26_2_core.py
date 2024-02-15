import pandas as pd
from scapy.all import *
import platform
import os
import ipaddress
import logging
from tqdm import tqdm
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Setup basic logging
size_handler = RotatingFileHandler('ops26-2.log', maxBytes=1000000, backupCount=5)
time_handler = TimedRotatingFileHandler('ops26-2.log', when='midnight', interval=1, backupCount=5)

size_handler.setLevel(logging.DEBUG)
time_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
size_handler.setFormatter(formatter)
time_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(size_handler)
logger.addHandler(time_handler)

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
        network_address = str(network.network_address)
        broadcast_address = str(network.broadcast_address)
        print(f"Network Address: {network_address}")
        print(f"Broadcast Address: {broadcast_address}")
        
        return [str(ip) for ip in network.hosts() if ip != network.network_address and ip != network.broadcast_address]
    except ValueError as e:
        logging.error(f"Invalid CIDR block: {str(e)}")
        return []

def icmp_ping_sweep(ip_list):
    online_hosts = 0
    for ip in tqdm(ip_list, desc="Ping Sweep"):
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
            print(f"Error during ICMP ping sweep on {ip}: {str(e)}")

    print(f"\nTotal online hosts: {online_hosts}")
    logging.info(f"Total online hosts: {online_hosts}")

def scan_ip_and_ports(target_ip):
    try:
        scan_results = []

        for port in tqdm(range(1, 101), desc="Port Scan"):
            result = scan_port(target_ip, port)
            scan_results.append(result)
            if result[1] == "Interrupted":
                raise KeyboardInterrupt

        export_results(scan_results, "scan_results")
        print("Scan results exported successfully.")
    except KeyboardInterrupt:
        logging.warning("Port scanning operation interrupted by user.")
        print("Scan interrupted by user.")
