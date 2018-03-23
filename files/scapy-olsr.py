#!/usr/bin/env python

#############################################################################
##                                                                         ##
## olsr.py --- OLSR protocol support for Scapy                             ##
##                                                                         ##
## Copyright (C) 2005  EADS/CRC security team <dcrstic.ccr(at)eads.net>    ##
##                     Arnaud Ebalard         <arnaud.ebalard@eads.net>    ##    
##                                                                         ##
## This program is free software; you can redistribute it and/or modify it ##
## under the terms of the GNU General Public License version 2 as          ##
## published by the Free Software Foundation; version 2.                   ##
##                                                                         ##
## This program is distributed in the hope that it will be useful, but     ##
## WITHOUT ANY WARRANTY; without even the implied warranty of              ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU       ##
## General Public License for more details.                                ##
##                                                                         ##
#############################################################################

#
# $Log: olsr.py,v $
# Revision 1.15  2006/02/08 13:22:52  ebalard
# Suppressed old comments.
#
# Revision 1.14  2006/02/08 13:14:51  ebalard
# Final Version. Evverything is up and running in v4/v6. Let's wait for bugs.
#
# Revision 1.13  2006/02/06 19:16:59  ebalard
# NetListField is now up and running, allowing user to pass hna list in
# many different ways.
#
# Revision 1.12  2006/02/06 15:41:35  ebalard
# _OLSROrigAddrField() is now ready.
#
# Revision 1.11  2006/02/03 15:19:29  ebalard
# In fact, _OLSROrigAddrField() is buggy due to _underlayer and Scapy
# internal games. bug correction is in progress.
#
# Revision 1.10  2006/02/03 12:14:41  ebalard
# _OLSROrigAddrField now supports v4 and v6 addresses depending on network
# protocols used. Simple tests performed. Require some more.
#
# Revision 1.9  2006/01/27 16:05:18  ebalard
# conf.olsr_IPv6available is now set if scapy6 has been loaded (else its
# value is 0).
#
# Revision 1.8  2006/01/27 15:11:16  ebalard
# Bug in _OLSRTimeField corrected.
# Added scapy6 loading if available (will be used for IPv6 version).
#
# Revision 1.7  2006/01/27 12:57:23  ebalard
# post_dissect() method is _now_ really ok.
#
# Revision 1.6  2006/01/27 10:04:00  ebalard
# Bug in do_dissect() corrected.
#
# Revision 1.5  2006/01/27 08:53:37  ebalard
# NetListField is now working fine.
#
# Revision 1.4  2006/01/26 18:41:29  ebalard
# Almost Everything is there. Need polish, debug, more tests and solving
# problems referenced in TODO marks.
#
# Revision 1.3  2006/01/25 18:30:51  ebalard
# Banner typo corrected.
#
# Revision 1.2  2006/01/25 18:29:14  ebalard
# All main classes are defined.
#
# Revision 1.1.1.1  2006/01/25 09:41:53  ebalard
# Creation of scapy-olsr repository.




# TODO List :
# - create overloaded_fields for classes that need them. For example
#   in order to set destination IP adresses (v4 and also v6)
# - Deal with the sequence number fields that should be incremented
#   automatically (sn, msgsn, ansn)
# - Everytime there is an originator address, we should use by default
#   the address provided by conf.iface. See if we can directly use
#   and IPSourceField.
# - Same for TC messages with addresses available on the system, other
#   than that of conf.iface ? 
# - See if 'anma' field in TC message needs a different default value to
#   basically include at least 1 IP
# - At the end of the file is an awful hack : we give UDP source port
#   a value different from 53 because Scapy would dissect such a packet
#   as DNS traffic. Let call that an unwanted feature of scapy ;-)
# - see with Phil to make this field available in Scapy. It has
#   disappeared somewhere in some version.
# - See "IPv6 for OLSR" to make it generic (v4/v6) and deal with v6
#   traffic if Scapy IPv6 extensions are available.

# Basic cases :
#
#  IP()/UDP()/OLSR()/OLSR_MID()
#  IP()/UDP()/OLSR()/OLSR_HELLO()/OLSR_HELLO_LinkMessage()/OLSR_HELLO_LinkMessage()/OLSR_HELLO_LinkMessage 
#  IP()/UDP()/OLSR()/OLSR_TC()
#  IP()/UDP()/OLSR()/OLSR_HNA()


