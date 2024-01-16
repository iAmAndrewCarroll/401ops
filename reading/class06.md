# Read 6: CIA Triad and CIS Benchmarks

[Resource 1: Applying the CIA Triad to Your Enterprise File Transfer](https://www.jscape.com/blog/implementing-the-cia-triad-when-transferring-files-through-the-internet)

[Resource 2: What Are MD5, SHA-1, and SHA-256 Hashes, and How Do I Check Them?](https://www.howtogeek.com/67241/htg-explains-what-are-md5-sha-1-hashes-and-how-do-i-check-them/)

**1. You have been made responsible for the company’s file server. How would you preserve the three elements of the CIA triad?**
- *Confidentiality*: To preserve confidentiality, ensure that access to sensitive company data is restricted to authorized individuals only. Use access controls, strong passwords, and encryption to protect data from unauthorized access.
- *Integrity*: Maintain data integrity by regularly checking files using hash functions (like MD5, SHA-1, or SHA-256) to detect any changes. Backup data to prevent loss, and implement measures to prevent unauthorized modifications.
- *Availability*: Ensure data availability by implementing redundancy and backup systems. This ensures that even if one server fails, the data remains accessible from another source, minimizing downtime.

**2. Explain how hashing verifies data integrity using non-technical terms.**
- Hashing is like creating a unique fingerprint for a file. When a file is downloaded, its hash value is generated. If the file is later altered, even by a small change, the hash value will be significantly different. By comparing the downloaded file's hash value to the provided hash value, you can quickly check if the file is exactly as it should be. It's like verifying if a picture matches its unique fingerprint; if they match, the picture is unchanged and trustworthy.

**3. How is hashing and encryption different?**
- *Hashing*: Hashing is a one-way process that generates a fixed-size string of characters (the hash value) from input data. It's primarily used for data integrity checks and cannot be reversed to retrieve the original data. It's like creating a unique seal for a document; you can verify if the document is tampered with, but you can't read its content from the seal.
- *Encryption*: Encryption is a two-way process that transforms data into a coded format using a key. It's reversible, meaning you can decrypt the data back to its original form if you have the key. Encryption is used to protect data confidentiality, ensuring that only authorized parties can access and decipher the information. It's like putting a document in a locked safe; you can unlock it with the right key to access the contents.
