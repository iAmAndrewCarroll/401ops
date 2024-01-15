# Ops Challenge: File Encryption

## Overview
Encryption has been used since ancient times, long before computers ever became handheld devices with processing power rivaling that of old NASA supercomputers. A primary confidentiality tool, encryption can be used in a multitude of ways, including protecting data in motion and data at rest. Today you will practice encrypting and decrypting files, which constitute data at rest. You’ll also get to see how data integrity can be validated using hashing.

## Scenario
Initrobe is attempting to write SOPs regarding the handling of classified data files. You’ve been consulted on how files can be encrypted, transmitted, then decrypted.

## Objectives
1. Encrypt a file and a folder with 7-Zip
2. Encrypt and decrypt a file using Powershell, then Windows CLI
3. Generate an MD5 hash value from a secret message of your choosing, then send it to a classmate
4. Crack the secret message of your classmate’s MD5 hash value
5. Validate the integrity of a downloaded file using its hash value
6. Generate base64 ciphertext using OpenSSL in Linux and share it with a classmate
7. Decode your classmate’s secret message

## Resources
### Downloads
- [class-05-cryptor.ova](link_to_download) (2.63 GB Download)
- [7-Zip Installer](link_to_download) (1414KB Download)
- Win10 VM

### References
- [7-Zip](7zip_link)
- [Microsoft: Get-FileHash](get_filehash_link)
- [How To Encrypt And Decrypt Files in Windows Using Command Prompt](encrypt_decrypt_windows_link)
- [OpenSSL](openssl_link)
- [Using OpenSSL to encrypt messages and files on Linux](openssl_linux_link)

## Tasks
### Part 1: Staging Windows 10
- You’ll need a Windows 10 VM. If you don’t have one, you can try a pre-made OVA at [Windows 10 VM](windows_10_vm_link) or load a fresh one from ISO.
- Install 7-Zip on the Windows 10 VM.
- Download and import class-05-cryptor.ova.
- Set the VM to Bridge Mode.
- Turn it on and identify its IP address. The login credentials are cryptor/cryptor.
- SSH into the VM using a shell app of your choosing. Cmder and Git Bash come to mind.
- Use this terminal for the OpenSSL activity.

### Part 2: Data Encryption with 7-Zip in Windows
- Compression tools like 7-Zip can be installed on various operating systems to allow for quick password encryption of a file or set of files.
- Encrypt a single file with 7-Zip in the Windows GUI.
- Validate the encryption succeeded by decrypting and decompressing the archive contents to your desktop.
- Document the steps taken and include screenshots. Explain the steps taken.
- We can also use 7-Zip to obfuscate the contents of an archive.
- Encrypt a folder containing multiple files with 7-Zip in the Windows GUI. This time, encrypt the file names.
- Include screenshots of encrypted files in your submission. Explain the steps taken and what changed when you encrypted file names.

### Part 3: Data Encryption with EFS in Windows
- Windows has some built-in encryption capabilities. One way to perform the encryption operation is via Powershell.
- Encrypt a single file using PowerShell in Windows 10. Include a screenshot and the line of code you used.
- Decrypt a the file using PowerShell in Windows 10. Include a screenshot and the line of code you used.
- In Windows, you can also perform encryption directly from the command line interface.
- Encrypt a single file in Windows 10 CLI.
- Decrypt that same file in Windows 10 CLI.
- Include screenshots of encrypted files in your submission. Explain the steps taken.

### Part 4: Secret Messages with PowerShell Hash Generation
- Determining the source data from a hash is called “cracking” and is a different operation than decryption. Here’s why.
- Use PowerShell to generate the hash value of a single word or simple sentence in MD5 algorithm. Keep your original string simple and code-of-conduct friendly please! An example would be “hello” as your string.
- Post your MD5 hash value to Slack class channel for others to crack using rainbow table techniques.
- Example: “What does a baby computer call its father? 8d777f385d3dfec8815d20f7496026dc”
- Once a classmate has posted a MD5 hash value, crack it using a rainbow table and add it to your submission alongside the original hash value.
- Stuck on cracking a hash? Hint: Try an online hash cracker like Hashes.com
- Is MD5 considered secure? Why/why not?

### Part 5: Hash Validation
- Hash validation is a process by which we compare a file’s original hash to the hash of the file in front of us. Sometimes file servers and GitHub repos will publish the file’s hash in order for you to verify that the file you downloaded is legitimate and safe.
- Use PowerShell to generate the hash value of a small file, such as “example.txt”.
- Upload the file to Google Drive and generate a shareable link.
- Share the file with a classmate, along with the hash value.
- Have your classmate generate the hash value of the downloaded file and compare it to the value you provided.
- Once you have validated the hash of a file sent to you by a classmate, post screenshot evidence to your submission for the day.

### Part 6: Data File Encryption and Secret Messages with OpenSSL in Linux
- A versatile cryptography library, OpenSSL can also help us encrypt files.
- Compose a .txt file in Linux and write a short sentence in it, such as “Hello world!” or the like.
- Encrypt the .txt file with OpenSSL.
- Contact a classmate and ask them if it’s OK to send an OpenSSL-encrypted file over. Transmit once they’ve responded.
- When you have received the OpenSSL-encrypted file from your classmate, decrypt it.
- Include screenshots and contents of the file you decrypted in your submission. Explain the steps taken.
- OpenSSL can also encrypt a string of text.
- Use OpenSSL to generate base64 ciphertext from a cleartext string sentence.
- Post your ciphertext to Slack class channel for others to decrypt. Don’t indicate this is Part 7; keep your classmates guessing!
- Once a classmate has posted a base64 ciphertext string, decrypt it and add it to your submission alongside the original hash value.

### Part 7: Reporting
- Include in your Google Doc the below:
  - Why might you encrypt data in the workplace?
  - Why might you hash a file in the workplace?
  - What are some limitations to this type of encryption? Describe a few scenarios where these techniques would not be as useful.
  - How could data file encryption be used offensively by a cybercriminal or a pentester?
- Keep both the Win 10 VM and class-05-cryptor VM installed on VirtualBox. You’ll need both in Lab: Class 07.
