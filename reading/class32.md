# Read 32: Malware Traffic Analysis with Wireshark

[Resource: What is Malware Analysis?](https://www.spiceworks.com/it-security/data-security/articles/what-is-malware-analysis-definition-types-stages-best-practices/)

[Resource: ChatGPT, Google, and YouTube](https://www.youtube.com/watch?v=H1bb92CPSGk)

# Malware Analysis Overview

**1. Explain your job responsibilities as a Malware Analyst to a family member.**
- As a Malware Analyst, my main responsibility is to dissect and understand malicious software, also known as malware, to protect computer systems from cyber threats. I examine the code of malware to determine how it works, where it came from, and what damage it can cause. My job involves running various tests and simulations to study the behavior of malware in controlled environments. I collaborate with other cybersecurity professionals to develop strategies for detecting and preventing malware attacks. Additionally, I keep up-to-date with the latest malware trends and techniques used by cybercriminals to stay ahead of potential threats.

**2. What are the six steps of the Malware Analysis process? What’s a good mnemonic you can use to remember it?**
- The six steps of the Malware Analysis process are:
  - **Capture**: Obtain the malware sample in an uncompressed format.
  - **Build**: Set up a safe environment, typically using virtual machines, to analyze the malware.
  - **Record**: Document the baseline of the operating environment before running the malware.
  - **Install**: Install necessary analysis tools in the virtual environment.
  - **Investigate**: Analyze the malware, which involves manual and automated techniques to understand its behavior.
  - **Document**: Compile detailed results into a report for further action and prevention.
- A good mnemonic to remember these steps could be "CBRIID" which stands for Capture, Build, Record, Install, Investigate, Document.

**3. You are tasked with analyzing a new malware sample. Which type of malware analysis would you conduct first and why?**
- For a new malware sample, I would conduct static malware analysis first. This involves examining the static properties of the malware, such as metadata and embedded assets, without running it. It helps to quickly identify indicators of compromise and assess the severity of the threat without risking damage to the system.
