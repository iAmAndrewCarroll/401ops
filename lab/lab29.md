# Lab: Modeling a Web Application

## Overview
The STRIDE model developed by Microsoft is a popular means of identifying computer threats, providing six major categories that most threats fall into. These threats can then be modeled into data flow diagrams (DFDs) to thoroughly visualize all movements of data in our system, granting a high level overview of processes, data stores, data flows, and trust boundaries. By utilizing threat models, protectors of essential computer systems can evaluate security threats in a systematic and structured fashion, allowing for more strategic and calculated formulation of defensive countermeasures.

## Scenario
This morning, Director Dyson addressed the final requirements for the project. “It has been a pleasure working with your team. We’ve made great progress in shoring up our defenses, and I have one last request to make of you. Our internal security teams would like to continue exploring the possibility of attack, and proactively implement defenses tailored to our environment. We suspect that the intruder was able to exploit a flaw in our public-facing web application, Genisys. Would you take a look at our processes and construct a threat model? This would be of long-term value as we make important changes to the way our systems interact with one another. I’ll forward you the details on our processes.”

## Objectives
- Use the Microsoft Threat Modeling Tool to construct a DFD based on the scenario above
- Clearly indicate all key assets, processes, and trust boundaries
- Generate a STRIDE threat model; after all, what could go wrong?

## Resources
- [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started)
- [Microsoft Threat Modeling Security Fundamentals](https://www.microsoft.com/en-us/download/details.aspx?id=6643)
- [Template: Web Application Threat Model](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff648866(v=pandp.10)?redirectedfrom=MSDN)
- [Template Sample: Web Application Threat Model](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff649779(v=pandp.10)?redirectedfrom=MSDN)

## Tasks

### Part 1: Staging your Toolkit
You will need Microsoft Threat Modeling Tool for today’s lab.

- Download and install Microsoft Threat Modeling Tool

### Part 2: Threat Modeling
Generate a threat model DFD using Microsoft Threat Modeling Tool. Elements of your DFD will include:
- Web application server
- WAF
- Data store
- All trust boundaries
- User/threat actor
- Tools used by threat actor
- Systems Administrator
- DBA
- All data flows and processes involved in the normal utilization and maintenance of your web app, including:
  - End user access
  - Administrator access
  - All security mechanisms in place such as encryption protocols

This is clearly [A Resourced: ChatGPT Image Generation: DFD](https://chat.openai.com/c/04f65164-8b5a-4484-8878-a51c73f6b3d5) that I prompted.
![TPS Reports and Data Flow Diagrams.  Somebody's got a case of the Mondays...From the 1999 movie Office Space with Ron Livingston, Jennifer Aniston, David Herman, Deidrich Bader, and Stephen Root.](media/lab29-1.jpg)

![Icons and teardrops.  A data flow diagram.](media/lab29-2.jpg)

### Part 3: Communicate Findings
Referencing the example in Template Sample: Web Application Threat Model, compose in your submission a full web application threat modeling report. Use DREAD to guide your thought process on what threats are present.
- Utilize Template: Web Application Threat Model
- When finished, submit both your Web Application Threat Model and DFD in a single Google Doc as indicated below.
