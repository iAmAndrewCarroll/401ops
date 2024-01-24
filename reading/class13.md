# Reading 13: What is a Reverse Proxy?

[Resource: What is a Reverse Proxy?](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)

**1. What are the benefits of a forward proxy?**
   - The benefits of a forward proxy include:
     - Avoiding state or institutional browsing restrictions, allowing users to access a broader internet.
     - Blocking access to specific content, useful for organizations restricting certain websites.
     - Enhancing online anonymity by masking users' IP addresses.

**2. Explain the differences between a forward and a reverse proxy?**
   - A forward proxy sits in front of client machines and routes their requests to websites or services, acting as an intermediary between clients and the internet.
   - A reverse proxy sits in front of one or more web servers and intercepts requests from clients, directing them to the appropriate server. It acts as a shield for origin servers.

**3. Explain to your manager why your organization might benefit from implementing a reverse proxy?**
   - Implementing a reverse proxy can offer several advantages for our organization:
     - Load balancing: It ensures even distribution of website traffic across multiple servers, preventing overloads and improving performance.
     - Protection from attacks: By hiding the IP addresses of our origin servers, it makes it harder for attackers to target them, enhancing security.
     - Global server load balancing (GSLB): It optimizes user experience by directing them to the nearest server, reducing load times.
     - Caching: It speeds up performance by storing and serving cached content.
     - SSL encryption: Offloading SSL encryption from origin servers conserves their resources.