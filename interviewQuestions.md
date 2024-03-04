# Final Interview Study Guide

The final interview may include both technical and behavioral question prompts. Brush up on your subject matter so that you can confidently and comprehensively answer the questions posed.

## Areas to Study

# Enhanced Final Interview Study Guide with HTTP Details

Prepare for a comprehensive assessment in your final interview, which may span both technical and behavioral questions. Delve into the subject matter detailed below to ensure a well-rounded understanding and the ability to discuss each topic confidently.

## In-depth Areas of Study

This guide is designed to help you navigate through the various domains we've encountered. Although this list is not all-encompassing, it aims to direct your study efforts effectively. Be mindful that the interview could cover topics beyond those mentioned here.

### Core Concepts

- **Linux Terminal Commands:**
  | Command    | Description                             |
  |------------|-----------------------------------------|
  | `ls`       | List files and directories             |
  | `cd`       | Change directory                       |
  | `mkdir`    | Make directory                         |
  | `pwd`      | Print working directory                |

- **Windows Terminal Commands:**
  | Command    | Description                             |
  |------------|-----------------------------------------|
  | `dir`      | List files and directories             |
  | `cd`       | Change directory                       |
  | `mkdir`    | Make directory                         |
  | `ipconfig` | Display IP configuration               |
  - **Example:** Navigating directories in Windows:

- **Troubleshooting Tools:**
  | Command        | Purpose                                |
  |----------------|----------------------------------------|
  | `ping`         | Verify network connectivity            |
  | `traceroute`   | Trace route to a destination           |
  | `netstat`      | Show network connections               |
  | `nslookup`     | Look up DNS information                |
  - **Example:** Testing connectivity to a website:

- **Shells, Scripts, Virtualization, and Active Directory Concepts**

### Automation and Scripting

#### Basics
Automation and scripting involve using code to automate tasks, reducing the need for manual intervention and increasing efficiency. Key concepts include:

- **Functions:** Reusable blocks of code that perform a specific task. In Python, functions are defined using the `def` keyword.
- **Loops:** Used to repeat a block of code multiple times. Python supports `for` and `while` loops.
- **Conditionals:** Allow the execution of code based on a condition. Python uses `if`, `elif`, and `else` statements.

#### Libraries and Scripting Languages
- **Python:** A versatile scripting language known for its readability and wide range of libraries such as NumPy for numerical computations and Pandas for data analysis.
- **PowerShell:** A task automation framework from Microsoft, built on .NET, offering advanced scripting capabilities for automating the management of Windows systems.
- **Bash:** A Unix shell and command language for the GNU Operating System, widely used for file manipulation, program execution, and printing text.
- **Batch files (.bat):** Scripts executed by the Windows Command Prompt, useful for automating repetitive command sequences.

### Computer Networking

#### Essentials
- **Ports and Protocols:** Critical for enabling communication between devices. Common protocols include HTTP (port 80) and HTTPS (port 443), with SSH on port 22 for secure access.
- **OSI Model Layers Overview:** A conceptual framework used to understand network interactions divided into seven layers:

| Layer          | Description                                             | Equipment                                           | Common Ports      |
|----------------|---------------------------------------------------------|-----------------------------------------------------|-------------------|
| Application    | Provides interface between user applications and network | Web browser, Email client                           | HTTP (80), HTTPS (443), SMTP (25), POP3 (110)    |
| Presentation   | Handles data translation, encryption, and compression   | SSL/TLS libraries, JPEG, GIF, PNG codecs            | -                 |
| Session        | Manages communication sessions between devices           | Session initiation protocol (SIP), NetBIOS          | -                 |
| Transport      | Ensures reliable data transmission and error recovery    | TCP, UDP, Flow control mechanisms                   | TCP (Transmission Control Protocol), UDP (User Datagram Protocol)   |
| Network        | Routes data packets across networks                      | Router, IP addressing, Routing protocols            | IP (Internet Protocol)                           |
| Data Link      | Controls access to physical network media                | Ethernet switches, MAC addressing, LAN protocols   | Ethernet (802.3), ARP (Address Resolution Protocol) |
| Physical       | Transmits raw data bits over physical media              | Network cables, Hubs, Repeaters                     | -                 |

| Port   | Protocol | Description                       |
|--------|----------|-----------------------------------|
| 80     | TCP      | HTTP - Hypertext Transfer Protocol (unencrypted) |
| 443    | TCP      | HTTPS - Hypertext Transfer Protocol Secure (encrypted) |
| 21     | TCP      | FTP - File Transfer Protocol      |
| 22     | TCP      | SSH - Secure Shell                |
| 25     | TCP      | SMTP - Simple Mail Transfer Protocol |
| 53     | TCP/UDP  | DNS - Domain Name System          |
| 110    | TCP      | POP3 - Post Office Protocol v3    |
| 143    | TCP      | IMAP - Internet Message Access Protocol |
| 3389   | TCP      | RDP - Remote Desktop Protocol     |
| 3306   | TCP      | MySQL Database                    |

