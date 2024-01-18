# Lab: Protecting Data at Rest

## Overview

It is common for organizations to have a FDE encryption policy, requiring all hard drives to be encrypted prior to deployment. Today you will perform FDE on Windows 10 and selective directory encryption on Ubuntu Linux Server.

## Objectives

- Perform FDE on a Windows 10 VM using BitLocker.
- Encrypt a Linux VM directory using ecryptfs

## Resources

- [What is a TPM chip?](https://www.laptopmag.com/articles/tpm-chip-faq)
- [How to Use BitLocker Without a Trusted Platform Module (TPM)](https://www.howtogeek.com/howto/6229/how-to-use-bitlocker-on-drives-without-tpm/)
- [How to Encrypt a USB Flash Drive or SD Card with Windows 10](https://www.groovypost.com/howto/encrypt-flash-drive-sd-card-windows-10-bitlocker/)
- [Enable-BitLocker via Powershell](https://docs.microsoft.com/en-us/powershell/module/bitlocker/enable-bitlocker?view=win10-ps)
- [Configuring LUKS: Linux Unified Key Setup](https://www.redhat.com/sysadmin/disk-encryption-luks)
- [How to use eCryptfs on Linux](https://linuxhint.com/ecryptfs_linux/)

## Tasks

### Part 1: Staging

To complete this lab, you will need:

- Class-05-cryptor VM
- Windows 10 VM

Warning: This lab involves the encryption of significant clusters of data. If you are unsure of the consequences of your actions, seek assistance. Your data is your responsibility to backup and protect, so careful decision making is necessary to safely complete this lab.

### Part 2: Windows FDE

1. Save state your Windows 10 VM before proceeding.
2. Find BitLocker settings in Windows 10 and toggle it on.
3. Under “Choose how to unlock your drive at start” select “Enter a password” and enter your usual password.
4. Under “How do you want to backup your recovery key” select “Print the recovery key” and save a PDF to your Desktop for now. In a production environment, you’d want to save this to a backed-up file server for recovery in the event of lockout.
5. Select “Encrypt the entire drive” since we’re attempting FDE.
6. Select “New encryption mode”
7. Tick the box for the “Encryption check” option.
8. Reboot. Grab a screenshot of “Enter the password to unlock this drive.”
9. After entering the password, it will take you to the normal user login. Login as normal. On the system tray at the bottom right, BitLocker should now begin encrypting your Windows C: drive. You’ll want to take a screenshot when it completes, but for now, feel free to move onto Part 3 while you wait for the FDE procedure to complete.
10. Verify your C: drive is in an encrypted state.

### Part 3: Linux Directory Encryption

Sometimes you may only need to encrypt part of a file system. The Linux tool eCryptfs allows us to encrypt directories in a Linux system. This software package comes preinstalled on class-05-cryptor VM, which is where you’ll perform this part of the lab.

1. SSH into class-05-cryptor using cryptor/cryptor credentials.
2. Mount a new encrypted directory using eCryptfs.
3. Create a new .txt document within the encrypted directory.
4. Try viewing the document. You should be able to see the document because the directory is currently mounted.
5. Unmount the directory with the `umount` command.
6. Try viewing the document. You should now only see the ciphertext. Include a screenshot of the ciphertext on your submission.

### Part 4: Reporting

1. **What is the purpose of the TPM chip and why is it normally required to operate BitLocker on a Windows 10 PC?**
   - The TPM (Trusted Platform Module) chip is a secure crypto-processor that is designed to carry out cryptographic operations. Its main purpose is to secure hardware through integrated cryptographic keys.
   - For BitLocker on a Windows 10 PC, the TPM chip provides a secure environment for the encryption keys used by BitLocker. It enhances security by ensuring that the system booting process hasn’t been tampered with and that the encrypted drive is in its original computer.
   - BitLocker typically requires a TPM to automatically encrypt the drive without needing user interaction at each startup, thus providing a seamless experience while maintaining strong security.

2. **Are laptop computers secured against theft out of the box? What precautions can be taken to ensure data confidentiality in the event of laptop theft?**
   - Laptop computers are not fully secured against theft out of the box. Physical access to a device can potentially compromise data, even if it is password-protected.
   - To ensure data confidentiality in the event of laptop theft, several precautions can be taken:
     - Full Disk Encryption (FDE): Using tools like BitLocker (Windows) or FileVault (macOS) to encrypt the entire hard drive.
     - Strong Passwords: Using complex, unique passwords for user accounts and disk encryption.
     - Regular Backups: Regularly backing up data to a secure, off-site location.
     - Physical Security: Using cable locks or secure docking stations to physically secure laptops, especially in public or semi-public spaces.
     - Tracking Software: Installing tracking software that can help locate a stolen laptop.

3. **What data theft scenarios do today’s tools not defend against?**
   - **Phishing Attacks:** Tools like BitLocker or eCryptfs do not protect against phishing attacks where users are tricked into revealing sensitive information.
   - **Malware Infection:** If a device is infected with malware, especially keyloggers or ransomware, the data can be compromised despite being encrypted.
   - **Insider Threats:** Employees or individuals with authorized access can potentially misuse data, bypassing encryption measures.
   - **Cold Boot Attacks:** Attackers with physical access can potentially extract encryption keys from a computer's RAM if it was recently powered down.

4. **Consider data at rest vs. data in motion. How do these two categories affect how you approach securing data?**
   - **Data at Rest:** Refers to data that is stored on a physical medium. Encryption at the disk level (like FDE) is crucial. This includes securing databases, hard drives, and any storage media. The focus is on preventing unauthorized access to data if the storage medium is compromised.
   - **Data in Motion:** Refers to data that is being transmitted across a network. The focus here is on securing the transmission channels. This is typically achieved through encryption protocols like SSL/TLS for internet traffic or VPNs for secure remote access.
   - The approach to securing each type varies:
     - For data at rest, the emphasis is on strong encryption standards, access controls, and physical security.
     - For data in motion, the priority is on secure, encrypted communication channels, network security practices, and ensuring endpoint security. 

Securing data requires a comprehensive approach that includes both protecting data at rest and in motion, each with its specific tools and strategies.
