# Lab 2

| Service Category | AWS | Azure | GCP |
|---|---|---|---|
| Security |
| - Security Management | SOC 2 Type 2, [AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) | SOC 2 Type 2, [Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager) | SOC 2 Type 2, [GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2) |
| - Data Security | SOC 2 Type 2, [AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) | SOC 2 Type 2, [Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager) | SOC 2 Type 2, [GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2) |
| - Privacy | SOC 2 Type 2, [AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) | SOC 2 Type 2, [Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager) | SOC 2 Type 2, [GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2) |
| Availability |
| - Service Availability | SOC 2 Type 2, [AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) | SOC 2 Type 2, [Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager) | SOC 2 Type 2, [GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2) |
| - Business Continuity | SOC 2 Type 2, AWS [Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) | SOC 2 Type 2, [Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager) | SOC 2 Type 2, [GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2) |
| Processing Integrity |
| - System and Data Integrity | SOC 2 Type 2, [AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) | SOC 2 Type 2, [Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager) | SOC 2 Type 2, [GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2) |
| - Change Management | SOC 2 Type 2, [AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) | SOC 2 Type 2, [Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager) | SOC 2 Type 2, [GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2) |

Notes:

This table summarizes the highest level of SOC 2 compliance available for each service category based on publicly available information. For specific services, Initrobe may need to confirm the available reports and compliance details relevant to their needs.
Additional compliance certifications and service-specific security features should be considered during vendor selection.
Sources:

**Recommendation:**
- [AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html) 
  - See above table for SOC 2 Compliance details.
  - Initrobe will be able to store HR (PII) data on this platform as it is SOC 2 compliant.  AWS

