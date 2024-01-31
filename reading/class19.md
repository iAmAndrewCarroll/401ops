# Reading 19: Cloud Detective Controls

[Resource: What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

**1. What are some of the IoCs that GuardDuty can detect?**
- Amazon GuardDuty can detect a variety of Indicators of Compromise (IoCs), including:
  - Unusual API activity: Such as a sudden spike in AWS resource creation or unusual API calls.
  - Anomalous behavior: Abnormal patterns in AWS account access, like new instances in unused regions or unusual login events.
  - Exposed credentials: Detection of exposed AWS access keys or secret access keys.
  - Malicious IP addresses and domains: GuardDuty maintains threat intelligence feeds to identify connections to known malicious IPs and domains.
  - Cryptojacking: Detection of instances involved in cryptocurrency mining.
  - Port scanning and probing: Identification of suspicious network activity like port scanning.

**2. What are some of the data sources which GuardDuty can use?**
- Amazon GuardDuty can analyze and process various data sources to detect potential threats. These include:
  - AWS CloudTrail management events.
  - AWS CloudTrail event logs.
  - VPC flow logs from Amazon EC2 instances.
  - DNS logs.
  - Kubernetes audit logs.
  - RDS login activity.
  - S3 access logs.
  - EBS volumes.
  - Runtime monitoring.
  - Lambda network activity logs.

**3. How does GuardDuty use access behavior to spot potential malicious activity?**
- GuardDuty monitors AWS account access behavior to identify signs of compromise. It looks for unusual patterns and activities that might indicate malicious intent. Some examples include:
  - Unauthorized infrastructure deployments in regions not previously used.
  - Unusual API calls, such as changes to password policies to weaken password strength.
  - Escalation of privileges or use of exposed credentials.
  - Communication with malicious IP addresses or domains.
  - Presence of malware on Amazon EC2 instances and container workloads.
  - Detection of compromised instances serving malware or involved in cryptocurrency mining.