import math

try:
    # Try to get IPv6 support
    from scapy6 import *
    conf.olsr_IPv6available=1
except:
    from scapy import *
    conf.olsr_IPv6available=0

# Emission interval constants : section 18.2 of RFC 3626
# Most of them are unused in Scapy, at the moment
conf.olsr_HELLO_INTERVAL=2
conf.olsr_REFRESH_INTERVAL=2
conf.olsr_TC_INTERVAL=5
conf.olsr_MID_INTERVAL=conf.olsr_TC_INTERVAL
conf.olsr_HNA_INTERVAL=conf.olsr_TC_INTERVAL

# Holding time constants : section 18.3 of RFC 3626
# Most of them are unused in Scapy, at the moment
conf.olsr_NEIGHB_HOLD_TIME=3*conf.olsr_REFRESH_INTERVAL
conf.olsr_TOP_HOLD_TIME=3*conf.olsr_TC_INTERVAL
conf.olsr_DUP_HOLD_TIME=30
conf.olsr_MID_HOLD_TIME=3*conf.olsr_MID_INTERVAL
conf.olsr_HNA_HOLD_TIME=3*conf.olsr_HNA_INTERVAL

# The proposed value of constant C in sect. 18.1 of RFC 3626 is 1/16
conf.olsr_C = 1.0/16

# Referenced in Section 18.4 of RFC 3626
olsr_types = { 1: "OLSR HELLO Message",
               2: "OLSR TC Message",
               3: "OLSR MID Message",
               4: "OLSR HNA Message"  }

# Provides a mapping between previous types and associated Scapy
# classes  
olsr_cls = { 1: "OLSR_HELLO",
             2: "OLSR_TC",
             3: "OLSR_MID",
             4: "OLSR_HNA" }

# Referenced in Section 18.5 of RFC 3626. Used by _OLSRLinkField
olsr_link_types = { 0: "UNSPEC_LINK",
                    1: "ASYM_LINK",
                    2: "SYM_LINK",
                    3: "LOST_LINK" }

# Referenced in Section 18.6 of RFC 3626. Used by _OLSRLinkField
olsr_neighbor_types = { 0: "NOT_NEIGH",
                        1: "SYM_NEIGH",
                        2: "MPR_NEIGH",
                        3: "Unknown (not defined by RFC 3626)" }

# Referenced in Section 18.7 of RFC 3626
olsr_link_hysteresis = { 0.8: "HYST_THRESHOLD_HIGH",
                         0.3: "HYST_THRESHOLD_LOW",
                         0.5: "HYST_SCALING" }

# Referenced in Section 18.8 of RFC 3626
olsr_willingness = { 0: "WILL_NEVER",
                     1: "WILL_LOW",
                     3: "WILL_DEFAULT",
                     6: "WILL_HIGH",
                     7: "WILL_ALWAYS"}


# This class provides OLSR Message classes (TC, MID, HNA, but not HELLO)
# with a guess_payload_class() method that performs early guessing of
# following message type and returns associated class that should be
# used for dissection. 
class _OLSRDefaultPayload(Packet):
    name = "Provides OLSR Message classes with default_payload_class() method"
    fields_desc = []
    def default_payload_class(self, p):
        # OLSR Message classes are at least 12 bytes long
        if len(p) >= 12:
            return globals().get(olsr_cls.get(ord(p[0]),"Raw"), "Raw")
        return Raw

# Main OLSR header, used to provide length and serial for specific
# stacked messages (HELLO, TC, MID and HNA)

class OLSR(_OLSRDefaultPayload):
    name = "OLSR Header"
    fields_desc = [ ShortField("len", None),
                    ShortField("sn", 0) ]
    def post_build(self, pkt):
        # Packet Length Computation
        if self.len is None:
            l = len(pkt)
            pkt = struct.pack("!H", l) + pkt[2:]
        return pkt


