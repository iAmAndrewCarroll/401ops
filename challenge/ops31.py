import os
import platform

def get_common_directories():
    # Get the home directory
    home_dir = os.path.expanduser('~')

    # Common directories
    common_dirs = {
        "Desktop": os.path.join(home_dir, "Desktop"),
        "Documents": os.path.join(home_dir, "Documents"),
        "Downloads": os.path.join(home_dir, "Downloads")
    }

    return common_dirs

def directory_menu():
    common_dirs = get_common_directories()
    options = list(common_dirs.keys()) + ["Enter a different directory"]

    # Display menu
    print("Choose a directory to search:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("Enter your choice (number): ")
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        if int(choice) == len(options):
            return input("Enter the full path of the directory: ")
        else:
            return common_dirs[options[int(choice) - 1]]
    else:
        print("Invalid choice. Please enter a valid number.")
        return None

def search_file(file_name, directory):
    matches = []
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            matches.append(os.path.join(root, file_name))
    return matches

def main():
    # Determine the operating system
    os_type = platform.system()
    print(f"Operating System Detected: {os_type}")

    # Prompt user for file name
    file_name = input("Enter the file name to search for: ")

    # Display directory menu and get user choice
    directory = directory_menu()
    if directory is None:
        return

    # Ensure the directory is valid
    if not os.path.isdir(directory):
        print("Invalid directory. Please enter a valid directory.")
        return

    # Search for the file
    found_files = search_file(file_name, directory)

    # Print results
    if found_files:
        print(f"{len(found_files)} file(s) found:")
        for file in found_files:
            print(file)
    else:
        print("No files found.")

    # Print number of files searched
    print(f"Searched in {len(found_files)} file(s).")

if __name__ == "__main__":
    main()

