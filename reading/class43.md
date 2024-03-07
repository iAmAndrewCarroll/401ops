# Read 43: Sniffing and Evasion

[Resource: What is a Sniffing Attack in System Hacking](https://geeksforgeeks.org/what-is-sniffing-attack-in-system-hacking/)

1. **Explain a Sniffing attack using non-technical terms.**
   - Imagine you're having a private conversation in a crowded place, and someone secretly listens in without you knowing. A sniffing attack is similar but occurs on the internet. It's when someone secretly watches the data moving across the network to steal or misuse information.

2. **What are the two types of sniffing attacks and what are some pros and cons of each approach?**
   - The article primarily discusses two methods involved in sniffing attacks: general packet sniffing and ARP spoofing.
     - **General Packet Sniffing**
       - **Pros**: Can analyze traffic for vulnerabilities or passwords without being detected, requires less active engagement with the target system.
       - **Cons**: Less direct control over the target system, limited to passively captured data, effectiveness depends on the amount of unencrypted data transmitted.
     - **ARP Spoofing**
       - **Pros**: Allows the attacker to reroute the victim's traffic through their machine, enabling data interception and session hijacking.
       - **Cons**: More easily detectable compared to passive sniffing, requires some level of access to the victim's network, less effective in well-secured environments.

3. **How does encryption protect traffic against sniffing attacks?**
   - Encryption scrambles the data transmitted over the network into a format that is unreadable without the correct decryption key. Even if a sniffer captures encrypted packets, without the key, the data remains inaccessible and meaningless. This acts like turning your private conversation into a secret code that only you and the intended recipient can understand, keeping it safe from eavesdroppers.