---
title: Scapy
date: 2018
---

Scapy
=====

{% raw %}
<ul style="display:flex; list-style:none;">
    <!-- SVG files are text files: easy to update when needed -->
    <li style="display: inline; margin-left: 10px;">
        <a href="https://pypi.python.org/pypi/scapy/"><img src="/img/badges/scapyversion.svg" alt="Scapy" /></a>
    </li>
    <li style="display: inline; margin-left: 10px;">
        <a href="https://pypi.python.org/pypi/scapy/"><img src="/img/badges/pyversions.svg" alt="Scapy versions" /></a>
    </li>
    <li style="display: inline; margin-left: 10px;">
        <a href="https://github.com/secdev/scapy/blob/master/LICENSE"><img src="/img/badges/gplv2.svg" alt="GPLv2" /></a>
    </li>
    <li style="display: inline; margin-left: 10px;">
        <a href="https://gitter.im/secdev/scapy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge"><img src="/img/badges/gitter.svg" alt="Join the chat at https://gitter.im/secdev/scapy" /></a>
    </li>
</ul>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
    If you like what I do, you can
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----">
    <input style="vertical-align:middle; border:0" type="image" src="https://www.paypal.com/en_US/i/btn/btn_donate_LG.gif" name="submit" alt="PayPal - The safer, easier way to pay online!">
    <img alt="" style="border: 0" src="https://www.paypal.com/fr_FR/i/scr/pixel.gif" width="1" height="1">
</form>
{% endraw %}
    

About Scapy
-----------

### What is Scapy

Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more. It can easily handle most classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery (it can replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump, tethereal, p0f, etc.). It also performs very well at a lot of other specific tasks that most other tools can't handle, like sending invalid frames, injecting your own 802.11 frames, combining technics (VLAN hopping+ARP cache poisoning, VOIP decoding on WEP encrypted channel, ...), etc. See [interactive tutorial](http://scapy.readthedocs.io/en/latest/#interactive-tutorial) and [the quick demo: an interactive session (some examples may be outdated)](/demo/).

### What makes scapy different from most other networking tools

First, with most other tools, you won't build something the author did not imagine. These tools have been built for a specific goal and can't deviate much from it. For example, an ARP cache poisoning program won't let you use double 802.1q encapsulation. Or try to find a program that can send, say, an ICMP packet with padding (I said padding, not payload, see?). In fact, each time you have a new need, you have to build a new tool.

Second, they usually confuse decoding and interpreting. Machines are good at decoding and can help human beings with that. Interpretation is reserved for human beings. Some programs try to mimic this behavior. For instance, they say "this port is open" instead of "I received a SYN-ACK". Sometimes they are right. Sometimes not. It's easier for beginners, but when you know what you're doing, you keep on trying to deduce what really happened from the program's interpretation to make your own, which is hard because you lost a big amount of information. And you often end up using tcpdump -xX to decode and interpret what the tool missed.

Third, even programs which only decode do not give you all the information they received. The network's vision they give you is the one their author thought was sufficient. But it is not complete, and you have a bias. For instance, do you know a tool that reports the padding?

Scapy tries to overcome those problems. It enables you to build exactly the packets you want. Even if I think stacking a 802.1q layer on top of TCP has no sense, it may have some for somebody else working on some product I don't know. Scapy has a flexible model that tries to avoid such arbitrary limits. You're free to put any value you want in any field you want and stack them like you want. You're an adult after all.

In fact, it's like building a new tool each time, but instead of dealing with a hundred line C program, you only write 2 lines of Scapy.

After a probe (scan, traceroute, etc.) Scapy always gives you the full decoded packets from the probe, before any interpretation. That means that you can probe once and interpret many times, ask for a traceroute and look at the padding for instance.

Scapy Project
-------------

Scapy runs natively on Linux, and on most Unixes with libpcap, libdnet and their respective python wrapper (see [scapy's installation page](http://scapy.readthedocs.io/en/latest/installation.html)).
The same code base now runs natively on both Python 2 and Python 3.

* Scapy ≥ 2.4.x needs Python2 ≥ 2.7, or Python3 ≥ 3.4.
* Scapy ≥ 2.x needs Python2 ≥ 2.7.
* Scapy 1.x needs Python2 ≥ 2.5.  Scapy 1.x is now deprecated.

### Download

*   [Development repository](https://github.com/secdev/scapy/)
*   [Scapy 2.4.0](https://github.com/secdev/scapy/archive/v2.4.0.zip)
*   [PyPI](https://pypi.python.org/pypi/scapy/)

### Related projects

*   [Scapytain](http://www.secdev.org/projects/scapytain/): a web application to store, organize and run test campaigns on top of Scapy
*   [UTscapy](http://www.secdev.org/projects/UTscapy/): Unit Testing with scapy (integrated with Scapy 2.x)
*   [WifiTap](http://sid.rstack.org/index.php/Wifitap_EN): Wi-Fi traffic injection
*   [The local copy of Scapy OLSR add-on](files/scapy-olsr.py)

### Help, documentation

#### Mailing-list

Send questions, bug reports, suggestions, ideas, cool usages of Scapy, etc. To avoid spam, you must subscribe to the mailing list to post.

*   To subscribe to the mailing-list, send a mail to scapy.ml-subscribe(at)secdev.org
*   To send a mail to the mailing-list: scapy.ml(at)secdev.org

#### Documents

*   [**Official Online HTML documentation**](http://scapy.readthedocs.io/)
*   [Security Power Tools](http://www.oreilly.com/catalog/9780596009632/) where Philippe Biondi wrote a complete chapter about Scapy.
*   [Quick demo: an interactive session](/demo/)
*   [Building your own tools with Scapy](/build-your-own-tools/)
*   [Scapy's installation page](http://scapy.readthedocs.io/en/latest/installation.html)
*   You will also find an article in the French [Linux Magazine #52](http://www.linuxmag-france.org/produit.php?produit=107)
*   [Report bugs/wishes/patches here](https://github.com/secdev/scapy/issues/new)
*   [Active tickets here](https://github.com/secdev/scapy/issues)

#### Slides

*   [Scapy's PacSec/core05 slides](/conf/scapy_pacsec05.pdf) ([printable version](/conf/scapy_pacsec05.handout.pdf))
*   [Scapy's Hack.lu 2005 slides](/conf/scapy_hack.lu.pdf)
*   [Scapy's Summerschool Applied IT Security 2005 slides](/conf/scapy_Aachen.pdf)
*   [Scapy's T2'2005 slides](/conf/scapy_T2.pdf)
*   [Scapy's CanSecWest/core05 slides](/conf/scapy_csw05.pdf)
*   [Scapy's LSM 2003 slides](/conf/scapy_lsm2003.pdf)

#### Other documents on Scapy :

*   A Scapy tutorial: [Packet Wizardry: Ruling the Network with Python](http://packetstorm.linuxsecurity.com/papers/general/blackmagic.txt) by Rob klein Gunnewiek.
*   [(now outdated) Scapy installation on OpenBSD 3.8 howto](http://pierre.droids-corp.org/scapy/README.openbsd)

### Development

Scapy development uses [Git](https://git-scm.com/) version control system. Scapy reference repository is at [https://github.com/secdev/scapy/](https://github.com/secdev/scapy/). It provides a ticket management service that I use to avoid forgetting patches or bugs.

#### Ongoing developments

*   IPv6
*   Session management
*   Bluetooth
*   ...

#### Known bugs

*   Link layer not well managed yet
*   DNS packets not reassembled exactly as the original (no compression used)
*   May miss packets under heavy load
*   BPF filters do not work on PPP interfaces