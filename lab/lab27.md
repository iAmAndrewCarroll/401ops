# Lab: Persistence

## Overview
As documented in MITRE ATT&CK® tactic TA0003, adversaries upon establishing a foothold will apply various methods of implementing a “backdoor” to the targeted system, generally known as establishing persistence. Our lab today explores how this is done using the infamous attack framework, PowerShell Empire. By reproducing the threat at a technical level, we can use this to build a model of the threat and hopefully implement proper defenses.

## Scenario
After reviewing your findings, Security Director Dyson shakes his head during a tense Zoom call. “Your T1021 findings suggest data leakage, perhaps an insider threat or some kind of credential exposure we’re not aware of. To address this, we are updating passwords and encryption keys across the organization to protect critical systems. However, something new has come to light; an internal analyst suggested to me that T1059.003 was used to establish persistence from a C2 server using the PowerShell Empire framework. If so, we’ll need to see in greater detail what that technique looks like. That’s where you come in: I’d like you to model out at a technical level how this kind of backdoor could have been installed on one of our Windows 10 endpoints to establish a persistent shell. Once we know how this works, we’ll be better prepared to defend against it.”

## Objectives
- Use PowerShell Empire to establish a persistent shell to a victim Windows 10 computer.
- Compose a detailed report on how this works

## Resources
- [MITRE ATT&CK®](https://attack.mitre.org/)
- [Empire Documentation](https://bc-security.gitbook.io/empire-wiki/)
- [Empire GitHub Repository](https://github.com/BC-SECURITY/empire-docs)
- [PowerShell Empire Complete Tutorial For Beginners](https://www.youtube.com/watch?v=52xkWbDMUUM&ab_channel=HackerSploit)

## Tasks

### Part 1: Staging
For today’s lab you’ll need a Windows 10 VM and a Kali Linux VM with Empire installed. Kali will be our C2 server. To install PowerShell Empire on your Kali VM, simply run the command: sudo apt install powershell-empire

Windows & Kali talking
![Windows & Kali Talking](media/lab27-1.png)


- Start PowerShell Empire
- Open up a terminal and start the Empire server by running `sudo powershell-empire server`. When the Empire server starts successfully, open up another terminal and start the Empire client by running `sudo powershell-empire client`. You should now have the Empire interactive prompt.

Empire Running
![Empire Running](media/lab27-2.png)

### Part 2: Setup a Listener
To prepare the attack, you’ll need to setup a listener in Empire. Reference the provided resources as to how to execute the procedures in this lab. Make sure the listener is running before proceeding to the next stage fo the lab.

- `listeners` will say no listeners currently active and enter listeners mode
- `back` will exit listeners mode
- `uselistener [protocol]` will add a listener for the entered protocol.
- `info` prints information about your listener. Key attributes to take notice of include:
  - Name
  - BindIP
  - Port
- `set Name` can change the name of your listener
- `set Port [number]` can change the port number of your listener
- `execute` will run the listener; a listener must be running in order to capture inbound data from the victim

Listening
![Listening](media/lab27-3.png)

### Part 3: Setup a Stager
Next, it’s time to setup a stager. Generate launcher.bat, copy it to the victim host, then run it from the terminal (you won’t see the output if you run it in File Explorer).

- The `usestager [stager]` command will setup a stager for use.
- Outfile is where the stager will be saved, which you can change
- `set Listener test` then `info` will show the updated listener name
- `execute` gives “Stager output written out to: /tmp/launcher.bat”
- `agents` lists compromised systems that you now have access to.
- `rename [current] [new]` changes the agent’s name.
- `interact [agent name]` launches the shell.

**Generate launcher.bat**
`/var/lib/powershell-empire/empire/client/generated-stagers/launcher.bat` is the path to the stager. Copy this file to the Windows 10 VM.

Generate launcher.bat
![Generate launcher.bat](media/lab27-4.png)

Rejected SSH Connection
![Rejected SSH Connection](media/lab27-5.png)

### Part 4: Reporting
Discuss in your own words the following:

- Why would an APT want to establish persistence on the Cyberdyne network?
- What kind of threat actor are we dealing with here?
- Based on your reproduction, how could the batch file payload have been transmitted to the victim and executed the first time?
- Reboot the Windows 10 VM. Is the agent still responding to Empire? Explore the limitations of such a technique.
- Is there a way to configure the batch file to not delete itself after executing? Explain.
- Evaluate technique T1037. As the threat actor, what kind of synergy does this technique offer alongside T1059.003?
- At a high level, brainstorm what we could potentially do as defenders to protect Cyberdyne against this type of threat. Explore the various types of security controls:
  - Preventative
  - Detective
  - Corrective
