---
title: Scapy
subtitle: Packet crafting for Python2 and Python3
---

{% raw %}
<ul style="display:flex; list-style:none; display: table; margin: 0 auto;">
    <!-- We rely on different services to provide the .svg dynamically -->
    <li style="display: inline; margin-left: 5px;">
        <a href="https://pypi.python.org/pypi/scapy/"><img src="https://img.shields.io/pypi/v/scapy.svg" alt="Scapy" /></a>
    </li>
    <li style="display: inline; margin-left: 5px;">
        <a href="https://pypi.python.org/pypi/scapy/"><img src="https://img.shields.io/pypi/pyversions/scapy.svg" alt="Scapy versions" /></a>
    </li>
    <li style="display: inline; margin-left: 5px;">
        <a href="https://github.com/secdev/scapy/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-GPL%20v2-blue.svg" alt="GPLv2" /></a>
    </li>
    <li style="display: inline; margin-left: 5px;">
        <a href="https://gitter.im/secdev/scapy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge"><img src="https://badges.gitter.im/secdev/scapy.svg" alt="Join the chat at https://gitter.im/secdev/scapy" /></a>
    </li>
    <li style="display: inline; margin-left: 5px;">
        <a href="https://repology.org/metapackage/scapy/versions"><img src="https://repology.org/badge/tiny-repos/scapy.svg" alt="Packaging status" /></a>
    </li>
</ul>
{% endraw %}

Scapy Project
=============

### What is Scapy?

Scapy is a powerful interactive packet manipulation program. It is able to
forge or decode packets of a wide number of protocols, send them on the wire,
capture them, match requests and replies, and much more. It can easily handle
most classical tasks like scanning, tracerouting, probing, unit tests, attacks
or network discovery (it can replace hping, 85% of nmap, arpspoof, arp-sk,
arping, tcpdump, tethereal, p0f, etc.). It also performs very well at a lot of
other specific tasks that most other tools can't handle, like sending invalid
frames, injecting your own 802.11 frames, combining technics (VLAN hopping+ARP
cache poisoning, VOIP decoding on WEP encrypted channel, ...), etc.

Scapy runs natively on Linux, Windows, OSX and on most Unixes with libpcap (see [scapy's installation page](http://scapy.readthedocs.io/en/latest/installation.html)).
The same code base now runs natively on both Python 2 and Python 3.

{% raw %}
<div class="d-flex justify-content-center">
    <a href="./download" class="btn btn-primary btn-lg mr-2">
        Download Scapy
    </a>
    <a href="https://scapy.readthedocs.io/en/latest/introduction.html" class="btn btn-primary btn-lg">
        Get started with Scapy
    </a>
</div>
{% endraw %}

### Shell demo

```python
$ sudo ./run_scapy -H
Welcome to Scapy (2.4.4.dev221)
>>> p = IP(dst="github.com")/ICMP()
>>> p
<IP  frag=0 proto=icmp dst=Net('github.com') |<ICMP  |>>
>>> r = sr1(p)
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
>>> r
<IP  version=4 ihl=5 tos=0x0 len=28 id=59762 flags= frag=0 ttl=57 proto=icmp
chksum=0x7792 src=140.82.121.4 dst=217.25.178.5 |<ICMP  type=echo-reply
code=0 chksum=0xffff id=0x0 seq=0x0 |>>
```


## Help, documentation


#### Documents

*   [**Official Online HTML documentation**](http://scapy.readthedocs.io/)
*   [Scapy's installation page](http://scapy.readthedocs.io/en/latest/installation.html)
*   [ThePacketGeek's Building Network Tools with Scapy tutorial](https://thepacketgeek.com/series/building-network-tools-with-scapy/)
*   [Security Power Tools](http://www.oreilly.com/catalog/9780596009632/) where Philippe Biondi wrote a complete chapter about Scapy.

#### Development

Scapy development uses [Git](https://git-scm.com/) version control system. Scapy reference repository is hosted on [GitHub secdev/scapy](https://github.com/secdev/scapy/).

It provides the ticket management service used for submitting patches or bugs.

*   [Submit patches](https://github.com/secdev/scapy/pulls/new)
*   [Report bugs/wishes here](https://github.com/secdev/scapy/issues/new)
*   [Active tickets here](https://github.com/secdev/scapy/issues)
*   Head over to [Scapy's GitHub Projects](https://github.com/secdev/scapy/projects) to see what is being worked on.

#### Slides

*   [Automotive Penetration Testing with Scapy - Troopers 2019 slides](/conf/troopers2019/index.html)
*   [Scapy's PacSec/core05 slides](/conf/scapy_pacsec05.pdf) ([printable version](/conf/scapy_pacsec05.handout.pdf))
*   [Scapy's Hack.lu 2005 slides](/conf/scapy_hack.lu.pdf)
*   [Scapy's Summerschool Applied IT Security 2005 slides](/conf/scapy_Aachen.pdf)
*   [Scapy's T2'2005 slides](/conf/scapy_T2.pdf)
*   [Scapy's CanSecWest/core05 slides](/conf/scapy_csw05.pdf)
*   [Scapy's LSM 2003 slides](/conf/scapy_lsm2003.pdf)

#### Other documents about Scapy :

*   [(french) @p-l- blog posts on scapy](http://pierre.droids-corp.org/blog/html/tags/scapy.html)
*   You will also find an article in the French [Linux Magazine #52](https://boutique.ed-diamond.com/numeros-deja-parus/354-misc52.html)

#### Mailing-list (very low activity)

Send questions, bug reports, suggestions, ideas, cool usages of Scapy, etc. To avoid spam, you must subscribe to the mailing list to post.

*   To subscribe to the mailing-list, send a mail to scapy.ml-subscribe(at)secdev.org
*   To send a mail to the mailing-list: scapy.ml(at)secdev.org

#### Known bugs

*   May miss packets under heavy load
*   BPF filters do not work on PPP interfaces

### Related projects

*   [UTscapy](http://www.secdev.org/projects/UTscapy/): Unit Testing with scapy (shipped with Scapy 2.X+)
*   [Scapytain](http://www.secdev.org/projects/scapytain/): a web application to store, organize and run test campaigns on top of Scapy (low project activity)

---

If you like Scapy, you can [sponsor us on Github](https://github.com/secdev/scapy#sponsor-button-repo)
