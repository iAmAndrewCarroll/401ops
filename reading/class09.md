# Reading 9: Public Key Infrastructure (PKI)

[Resource: What is Public Key Infrastructure (PKI)?](https://www.ssh.com/academy/pki)

# PKI Overview

**1. What are the three main components which make up PKI?**
- **Certificate Authorities (CAs):** These are trusted entities that issue digital certificates, authenticating the identity of users or devices.
- **Digital Certificates:** These are electronic documents issued by CAs that link public keys with entities (like users or devices), thus validating their identity.
- **Public and Private Keys:** A pair of cryptographic keys where the private key is known only by the entity and used for signing, and the public key is used by others to verify signatures.

**2. How would you explain, to a non-technical friend, the role PKI plays in protecting traffic between your browser and a web server?**
- **Internet Security Simplified:** Think of PKI as a system for creating secure IDs for websites. When you visit a website, PKI helps ensure you're talking to the real website and not an imposter.
- "It's like checking a person's ID before letting them into a secure building. PKI checks the website's ID (certificate) to make sure it's legitimate before establishing a secure connection."

**3. What is the main weakness of the PKI architecture?**
- **Trust Issues:** The primary weakness is that any CA can issue a certificate for any entity, which can be problematic if a CA is compromised or acts maliciously.
- **Global Concerns:** This is especially concerning in cases where CAs are under the control of authoritarian regimes, potentially leading to the issuance of fraudulent certificates for espionage or other malicious activities.
