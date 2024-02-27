#!/usr/bin/env python3

import subprocess

def banner_grabbing_nc(target, port):
    print("Performing banner grabbing using netcat...")
    try:
        result = subprocess.run(['nc', '-v', target, str(port)], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def banner_grabbing_telnet(target, port):
    print("Performing banner grabbing using telnet...")
    try:
        result = subprocess.run(['telnet', target, str(port)], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def banner_grabbing_nmap(target):
    print("Performing banner grabbing using Nmap...")
    try:
        result = subprocess.run(['nmap', '-sV', '--script=banner', target], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def main():
    target = input("Enter the URL or IP address: ")
    port = int(input("Enter the port number: "))

    banner_grabbing_nc(target, port)
    banner_grabbing_telnet(target, port)
    banner_grabbing_nmap(target)

if __name__ == "__main__":
    main()