References:
[AWS Artifact Portal](https://docs.aws.amazon.com/audit-manager/latest/userguide/SOC2.html)
[Azure Trust Center](https://learn.microsoft.com/en-us/purview/compliance-manager)
[GCP Compliance Resource Center](https://cloud.google.com/security/compliance/soc-2)

Initrobe can securely store HR (PII) data on AWS, including through the AWS Artifact Portal.

# Can Initrobe Securely Store HR (PII) Data on AWS?

Yes, Initrobe can securely store HR (PII) data on AWS, including through the AWS Artifact Portal.

## Key Points:

### Compliance and Certifications:
- SOC 2 Type 2 compliance for relevant services
- Adheres to GDPR, CCPA, HIPAA, PCI DSS, and more

### Security Controls:
- Robust encryption (at rest and in transit)
- Fine-grained access controls (IAM)
- Data loss prevention tools
- Comprehensive logging and monitoring

### Shared Responsibility Model:
- AWS secures infrastructure
- Initrobe configures security controls for their data

### AWS Artifact Portal:
- Access compliance reports and certifications
- PII-specific documentation

**Storing Financial (SOX) Data on AWS**
| Aspect               | Explanation                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------|
| **AWS Compliance**   | AWS offers services and features to help meet SOX compliance. Compliance is shared responsibility. |
| **Security Controls**| AWS provides encryption, access controls, and logging for data protection.                         |
| **Data Classification**| Initrobe must classify financial data appropriately to apply SOX controls.                        |
| **Audit Trails**     | AWS provides logging and monitoring capabilities for auditing compliance.                          |
| **Shared Responsibility**| AWS secures infrastructure, Initrobe configures data security.                                     |
| **Compliance Documentation**| AWS provides compliance reports and certifications.                                      |
| **Consultation**     | Initrobe may consult AWS experts or third-party auditors for SOX compliance.                      |


## Conclusion:
AWS provides a secure and compliant platform, but Initrobe must:
- Understand their security responsibilities
- Configure controls appropriately
- Adhere to applicable regulations

# Here is the Cloud Security Policy:

## Initrobe Cloud Security Policy

## 1. Purpose

This Cloud Security Policy establishes a framework to ensure the confidentiality, integrity, and availability of Initrobe's information assets hosted in cloud environments. It aligns with SOC 2 compliance requirements and reinforces Initrobe's commitment to secure cloud adoption.

## 2. Scope

This policy applies to all employees, contractors, and third-party vendors who access, process, or store Initrobe's information assets within cloud environments. It encompasses all cloud services used by Initrobe, regardless of provider.

### 2.1 Information Types

This policy covers the following information types:

- Confidential business information
- Personal identifiable information (PII)
- Financial data
- Intellectual property
- Other sensitive or regulated data

## 3. Ownership and Responsibilities

**Chief Technology Officer (CTO):**
- Overall responsibility for cloud security strategy and policy enforcement
- Approval of cloud service providers and usage
- Oversight of security incident response

**IT Security Team:**
- Implementation and maintenance of security controls
- Regular risk assessments and vulnerability management
- Security awareness training and education
- Security incident investigation and reporting

**All Employees:**
- Compliance with this policy and all security procedures
- Reporting of suspected security incidents

## 4. Secure Usage of Cloud Computing Services

### 4.1 Inventory
Maintain a comprehensive inventory of all cloud services in use, including:
- Provider name
- Service type
- Data stored or processed
- Access controls in place

### 4.2 Approved Services
Use only cloud services that have been approved by the CTO and meet Initrobe's security requirements.

### 4.3 Unauthorized Services
The use of unauthorized cloud services is prohibited.

## 5. Risk Assessment

Conduct regular risk assessments to identify and prioritize security risks associated with cloud services. Implement appropriate controls to mitigate risks to an acceptable level.

## 6. Security Controls

### 6.1 Technical Security Controls Requirements

- **Access Controls:**
    - Enforce least privilege access principles.
    - Implement role-based access control (RBAC).
    - Require multi-factor authentication for all cloud access.
    - Enforce strong password policies.
- **Data Security:**
    - Encrypt sensitive data at rest and in transit.
    - Implement data classification and labeling.
    - Use data loss prevention (DLP) tools.
- **Network Security:**
    - Configure firewalls and network segmentation.
    - Use intrusion detection and prevention systems (IDS/IPS).
    - Regularly scan for vulnerabilities and apply patches.
- **Vulnerability Management:**
    - Regularly scan cloud environments for vulnerabilities.
    - Promptly apply security patches and updates.
- **Logging and Monitoring:**
    - Implement comprehensive logging and monitoring of cloud activity.
    - Retain logs for a sufficient period for compliance and forensic purposes.

### 6.2 Mobile Security Requirements

- **Device Security:**
    - Enforce device encryption and password protection.
    - Implement remote wipe capabilities for lost or stolen devices.
- **Application Security:**
    - Restrict app installation from trusted sources.
    - Regularly update mobile apps.

### 6.3 Physical Security Requirements

- **Secure Data Centers:**
    - Ensure physical security of cloud provider data centers.
    - Address environmental controls (e.g., fire suppression, power backup).

### 6.4 Security Controls Assurance

- Regularly review and update security controls.
- Conduct penetration testing and vulnerability assessments.
- Obtain independent security certifications for cloud providers (e.g., SOC 2).

## 7. Security Incident Recovery

- Establish a formal incident response plan to address security breaches.
- Define roles and responsibilities for incident response.
- Communicate incidents to affected parties promptly.
- Conduct post-incident analysis and implement corrective actions.

## 8. Awareness-Raising

- Provide regular cloud security awareness training to employees.
- Educate employees on common threats and best practices.
- Emphasize the importance of reporting security incidents.

## 9. Enforcement

- Violations of this policy may result in disciplinary action, up to and including termination of employment.
- Regularly review and update this policy to reflect changes in cloud technologies and security threats.

## 10. Related Documents

- Initrobe Data Classification Policy
- Initrobe Information Security Policy
- Cloud Service Provider Security Assessment Questionnaire

## 11. Revision History

| Date | Revision | Description |