#### Devices and Configurations
- **Routers:** Direct traffic on the internet, determining the best path for data packets.
- **Firewalls:** Monitor and control incoming and outgoing network traffic based on predetermined security rules.
- **Switches:** Connect devices within a network, using MAC addresses to forward data to the correct destination.
- **Subnets, LANs, WANs:** Organize network connections. Subnets divide a network into manageable pieces, LANs connect devices in close proximity, and WANs link large geographic areas.

#### Protocols and VPNs
- **DHCP (Dynamic Host Configuration Protocol):** Automatically assigns IP addresses to devices on a network.
- **DNS (Domain Name System):** Translates domain names to IP addresses.
- **VPN (Virtual Private Network):** Creates a secure connection over the internet, encrypting data as it travels.

#### APIs and Network Security
- **APIs (Application Programming Interfaces):** Allow different software applications to communicate with each other.
- **Network Security:** Involves measures to protect data during transfer, including encryption and the use of secure protocols like TLS/SSL.

### Security Operations

#### Systems and Analysis
- **SIEM (Security Information and Event Management):** Combines security information management (SIM) and security event management (SEM) to provide real-time analysis of security alerts.
- **Log Management:** Involves the collection, analysis, and retention of computer security logs to identify security incidents.
- **Sysmon:** A Windows system service and device driver that monitors and logs system activity to the Windows event log.
- **Log Analysis:** The process of examining logs to identify security incidents, policy violations, fraudulent activity, and operational problems.

#### Threats and Protections
- **Data Formats:** Include structured (e.g., databases) and unstructured data (e.g., emails).
- **Incident Response:** The organized approach to addressing and managing the aftermath of a security breach or attack.
- **MITRE ATT&CK:** A globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.
- **TTPs (Tactics, Techniques, and Procedures):** The behavior of an attacker, used to understand threat actors and their methods.
- **APTs (Advanced Persistent Threats):** Targeted attacks that remain undetected for long periods.

### Data Protection

#### Encryption, Hashing, PKI, TLS/SSL, Certificates, Password Security
- **Encryption:** The process of converting data into a code to prevent unauthorized access. It includes at-rest and in-transit protections.
- **Hashing:** A form of encryption that converts data into a fixed-size hash, which cannot be reversed.
- **PKI (Public Key Infrastructure):** A framework for managing digital certificates and public-key encryption.
- **TLS/SSL (Transport Layer Security/Secure Sockets Layer):** Protocols for securing communications over computer networks.
- **Certificates:** Digital

 documents that bind a public key with an identity (e.g., a person or organization).
- **Password Security:** Practices and methods used to protect passwords from unauthorized access and exploitation.

### Cloud Computing Security

#### Providers, Models, AWS Security, Virtual Networks, Monitoring and Logging
- **Providers:** Companies that offer cloud computing services, such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).
- **Models:** Include public clouds, private clouds, and hybrid clouds, each with different levels of security control.
- **AWS Security:** Encompasses a wide range of features and services designed to protect AWS resources, including Identity and Access Management (IAM), Security Groups, and AWS Shield for DDoS protection.
- **Virtual Networks:** Isolated networks within the cloud that control inbound and outbound connections to resources.
- **Monitoring and Logging:** Essential for detecting and responding to security incidents within cloud environments. Services like AWS CloudTrail and CloudWatch provide logging and monitoring capabilities.

### Web Application Security

- **OWASP, Exploration Tools, Client-Side Storage, Session Management**
- **HTTP Communication:**
  - **HTTP Request-Response Cycle:** The essential interaction between client and server. 
  - **Common HTTP Request Methods:** Details the types of requests such as GET, POST, PUT, DELETE.
  - **HTTP Status Codes:** Provides feedback on the outcome of the HTTP request.

#### HTTP Request-Response Cycle

Understanding the HTTP request-response cycle is crucial for web application security, detailing how clients and servers exchange data.

1. **Client Sends Request:** Initiates the cycle with a request to the server.
2. **Server Processes Request:** The server processes the incoming request.
3. **Server Sends Response:** The server responds back to the client.
4. **Client Receives Response:** The client receives and, typically, displays the response.

#### Common HTTP Request Methods

| Method | Description                                      |
|--------|--------------------------------------------------|
| GET    | Requests data from a specified resource.         |
| POST   | Submits data to be processed to a resource.      |
| PUT    | Updates a specified resource with new data.      |
| DELETE | Deletes the specified resource.                  |

#### HTTP Status Codes

| Code | Description                                      |
|------|--------------------------------------------------|
| 200  | OK - The request was successful.                 |
| 404  | Not Found - The resource was not found.          |
| 500  | Internal Server Error - A server error occurred. |
| 403  | Forbidden - Request is understood but refused.   |

