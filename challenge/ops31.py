#!/usr/bin/env python3

import os
import sys

def search_for_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

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

    except KeyboardInterrupt:
        print("\nScript interrupted. Exiting.")
        sys.exit()

if __name__ == "__main__":
    main()