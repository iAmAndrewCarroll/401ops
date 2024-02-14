from ops26_1_core import read_wordlist, dictionary_iterator, password_recognized, ssh_brute_force, zip_brute_force

def main():
    while True:
        print("\nMenu:")
        print("1: Original Functionality (Word List Operations)")
        print("2: SSH Brute Force")
        print("3: ZIP File Brute Force")
        print("4: Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            mode = input("Select mode (1: Offensive, 2: Defensive): ")
            file_path = input("Enter the word list file path: ")

            words = read_wordlist(file_path)
            if words is not None:
                if mode == '1':
                    dictionary_iterator(words)
                elif mode == '2':
                    search_string = input("Enter the string to search: ")
                    if password_recognized(search_string, ''.join(words)):
                        print(f"'{search_string}' appeared in the word list.")
                    else:
                        print(f"'{search_string}' did not appear in the word list.")
                else:
                    print("Invalid mode selected.")

        elif choice == '2':
            host = input("Enter the SSH server's IP address: ")
            username = input("Enter the username to brute force: ")
            file_path = input("Enter the word list file path: ")

            words = read_wordlist(file_path)
            if words is not None and ssh_brute_force(host, username, words):
                print(f"Successful SSH login - Username: {username}")
            else:
                print("SSH Brute Force attempt failed or completed without success.")

        elif choice == '3':
            zip_file_path = input("Enter the path to the password-protected ZIP file: ")
            file_path = input("Enter the word list file path (RockYou.txt recommended): ")

            words = read_wordlist(file_path)
            if words is not None and zip_br
