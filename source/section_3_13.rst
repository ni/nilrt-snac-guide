
.. _3-13--system-and-communications-protection:

==========================================
3.13. System and Communications Protection
==========================================


.. _3-13-1--boundary-protection:

---------------------------
3.13.1. Boundary Protection
---------------------------

#. Monitor and control communications at the external managed   interfaces to the system and at key internal managed interfaces within   the system.
#. Implement subnetworks for publicly accessible system components   that are physically or logically separated from internal networks.
#. Connect to external networks or systems only through managed   interfaces consisting of boundary protection devices arranged in   accordance with an organizational security architecture.

**DISCUSSION**

Managed interfaces include gateways, routers, firewalls, guards,
network-based malicious code analysis, virtualization systems, or
encrypted tunnels implemented within a security architecture.
Subnetworks that are either physically or logically separated from
internal networks are referred to as demilitarized zones or DMZs.
Restricting or prohibiting interfaces within organizational systems
includes restricting external web traffic to designated web servers
within managed interfaces, prohibiting external traffic that appears to
be spoofing internal addresses, and prohibiting internal traffic that
appears to be spoofing external addresses. Boundary protection may be
implemented as a common control for all or part of an organizational
network such that the boundary to be protected is greater than a
system-specific boundary (i.e., an authorization boundary).

Organizations consider the shared nature of commercial
telecommunications services in the implementation of security
requirements associated with the use of such services. Commercial
telecommunications services are commonly based on network components and
consolidated management systems shared by all attached commercial
customers and may also include third party-provided access lines and
other service elements. Such transmission services may represent sources
of increased risk despite contract security provisions.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
|   | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
| X | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| System communication boundaries are defined across fixed-function networking     |
| devices like routers and firewalls, and VPNs and related tunnel technologies.    |
| Customers retain all responsibility for configuration and maintenance of these   |
| devices. NILRT+SNAC devices are equipped with a software firewall -              |
| ``firewalld`` - that provides protection to the device and the network.          |
| Additional configuration of ``firewalld`` can be performed by system             |
| administrators using the ``firewall-cmd`` utility.                               |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-2--withdrawn--incorporated-into-3-16-1-:

--------------------------------------------
3.13.2. Withdrawn: Incorporated into 3.16.1.
--------------------------------------------

.. raw:: latex

    \newpage



.. _3-13-3--withdrawn--addressed-by-03-01-01--03-01-02--03-01-03--03-01-04--03-01-05--03-01-06--03-01-07:

----------------------------------------------------------------------------------------------------
3.13.3. Withdrawn: Addressed by 03.01.01, 03.01.02, 03.01.03, 03.01.04, 03.01.05, 03.01.06, 03.01.07
----------------------------------------------------------------------------------------------------

.. raw:: latex

    \newpage



.. _3-13-4--information-in-shared-system-resources:

----------------------------------------------
3.13.4. Information in Shared System Resources
----------------------------------------------

Prevent unauthorized and unintended information transfer via shared
system resources.

**DISCUSSION**

Preventing unauthorized and unintended information transfer via shared
system resources stops information produced by the actions of prior
users or roles (or actions of processes acting on behalf of prior users
or roles) from being available to current users or roles (or current
processes acting on behalf of current users or roles) that obtain access
to shared system resources after those resources have been released back
to the system. Information in shared system resources also applies to
encrypted representations of information. In other contexts, the control
of information in shared system resources is referred to as object reuse
and residual information protection. Information in shared system
resources does not address information remanence, which refers to the
residual representation of data that has been nominally deleted, covert
channels (including storage and timing channels) in which shared system
resources are manipulated to violate information flow restrictions, or
components within systems for which there are only single users or
roles.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
|   | Implemented by vendor           |
+---+---------------------------------+
| X | Not implemented by vendor       |
+---+---------------------------------+
|   | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| Shared system resources potentially include data written to temporary locations  |
| on permanent storage or RAM-disk, and may provide an exploitable side channel of |
| communication, or disclose sensitive metadata about past system interactions.    |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| Preventing this kind of information transfer requires system software to only    |
| store session-bounded ephemera in locations whose existence is also              |
| session-bounded. This requires software changes which are unavailable to the end |
| user.                                                                            |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-5--withdrawn--incorporated-into-3-13-1-:

--------------------------------------------
3.13.5. Withdrawn: Incorporated into 3.13.1.
--------------------------------------------

.. raw:: latex

    \newpage



.. _3-13-6--network-communications---deny-by-default---allow-by-exception:

---------------------------------------------------------------------
3.13.6. Network Communications - Deny by Default - Allow by Exception
---------------------------------------------------------------------

Deny network communications traffic by default, and allow network
communications traffic by exception.

