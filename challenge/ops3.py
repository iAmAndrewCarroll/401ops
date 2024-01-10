import pickle
import os.path
import base64
import subprocess
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(f'An error occurred: {error}')

def ping_host(target_ip):
    response = subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response.returncode == 0

def log_to_file(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
    with open("uptime_sensor.log", "a") as log_file:
        log_file.write(f"{timestamp} {message}\n")

def main():
    target_ip = input("Enter target IP address: ")
    to_email = input("Enter your email address: ")
    from_email = "codefellows.ops@gmail.com"  # Replace with your email address

    service = get_service()

    previous_status = None
    initial_check_done = False

    while True:
        current_status = ping_host(target_ip)
        status_message = "Network Active" if current_status else "Network Inactive"
        output_message = f"{status_message} to {target_ip}"
        print(output_message)
        log_to_file(output_message)

        if not initial_check_done or (previous_status is not None and previous_status != current_status):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
            email_subject = "Host Status Notification for {}".format(target_ip)
            email_body = "Status as of {}: {}".format(timestamp, output_message)
            message = create_message(from_email, to_email, email_subject, email_body)
            send_message(service, "me", message)
            initial_check_done = True
        
        previous_status = current_status
        time.sleep(2)

if __name__ == "__main__":
    main()
