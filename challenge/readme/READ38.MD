# Ops Challenge: XSS Vulnerability Detection with Python

## Overview
Now that you’ve studied and practiced XSS, it’s time to explore Python’s capabilities in helping us automate the detection of vulnerabilities like XSS. Today you will learn how a Python script can be written to evaluate a target for XSS vulnerabilities. Due to its extensive libraries and modules, the possibilities for creating useful security tools in Python are seemingly boundless! Check out [Wapiti](https://pypi.org/project/wapiti3/), a full web application security scanner coded in Python and installable using pip.

## Objectives
Programmatically detect the presence (or lack) of a XSS vulnerability in a given target URL using a Python script

## Resources
[How to Build a XSS Vulnerability Scanner in Python](https://www.thepythoncode.com/article/make-a-xss-vulnerability-scanner-in-python)

## Staging
For this Ops Challenge, you’ll need to use VS Code to SSH into Web Security Dojo and prepare a few things. Here are the steps to take:
1. Set Web Security Dojo to Bridged mode in VirtualBox.
2. Identify its IP address in terminal.
3. Verify SSH is running with `sudo systemctl status sshd` (the credentials to this VM are dojo/dojo)
4. SSH into Web Security Dojo from VS Code using `ssh dojo@ip` where “ip” is its IP address
5. In VS Code, install the Python extension via the extensions marketplace.
6. Run `sudo apt update`
7. Try `sudo apt install python3` to verify Python 3 is installed as an APT package on Web Security Dojo.
8. Try `pip3 --version` to verify Pip3 is installed.
9. Run `pip3 install bs4` to install Beautiful Soup, which is used by the demo code
10. In VS Code, open the desktop of Web Security Dojo and access today’s folder on the desktop.
11. Create a new `challenge.py` file and paste the demo code into it.
12. Now you’re all set to execute today’s Ops Challenge.

## Requirements
Copy the DEMO.md file from class repo > class-38 > challenges and complete the TODOs. Fully annotate any missing comments and populate any missing variables/code. Test the script in Web Security Dojo to confirm the output is correct.
- This target URL should yield a positive vulnerability detection: https://xss-game.appspot.com/level1/frame
- This target URL should yield a negative vulnerability detection: http://dvwa.local/login.php

## Stretch Goals (Optional Objectives)
- Write a separate Python script that detects for SQL vulnerability in the target web app.
- Reference [How to Build a SQL Injection Scanner in Python](https://www.thepythoncode.com/article/sql-injection-vulnerability-detector-in-python)
- Test the script in Web Security Dojo to confirm the output is correct

#############################################################################################################

:syringe: SQL Injection Links :syringe:
- [SQL Injection Payloads list](https://github.com/payloadbox/sql-injection-payload-list)
Scanning Tools:
- https://github.com/sqlmapproject/sqlmap :star: - the one I use the most
- https://github.com/ron190/jsql-injection
- https://github.com/Neohapsis/bbqsql
- https://github.com/codingo/NoSQLMap
- https://github.com/stamparm/DSSS

[A youtube link for some stuffs](https://www.youtube.com/watch?v=ciNHn38EyRc&ab_channel=Computerphile)