**DISCUSSION**

This requirement applies to inbound and outbound network communications
traffic at the system boundary and at identified points within the
system. A deny-all, allow-by-exception network communications traffic
policy ensures that only essential and approved connections are allowed.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
| X | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
|   | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| Network communications to and from the NILRT+SNAC system are controlled by the   |
| 'firewalld' firewall daemon. By default, all communications which are not        |
| strictly necessary for system configuration and administration or which are      |
| legitimate NI software communications, are denied. Runtime reconfiguration of    |
| firewalld by system administrators is possible using the 'firewall-cmd' utility. |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-7--withdrawn--addressed-by-03-01-12--03-04-02--03-04-06:

------------------------------------------------------------
3.13.7. Withdrawn: Addressed by 03.01.12, 03.04.02, 03.04.06
------------------------------------------------------------

.. raw:: latex

    \newpage



.. _3-13-8--transmission-and-storage-confidentiality:

------------------------------------------------
3.13.8. Transmission and Storage Confidentiality
------------------------------------------------

Implement cryptographic mechanisms to prevent the unauthorized
disclosure of CUI during transmission and while in storage.

**DISCUSSION**

This requirement applies to internal and external networks and any
system components that can transmit CUI, including servers, notebook
computers, desktop computers, mobile devices, printers, copiers,
scanners, facsimile machines, and radios. Communication paths outside of
the physical protection of controlled boundaries are susceptible to both
interception and modification. Encryption protects CUI from unauthorized
disclosure during transmission. Cryptographic mechanisms that protect
the confidentiality and integrity of information during transmission
include TLS and IPsec. Cryptographic standards include FIPS-validated
cryptography [30] [31] [32] and NSA-approved cryptography. Information
at rest refers to the state of CUI when it resides on the system and is
not in process or in transit, including internal or external storage
devices, storage area network devices, and databases. The focus of
protecting CUI at rest is not on the type of storage device or the
frequency of access to that device but rather on the state of the
information.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
|   | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
| X | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+-------------------------------------------------------------------------------------------------+
| Solution Implementation                                                                         |
+=================================================================================================+
| CUI in transit can be secured in LabVIEW over the TLS, SFTP, SSH, and WebDAV+HTTPS protocols    |
| without additional software installation. Non-LabVIEW applications should use TLS or DTLS.      |
+-------------------------------------------------------------------------------------------------+
+-------------------------------------------------------------------------------------------------+
| CUI in storage should either be stored in encrypted forms and only decrypted into memory using  |
| the included ``gnupg`` and ``openssl`` utilities, or stored in a block-encrypted partition or   | 
| removable storage device. For more information about how to setup an encrypted data             |
| partition, see the                                                                              |
| :ref:`Non-Runtime Partition Encryption<non-runtime-partition-encryption>` section               |
| in Appendix 1.                                                                                  |
+-------------------------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-9--network-disconnect:

--------------------------
3.13.9. Network Disconnect
--------------------------

Terminate network connections associated with communications sessions at
the end of the sessions or after [*Assignment: organization-defined time
period*] of inactivity.

**DISCUSSION**

This requirement applies to internal and external networks. Terminating
network connections associated with communications sessions includes
de-allocating associated TCP/IP address or port pairs at the operating
system level or de-allocating networking assignments at the application
level if multiple application sessions are using a single operating
system-level network connection. Time periods of user inactivity may be
established by organizations and include time periods by type of network
access or for specific network accesses.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
| X | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
|   | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| The SSH daemon is configured to terminate inactive network sessions after a 60   |
| second period of inactivity. This value is configurable by system administrators |
| by modifying the 'ClientAlive' settings in the ' /etc/ssh/sshd_config' file.     |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| System owners create programs to connect and send data from the NILRT device. It |
| is the responsibility of the system owner to ensure that all open connections in |
| these programs are terminated properly.                                          |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-10--cryptographic-key-establishment-and-management:

-------------------------------------------------------
3.13.10. Cryptographic Key Establishment and Management
-------------------------------------------------------

Establish and manage cryptographic keys when cryptography is implemented
in the system in accordance with the following key management
requirements: [*Assignment: organization-defined requirements for key
generation, distribution, storage, access, and destruction*].

**DISCUSSION**

Cryptographic key management and establishment can be performed using
manual procedures or mechanisms supported by manual procedures.
Organizations define key management requirements in accordance with
applicable federal laws, Executive Orders, policies, directives,
regulations, and standards specifying appropriate options, levels, and
parameters.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
|   | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
|   | Must be implemented by end user |
+---+---------------------------------+
| X | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| In general, NI software only permits low-level, manual configuration of public   |
| or private keys; higher-level functionality, like key rotation, is generally not |
| provided. The default certificate store is sourced from NSS (via curl) and is    |
| manipulated like any other OpenSSL certificate store.                            |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-11--cryptographic-protection:

