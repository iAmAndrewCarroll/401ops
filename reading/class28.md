# Reading 28: Log Clearing

[Resource: Log Tampering 101](https://resources.infosecinstitute.com/topics/hacking/ethical-hacking-log-tampering-101/)

**1. Explain some specifics of why a hacker might want to clear log files to a family member. Do not use the example from the article.**
- Hackers clear log files to cover their tracks and evade detection. Just as someone might erase footprints after sneaking into a house to avoid being caught, hackers delete log files to remove evidence of their unauthorized activities on a computer or network.

**2. What are three methods by which you can clear logs in a Windows system?**
- Three methods to clear logs in a Windows system are:
  - *Using 'clearlogs.exe' tool*: This utility clears security logs on a Windows system when executed.
  - *Meterpreter Command*: In the Metasploit framework, the command `clearev` in Meterpreter clears all logs.
  - *Windows Event Viewer*: Manually accessing the Event Viewer allows users to delete logs from the system.

**3. What are the four steps in the process of covering your tracks?**
- The four steps in covering tracks are:
  - *Disable Auditing*: Turn off the logging system to prevent recording new activities.
  - *Clearing Logs*: Erase existing logs that document the hacker's actions.
  - *Modifying Logs*: Alter log information to conceal or falsify activities, misleading investigators.
  - *Erasing Command History*: Delete command histories, especially in systems like Linux, where commands are logged.
