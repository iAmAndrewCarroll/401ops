# The Pros & Cons of Intrusion Detection Systems

[Resource: The Pros & Cons of Intrusion Detection Systems](https://www.rapid7.com/blog/post/2017/01/11/the-pros-cons-of-intrusion-detection-systems/)

**1. List 2 differences between firewalls and an IDS:**
- **Function:** Firewalls primarily act as a barrier between a network and potential threats, controlling incoming and outgoing traffic based on predefined rules. In contrast, an Intrusion Detection System (IDS) identifies incidents and potential threats within the network, notifying administrators when suspicious activity is detected.
- **Blocking vs. Monitoring:** Firewalls have the capability to block or allow traffic based on rules, providing a proactive defense mechanism. IDS, on the other hand, only monitors and reports suspicious activity without actively blocking it.

**2. Under what circumstances would you choose a network-based IDS over a host-based IDS:**
- A network-based IDS (NIDS) is preferable when:
  - Quick Response is Needed: NIDS offers faster response times as it operates at the network level, making it suitable for detecting and reacting to threats in real-time.
  - Broader Network Monitoring: NIDS can monitor an entire network segment, regardless of the target host's operating system, without requiring software installation on individual hosts. This makes it more suitable for large-scale network monitoring.

**3. Name 3 major drawbacks of a NIDS:**
- 1. **Inability to Prevent Incidents:** NIDS can detect and report intrusions but does not have the capability to block or prevent attacks on its own.
- 2. **False Positives:** NIDS frequently generates false alarms, which can consume resources and require manual investigation. Responding to false positives effectively is crucial to avoid missing real threats.
- 3. **Susceptibility to Protocol-Based Attacks:** NIDS, like network hosts, can be vulnerable to attacks targeting protocol vulnerabilities or causing protocol analyzer bugs.
