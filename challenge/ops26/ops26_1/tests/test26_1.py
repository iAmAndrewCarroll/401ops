import sys
import os
from dotenv import load_dotenv
from ops26_1.ops26_1_core import read_wordlist, dictionary_iterator, password_recognized, ssh_brute_force, zip_brute_force

# Get the current directory of the test script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the grandparent directory to reach the root of the project
root_dir = os.path.join(current_dir, '..', '..')

# Add the root directory to the Python path
sys.path.append(root_dir)

# Load environment variables from .env file
load_dotenv()

# Retrieve values from environment variables
test_ssh_host = os.getenv('SSH_HOST')
test_ssh_username = os.getenv('SSH_USERNAME')

# Print statements to debug file creation
print("Current directory:", current_dir)
print("Root directory:", root_dir)

# Create a test wordlist
test_words = ["password123", "123456", "admin123"]
test_wordlist_path = "test_wordlist.txt"
print("Attempting to create test wordlist file...")

try:
    with open(test_wordlist_path, "w") as file:
        for word in test_words:
            file.write(word + "\n")
    print("Test wordlist file created successfully.")
except Exception as e:
    print(f"Error creating wordlist file: {e}")

# Test read_wordlist
def test_read_wordlist():
    print("Testing read_wordlist...")
    words = read_wordlist(test_wordlist_path)
    assert words is not None, "read_wordlist failed to read words"
    assert len(words) == len(test_words), "Word count mismatch"

# # Test dictionary_iterator
# def test_dictionary_iterator():
#     print("Testing dictionary_iterator...")
#     words = [word.strip() for word in open(test_wordlist_path).readlines()]
#     dictionary_iterator(words)  # This will print the words

# # Test password_recognized
# def test_password_recognized():
#     print("Testing password_recognized...")
#     words = [word.strip() for word in open(test_wordlist_path).readlines()]
#     assert password_recognized("password123", words), "password_recognized failed to recognize password"

# # Test ssh_brute_force
# def test_ssh_brute_force():
#     print("Testing ssh_brute_force...")
#     words = [word.strip() for word in open(test_wordlist_path).readlines()]
#     assert ssh_brute_force(test_ssh_host, test_ssh_username, words), "ssh_brute_force failed"

# # Test zip_brute_force (if needed)
# def test_zip_brute_force():
#     print("Testing zip_brute_force...")
#     words = [word.strip() for word in open(test_wordlist_path).readlines()]
#     test_zip_file_path = "path/to/test/zipfile.zip"
#     assert zip_brute_force(test_zip_file_path, words), "zip_brute_force failed"

# Clean up
try:
    os.remove(test_wordlist_path)
    print("Test wordlist file removed successfully.")
except Exception as e:
    print(f"Error removing wordlist file: {e}")
