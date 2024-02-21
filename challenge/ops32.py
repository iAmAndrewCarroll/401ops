#!/usr/bin/env python3

import os
import sys
import hashlib
import time
import logging

# Initialize logging
logging.basicConfig(filename="malware_scan_log.txt", level=logging.INFO, format='%(asctime)s %(message)s')

def generate_md5_hash(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
        md5_hash = hashlib.md5(file_content).hexdigest()
    return md5_hash

def search_for_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            md5_hash = generate_md5_hash(file_path)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Timestamp: {timestamp}, File: {filename}, Size: {file_size} bytes, MD5: {md5_hash}, Path: {file_path}")
            logging.info(f"File: {filename}, Size: {file_size} bytes, MD5: {md5_hash}, Path: {file_path}")
            return file_path
    return None

def scan_directory(directory):
    scan_results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            md5_hash = generate_md5_hash(file_path)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            scan_results.append([timestamp, file, file_size, md5_hash, file_path])
    return scan_results

def print_directory_suggestions():
    print("Here are some common directory suggestions:")
    print(f"Home Directory: {os.path.expanduser('~')}")
    print("Root Directory: /")
    print("Current Working Directory: ./")
    print("You can enter one of these paths, or any other valid full path to a directory.")

def display_results_page(scan_results, start_index=0):
    end_index = min(start_index + 5, len(scan_results))
    for i in range(start_index, end_index):
        timestamp, file, file_size, md5_hash, file_path = scan_results[i]
        print(f"Timestamp: {timestamp}, File: {file}, Size: {file_size} bytes, MD5: {md5_hash}, Path: {file_path}")
    return end_index

def paginate_results(scan_results):
    start_index = 0
    while True:
        end_index = display_results_page(scan_results, start_index)
        if end_index >= len(scan_results):
            print("End of results.")
            break
        print("\n'N' for Next, 'P' for Previous, 'E' to Exit")
        action = input("Choose an option: ").lower()
        if action == 'n':
            start_index = end_index
        elif action == 'p':
            start_index = max(0, start_index - 10)
        elif action == 'e':
            break

def main():
    try:
        print("Operating System Detected:", os.name)

        # File name input with help option
        filename = input("Enter the file name to search for (or type 'help' for instructions): ")
        if filename.lower() == 'help':
            print("Enter the name of the file you're looking for, e.g., 'myfile.txt'.")
            return

        # Directory choice with help option
        print("Choose a directory to search:")
        print("1. Desktop")
        print("2. Documents")
        print("3. Downloads")
        print("4. Enter a different directory")
        print("Type 'help' for instructions on directory selection.")
        choice = input("Enter your choice (number): ")
        if choice.lower() == 'help':
            print("Enter the number corresponding to the directory you want to search in.")
            return

        # Handling directory selection
        directory = ''
        if choice == '1':
            directory = os.path.expanduser('~/Desktop')
        elif choice == '2':
            directory = os.path.expanduser('~/Documents')
        elif choice == '3':
            directory = os.path.expanduser('~/Downloads')
        elif choice == '4':
            print_directory_suggestions()
            directory = input("Enter the full path of the directory: ")
            if not os.path.isdir(directory):
                print("Invalid directory. Please enter a valid directory.")
                return

        found_file = search_for_file(directory, filename)
        if found_file:
            print(f"File found: {found_file}")
        else:
            print("File not found.")

        # Additional Part 2 functionality: Scan directory for malware detection
        print("\nStarting malware scan in the directory...")
        scan_results = scan_directory(directory)

        print_results = input("Do you want to print the results to the screen? (yes/no): ").lower()
        if print_results == 'yes':
            paginate_results(scan_results)

    except KeyboardInterrupt:
        print("\nScript interrupted. Exiting.")
        sys.exit()

if __name__ == "__main__":
    main()
