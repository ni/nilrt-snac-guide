
.. _appendix-3--firewall-configuration:

==================================
Appendix 3: Firewall Configuration
==================================


.. _introduction:

------------
Introduction
------------

NI Linux RT in the SNAC configuration uses firewalld
(https://firewalld.org/). The most important concepts of firewalld
configuration are briefly explained here. For more information, see the
firewalld documents "Concepts"
(https://firewalld.org/documentation/concepts.html) and "Architecture"
(https://firewalld.org/documentation/architecture.html).

firewalld classifies networks (whether IP address ranges or network
interfaces) into *zones*, allowing remote hosts to be grouped into
different levels of trust. The pseudo-zone HOST represents the local
host itself; the pseudo-zone ANY is the complement of HOST. Unclassified
interfaces and hosts are placed in a default zone.

Firewall rules are organized into *policies*. Each policy has one or
more ingress and egress zones. (If no egress zone is defined, HOST is
assumed. Likewise, policy definitions can also be added to zone
definitions, in which case the zone is assumed to be the ingress zone
and HOST is the egress zone.) Policies can match on any of its defined
ingress and egress zones, protocols, and source/destination ports; they
also define what should be done with a matching packet. Packets will be
processed by all policies whose ingress and egress zones match its
source and destination addresses/ports.

firewalld also allows *services* to be symbolically defined as a set of
protocols, ports, and destination ports (for e.g. multicast traffic).
This allows complex service definitions to be referenced by simple
service names in policy definitions.

The Linux kernel includes two low-level firewall implementations:
iptables (https://www.netfilter.org/projects/iptables) and nftables
(https://www.nftables.org/). iptables has been superseded by nftables
since 2014. Firewalld can be configured to use either iptables or
nftables. Under NI Linux RT, firewalld is configured to use nftables.


.. _how-snac-configures-firewalld:

-------------------------------------
How SNAC configures firewalld
-------------------------------------

SNAC configuration (with the nilrt-snac configure command) installs
firewalld, resets its configuration, and populates a default set of
rules.

Zones and policies are configured as follows. The work zone includes
wglv0. All other network interfaces remain at their default zone which
is public. Firewall rules are always defined separately for outbound and
inbound traffic. This requires explicitly constructed policies to manage
outbound traffic rules; for symmetry, inbound policies are also created.
(This is contrary to the typical firewalld practice of adding services
to zones rather than policies; when added to a zone, the rule is always
interpreted as inbound.)

+----------------------+-----------------------+-----------------------+
| Policy name          | INGRESS               | EGRESS                |
+======================+=======================+=======================+
| work-in              | work                  | HOST                  |
+----------------------+-----------------------+-----------------------+
| work-out             | HOST                  | work                  |
+----------------------+-----------------------+-----------------------+
| public-in            | public                | HOST                  |
+----------------------+-----------------------+-----------------------+
| public-out           | HOST                  | public                |
+----------------------+-----------------------+-----------------------+

Users with dedicated private networks for e.g. plant operations are
expected to define their own zones and policies as appropriate for their
own applications. For instance, EtherCAT traffic over eth1 should happen
in a separate zone from work or public.

Unmatched traffic is generally REJECTed, not DROPped. The distinction is
that REJECT will emit an ICMP error message, but DROP will emit nothing.
This is an expedient for efficient system development, and while
generally following best practices, high-security deployments should
consider changing the targets for public-in and public-out to DROP.

Allowed traffic through the public zone, as controlled by the public-in
and public-out policies, generally includes everything necessary for the
RT target to configure itself on the local network and to let it be
managed through secured facilities. For inbound traffic, this includes
ssh, ICMP, and WireGuard. For outbound traffic, this includes DHCP,
ICMP, HTTP (for opkg), WireGuard, DNS, and NTP.

Allowed traffic through the work zone, as controlled by the work-in and
work-out policies, generally includes protocols necessary for NI
software operations. This includes (but is not limited to) LabVIEW RT,
LabVIEW VI Server, NI Service Locator, and several other internal
services.

For more information about the exact nature of the firewall
configuration installed by nilrt-snac, consult the source code,
installed at /usr/lib/nilrt-snac/nilrt_snac/_configs/_firewall_config.py
(also viewable at GitHub `here <https://github.com/ni/nilrt-snac/blob/master/nilrt_snac/_configs/_firewall_config.py>`__).


.. _reconfiguring-network-interfaces-in-firewalld:

---------------------------------------------
Reconfiguring network interfaces in firewalld
---------------------------------------------

The following command adds interface eth1 to the work zone, making it as
trusted as wglv0.

`firewall-cmd --zone=work --add-interface=eth1`

That command updates the running firewalld configuration, but not the
permanent configuration. To persist the change, add --permanent:

`firewall-cmd --permanent --zone=work --add-interface=eth1`

Users are free to create their own zones and policies, with the
following caveat: running nilrt-snac --configure will run firewall-cmd
--reset-to-defaults, which will erase all user customizations; you must
re-apply them yourself.


.. _reconfiguring-firewalld-for-additional-ni-services:

--------------------------------------------------
Reconfiguring firewalld for additional NI services
--------------------------------------------------

The SNAC configuration only enables a minimal set of NI services across
the firewall --- primarily what is needed for LabVIEW RT and DAQmx --- and
only across the work zone. It is anticipated that many users may require
additional firewall rules additional services for their own
applications. When possible, we suggest controlling NI services
symbolically, not through numeric TCP/UDP ports, by referencing the
firewalld XML service definitions for NI software installed in the
ni-firewalld-servicedefs package (source
`here <https://github.com/ni/meta-nilrt/tree/nilrt/master/next/recipes-ni/ni-firewalld-servicedefs>`__).
This may improve the readability of firewall rules and future-proof
those rules against future changes.

For instance, the command to open incoming traffic to UDP port 2222 in
the running configuration is:

`firewall-cmd --policy=work-in --add-port=2222/udp`

However, 2222/udp is ostensibly used by Ethernet/IP Explicit Messaging;
the following will enable all ports used by that protocol, both 2222/udp
and 44818/tcp:

`firewall-cmd --policy=work-in --add-service=ethernet-ip-explicit`

That command updates the running firewalld configuration, but not the
permanent configuration. To persist the change, add --permanent:

`firewall-cmd --permanent --policy=work-in --add-service=ethernet-ip-explicit`

See the ni-firewalld-servicedefs
`source <https://github.com/ni/meta-nilrt/tree/nilrt/master/next/recipes-ni/ni-firewalld-servicedefs>`__
for a list of currently-defined NI services; or, on a live SNAC target,
run opkg files ni-firewalld-servicedefs. To see a list of all firewalld
services, run firewall-cmd --get-services (warning: long).

At present, some NI services remain generally incompatible with
firewalls, typically because their listening ports are dynamically
allocated. If one of these services are needed, the firewall (across the
work zone, i.e. the WireGuard interface) may need to be disabled. This
can be accomplished with

`firewall-cmd --policy=work-in --set-target=ACCEPT`

`firewall-cmd --policy=work-out --set-target=ACCEPT`


.. _troubleshooting:

---------------
Troubleshooting
---------------

Initial application testing under SNAC may fail because of ports blocked
by the firewall; knowing when this occurs is vital for efficient
application testing and triage. firewalld can be configured to write a
log message for every dropped packet, by setting e.g. LogDenied=unicast
in /etc/firewalld/firewalld.conf.

.. code-block:: ini

    # Add logging rules right before reject and drop rules in the INPUT, FORWARD
    # and OUTPUT chains for the default rules and also final reject and drop Rules
    # in zones. Possible values are: all, unicast, broadcast, multicast and off.
    # Default: off
    LogDenied=unicast

Logged packets will be written to the kernel log and can be browsed via
dmesg; use dmesg -w to watch the log in real-time.


.. _limitations:

-----------
Limitations
-----------

NI Linux RT has supported the iptables since the 2014 release; but under
SNAC, iptables is untested and unsupported.

NI Linux RT does not support filtering by DNS hostnames; hosts can only
be filtered by IP address.
