# Read 16: Anatomy of a Cloud Breach

[Resource: ZScaler.com: Lessons Learned from the Capital One Data Breach](https://www.zscaler.com/resources/white-papers/capital-one-data-breach.pdf)

**1. What were the three commands used for the attack?**
- `http://169.254.169.254/iam/security-credentials command`
- `http://169.254.169.254/iam/security-credentials/*****-WAF-Role`
- `aws s3 ls`
- `aws s3 sync s3://somebucket`

**2. What misconfiguration of AWS components allowed the attacker to access sensitive data?**
The misconfiguration involved a Web Application Firewall (WAF) in AWS that was vulnerable to a server-side request forgery (SSRF) attack. This vulnerability allowed the attacker to execute commands to access AWS metadata services and retrieve sensitive data from AWS S3 buckets.

**3. What are two of the AWS Governance practices that could have prevented such attack?**
1. **Implementation of the Principle of Least Privilege**: This involves configuring IAM roles and policies to provide minimal necessary access, which would have limited the scope of accessible data after the SSRF vulnerability was exploited.
   
2. **Regular Security Audits and Remediation**: Conducting continuous monitoring and audits for security misconfigurations and non-compliance with AWS best practices could have identified and rectified the SSRF vulnerability in the WAF.
