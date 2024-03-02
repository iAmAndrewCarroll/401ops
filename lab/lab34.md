### Lab 34: Forensic Investigation with Autopsy

#### Overview

Sometimes you’ll be evaluating an incident that already occurred, and receive data samples to investigate. Tools like Autopsy can facilitate this process. Today you’ll use Autopsy to explore data samples.

#### Objectives

- Complete at least three different scenarios using Autopsy

#### Resources

- [Autopsy Digital Forensics](https://www.autopsy.com/)
- [Data Artificats, Analysis Results and Reporting in Autopsy 4.19+](https://www.youtube.com/watch?v=5SHB4HwkX28&ab_channel=DFIRScience)
- 

#### Tasks

##### Part 1: Staging

You will need FLARE VM for this lab.

##### Part 2: Investigating with Autopsy

In today’s folder you’ll see twelve different scenarios you can investigate using Autopsy.

- Complete at least three different scenarios using Autopsy.
- If a results.txt file is present for the scenario, copy its text over to your Google Doc submission and fill out your findings using this as a template. Otherwise, document your own findings in your submission today.

Screenshots of getting staged and rolling:
![files and such](media/lab34-1)
![files and such](media/lab34-2)
![files and such](media/lab34-3)

Starting Autopsy:
![files and such](media/lab34-4)
![files and such](media/lab34-5)
![more setup](media/lab34-6)
![more setup](media/lab34-7)
![more setup](media/lab34-8)
![more setup](media/lab34-9)
![more setup](media/lab34-10)
![more setup](media/lab34-11)
![more setup](media/lab34-12)
![more setup](media/lab34-13)
![more setup](media/lab34-14)

Reminders from Lab 32 Suspicious Activities:
**Executables or Scripts:** Likely Evil EzXE download events
**DLL files:** Dotted Quad Host DLL Request entries (maybe 3.dll...)
**Anomalies (in the registry or system):** *ET SCAN* Behavioral Unusual and *ET EXPLOIT* Possible Zerologon entries
- Looking for unusual network traffic or signs of system compromise

Top Level Autopsy View:
![Top Level Autopsy View](media/lab34-15)

Deleted Files > File System (1) > SECOND-3.TXT & Listing info:
![Deleted Files > File System (1) > SECOND-3.TXT](media/lab34-16)
![Listing of Second-3.TXT](media/lab34-17)
**MD5 HASH: `d41d8cd98f00b204e9800998ecf8427e`**
![md5 hash](media/lab34-18)

VirusTotal Results for MD5 Hash `d41d8cd98f00b204e9800998ecf8427e`:
![VirusTotal Results](media/lab34-19)
![VirusTotal Results](media/lab34-20)
![VirusTotal Results](media/lab34-21)
![VirusTotal Results](media/lab34-22)
![VirusTotal Results](media/lab34-23)
![VirusTotal Results](media/lab34-24)

Tag the file:
![Tag the file](media/lab34-25)
![Tag the file](media/lab34-26)

Generate Report > HTML > All Results:
![Generate Report](media/lab34-27)
![Generate Report](media/lab34-28)
![Generate Report](media/lab34-29)
![Generate Report](media/lab34-30)

##### Part 3: Reporting

Answer these discussion prompts:

1. **How can Autopsy accelerate your ability to find important data on a hard disk image?**

   Autopsy can accelerate the process of finding important data on a hard disk image by providing comprehensive and specialized tools for forensic investigation. It automates many tasks that would otherwise be time-consuming if done manually, such as keyword searching, file carving, and analysis of file metadata. Additionally, Autopsy's indexing capabilities enable quick searching through large volumes of data, allowing investigators to efficiently pinpoint relevant information within the disk image.

2. **Why might the Autopsy timeline view be relevant in an investigation?**

   The Autopsy timeline view is relevant in an investigation because it provides a chronological overview of file activity and system events on the disk image. This timeline allows investigators to reconstruct the sequence of events leading up to and following an incident, which can be crucial for understanding the context and timeline of suspicious activities or data breaches. By visualizing the timeline, investigators can identify patterns, anomalies, and potential correlations between different events, aiding in the overall investigation process.

3. **How does Autopsy compare to manually searching a hard disk in something like Windows Explorer?**

   Autopsy offers several advantages over manually searching a hard disk using tools like Windows Explorer. Firstly, Autopsy is specifically designed for forensic analysis, providing features tailored to the needs of investigators, such as advanced search capabilities, file system analysis, and integration with external tools like VirusTotal for malware analysis. Additionally, Autopsy automates many tasks that would be tedious to perform manually, such as hashing, file carving, and generating detailed reports. This automation not only speeds up the investigation process but also reduces the risk of human error. Overall, Autopsy provides a more efficient and comprehensive solution for forensic investigation compared to manual methods using standard file management tools like Windows Explorer.

##### Stretch Goal (Optional Objectives)

Pursue optional objectives if you are an advanced user or have remaining lab time.

- Complete additional scenarios with Autopsy.