class IPListField(StrLenField):
    islist = 1

    def getfield(self, pkt, s):

        # grab announced length
        l = getattr(pkt, self.fld)  
        f = pkt.get_field(self.fld)
        if isinstance(f, FieldLenField):
            l += f.shift

        # Are we carried by IPv4 or IPv6 ? -> set self.af and self.addrlen
        under = pkt.underlayer
        while under is not None:
            if conf.olsr_IPv6available and isinstance(under, IPv6):
                self.af =socket.AF_INET6
                self.addrlen = 16
                break
            elif isinstance(under, IP):
                self.af = socket.AF_INET
                self.addrlen = 4
                break
            under = under.underlayer

        if under is None:
            warning("No IP or IPv6 underlayer to select OLSR carried")
            warning("address type. Using IPv6 as fallback.")            

        return s[l:], self.m2i(pkt,s[:l])

    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt,val)

    def any2i(self, pkt, x): 
        if type(x) is list:
            return map(lambda z,pkt=pkt:self.any2i_one(pkt,z), x)
        else:
            r = []
            r.append(self.any2i_one(pkt,x))
            return r

    def any2i_one(self, pkt, x):
        if x is None or x is "":
            return None

        if x.count(':') > 0: # IPv6
            self.af =socket.AF_INET6
            self.addrlen = 16
            return x
        else:                # IPv4
            self.af =socket.AF_INET
            self.addrlen = 4                
            return x

    
    def m2i(self, pkt, x):
        r = []
        l = self.addrlen # has been set by getfield (I hope so)
        while len(x) >= l:
            r.append(socket.inet_ntop(self.af, x[:l]))
            x = x[l:]
        return r

    def i2m(self, pkt, x):
        s = ""
        if len(x) > 0:
            for ip in x:
                s += socket.inet_pton(self.af, ip)
            return s
        return ""

    def i2repr(self, pkt, x):      
        s = []
	if x == None:
	    return "[]"
	for y in x:
	    s.append('%s' % y)
        return "[ %s ]" % (", ".join(s))

        
# This OLSR Time field is used for VTime and HTime (respectively in
# Message headers and Hello messages). Decription is provided in
# section 18.3 of RFC 3626. Defaut value of C is the one found in
# conf.olsr_C (default to 1/16).
#
# TODO : check if 'from scratch' formulas give same results as that
# provided in section 18.3 of RFC  3626
class _OLSRTimeField(ByteField):
    def m2i(self, pkt, x):
        a = ((int(x)>>4) & 0x0f)
        b = int(x) & 0x0f
        C = conf.olsr_C
        return C*(1+float(a)/16)*(2**b)
        
    def i2m(self, pkt, x):
        C = conf.olsr_C
        tmp = float(x)/C
        # base arg is available from python 2.3
        b = int(math.log(tmp, 2)) 
        a = int((float(tmp)/(2**b) - 1)*16)
        # TODO : perform some tests on computed value.
        return a*16+b 

    def i2repr(self, pkt, x):
        x=int(x)
        a = ((x>>4) & 0x0f)
        b = x & 0x0f
        C = conf.olsr_C
        return "%d sec (with C=%.4f, a is %d and b is %d)" % (x, C, a, b)



# Hack :to avoid errors in following class when IPv6 extensions are not
#       available. 
if not conf.olsr_IPv6available:
    class IP6Field: pass

