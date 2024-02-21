### Lab: Threat Hunting with Zeek, RITA

#### Overview

Many organizations now employ security teams that proactively search for cyber threats on the company network. We can use the capabilities of tools like RITA to actively hunt for threats in our systems.

#### Objectives

- Complete all four of the Active Countermeasures Threat Hunting Labs: [Active Countermeasures Threat Hunting Labs](https://activecm.github.io/threat-hunting-labs/)

#### Resources

- [Rita VM](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table)
- [Active Countermeasures Threat Hunting Labs](https://activecm.github.io/threat-hunting-labs/)
- [Analyzing pcap files](https://tshark.dev/analyze/packet_hunting/packet_hunting/)
- [A guide to using tshark](https://linuxhint.com/wireshark-command-line-interface-tshark/)

#### Tasks

##### Part 1: Staging

The lab today utilizes the following tools:

- Wireshark
- tshark
- Zeek
- Rita
- LibreOffice Calc

Use the Rita VM provided which already has Zeek and Rita installed for you.

##### Part 2: Active Countermeasures Labs

Complete all four of the Active Countermeasures Threat Hunting Labs.
Take notes as you work through the AC lab segments. Document your experiences in your submission today.
NOTE: The large pcap files from the labs may cause Wireshark to crash, if this occurs, perform the exercise using tshark.

***

***

***

## Lab: Threat Hunting with Zeek, RITA (Enhanced Markdown Guide)

### Overview

Proactive threat hunting is employed by many organizations to secure their networks. This lab utilizes RITA to actively seek potential threats within your system.

### Objectives

* Complete all Active Countermeasures Threat Hunting Labs: [https://activecm.github.io/threat-hunting-labs/](https://activecm.github.io/threat-hunting-labs/)

### Resources

* Rita VM: [https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table)
* Active Countermeasures Threat Hunting Labs: [https://activecm.github.io/threat-hunting-labs/](https://activecm.github.io/threat-hunting-labs/)
* Analyzing pcap files: [https://tshark.dev/analyze/packet_hunting/packet_hunting/](https://tshark.dev/analyze/packet_hunting/packet_hunting/)
* A guide to using tshark: [https://linuxhint.com/wireshark-command-line-interface-tshark/](https://linuxhint.com/wireshark-command-line-interface-tshark/)

### Tasks

#### Part 1: Staging

**Tools:**

* Wireshark
* tshark
* Zeek
* Rita
* LibreOffice Calc (Optional)

**Environment:**

* Rita VM (pre-installed with Zeek and Rita)

**Steps:**

1. **Launch Rita VM:** Ensure proper VM function and network access within it.
2. **Open Wireshark:** Locate and launch Wireshark from the Rita VM applications menu.
3. **Capture Traffic:**
    - Click the red "Start capturing packets" button on the Wireshark toolbar.
    - Optionally, use the capture filter bar for specific criteria (e.g., `ip.src == 192.168.1.10`). Refer to Wireshark's capture filter documentation for advanced options: [https://wiki.wireshark.org/CaptureFilters](https://wiki.wireshark.org/CaptureFilters)
4. **Analyze Traffic:**
    - Look for unusual spikes, connections to known malicious IPs/domains (check threat intelligence feeds), suspicious protocols/ports, or strings indicating malware activity.
    - Utilize Wireshark's coloring rules to highlight potential threats: [https://wiki.wireshark.org/ColoringRules](https://wiki.wireshark.org/ColoringRules)
5. **Utilize Zeek (Optional):**
    - Use Zeek's scripting language for specific questions about captured traffic.
    - Example commands:
        - `conn count`: Count connections by various criteria.
        - `http.req_header`: Analyze HTTP request headers for threats.
        - `dns.qry`: Investigate DNS queries for suspicious domains.
    - Refer to Zeek documentation for comprehensive commands and functionalities: [invalid URL removed]
6. **Utilize Rita (Optional):**
    - Rita offers features like identifying potential C2 channels, detecting lateral movement, and correlating events from various network sources.
    - Consult Rita's documentation for specific commands and features: [invalid URL removed]
7. **Document Findings:**
    - Take detailed notes, including:
        - Timestamps of suspicious activity.
        - Source/destination IPs, ports, and protocols involved.
        - Observed strings or behaviors suggesting threats.
        - Screenshots of relevant Wireshark displays.
8. **Export Data (Optional):**
    - Exporting data from Zeek or Rita can be helpful for further analysis or reporting.
    - Zeek supports various formats (CSV, JSON). Consult the documentation for specific commands. Rita also offers export options depending on the feature used.
9. **Use LibreOffice Calc (Optional):**
    - Organize and analyze exported data, especially for large datasets.
    - Learn about useful functions and formulas for data manipulation and analysis: [invalid URL removed]

#### Part 2: Active Countermeasures Labs

**Steps:**

1. **Access Labs:** Visit the Active Countermeasures Threat Hunting Labs website: [https://activecm.github.io/threat-hunting-labs/](https://activecm.github.io/threat-hunting-labs/)
2. **Complete Labs:**
    - Work through each lab meticulously, following the provided instructions.
    - Take notes as you progress, capturing key findings and challenges encountered.

