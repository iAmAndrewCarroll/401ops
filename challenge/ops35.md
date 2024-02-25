### Lab: Web Vulnerability Scanning with Nmap

#### Overview

As security professionals, we are sometimes called upon to evaluate web applications for vulnerabilities. Today you will experiment with a tool not traditionally known as a vulnerability scanner: Nmap!

#### Objectives

- Perform basic Nmap scans against a web server
- Utilize the Nmap Scripting Engine (NSE) for vulnerability detection
- Investigate web server vulnerabilities and report findings

#### Resources

- [Nmap Cheat Sheet](https://www.stationx.net/nmap-cheat-sheet/)
- [http-enum NSE Script](https://vulners.com/nmap/NMAP:HTTP-ENUM.NSE)
- [Get Started Writing Your Own NSE Scripts for Nmap](https://null-byte.wonderhowto.com/how-to/get-started-writing-your-own-nse-scripts-for-nmap-0187403/)
- [Lua Language Documentation](https://www.lua.org/manual/5.1/)

#### Tasks

##### Part 1: Staging

Your instructor will provide the class an OVA of the target system.

- Download and import the “class-35-webserv” OVA, insert the DVWA ISO, then boot from the ISO. Set it to NAT Network.
- Startup Kali Linux VM on the same NAT Network. Check that you can ping the web server and view its hosted page via a browser.

##### Part 2: Basic Nmap Scans

Perform basic Nmap scans against the target web server:

- Perform the highest intensity service and version scan against the target.
- Attempt to detect the operating system of the target.
- Have Nmap perform a port scan of only the well-known port numbers.

##### Part 3: Scanning with the Nmap Scripting Engine (NSE)

Execute Nmap scripts against the target:

- Execute `http-title.nse` to grab the title of a web page.
- Execute `http-enum.nse` to aggressively enumerate files and directories.
- Execute `vulscan.nse` to query CVE databases for vulnerabilities.
- Write your own .nse script to gather information about the target.

##### Part 4: Reporting

Answer the discussion prompts:

1. What are some of the biggest security concerns on the web server?
2. Why might a security professional choose to use Nmap NSE for evaluating a web app target?
3. In your opinion, how can adopting scripting and extensible defenses change the way security professionals handle operations?

#### Stretch Goals (Optional Objectives)

- Achieve root user access to the web server and explain how you accomplished this feat of hacking.

#### Submission

- Create a new blank Google Doc.
- Include the above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that “Anyone with the link can view”.
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