# How do we know the AF for input parameters :
# - in getfield() : we access underlayer till we find an IP or IPv6 layer.
# - in h2i() : we try to find ':' in input parameter to see if it's an IPv6 @.
class _OLSROrigAddrField(IPField, IP6Field):

    # In getfield(), we will get AF based on kind of IP layer carrying 
    # the packet
    def getfield(self, pkt, s):
        under = pkt.underlayer
        while under is not None:
            if conf.olsr_IPv6available and isinstance(under, IPv6):
                self.sz = 16
                self.fmt = "16s"
                break
            elif isinstance(under, IP):
                self.sz = 4
                self.fmt = "4s"
                break
            under = under.underlayer

        if under is None:
            warning("No IP or IPv6 underlayer to select OLSR carried address type. Using IPv6 as fallback.")            

        return s[self.sz:], self.m2i(pkt,s[:self.sz])

    def addfield(self, pkt, s, val):
        return s+struct.pack(self.fmt, self.i2m(pkt,val))            

    # In h2i(), the only way to get AF is by parsing given address string
    # looking for ':'
    def h2i(self, pkt, x):
        if (conf.olsr_IPv6available and
            ((type(x) is str and  x.count(':') > 0)
             or (type(x) is list and len(x) > 0 and x[0].count(':') > 0))):
            self.fmt="16s"
            self.sz=16
            return IP6Field.h2i(self, pkt, x)
        else:
            self.fmt="4s"
            self.sz=4
            return IPField.h2i(self, pkt, x)

    def m2i(self, pkt, x):
        if conf.olsr_IPv6available and self.sz == 16:
            return IP6Field.m2i(self, pkt, x)
        else:
            return IPField.m2i(self, pkt, x)

    def i2m(self, pkt, x):
        # Deal with default value if user does not provide one
        if x is None:
            if conf.iface is not None:
                if conf.olsr_IPv6available:
                    warning("No address provided. IPv6 extensions being available, IPv6 global address")
                    warning("of %s interface will be used." % conf.iface)
                    x=get_if_addr6(conf.iface)
                    self.sz=16
                    self.fmt="16s"
                    if x is None:
                        warning("%s has no IPv6 address. Using :: as fallback." % conf.iface)
                        x="::"
                else:
                    warning("No address provided. IPv4 address of %s interface will be used." % conf.iface)
                    x=get_if_addr(conf.iface)
                    self.sz=4
                    self.fmt="4s"
                    if x is None:
                        warning("%s has no IPv4 address. Using 0.0.0.0 as fallback." % conf.iface)
                        x="0.0.0.0"

        # Call IPv4/v6 specific method
        if self.sz == 16: # implies conf.IPv6available
            return IP6Field.i2m(self, pkt, x)
        else:
            return IPField.i2m(self, pkt, x)

#### OLSR MID Message class : section 5.1 of RFC 3626
class OLSR_MID(_OLSRDefaultPayload, Packet):
    name = "OLSR MID Message"
    fields_desc = [ ByteEnumField("type", 3, olsr_types ),
                    _OLSRTimeField("vtime", conf.olsr_MID_HOLD_TIME ),
                    FieldLenField("msgsize", None , "interfaces", "!H", shift=-12),
                    _OLSROrigAddrField("oaddr", None),
                    ByteField("ttl", 255), # RFC 3626 sect 5.1
                    ByteField("hopcount", 0 ),
                    ShortField("msgsn", 0),
                    IPListField("interfaces", [], "msgsize") ]


# This class performs specific processing for "Link Code" fields found
# in Hello Link Messages. Described in section 6.1.1 of RFC 3626.
class _OLSRLinkField(ByteField):
    def any2i(self, pkt, x):
        return x

    def i2repr(self, pkt, x):
        # RFC 3626 only specifies processing of Link Codes < 16
        if x < 16:
            ntype= olsr_neighbor_types[(x & 0x0c)>>2]
            ltype= olsr_link_types[(x & 0x03)]
            res = "%d  (Neighbor type:%s, Link type:%s)" % (x, ntype, ltype)
        else:
            res = "%d  (not < 16, i.e. not RFC 3626 compliant)" % x
        return res

    #TODO : what about writing any2i ?

# This messages are intended to be stacked behind OLSR_HELLO messages
class OLSR_HELLO_LinkMessage(Packet):
    name = "OLSR HELLO - Link Message"
    fields_desc = [ _OLSRLinkField("linkcode", 0x06), # SYM_NEIGH and SYM_LINK
                    ByteField("res", 0),
                    FieldLenField("size", None, "neighint", "!H", shift=-4),
                    IPListField("neighint", [], "size") ]

    # TODO : find a better wayt to have same level of indentation for
    #        link message packet
    def show(self, indent=3, lvl=0):
        ct = conf.color_theme
        print "%s %s %s" % (ct.punct("###["),
                            ct.layer_name(self.name),
                            ct.punct("]###"))
        for f in self.fields_desc:
            if isinstance(f, Emph):
                ncol = ct.emph_field_name
                vcol = ct.emph_field_value
            else:
                ncol = ct.field_name
                vcol = ct.field_value
            print "  %s%-10s%s %s" % (" "*indent*lvl,
                                      ncol(f.name),
                                      ct.punct("="),
                                      vcol(f.i2repr(self,self.__getattr__(f))))
        dec = 1
        if isinstance(self.payload, OLSR_HELLO_LinkMessage):
            dec = 0
        self.payload.display(indent=indent,lvl=lvl+dec)


