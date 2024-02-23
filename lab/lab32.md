### Lab: Malware Traffic Analysis with Wireshark

#### Overview

Malware analysts use sandboxed lab environments to study malware behavior. You need not be a dedicated malware researcher to be tasked with the same; oftentimes post-incident activities necessitate an investigation activity in which you scrutinize all minutiae of evidence in an effort to better prepare for next time.

“In June 2017, there were 1,726 job postings for malware analysts for which only 52 candidates applied. This is because malware analysis is an arduous process, requiring a wealth of knowledge, a lot of patience, and, occasionally, disruptive thinking.” -Toolbox.com

#### Objectives

- Download a set of data from a scenario
- Analyze the data to determine what took place
- Write an incident report

#### Resources

This lab requires FLARE VM on an isolated subnet. Review the below articles to brush up on your Wireshark skills for this lab.

- [Wireshark Tutorial: Changing Your Column Display](https://unit42.paloaltonetworks.com/unit42-customizing-wireshark-changing-column-display/)
- [Wireshark Tutorial: Identifying Hosts and Users](https://unit42.paloaltonetworks.com/using-wireshark-identifying-hosts-and-users/)
- [Wireshark Tutorial: Display Filter Expressions](https://unit42.paloaltonetworks.com/using-wireshark-display-filter-expressions/)
- [Wireshark Tutorial: Exporting Objects from a Pcap](https://unit42.paloaltonetworks.com/using-wireshark-exporting-objects-from-a-pcap/)
- [Wireshark Cheat Sheet](https://cdn.comparitech.com/wp-content/uploads/2019/06/Wireshark-Cheat-Sheet-1.jpg)

#### Tasks

##### Part 1: Staging

Time to figure out what really took place based on the evidence we have available.

- Disable Windows Defender Antivirus in FLARE VM
  - Virus & threat protection > Manage settings > Real-time protection > Off
- Open the evidence package named “class-32-traffic.7z” on your FLARE VM desktop using password “malwareinside” to open.
  WARNING: Part of this package contains live malware. Ensure that you download this into a sandboxed VM that is isolated from the host PC and the rest of your network. You have been warned.
  - NAT Network so you have internet access OR you can leave network adapters unattached but you will not have internet access.

##### Part 2: Malware Traffic Analysis

Refer to this information about the environment:

- LAN segment range: 192.168.200.0/24 (192.168.200.0 through 192.168.200.255)
- Domain: quiethub.net
- Domain controller: 192.168.200.8 - Quiethub-DC
- LAN segment gateway: 192.168.200.1
- LAN segment broadcast address: 192.168.200.255

Evaluate the evidence; use the tools you’ve learned thus far to piece together the details of what took place. In order to complete this lab, you’ll need to use critical thinking and careful analysis to reconstruct the events that took place.
- Open the packet capture file in Wireshark.
- Open the alerts.txt file
- Now start digging...
- Notice that local environment info for the Flare VM and we can see that the IP 25.185.113.20 is a rogue connection!  An external connection.

Forensic analysis of data files can be tedious, dry, tiresome, and even frustrating! If you ever get stuck, start with the most obvious signals and let those clues guide your next steps. Ask yourself: “Did the evidence lead me here?” If the answer is no, go back to the beginning and rethink your approach.

##### Part 3: Reporting

Write an incident report based on your findings. Include the following components:

- Executive Summary: Include when, who, and what happened.
- Details: Include details of the victim such as hostname, IP address, MAC address, Windows user account name.
- Indicators of Compromise (IOCs): Include SHA256 hashes and details of the malware and/or artifacts, IP addresses, domains and URLs associated with the infection.

Take care not to accidentally transmit malware. All artifacts should remain on your FLARE VM.
