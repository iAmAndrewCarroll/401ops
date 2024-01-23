# Lab: Foundational SIEM Operations

## Overview
A threat detection ecosystem is an essential part of efficient incident response. SIEM (Security Information and Event Management) tools help us aggregate valuable event logs and network traffic information from across the enterprise, granting full visibility to the security operations technician of the events taking place on the network. A proficiency in SIEM tools will allow you to respond quickly to security events unfolding in real time.

Today you will perform queries against a data set on Splunk Enterprise and develop various analytics.

## Objectives
- Import the SIEM into VirtualBox
- Complete the official Splunk Search Tutorial, these parts only:
  - Part 3: Using the Splunk Search App
  - Part 4: Searching the tutorial data
  - Part 5: Enriching events with lookups
  - Part 6: Creating reports and charts
  - Part 7: Creating dashboards
- Answer the reporting prompts

## Resources
- This VM is required for classes 11 through 13.
- [Splunk Server](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table)
- [Splunk How to Search Tutorial](https://docs.splunk.com/Documentation/Splunk/8.1.0/SearchTutorial/WelcometotheSearchTutorial)
- [Official Splunk Training Courses](https://www.splunk.com/en_us/training/free-courses/overview.html)

## Tasks
### Part 1: Staging Splunk
1. Download the pre-staged Splunk Server from the downloads table.
2. Import the VM into VirtualBox.
3. Set the network adapter to Bridge Mode. You’ll want to access the web portal via your immediate web browser for the least latency.
4. Launch the VM and login to the VM using vagrant/vagrant to identify its IP address.
5. Access the VM by opening a web browser to http://ipaddress:8000 where ipaddress is replaced with the VM’s IP address.
   
**Note**: If your Splunk instance has an expired enterprise license, you will have daily indexing limits of 500MB per day.

### Part 2: Incident and Analysis
Complete the official Splunk Search Tutorial. For each component of the lab tutorial, create notes in your submission, including screenshots of successful execution of today’s tutorial.

Skip Parts 1 and 2. The required datasets have already been uploaded and indexed.
- Part 3: Using the Splunk Search App
- Part 4: Searching the tutorial data
- Part 5: Enriching events with lookups
- Part 6: Creating reports and charts
- Part 7: Creating dashboards

**Note**: The tutorial might ask you to set specific time ranges e.g., Previous Week, Last 24 hours. These might not yield the expected results; instead, select “All time”.

### Part 3: Reporting
Answer the below discussion prompts in your own words in your Google Doc submission.

**1. Why would a security team benefit from SIEM implementation?**
   - A Security Information and Event Management (SIEM) system helps a security team by providing centralized monitoring and analysis of security events and incidents across an organization's IT infrastructure. It offers benefits like real-time threat detection, incident response automation, and compliance reporting. SIEM helps security teams detect and respond to threats faster, improve incident management, and enhance overall cybersecurity.

**2. What is an index?**
   - In the context of data management, an index is a data structure used to optimize the retrieval of records from a database or dataset. It acts like a table of contents in a book, allowing quick access to specific data points without the need to scan through the entire dataset. Indexing is crucial for improving the speed and efficiency of data retrieval in databases and search engines.

**3. What is a forwarder?**
   - A forwarder, in the context of IT and network management, is a software or hardware component used to collect and forward data from one system or source to another. In the context of log management and SIEM, a forwarder collects log data from various sources, like servers or network devices, and forwards it to a central SIEM system for analysis and storage. It helps streamline the process of aggregating and analyzing logs for security and monitoring purposes.

**4. How does a SIEM add value to an organization like Buttercup Games?**
   - A SIEM system adds value to organizations like Buttercup Games by enhancing their cybersecurity posture and overall operational efficiency. Here's how:
     - **Threat Detection:** SIEM can detect suspicious activities and security threats in real-time, helping Buttercup Games proactively respond to potential breaches.
     - **Incident Response:** It streamlines incident response by providing actionable insights and automated workflows, reducing response time.
     - **Compliance:** SIEM helps meet regulatory compliance requirements by generating reports and ensuring data protection standards are maintained.
     - **Data Analysis:** It provides valuable insights into network and system performance, helping optimize operations.
     - **Cost Reduction:** SIEM can help identify and mitigate security risks, potentially reducing the financial impact of data breaches.