# OLSR Hello Header : on this packet, multiple OLSR Link Messages can
# be stacked. 
class OLSR_HELLO(Packet):
    name = "OLSR HELLO Message"
    fields_desc = [ ByteEnumField("type", 1, olsr_types),
                    ByteField("vtime", conf.olsr_NEIGHB_HOLD_TIME), 
                    ShortField("msgsize", None),
                    _OLSROrigAddrField("oaddr", None),
                    ByteField("ttl", 1), #RFC 3626 sect 6.1
                    ByteField("hopcount", 0 ),
                    ShortField("msgsn", 0),
                    XShortField("res", 0),
                    _OLSRTimeField("htime", conf.olsr_HELLO_INTERVAL),
                    ByteEnumField("willingness", 3, olsr_willingness) ]

    def do_dissect(self, s):
        # Dissecting fields of OLSR_HELLO packet
        flist = self.fields_desc[:]
        flist.reverse()
        while s and flist:
            f = flist.pop()
            s,fval = f.getfield(self, s)
            self.fields[f] = fval

        # post_dissect() call has been removed. Make no sense here.
        # extract_padding() call has been removed. Make no sense here.

        # l will be the length of following link messages train (beginning)
        # what follows beginning (end) is another OLSR message
        l = self.msgsize - 16
        print hexdump(s[:l])
        print hexdump(s[l:])
        beginning,end = s[:l], s[l:]
        self.do_dissect_payload(beginning)

        # beginning has been dissected has a chain of Link messages.
        # Let's gain the end of that train
        while isinstance(self.payload, OLSR_HELLO_LinkMessage):
            self = self.payload

        # If end can be parsed  has an OLSR Message Header, let's find
        # its type, instantiate it and add the result to our packet
        if len(end) >= 12:
            cls = globals().get(olsr_cls.get(ord(end[0]),"Raw"), "Raw")
            self.add_payload(cls(end))


    def post_build(self, p):
        # compute length till payload is end of Link Message classes
        if self.msgsize is None:
            while isinstance(self.payload, OLSR_HELLO_LinkMessage):
                self = self.payload
            self=self.payload
            l = len(p)
            if self is not None:
                l -= len(str(self))
            p = p[:2]+struct.pack("!H", l)+p[4:]
        return p


# Defined in section 9.1
class OLSR_TC(_OLSRDefaultPayload):
    name = "OLSR Topology Control (TC) Message"
    fields_desc = [ ByteEnumField("type", 2, olsr_types),
                    ByteField("vtime", conf.olsr_TOP_HOLD_TIME),
                    FieldLenField("msgsize", None, "anma", "!H", shift=-16),
                    _OLSROrigAddrField("oaddr", None),
                    ByteField("ttl", 255), # RFC 3626 Sect 9.1
                    ByteField("hopcount", 0 ),
                    ShortField("msgsn", 0),
                    XShortField("ansn", 0),
                    XShortField("res", 0),
                    IPListField("anma", [], "msgsize") ]


