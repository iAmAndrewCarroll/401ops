# Lab: Data File Encryption and Hashing

## Overview
Encryption plays a vital role in the securing of data on computer systems and can serve many purposes. Sometimes, encryption is used for good: Keeping confidential data out of the hands of criminals. Other times, encryption is used for more nefarious deeds, such as locking files with ransomware. If the organization needs to protect sensitive information, the security professional should be prepared with solutions to facilitate the confidentiality and integrity of a given data both at rest and in motion.

## Objectives
- Host a SFTP server in AWS and securely share a file with a classmate.
- Use SCP via terminal to copy a file from your local PC to the AWS instance.
- Dump the hash of your Linux instance’s user credentials.

## Resources
- [Linux SFTP Command](link-to-sftp-command)
- [How to set up an SFTP server on Linux](link-to-sftp-setup)
- [SSH public key authentication on AWS EC2](link-to-ssh-auth)
- [How to Use Linux SCP Command](link-to-scp-command)
- [How to Un-shadow the file and dump Linux password Beginner’s Guide](link-to-linux-password-guide)
- [How to Crack Passwords with John the Ripper](link-to-john-the-ripper)

## Tasks
### Part 1: Staging
Prepare the following operating systems for today’s lab:
- Deploy a Linux EC2 instance in AWS. A recent version of Ubuntu works fine for this.
  - Note: Make sure your EC2 instance is assigned a public IP address; otherwise, you won’t be able to complete this lab.
- In your Linux VM, install OpenSSH.

### Part 2: Secure File Transmission with SCP and SFTP on Linux
Deploy an SFTP server on your cloud Linux instance, carefully following these instructions: [How to set up an SFTP server on Linux](link-to-sftp-setup).
- Successfully perform a file upload and download from your local computer to your Linux cloud VM using the `scp` command.
- Upload some cybersecurity meme images to the SFTP directory to share with your classmate.

### Part 3: SSH Public Key Authentication on Linux
On your Linux VM in the cloud:
- Install OpenSSH.
- Ask a classmate to authenticate into your server using SSH keys. Steps:
  - Your classmate needs to generate a pair of SSH keys if they do not have one already.
  - Ask your classmate to provide you with their public key.
  - Connect to the instance using your existing private key (.pem key).
  - Navigate to the home directory of the user you created in Part 2. Example: `/home/USERNAME`.
  - Using a text editor of your choice, open the `.ssh/authorized_keys` file on the instance. Paste the public key your classmate provided underneath the existing public key information. Save the file.
  - If the `.ssh/authorized_keys` file does not exist, create both the `.ssh` directory and the `authorized_keys` (no file extension) file.
  - Disconnect from your instance, and test that your classmate can connect to your instance using their private key.
  - Confirm that they have SFTP access, by having them prove they can download an image from your SFTP server.
  - Confirm that they do NOT have full SSH shell access.
- Document your setup and file transmission process and confirmations with screenshots and descriptions.

### Part 4: Encryption and Decryption on Linux
Let’s take a look at where Linux stores user credentials.
- As the administrator of the Ubuntu Linux VM, dump the password hash file or strings.
- Document your setup and process with screenshots and descriptions.

### Part 5: Report Via End-User Training
Your CISO asked you to present what you learned at an all-team meeting, so all the employees who send files frequently can learn to do so safely. Conclude your submission with some brief end-user training to address the following:
- Explain the need for secure data transmission as it relates to confidentiality.
- Explain the difference between FTP and SFTP.
  - Do they use the same ports?
  - Do they use the same software?
  - What are some examples of software used to access FTP and SFTP servers?
- How does SCP protect the data being transmitted?
- How difficult was it to exfiltrate credentials from Linux system files?
- How might a threat actor (or a pentester) utilize insecure FTP access?

### Stretch Goal
Password Cracking
Attempt to crack the Linux user hashes with Kali Linux tools like John the Ripper.
- Reporting: What performance limitations are you observing with password cracking tools?

## Wrapup
Terminate any cloud systems you no longer need to avoid incurring unexpected charges.
