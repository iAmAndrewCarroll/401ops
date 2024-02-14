import logging
from ops26_2_core import scan_ip_and_ports, icmp_ping_sweep, generate_ip_range

# Setup basic logging
logging.basicConfig(filename='ops26-2.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

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
