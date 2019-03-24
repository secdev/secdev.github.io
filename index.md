---
title: Scapy
subtitle: Packet crafting for Python2 and Python3
date: 2019
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

<link rel="stylesheet" href="/css/button.css">
<link rel="stylesheet" href="/css/table.css">

Scapy Project
=============

Scapy runs natively on Linux, and on most Unixes with libpcap and its python wrappers (see [scapy's installation page](http://scapy.readthedocs.io/en/latest/installation.html)).
The same code base now runs natively on both Python 2 and Python 3.

{% raw %}
<div>
    <a href="/download" class="button button_main">
        DOWNLOAD SCAPY
    </a>
</div>
{% endraw %}

{: .box-note}
## [Get started with Scapy](https://scapy.readthedocs.io/en/latest/introduction.html)

### Related projects

*   [UTscapy](http://www.secdev.org/projects/UTscapy/): Unit Testing with scapy (shipped with Scapy 2.X+)
*   [Scapytain](http://www.secdev.org/projects/scapytain/): a web application to store, organize and run test campaigns on top of Scapy (low project activity)

### Other

An independent fork of Scapy was created from v2.2.0 in 2015, aimed at
supporting only Python3 (<a rel="nofollow"
href="https://github.com/phaethon/scapy">scapy3k</a>). The fork
diverged, did not follow evolutions and fixes, and has had its own
life without contributions back to Scapy. Unfortunately, it has been
packaged as python3-scapy in some distributions, and as scapy-python3
on PyPI leading to confusion amongst users. It should not be the case
anymore soon.  Scapy supports Python3 in addition to Python2 since
2.4.0. Scapy v2.4.0 should be favored as the official Scapy code
base. The fork has been renamed as kamene.

### Help, documentation


### Development

Scapy development uses [Git](https://git-scm.com/) version control system. Scapy reference repository is at [https://github.com/secdev/scapy/](https://github.com/secdev/scapy/).
It provides the ticket management service used for submitting patches or bugs.
You can [report a bug](https://github.com/secdev/scapy/issues) or [create a PR](https://github.com/secdev/scapy/pulls)

Head over to [Scapy's GitHub Projects](https://github.com/secdev/scapy/projects) to see what is being worked on.

#### Documents

*   [**Official Online HTML documentation**](http://scapy.readthedocs.io/)
*   [Scapy's installation page](http://scapy.readthedocs.io/en/latest/installation.html)
*   [ThePacketGeek's Building Network Tools with Scapy tutorial](https://thepacketgeek.com/series/building-network-tools-with-scapy/)
*   [Security Power Tools](http://www.oreilly.com/catalog/9780596009632/) where Philippe Biondi wrote a complete chapter about Scapy.
*   [Report bugs/wishes/patches here](https://github.com/secdev/scapy/issues/new)
*   [Active tickets here](https://github.com/secdev/scapy/issues)

#### Slides

*   [Scapy's PacSec/core05 slides](/conf/scapy_pacsec05.pdf) ([printable version](/conf/scapy_pacsec05.handout.pdf))
*   [Scapy's Hack.lu 2005 slides](/conf/scapy_hack.lu.pdf)
*   [Scapy's Summerschool Applied IT Security 2005 slides](/conf/scapy_Aachen.pdf)
*   [Scapy's T2'2005 slides](/conf/scapy_T2.pdf)
*   [Scapy's CanSecWest/core05 slides](/conf/scapy_csw05.pdf)
*   [Scapy's LSM 2003 slides](/conf/scapy_lsm2003.pdf)

#### Other documents about Scapy :

*   [(french) @p-l- blog posts on scapy](http://pierre.droids-corp.org/blog/html/tags/scapy.html)
*   You will also find an article in the French [Linux Magazine #52](http://www.linuxmag-france.org/produit.php?produit=107)

#### Mailing-list (very low activity)

Send questions, bug reports, suggestions, ideas, cool usages of Scapy, etc. To avoid spam, you must subscribe to the mailing list to post.

*   To subscribe to the mailing-list, send a mail to scapy.ml-subscribe(at)secdev.org
*   To send a mail to the mailing-list: scapy.ml(at)secdev.org

#### Known bugs

*   May miss packets under heavy load
*   BPF filters do not work on PPP interfaces

---

{% raw %}
<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
    If you like Scapy, you can
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----">
    <input style="vertical-align:middle; border:0" type="image" src="https://www.paypal.com/en_US/i/btn/btn_donate_LG.gif" name="submit" alt="PayPal - The safer, easier way to pay online!">
    <img alt="" style="border: 0" src="https://www.paypal.com/fr_FR/i/scr/pixel.gif" width="1" height="1">
</form>
{% endraw %}