# Internal representation of the NetListField is a list of tuple (net, mask).
# - net is in printable representation (output of inet_ntop)
# - mask is in printable representation (output of inet_ntop)
# Supports v4 and v6. See IPListField comment.
class NetListField(StrLenField):
    islist = 1

    def i2repr(self, pkt, x): # v4/v6 independent
        s = []
        if x is None:
            return "[]"
        for y in x:
            net, mask = y
            s.append('(%s, %s)' % (net, mask))
        return "[ %s ]" % (", ".join(s))

    def getfield(self, pkt, s):

        # grab announced length
        l = getattr(pkt, self.fld)  
        f = pkt.get_field(self.fld)
        if isinstance(f, FieldLenField):
            l += f.shift

        # Are we carried by IPv4 or IPv6 ? -> set self.af and self.addrlen
        under = pkt.underlayer
        while under is not None:
            if conf.olsr_IPv6available and isinstance(under, IPv6):
                self.af =socket.AF_INET6
                self.addrlen = 16
                break
            elif isinstance(under, IP):
                self.af = socket.AF_INET
                self.addrlen = 4
                break
            under = under.underlayer

        if under is None:
            warning("No IP or IPv6 underlayer to select OLSR carried")
            warning("address type. Using IPv6 as fallback.")            

        return s[l:], self.m2i(pkt,s[:l])

    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt,val)

    def any2i(self, pkt, x): 
        if type(x) is list:
            return map(lambda z,pkt=pkt:self.any2i_one(pkt,z), x)
        else:
            r = []
            r.append(self.any2i_one(pkt,x))
            return r

    # TODO : reread this function and search the bugs
    def any2i_one(self, pkt, x):
        if x is None or x is "":
            return None

        if type(x) is str: # v4/v6 host/net (2001::/64 or 172.16.0.0/24)

            if x.count(':') > 0: # IPv6
                self.af =socket.AF_INET6
                self.addrlen = 16

                res=x.split("/")
                l = len(res)
                if l == 1: # host case. Prefix will be 128
                    return self.any2i_one("%s/%d", (res[0],128))
                elif l == 2: # net case (most common case)
                    return (res[0], socket.inet_ntop(socket.AF_INET6, in6_cidr2mask(int(res[1]))))
                else: # error
                    warning( "give me something better" )
                    return None
                
            else:          # v4 net or host : "172.16.0.0/24"
                self.af =socket.AF_INET
                self.addrlen = 4                

                res=x.split("/")
                l = len(res)
                if l == 1: # host case. Prefix will be 32
                    return (res[0], ltoa(itom(32)))
                elif l == 2: # net case (most common case)
                    return (res[0], ltoa(itom(int(res[1]))))
                else: # error
                    warning( "give me something better" )
                    return None

        elif type(x) is tuple: # for thos loving tuples
            if type(x[1]) is int:
                return self.any2i_one(pkt, "%s/%d" % (x[0], x[1]))
            else:
                # tuple (Net, Mask) to be able to send corrupted values.
                # Valid values are : ("2001::1", "ff:ff::"), ("172.16.0.0", "255.255.0.0")
                return x
        # Third case : error
        else:
            return None
    
    def m2i(self, pkt, x):
        r = []
        l = self.addrlen
        while len(x) >= 8:
            r.append((socket.inet_ntop(self.af, x[:l]),
                      socket.inet_ntop(self.af, x[l:2*l])))
            x = x[2*l:]
        return r

    def i2m(self, pkt, x):
        s = ""
        if len(x) > 0:
            for net in x:
                s += socket.inet_pton(self.af, net[0]) + socket.inet_pton(self.af, net[1])
            return s
        return ""



# Host and Network Association Message. Sect 12 of RFC 3626
# 
# "In order to provide this capability of injecting external routing
# information into an OLSR MANET, a node with such non-MANET
# interfaces periodically issues a Host and Netwrok Association (HNA)
# message, containing sufficient information for the recipients to
# construct an appropriate routing table"
#
# TODO :
# - set Vtime and ttl
class OLSR_HNA(_OLSRDefaultPayload):
    name = "OLSR Host and Network Association Message"
    fields_desc = [ ByteEnumField("type", 4, olsr_types),
                    ByteField("vtime", conf.olsr_HNA_HOLD_TIME),
                    FieldLenField("msgsize", None, "hna", "!H", shift=-12),
                    _OLSROrigAddrField("oaddr", None),
                    ByteField("ttl", 255), # RFC 3626 Sect. 12.1
                    ByteField("hopcount", 0 ),
                    ShortField("msgsn", 0),
                    NetListField("hna", [], "msgsize") ]
    
bind_layers(                    UDP, OLSR                  , { "sport":54, "dport":698 } )
bind_layers(             OLSR_HELLO, OLSR_HELLO_LinkMessage, { })
bind_layers( OLSR_HELLO_LinkMessage, OLSR_HELLO_LinkMessage, { } )


interact(mydict=globals(),mybanner="OLSR add-ons $Revision: 1.15 $")