---------------------------------
3.13.11. Cryptographic Protection
---------------------------------

Implement the following types of cryptography when used to protect the
confidentiality of CUI: [*Assignment: organization-defined types of
cryptography*].

**DISCUSSION**

Cryptography can be employed to support a variety of security solutions,
including the protection of CUI. Cryptography is implemented in
accordance with applicable laws, Executive Orders, directives,
regulations, policies, standards, and guidelines. FIPS-validated
cryptography is described in [30] [31] [32].

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
|   | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
| X | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| NI Linux RT does not presently support the specification of FIPS-validated       |
| algorithms, i.e. "FIPS mode" (where the only permitted algorithms are those      |
| validated by FIPS). While the algorithms are present, their implementations are  |
| not FIPS-validated, and exist alongside unapproved algorithms.                   |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| The system owner is responsible to ensure that any CUI handled in the system is  |
| encrypted to FIPS standards.                                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-12--collaborative-computing-devices-and-applications:

---------------------------------------------------------
3.13.12. Collaborative Computing Devices and Applications
---------------------------------------------------------

#. Prohibit remote activation of collaborative computing devices and   applications with the following exceptions:
   [*Assignment:   organization-defined exceptions where remote activation is to be   allowed*].
#. Provide an explicit indication of use to users physically present   at the devices.

**DISCUSSION**

Collaborative computing devices include networked white boards,
microphones, and cameras. Indication of use includes signals to users
when collaborative computing devices are activated. Dedicated video
conferencing systems, which rely on one of the participants calling or
connecting to the other party to activate the video conference, are
excluded. Solutions to prevent device usage include webcam covers and
buttons to disable microphones.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
|   | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
|   | Must be implemented by end user |
+---+---------------------------------+
| X | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| NILRT devices do not normally support collaborative devices. It is the           |
| responsibility of the system owner to review components to ensure none of these  |
| devices are in the system.                                                       |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-13--mobile-code:

--------------------
3.13.13. Mobile Code
--------------------

#. Define acceptable and unacceptable mobile code and mobile code   technologies.
#. Authorize, control, and monitor the use of mobile code.

**DISCUSSION**

Mobile code includes any program, application, or content that can be
transmitted across a network (e.g., embedded in an email, document, or
website) and executed on a remote system. Decisions regarding the use of
mobile code within the system are based on the potential for the code to
cause damage to the system if used maliciously. Mobile code technologies
include Java applets, JavaScript, HTML5, VBScript, and WebGL. Usage
restrictions and implementation guidelines apply to the selection and
use of mobile code installed on servers as well as mobile code
downloaded and executed on individual workstations and devices,
including notebook computers and smart phones. Mobile code policy and
procedures address the specific actions taken to prevent the
development, acquisition, and introduction of unacceptable mobile code
within the system, including requiring mobile code to be digitally
signed by a trusted source.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
| X | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
|   | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| NILRT+SNAC makes no use of, nor supports, mobile code.                           |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-14--withdrawn--technology-specific-:

----------------------------------------
3.13.14. Withdrawn: Technology-specific.
----------------------------------------

.. raw:: latex

    \newpage



.. _3-13-15--session-authenticity:

-----------------------------
3.13.15. Session Authenticity
-----------------------------

Protect the authenticity of communications sessions.

**DISCUSSION**

Protecting session authenticity addresses communications protection at
the session level, not at the packet level. Such protection establishes
grounds for confidence at both ends of the communications sessions in
the ongoing identities of other parties and validity of transmitted
information. Authenticity protection includes protecting against
"adversary-in-the-middle" attacks (also known as "man-in-the middle"
attacks), session hijacking, and the insertion of false information into
sessions.

+---+---------------------------------+
|   | Control Summary Information     |
+===+=================================+
|   | Implemented by vendor           |
+---+---------------------------------+
|   | Not implemented by vendor       |
+---+---------------------------------+
| X | Must be implemented by end user |
+---+---------------------------------+
|   | Not applicable                  |
+---+---------------------------------+

+----------------------------------------------------------------------------------+
| Solution Implementation                                                          |
+==================================================================================+
| The authenticity of NILRT configuration session is protected by SSH.             |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| LabVIEW communications should be protected by transmitting to and from the NILRT |
| system using the encrypted Wireguard tunnel.                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-13-16--withdrawn--incorporated-into-3-13-8-:

---------------------------------------------
3.13.16. Withdrawn: Incorporated into 3.13.8.
---------------------------------------------

.. raw:: latex

    \newpage

