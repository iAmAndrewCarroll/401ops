# Reading 36: Cross Site Scripting with w3af, DVWA

**1. Explain how a cross-site scripting attack works in non-technical terms.**
- Cross-site scripting (XSS) is like leaving a hidden message on a public notice board. Imagine someone slips a note into a community bulletin board, and everyone who reads it unknowingly follows the instructions written on it. In the digital world, XSS works similarly. Hackers inject malicious code into a website, and when users visit that site, their browsers execute the code, allowing the hacker to hijack their sessions, steal their information, or perform actions on their behalf.

**2. What are the three types of XSS attacks?**
- Reflected XSS: The malicious script comes from the current HTTP request.
- Stored XSS: The malicious script comes from the website's database.
- DOM-based XSS: The vulnerability exists in client-side code rather than server-side code.

**3. If an attacker successfully exploits a XSS vulnerability, what malicious actions would they be able to perform?**
- An attacker who exploits an XSS vulnerability can:
  - Impersonate or masquerade as the victim user.
  - Carry out any action that the user is able to perform.
  - Read any data that the user is able to access.
  - Capture the user's login credentials.
  - Perform virtual defacement of the web site.
  - Inject trojan functionality into the web site.

**4. What are some security controls that can be implemented to prevent XSS attacks?**
- Filter input on arrival to remove or encode characters that could potentially be used in XSS attacks.
- Encode data on output to prevent it from being interpreted as active content.
- Use appropriate response headers such as Content-Type and X-Content-Type-Options to control how browsers interpret responses.
- Implement Content Security Policy (CSP) to reduce the severity of XSS vulnerabilities and mitigate their impact.
