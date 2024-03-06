Reading 42: Pass the Hash with Mimikatz

[Resource: What is Mimikatz](https://www.varonis.com/blog/what-is-mimikatz)

1. **Name the six credential-gathering techniques which Mimikatz is able to perform and explain how two of them work.**
   - **Pass-the-hash:** Utilizes stored password data (NTLM hash) to log in without needing to crack the password. It passes the hash string to the target computer for authentication.
   - **Pass-the-ticket:** Involves passing Kerberos tickets from one computer to another to gain unauthorized access. It's similar to pass-the-hash but with tickets instead of hash strings.
   - Overpass-the-hash (pass-the-key): Similar to pass-the-hash, this technique involves passing a unique key obtained from a domain controller to impersonate a user.
   - Kerberoast golden tickets: Attackers use a specific ticket for a hidden account called KRBTGT, granting non-expiring domain admin credentials to any computer on the network.
   - Kerberoast silver tickets: Leveraging a feature in Windows, this attack allows users to utilize tickets-granting server (TGS) tickets for authenticating to service accounts on the network.
   - Pass-the-cache: This attack, while not specific to Windows, utilizes saved and encrypted login data on non-Windows systems, like Mac/UNIX/Linux.

2. **What are four ways we can defend against Mimikatz attacks. Explain how two of the mitigations can stop Mimikatz.**
   - **Restrict admin privileges:** By limiting admin privileges to only those who need them, organizations can reduce the attack surface area. This prevents attackers from gaining root access on a Windows box, which is often a prerequisite for executing Mimikatz.
   - **Disable password caching:** Windows caches recently used password hashes, which Mimikatz can exploit. Disabling password caching reduces the likelihood of attackers accessing these cached passwords, thereby mitigating potential Mimikatz attacks.