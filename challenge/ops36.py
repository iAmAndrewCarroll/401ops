#!/usr/bin/env python3

import subprocess
import logging

logging.basicConfig(filename='banner_grabbing.log', level=logging.ERROR)

def banner_grabbing_nc(target, port):
    """Perform banner grabbing using netcat."""
    command = f"nc -v {target} {port}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def banner_grabbing_telnet(target, port):
    """Perform banner grabbing using telnet."""
    telnet_path = "/opt/homebrew/bin/telnet"
    command = f"{telnet_path} {target} {port}"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, command)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while running telnet: {e}")
        return f"Error occurred while running telnet. Check logs for details."

def banner_grabbing_nmap(target):
    """Perform banner grabbing using Nmap."""
    nmap_path = "/opt/homebrew/bin/nmap"
    command = f"{nmap_path} -Pn -sV --script=banner {target}"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, command)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while running Nmap: {e}")
        return f"Error occurred while running Nmap. Check logs for details."

def main():
    target = input("Enter the target URL or IP address: ")
    port = input("Enter the port number: ")

    # Perform banner grabbing using netcat
    print("\nPerforming banner grabbing using netcat...")
    nc_output = banner_grabbing_nc(target, port)
    print(nc_output)

    # Perform banner grabbing using telnet
    print("\nPerforming banner grabbing using telnet...")
    telnet_output = banner_grabbing_telnet(target, port)
    print(telnet_output)

    # Perform banner grabbing using Nmap
    print("\nPerforming banner grabbing using Nmap...")
    nmap_output = banner_grabbing_nmap(target)
    print(nmap_output)

if __name__ == "__main__":
    main()
