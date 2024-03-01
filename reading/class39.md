# Reading 39: SQLi with Burp Suite, WebGoat

[Resource: Understanding SQL Injection, Identification & Prevention](https://www.varonis.com/blog/sql-injection-identification-and-prevention-part-1_)

**1. What is SQL injection?**
- SQL injection is a type of cyber attack where an attacker manipulates a web application's input fields to execute unauthorized SQL commands. By injecting malicious SQL code into these fields, attackers can gain unauthorized access to databases, manipulate data, and perform other malicious actions.

**2. Can you give an example of how a hacker could use SQL injection to gain unauthorized access?**
- Sure. Let's say there's a login form on a website where users enter their username and password. Normally, the website would authenticate the user by checking their credentials against a database. However, if the website is vulnerable to SQL injection, an attacker could input something like `' OR '1'='1'--` into the username or password field. This input alters the SQL query executed by the server to always return true, effectively bypassing the authentication process and granting the attacker unauthorized access to the system.

**3. What are some ways to prevent SQL injection attacks on a web server?**
- There are several methods to prevent SQL injection attacks:
  - Input validation: Validate and sanitize user inputs to ensure they meet expected formats and do not contain malicious code.
  - Parameterized queries: Use parameterized queries or prepared statements to separate SQL code from user input, preventing attackers from injecting malicious code.
  - Least privilege: Limit database user privileges to only necessary actions, reducing the impact of successful SQL injection attacks.
  - Web application firewalls (WAFs): Implement WAFs to filter and block malicious SQL injection attempts before they reach the web server.
  - Regular updates and patches: Keep software, frameworks, and libraries up to date to patch known vulnerabilities that could be exploited by attackers.
