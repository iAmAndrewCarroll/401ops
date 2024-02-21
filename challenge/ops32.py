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

def scan_directory(directory):
    scan_results = []  # 2D array for stretch goal
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            md5_hash = generate_md5_hash(file_path)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Timestamp: {timestamp}, File: {file}, Size: {file_size} bytes, MD5: {md5_hash}, Path: {file_path}")
            logging.info(f"File: {file}, Size: {file_size} bytes, MD5: {md5_hash}, Path: {file_path}")
            scan_results.append([timestamp, file_path, md5_hash])
    return scan_results

def print_directory_suggestions():
    print("Here are some common directory suggestions:")
    print(f"Home Directory: {os.path.expanduser('~')}")
    print("Root Directory: /")
    print("Current Working Directory: ./")
    print("You can enter one of these paths, or any other valid full path to a directory.")

def main():
    try:
        while True:
            print("Operating System Detected:", os.name)

            # File name input with help option
            filename = input("Enter the file name to search for (or type 'help' for instructions): ")
            if filename.lower() == 'help':
                print("Enter the name of the file you're looking for, e.g., 'myfile.txt'.")
                continue

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
                continue

            # Handling directory selection
            while True:
                directory = ''
                if choice == '1':
                    directory = os.path.expanduser('~/Desktop')
                    break
                elif choice == '2':
                    directory = os.path.expanduser('~/Documents')
                    break
                elif choice == '3':
                    directory = os.path.expanduser('~/Downloads')
                    break
                elif choice == '4':
                    print_directory_suggestions()
                    dir_input = input("Enter the full path of the directory (or type 'help' for instructions): ")
                    if dir_input.lower() == 'help':
                        print("Enter the full path to the directory where you want to search for the file.")
                        continue
                    if os.path.isdir(dir_input):
                        directory = dir_input
                        break
                    else:
                        print("Invalid directory. Please enter a valid directory.")
                        continue
                else:
                    print("Invalid choice. Please enter a valid number.")
                    continue

            # File searching logic
            found_file = search_for_file(directory, filename)
            if found_file:
                print(f"File found: {found_file}")
            else:
                print("File not found.")

            # Additional Part 2 functionality: Scan directory for malware detection
            print("\nStarting malware scan in the directory...")
            scan_results = scan_directory(directory)
            # You can process or display scan_results as needed

    except KeyboardInterrupt:
        print("\nScript interrupted. Exiting.")
        sys.exit()

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

if __name__ == "__main__":
    main()
