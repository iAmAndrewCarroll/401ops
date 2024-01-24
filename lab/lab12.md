# Lab: Log Analysis with Splunk

## Overview
Now that we’ve established a basic foundation of how a SIEM is deployed and configured to ingest log data, the next step is to start making sense of the data and how it will aid us in our day-to-day security operations. Logs that the SIEM collects can contain telltale signs of malicious activity, or direct evidence of incident-related actions on systems. Finding such clues is like finding a “needle in a haystack” as you parse oceans of text in your investigation. Aspiring security operations professionals should practice log parsing, searching, and analysis often in order to derive value from a system like a SIEM.

## Scenario
Wayne Enterprises has been a long time client of your MSSP. Today reports of the below graphic come in from their user community when people visited the Wayne Enterprises website, and some of the reports reference “P01s0n1vy.” P01s0n1vy is an APT group that has targeted Wayne Enterprises. Your goal is to investigate the defacement, with an eye towards reconstructing the attack via the Lockheed Martin Kill Chain.

- ![Defacement Image](media/defacement.png)

## Objectives
- Complete Boss of the SOC (BOTS) Version 1, Scenario #1 - APT.
- Analyze the log data to reconstruct the cyber kill chain.
- Document and report your findings.

## Resources
- This VM is required for classes 11 through 13.
  - [Splunk Server](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table)
- [Splunk Quick Reference Guide PDF](https://www.splunk.com/pdfs/solution-guides/splunk-quick-reference-guide.pdf)
- [Hunting with Splunk: The Basics](https://www.splunk.com/en_us/blog/security/hunting-with-splunk-the-basics.html)
- [Source repo for BOTSv1](https://github.com/splunk/botsv1)

## Tasks
### Part 1: Staging
1. Log into the same Splunk server you used yesterday and run the “Investigating with Splunk Workshop” app to access the lab instructions.
2. You’ll want to open a separate browser tab for querying data using the Search and Reporting app on this same Splunk server.

### Part 2: BOTSv1
Boss of the SOC is a blue-team CTF workshop that lets participants practice hunting and analysis skills. You will use Splunk and other tools to answer questions about security incidents that have occurred in a realistic but fictitious enterprise environment. It’s designed to emulate how real security incidents look in Splunk and the type of questions analysts must answer. The idea is to recreate the life of a security analyst facing down an adversary at all stages of an attack.

**Note**: This dataset contains evidence captured during actual computer security incidents, or from realistic lab recreations of security incidents. As such, the dataset may contain profanity, slang, vulgar expressions, and/or generally offensive terminology. If the possibility of encountering this type of offensive material is a concern to you or to any audience with whom you plan to share the dataset, please stop now and do not continue.

- Run the Splunk app, Investigating with Splunk Workshop.
- Work on completing the following sections in Boss of the SOC (BOTS) Version 1, Scenario #1 - APT:
  - Reconnaissance
  - Exploitation
- ![BOTSv1 Goals](botsv1_goals.png)
- Document your operations with attention to:
  - Function of each SPL query.
  - Reasons for running each SPL query.
  - How you obtained the requested information.

### Part 3: Reporting
Explain in your own words:

1. **What kind of attack was taking place on Wayne Enterprises systems?**
2. **Describe your findings for these stages of the kill chain:**
   - Reconnaissance
   - Exploitation
3. **How could the kill chain have been disrupted to prevent the attacker from progressing?**

**If you enjoyed today’s lab, find other blue team labs at CyberDefenders. Another blue team workshop similar to this is SANS DFIR NetWars.**

## Submission Instructions
- Create a new blank Google Doc.
- Include the above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that “Anyone with the link can view”.
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
