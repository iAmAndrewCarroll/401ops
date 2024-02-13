import sys
import os

# Update the path to include the ops26_1 directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ops26_1'))

from ops26_1_core import read_wordlist, dictionary_iterator, password_recognized, ssh_brute_force, zip_brute_force

def run_tests():
    # Create a test wordlist
    test_words = ["password123", "123456", "admin123"]
    test_wordlist_path = "test_wordlist.txt"
    with open(test_wordlist_path, "w") as file:
        for word in test_words:
            file.write(word + "\n")

    # Test read_wordlist
    print("Testing read_wordlist...")
    words = read_wordlist(test_wordlist_path)
    assert words is not None, "read_wordlist failed to read words"
    # Strip newline characters from each word
    words = [word.strip() for word in words]

    # Test dictionary_iterator
    print("Testing dictionary_iterator...")
    dictionary_iterator(words)  # This will print the words

    # Test password_recognized
    print("Testing password_recognized...")
    assert password_recognized("password123", words), "password_recognized failed to recognize password"

    # Test ssh_brute_force
    # Uncomment and modify the below lines to test ssh_brute_force
    # print("Testing ssh_brute_force...")
    # test_ssh_host = "your.test.ssh.host"
    # test_ssh_username = "yourusername"
    # assert ssh_brute_force(test_ssh_host, test_ssh_username, words), "ssh_brute_force failed"

    # Test zip_brute_force
    # Uncomment and modify the below lines to test zip_brute_force
    # print("Testing zip_brute_force...")
    # test_zip_file_path = "path/to/test/zipfile.zip"
    # assert zip_brute_force(test_zip_file_path, words), "zip_brute_force failed"

    # Clean up
    os.remove(test_wordlist_path)

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
