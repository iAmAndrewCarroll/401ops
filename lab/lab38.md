# Lab: Attacking Juice Shop with Burp Suite

## Overview
Burp Suite is a popular security tool in the web application security space. Complete with a GUI and a paid Professional edition, Burp Suite is often the web security professional’s tool of choice.

Today you’ll use Burp Suite Community Edition to probe a vulnerable web app, the OWASP Juice Shop.

**Objectives:**
- Download the Seclists word lists
- Complete the lab at [TryHackMe OWASP Juice Shop Room](https://tryhackme.com/room/owaspjuiceshop)
- Do not complete Part 2 Task 7, Persistent XSS and Reflected XSS
- Answer the reporting prompts

**Resources:**
- [Portswigger: Getting Started with Burp Suite Pro/Community](https://portswigger.net/burp/documentation/desktop/getting-started)
- [OWASP Juice Shop Project Page](https://owasp.org/www-project-juice-shop/)
- [TryHackMe OWASP Juice Shop Room](https://tryhackme.com/room/owaspjuiceshop)
- [the latest OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [TryHackMe Web Fundamentals room](https://tryhackme.com/room/webfundamentals)
- [Daniel Miessler’s SecLists GitHub repo](https://github.com/danielmiessler/SecLists)
- [Juan Miguel Cano's Lab 38](https://docs.google.com/document/d/1fh4YJhrGxJsTnfaYsXo7cRwxiGWHptlnNsdRJ8aNuko/edit#heading=h.kcpbyn7nzuwg)

## Tasks

### Part 1: Staging
This lab requires Web Security Dojo VM.

1. Juice Shop is manually launched via shell script from the start menu (top left, round blue and white icon)> targets section.
2. Access the Juice Shop page to verify it is up.
3. Install Git with `sudo apt update` then `sudo apt install git`.
4. Git clone [SecLists](https://github.com/danielmiessler/SecLists) to your Web Security Dojo.
5. If you reboot Web Security Dojo, you’ll need to re-launch Juice Shop manually.
**You must go through the steps to generate a new certificate and install it in your browser.  Once complete you can do part 2.  Juan Miguel has the pics in his lab.  I am so far behind I'm not going to try and get screenshots of the setup stuff.**

### Part 2: TryHackMe Burp Suite Lab
We’ll be revisiting TryHackMe’s site once again, this time in guiding us on how to use Burp Suite against OWASP Juice Shop.

Complete the lab at [TryHackMe OWASP Juice Shop Room](https://tryhackme.com/room/owaspjuiceshop). Respond to any questions/prompts here in your submission instead of on the TryHackMe page.

1. **Task 1: Open for business!**
    - Nothing to do here but to review the primer and move forward into Task 2.

2. **Task 2: Let’s go on an adventure!**
    - What is the administrator’s email address? 
      - **admin@juice-sh.op**
      - ![admin email](lab38-1.png)
    - What parameter is used for searching?
      - **q**
      - ![search parameter](lab38-2.png)
    - What show does Jim reference in his review?
      - **Star Trek**
      - ![Jim's review](lab38-3.png)

**At this point I have been trying to do this lab for like a week and every time I do it breaks.  The VM freezes.  The systems fail.  I'm going to stop here and submit what I have.  I've gone through the lecture videos and tried redownloading the VM and still it just crashes.  I've deleted a bunch off the lab machine to see if it was a storage space issue but I'm done.  This is ridiculous.**

3. **Task 3: Inject the juice**
    - How did you log into Bender’s account?
    - How did you log into the administrator’s account?
4. **Task 4: Who broke my lock?!**
    - Brute force the administrator’s password. How did you do it?
    - Reset the password. How did you do it?
5. **Task 5: AH! Don’t look!**
    - Access the confidential document. How did you do it?
    - Log into MC SafeSearch’s account. How did you do it?
    - Download package.json.bak. How did you get past the error?
6. **Task 6: Who’s flying this thing?**
    - Access the administration page. How did you do it?
    - View another user’s shopping basket. How did you do it?
    - Remove all 5-star reviews. How did you accomplish this?
7. **Task 7: Where did that come from?**
    - This task does not need to be completed, no action required.
8. **Task 8: Exploration!**
    - View the scoreboard page, no action required.

### Part 3: Reporting
Define the below terms in your own words:

- **Injection**
- **Broken authentication**
- **Sensitive data exposure**
- **Broken access control**
- **XSS**

### Stretch Goals (Optional Objectives)
- There are 100 Juice Shop challenges that await you. How many can you complete?
- First, discover the carefully hidden ‘Score Board’ page.
- There seems to be no link that leads you there! What techniques have you learned this module that would help you find something that’s not readily available on a web app?
- Reference Björn Kimminich’s book/website, [Pwning OWASP Juice Shop](https://pwning.owasp-juice.shop/), as a “hacking guide” to help you clear more challenges.
