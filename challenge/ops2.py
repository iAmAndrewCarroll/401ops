import os
import time
import subprocess

def ping_host(target_ip):
    """Pings the target IP and returns True for success, False for failure."""
    response = subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.DEVNULL)
    return response.returncode == 0

def log_to_file(message):
    """Appends a message to the log file with a timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
    with open("uptime_sensor.log", "a") as log_file:
        log_file.write(f"{timestamp} {message}\n")

def main():
    """Main function to manage the uptime sensor."""
    target_ip = input("Enter target IP address: ")
    while True:
        status = "Network Active" if ping_host(target_ip) else "Network Inactive"
        output_message = f"{status} to {target_ip}"
        print(output_message)
        log_to_file(output_message)
        time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    main()
