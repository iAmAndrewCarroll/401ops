Lab: Traffic Sniffing with Ettercap
===================================

Overview
--------

ARP poisoning can be used in tandem with traffic sniffing to create a man-in-the-middle (MITM) attack on a targeted network.

Today, you will perform a man-in-the-middle (MITM) attack using Ettercap and also get some additional practice with Wireshark.

Objectives
----------

* Perform offensive network traffic capture using Ettercap
* Decrypt HTTPS packets using Wireshark
* Perform ARP spoofing with the Ettercap command line

Resources
---------

* [Ettercap Linux Man Page](https://www.google.com/url?q=https://linux.die.net/man/8/ettercap&sa=D&source=editors&ust=1710195772649422&usg=AOvVaw1Tp1H8tbpz-_sL-5nAO5Bg)
* [MITM/Wired/ARP Poisoning with Ettercap](https://www.google.com/url?q=https://charlesreid1.com/wiki/Man_in_the_Middle/Wired/ARP_Poisoning_with_Ettercap&sa=D&source=editors&ust=1710195772649650&usg=AOvVaw060lL8zrvXqrXDXadwxr_I)
* [Pentest Tips: ARP Spoofing](https://www.google.com/url?q=https://pentestfreak.blogspot.com/2013/05/redirect-someone-to-different-website.html&sa=D&source=editors&ust=1710195772649826&usg=AOvVaw2GFFK5U6XGkKeYXP52Wv3V)
* Fellow students completed labs (Juan Cano, Wil Baur, etc.)

Tasks
-----

### Part 1: Staging

Deploy two VMs to a NAT Network:

* One Kali VM
* class-42-target2-win7.ova

Feel free to use a different target VM if you prefer, instead of class-42-target2-win7.ova.

Confirm Ettercap is installed and operational on your Kali machine using the ettercap --version command on a terminal window. If Ettercap is installed, the command will display the version information. You will see output similar to: Ettercap v0.8.3 (IPv6) …

![](media/lab43-1.png)![](media/lab43-2.png)

![](media/lab43-3.png)

![](media/lab43-4.png)

![](media/lab43-5.png)

![](media/lab43-6.png)

![](media/lab43-7.png)

![](media/lab43-8.png)

![](media/lab43-9.png)![](media/lab43-10.png)![](media/lab43-11.png)

When I clicked on the check mark, the Ettercap disappeared.

* Download [PCAP and log key](https://www.google.com/url?q=https://github.com/pan-unit42/wireshark-tutorial-decrypting-HTTPS-traffic&sa=D&source=editors&ust=1710195772651392&usg=AOvVaw0dPtg7kgEuDffmcPboEP_n) that will be used in Part 3 to your Kali box.
* Skip this till Part 3.

![](media/lab43-12.png)

### Part 2: MITM and ARP Cache Poisoning with Ettercap GUI

First, let’s practice some basics by having Ettercap capture network traffic transmitted between class-42-target2-win7.ova and the internet. To do this, we’ll need to perform a simple ARP poisoning attack and then analyze the sniffed packets with Wireshark.

* Set packets to automatically forward from Kali Linux’s eth0 interface using the terminal command sysctl -w net.ipv4.ip\_forward=1.
* In Kali, launch Ettercap and select a sniffing mode.

![](media/lab43-13.png)

![](media/lab43-14.png)![](media/lab43-15.png)![](media/lab43-16.png)![](media/lab43-17.png)![](media/lab43-18.png)![](media/lab43-19.png)![](media/lab43-20.png)![](media/lab43-21.png)

I already had ettercap open, so when I ran the ‘ettercap -G’ command, a second one appeared so I erased the new one.

![](media/lab43-22.png)

* Designate your targets.

![](media/lab43-23.png)![](media/lab43-24.png)![](media/lab43-25.png)![](media/lab43-26.png)

* On Windows PC, grab a screenshot of the ARP cache.

![](media/lab43-27.png)

* Perform an ARP poisoning attack to grant Ettercap access to a Windows PC.

![](media/lab43-28.png)![](media/lab43-29.png)![](media/lab43-30.png)

* On a Windows PC, grab a screenshot of the poisoned ARP cache. How can you tell it’s poisoned?

![](media/lab43-31.png)

* Initialize live sniffing in Ettercap, then launch Wireshark. Have Wireshark perform live packet capture on the sniffer interface.

Below is how you stop sniffing:

![](media/lab43-32.png)

Below is how you start sniffing:

![](media/lab43-33.png)

![](media/lab43-34.png)![](media/lab43-35.png)![](media/lab43-36.png)

* Perform a ping from the Windows PC to any valid destination IP or URL. If you have successfully performed an MITM attack, you’ll see these ping packets.

![](media/lab43-37.png)

* Have Wireshark filter down the view to only ICMP packets. Take a screenshot of this successful outcome.

![](media/lab43-38.png)

![](media/lab43-39.png)

* On the Windows PC, navigate a web browser to [http://www.wikidot.com](https://www.google.com/url?q=http://www.wikidot.com/&sa=D&source=editors&ust=1710195772653933&usg=AOvVaw0CRvqAddQO9w5rwhWWckiy), then navigate to the “Pricing” link at the top.

![](media/lab43-40.png)![](media/lab43-41.png)![](media/lab43-42.png)![](media/lab43-43.png)![](media/lab43-44.png)

* Have Wireshark filter down the view to only HTTP packets. Take a screenshot of the HTTP GET request for the Pricing page.

Look for plans located at the end of the http in the browser.

![](media/lab43-45.png)![](media/lab43-46.png)![](media/lab43-47.png)![](media/lab43-48.png)

![](media/lab43-49.png)

* Save a PCAP of the captured data to your desktop > Class 43 folder and take a screenshot of the PCAP.

![](media/lab43-50.png)![](media/lab43-51.png)![](media/lab43-52.png)![](media/lab43-53.png)

Nice work! You’ve now achieved foundational proficiency with offensive network traffic capture using Ettercap. That’s some useful network traffic you’ve captured, but what about encrypted HTTPS traffic?

### Part 3: Decrypting HTTPS with Wireshark

Let’s get some more Wireshark practice; in this part of the lab, we’re going to figure out how to deal with pesky encryption protocols like HTTPS that are getting between us and the precious data we’re wanting to capture. Access the [Wireshark Tutorial: Decrypting HTTPS Traffic](https://www.google.com/url?q=https://unit42.paloaltonetworks.com/wireshark-tutorial-decrypting-https-traffic/&sa=D&source=editors&ust=1710195772655467&usg=AOvVaw18ZD5IQM65BW6aevxi-EUT).

* If you have not done so in staging, download the [PCAP and log key used in this exercise](https://www.google.com/url?q=https://github.com/pan-unit42/wireshark-tutorial-decrypting-HTTPS-traffic&sa=D&source=editors&ust=1710195772655718&usg=AOvVaw0aUGXK9PtN6wfM9BZ9x4gl) to your Kali system.

![](media/lab43-54.png)![](media/lab43-55.png)![](media/lab43-56.png)![](media/lab43-57.png)![](media/lab43-58.png)![](media/lab43-59.png)![](media/lab43-60.png)![](media/lab43-61.png)![](media/lab43-62.png)![](media/lab43-63.png)![](media/lab43-64.png)

* Complete the tutorial. Document in your submission today your thoughts and screenshots of key milestones achieved during the tutorial.

![](media/lab43-65.png)![](media/lab43-66.png)![](media/lab43-67.png)![](media/lab43-68.png)![](media/lab43-69.png)![](media/lab43-70.png)![](media/lab43-71.png)![](media/lab43-72.png)![](media/lab43-73.png)

![](media/lab43-74.png)

Right-click on the purple bar.

![](media/lab43-75.png)

![](media/lab43-76.png)

2nd Attempt:

![](media/lab43-77.png)![](media/lab43-78.png)![](media/lab43-79.png)![](media/lab43-80.png)![](media/lab43-81.png)![](media/lab43-82.png)![](media/lab43-83.png)![](media/lab43-84.png)![](media/lab43-85.png)![](media/lab43-86.png)![](media/lab43-87.png)![](media/lab43-88.png)![](media/lab43-89.png)![](media/lab43-90.png)![](media/lab43-91.png)![](media/lab43-92.png)![](media/lab43-93.png)![](media/lab43-94.png)![](media/lab43-95.png)

Nice work! It looks like there’s quite a few approaches we can take to decrypting SSL traffic. Next, let’s take a look at some other capabilities of Ettercap.

### Part 4: ARP Spoofing with Ettercap Command Line

Now that you’re familiar with the Ettercap GUI let’s delve into a more advanced operation: ARP spoofing. Let’s redirect the Windows PC to a different website every time it tries to access apache.org.

* For this part of the lab, use all resources at your disposal to determine how this attack is performed with Ettercap.
* For the website, you redirect the Windows user to, try setting up a quick Apache web server on Kali. Alternatively, redirect it to an entirely different website on the internet.
* When the successful outcome is achieved, capture a screenshot of Ettercap’s terminal performing the redirect, as well as a screen of the site you sent the unsuspecting user to.

![](media/lab43-96.png)![](media/lab43-97.png)![](media/lab43-98.png)![](media/lab43-99.png)![](media/lab43-100.png)![](media/lab43-101.png)![](media/lab43-102.png)![](media/lab43-103.png)

That’s some impressive work you did there! I wonder what a cybercriminal could use this for?

### Part 5: Reporting

Answer the discussion prompts below:

* What is ARP poisoning, and how does it work?
* ARP poisoning is a technique that misleads a network by associating an attacker’s MAC address with the IP address of another host, such as the default gateway. This allows the attacker to intercept data.
* How is ARP spoofing different from DNS poisoning?
* Arp spoofing tricks a local network into sending data to an attacker, while DNS poisoning misleads devices about the IP address associated with a domain name, affecting web traffic.
* Why might a penetration tester utilize Ettercap on a targeted subnet?
* A penetration tester might use Ettercap to assess the network’s vulnerability to man-in-the-middle attacks, disrupt network services, or redirect traffic to fraudulent or malicious sites.
* For what purposes would a malicious attacker use these techniques?
* Attackers might use ARP spoofing and DNS poisoning to intercept and manipulate data, perform man-in-the-middle attacks, disrupt network services, or redirect traffic to fraudulent or malicious sites.