#### TCP Handshake (SYN/ACK)

The TCP handshake, also known as the three-way handshake, is a three-step process used to establish a connection between a client and server in a TCP/IP network. It involves the following steps:

| Step      | Description                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------|
| 1. SYN    | The client sends a SYN packet to the server to initiate a connection request.                           |
| 2. SYN-ACK| If the server is available and willing to establish a connection, it responds with a SYN-ACK packet, indicating acknowledgment of the client's request and its readiness to proceed. |
| 3. ACK    | Finally, the client sends an ACK packet back to the server, acknowledging the server's response. This completes the handshake process, and both sides are now synchronized and can start exchanging data. |

The TCP handshake is a fundamental aspect of network communication, ensuring reliable and orderly transmission of data between clients and servers.

## Governance and Compliance

### CIA Triad
The CIA Triad is a model designed to guide policies for information security within an organization. It stands for:

- **Confidentiality:** Ensuring that data is accessible only to those authorized to access it.
- **Integrity:** Assuring the accuracy and reliability of data and information, ensuring it's not altered by unauthorized individuals.
- **Availability:** Ensuring that authorized users have access to the data and resources when needed.

### Risk Analysis
Risk analysis involves identifying potential threats to an organization's information and information systems and determining the likelihood and impact of these threats. It can be divided into two main types:

- **Qualitative Risk Analysis:** Uses subjective judgment based on non-quantifiable information, such as the severity of the impact or the probability of occurrence.
- **Quantitative Risk Analysis:** Involves the use of quantifiable metrics to assess risk, including potential financial costs.

### Policies and Procedures
Policies and procedures are essential for establishing a security framework within an organization. They include:

- **Policies:** Broad statements that provide guidance and principles for decision-making.
- **Procedures:** Detailed steps that must be followed to adhere to the policies.

### Reporting
Reporting in governance and compliance refers to the process of collecting, analyzing, and distributing security-related information within an organization. It includes incident reports, audit findings, and compliance reports.

### Compliance
Compliance involves adhering to laws, regulations, and guidelines relevant to an organization's operations. This includes industry-specific regulations like PCI-DSS for payment card data, HIPAA for healthcare information, and GDPR for data protection and privacy in the European Union.

### Auditing
Auditing is the process of evaluating an organization's adherence to regulatory compliance, policies, and procedures. Audits can be internal or external and are essential for identifying non-compliance and areas for improvement.

## Advanced Security Topics

### Threat Modeling
Threat modeling is a proactive approach to identifying potential threats to a system, including the motivations and capabilities of adversaries, and determining the likelihood and impact of these threats. It involves the identification of valuable assets, the software and system architecture, the identification of potential threats, and the implementation of measures to mitigate these threats.

### Cyber Kill Chain
The Cyber Kill Chain framework, developed by Lockheed Martin, describes the stages of a cyberattack, from reconnaissance to actions on objectives. Understanding these stages helps organizations to better defend against attacks:

1. **Reconnaissance:** Gathering information about the target before the attack.
2. **Weaponization:** Creating malware designed to exploit the target.
3. **Delivery:** Transmitting the malware to the target.
4. **Exploitation:** Executing the malware on the target system.
5. **Installation:** Installing a backdoor for persistent access.
6. **Command and Control (C2):** Establishing a channel to control the compromised system.
7. **Actions on Objectives:** Executing the actual objective of the attack.

### Threat Hunting
Threat hunting is a proactive security search through networks, endpoints, and datasets to detect and isolate advanced threats that evade existing security solutions. This involves understanding normal baselines and seeking anomalies that could indicate a threat.

### Digital Forensics
Digital forensics involves the investigation of digital devices to preserve, identify, extract, and document computer evidence. This evidence can be used in the prosecution of cybercrime. The process includes securing the scene, collecting evidence, analysis, and reporting.

### Network Analysis
Network analysis involves monitoring and analyzing network traffic to detect anomalies, optimize performance, and identify security threats. Tools for network analysis include packet sniffers, network mappers, and flow data analyzers.

### Penetration Testing
Penetration testing (pentesting) is an authorized simulated cyberattack on a computer system, performed to evaluate the security of the system. The test is used to identify weaknesses (including the potential for unauthorized parties to gain access) as well as strengths, enabling a full risk assessment to be completed.

| Stage                     | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Planning and Reconnaissance| Define the scope and goals of a test, including the systems to be addressed and the testing methods to be used. |
| Scanning                  | Understand how the target application will respond to various intrusion attempts. |
| Gaining Access            | Web application attacks, such as cross-site scripting, SQL injection, and backdoors. |
| Maintaining Access        | To see if the vulnerability can be used to achieve a persistent presence in the exploited system. |
| Analysis                  | Compiling the results of the penetration test and making recommendations for security improvements. |

