import time

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
        time.sleep(.5)  # Delay of 0.5 seconds between words

def password_recognized(search_string, words):
    if search_string in words:
        print(f"'{search_string}' appeared in the word list.")
    else:
        print(f"'{search_string}' did not appear in the word list.")

def main():
    mode = input("Select mode (1: Offensive, 2: Defensive): ")
    file_path = input("Enter the word list file path: ")

    words = read_wordlist(file_path)
    if words is None:
        return

    if mode == '1':
        dictionary_iterator(words)
    elif mode == '2':
        search_string = input("Enter the string to search: ")
        password_recognized(search_string, ''.join(words))
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
