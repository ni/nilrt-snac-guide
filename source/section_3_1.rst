
.. _3-1--access-control:

===================
3.1. Access Control
===================


.. _3-1-1--account-management:

-------------------------
3.1.1. Account Management
-------------------------

#. Define and document the types of system accounts allowed and   prohibited.
#. Create, enable, modify, disable, and remove accounts in accordance   with [*Assignment: organization-defined policy, procedures,   prerequisites, and criteria*].
#. Specify authorized users of the system, group and role membership,   and access authorizations (i.e., privileges).
#. Authorize access to the system based on a valid access   authorization and intended system usage.
#. Monitor the use of accounts.
#. Disable accounts of individuals within [*Assignment:   organization-defined time period*] when the ac­counts:

   #. Have expired;
   #. Are no longer associated with a user or individual;
   #. Are in violation of organizational policy; or
   #. Have been inactive for [*Assignment: organization-defined time      period*].

#. Disable accounts of individuals within [*Assignment:   organization-defined time period*] of discovery of [*Assignment:   organization-defined significant risks*].
#. Notify [*Assignment: organization-defined personnel or roles*]   within [*Assignment: organization-defined time period*]:

   #. When accounts are no longer required;
   #. When users are terminated or transferred; and
   #. When system usage or need-to-know changes for an individual.

**DISCUSSION**

This requirement focuses on account management for systems and
applications. The definition of and enforcement of access authorizations
other than those determined by account type (e.g., privileged access,
non-privileged access) are addressed in requirement 3.1.2. System
account types include individual, shared, group, temporary, system,
guest, anonymous, emergency, developer, and service. Users who require
administrative privileges on system accounts receive additional scrutiny
by organizational personnel responsible for approving such accounts and
privileged access. Types of accounts that organizations may prohibit
due to increased risk include shared, group, emergency, guest,
anonymous, and temporary.

Organizations may choose to define access privileges or other attributes
by account, by type of account, or a combination of both. Other
attributes required for authorizing access include restrictions on
time-of-day, day-of-week, and point-of-origin. In defining other account
attributes, organizations consider system-related requirements (e.g.,
system upgrades, scheduled maintenance) and mission and business
require­ments (e.g., time zone differences, remote access to support
travel requirements).

Users who pose a significant security risk include individuals for whom
reliable evidence indicates either the intention to use authorized
access to the system to cause harm or that adversaries will cause harm
through them. Close coordination among human resource managers, system
administrators, legal staff, and human resource managers is essential
when disabling system accounts for high-risk individuals. Time periods
for notification of organizational personnel or roles may vary.

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
| NILRT SNAC implements a Linux Pluggable Authentication Module (PAM)              |
| authentication scheme using standard Linux tools for account management. With    |
| these libraries, the NILRT system owner can enable account management with       |
| methods such as local passwords or LDAP.                                         |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| The system is configured with a privileged 'root' account for maintenance and    |
| administration, and other system accounts for use by services on the system.     |
| System owners are directed to define a schema of access roles that are           |
| appropriate for the system's mission. System administrators are directed to      |
| implement that role schema on the NILRT device, via the shell, using the         |
| included standard linux account management utilities (passwd, useradd,           |
| groupadd, et c.). System owners should define policies that govern how these     |
| accounts are monitored and how privileges are revoked, in accordance with SP     |
| _800_171/SR-03.01.01.                                                            |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-2--access-enforcement:

-------------------------
3.1.2. Access Enforcement
-------------------------

Enforce approved authorizations for logical access to CUI and system
resources in accordance with ap­plicable access control policies.

**DISCUSSION**

Access control policies control access between active entities or
subjects (i.e., users or processes acting on behalf of users) and
passive entities or objects (i.e., devices, files, records, domains) in
organizational systems. Types of system access include remote access and
access to systems that communicate through external networks, such as
the internet. Access enforcement mechanisms can also be employed at the
application and service level to provide increased protection for CUI.
This recognizes that the system can host many applications and services
in support of mission and business functions.

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
| NILRT segregates access to resource domains by user and group account, and       |
| restricts process' access to privileged kernel operations through                |
| explicitly-assigned 'capabilities'. CUI domains are not implemented in the       |
| NILRT OS design by default. System owners whose applications store, manipulate,  |
| or transmit CUI data should implement access control policies specific to their  |
| design.                                                                          |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-3--flow-enforcement:

-----------------------
3.1.3. Flow Enforcement
-----------------------

Enforce approved authorizations for controlling the flow of CUI within
the system and between connected systems.

**DISCUSSION**

Information flow control regulates where information can transit within
a system and between systems (versus who can access the information) and
without explicit regard to subsequent accesses to that information.
Flow control restrictions include the following: keeping
export-controlled information from being transmitted in the clear to the
internet, blocking outside traffic that claims to be from within the
organization, restricting requests to the internet that are not from
the internal web proxy server, and limiting information transfers
between organizations based on data structures and content.

Organizations commonly use information flow control policies and
enforcement mechanisms to control the flow of information between
designated sources and destinations (e.g., networks, individuals, and
devices) within systems and between interconnected systems. Flow
control is based on characteristics of the information or the
information path. Enforcement occurs in boundary protection devices
(e.g., encrypted tunnels, routers, gateways, and firewalls) that employ
rule sets or establish configuration settings that restrict system
services, provide a packet-filtering capability based on header
information, or provide a message-filtering capability based on message
content (e.g., implementing key word searches or using document
characteristics). Organizations also consider the trustworthiness of
filtering and inspection mechanisms (i.e., hardware, firmware, and
software components) that are critical to information flow enforcement.

Transferring information between systems that represent different
security domains with different security policies introduces risk that
such transfers violate one or more domain security policies. In such
situations, information owners or stewards provide guidance at
designated policy enforcement points between interconnected systems.
Organizations consider mandating specific architectural solutions when
required to enforce specific security policies. Enforcement includes
prohibiting information transfers between interconnected systems (i.e.,
allowing information access only), employing hardware mechanisms to
enforce one-way information flows, and implementing trustworthy
regrading mechanisms to reassign security attributes and security
labels.

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
| NILRT and operating systems generically do not have domain knowledge about       |
| organizational boundaries. CUI flow enforcement between connected systems is     |
| best implemented by dedicated network equipment that can enforce domain          |
| boundaries on the network.                                                       |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-4--separation-of-duties:

---------------------------
3.1.4. Separation of Duties
---------------------------

#. Identify the duties of individuals requiring separation.
#. Define system access authorizations to support separation of   duties.

**DISCUSSION**

Separation of duties addresses the potential for abuse of authorized
privileges and helps reduce the risk of malevolent activity without
collusion. Separation of duties includes dividing mission functions and
support functions among different individuals or roles, conducting
system support functions with different individuals or roles (e.g.,
quality assurance, configuration management, testing, system management,
programming, and network security), and ensuring that security
personnel who administer access control functions do not also administer
audit functions. Because separation of duty violations can span systems
and application domains, organizations consider the entirety of their
systems and system components when developing policies on separation of
duties.

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
| NILRT+SNAC uses a single account for maintenance duties (root), a user account   |
| for LabVIEW processes (lvuser), and segregated system service accounts based on  |
| their domain of responsibility. Individuals who require administrative or        |
| auditing permissions should have user accounts created for them using the        |
| \`useradd\` command, and be given membership in the \`sudo\` or \`adm\` group    |
| respectively.                                                                    |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| Individuals whose roles require them to use deployed LabVIEW applications should |
| be authorized at a network-connected Windows host machine. The user's            |
| application design should only permit those authorized Windows users to receive  |
| and decrypt LabVIEW network traffic to which their role requires they have       |
| access.                                                                          |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-5--least-privilege:

----------------------
3.1.5. Least Privilege
----------------------

#. Allow only authorized system access for users (or processes acting   on behalf of users) that are necessary to accomplish assigned   organizational tasks.
#. Authorize access for [*Assignment: organization-defined individuals   or roles*] to [*Assignment: organization-defined security functions   and security-relevant information*].
#. Review [*Assignment: organization-defined frequency*] the   privileges assigned to [*Assignment: organization-defined roles or   classes of users*] to validate the need for such privileges.
#. Reassign or remove privileges, as necessary.

**DISCUSSION**

Organizations employ the principle of least privilege for specific
duties and authorized access for users and processes. Security functions
include establishing system accounts, configuring access authorizations
(i.e., permissions, privileges), configuring settings for events to be
audited, and establishing intrusion detection parameters.
Security-relevant information includes filtering rules for routers or
firewalls, configuration parameters for security services, cryptographic
key management information, and access control lists. Authorized
personnel include security administrators, system administrators, system
security officers, system programmers, and other privileged users.
Organizations consider creating additional processes, roles, and system
accounts to achieve least privilege. Least privilege is also applied to
the development, implementation, and operation of the system.

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
| NILRT device configuration and LabVIEW deployment workflows require the use of   |
| the 'root' account and 'lvuser', respectively. Both accounts have over-broad     |
| permissions for their duties. Integrators can mitigate attacks against these     |
| accounts by enforcing policy limitations on who has networked and physical       |
| access to the NILRT device.                                                      |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-6--least-privilege---privileged-accounts:

--------------------------------------------
3.1.6. Least Privilege - Privileged Accounts
--------------------------------------------

#. Restrict privileged accounts on the system to [*Assignment: organization-defined personnel or roles*].
#. Require that users of system accounts (or roles) with access to
   [*Assignment: organization-defined security functions or security-relevant information*]
   use non-privileged accounts or roles when accessing non-security functions.

**DISCUSSION**

Privileged accounts, including super user accounts, are typically
described as system administrator accounts for various types of
commercial off-the-shelf operating systems. Restricting privileged
accounts to specific personnel or roles prevents nonprivileged users
from accessing privileged information or privileged functions. In
restricting privileged accounts, organizations may differentiate between
allowed privileges for local accounts and domain accounts provided that
they retain the ability to control system configurations for key
parameters and as otherwise necessary to sufficiently mitigate risk.

Requiring the use of non-privileged accounts when accessing non-security
functions limits exposure when operating from within privileged accounts
or roles. The inclusion of roles addresses situations in which
organizations implement access control policies, such as role-based
access control, and where a change of role provides the same degree of
assurance in the change of access authorizations for the user and the
processes acting on behalf of the user as would be provided by a change
between a privileged and non-privileged account.

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
| System owners are directed to define and enforce policies that restrict          |
| credentialed access to administrative accounts to only personnel whose roles     |
| require that access. System administrators should use the 'useradd' command to   |
| create non-privileged user accounts for use when performing non-privileged       |
| operations on the device.                                                        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-7--least-privilege---privileged-functions:

---------------------------------------------
3.1.7. Least Privilege - Privileged Functions
---------------------------------------------

#. Prevent non-privileged users from executing privileged functions.
#. Log the execution of privileged functions.

**DISCUSSION**

Privileged functions include establishing system accounts, performing
system integrity checks, conducting patching operations, or
administering cryptographic key management activities. Non-privileged
users do not possess appropriate authorizations. Circumventing intrusion
detection and prevention mechanisms or malicious code protection
mechanisms are examples of privileged functions that require protection
from non-privileged users. Note that this requirement represents a
condition to be achieved by the definition of authorized privileges in
3.1.2.

The misuse of privileged functions - whether intentionally or
unintentionally by authorized users or by unauthorized external entities
that have compromised system accounts - is a serious and ongoing concern
that can have significant adverse impacts on organizations. Logging the
use of privileged functions is one way to detect such misuse and
mitigate the risk from insider threats and advanced persistent threats.

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
| NILRT restricts privileged function execution to the 'root' maintenance account  |
| and members of the 'sudo' group. Privileged function execution is logged by the  |
| audit subsystem and the sudo service to '/var/log/audit/' and                    |
| '/var/log/auth.log' respectively. System owners are directed to enforce policies |
| whereby non-privileged actions are performed on less-privileged user accounts.   |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-8--unsuccessful-logon-attempts:

----------------------------------
3.1.8. Unsuccessful Logon Attempts
----------------------------------

Limit the number of consecutive invalid logon attempts by a user to
[*Assignment: organization-defined number*] in [*Assignment:
organization-defined time period*].

**DISCUSSION**

Due to the potential for denial of service, automatic system lockouts
are in most cases, temporary and automatically release after a
predetermined period established by the organization (i.e., using a
delay algorithm). Organizations may employ different delay algorithms
for different system components based on the capabilities of the
respective components. Responses to unsuccessful system logon attempts
may be implemented at the system and application levels.

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
| The SNAC configuration uses the PAM faillock module to lock user accounts after  |
| 3 authentication failures within a 15 minute time period.                        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-9--system-use-notification:

------------------------------
3.1.9. System Use Notification
------------------------------

Display system use notification message or banner to users before
granting access to the system that provides privacy and security notices
consistent with applicable CUI rules.

**DISCUSSION**

System use notifications can be implemented using messages or warning
banners that are displayed before individuals log in to the system.
System use notifications are used only for access via logon interfaces
with human users and are not required when human interfaces do not
exist. Based on a risk assessment, organizations consider whether a
secondary system use notification is needed to access applications or
other system resources after the initial network logon. Where necessary,
posters or other printed materials may be used in lieu of an automated
system banner. Organizations consult with the Office of General Counsel
for a legal review and approval of warning banner content.

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
| NILRT displays notification messages to the user prior to login via the 'issue'  |
| banner system. System owners are directed to prepare a compliant text banner     |
| that gives privacy and security notice to users, and to insert that banner       |
| message into the \`/etc/issue\` and \`/etc/issue.net\` files.                    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-10--device-lock:

-------------------
3.1.10. Device Lock
-------------------

#. Prevent access to the system by [*Selection (one or more): initiating a device lock after* [*Assignment: organization-defined time period*]
   *of inactivity; requiring the user to initiate a device   lock before leaving the system unattended*].
#. Retain the device lock until the user reestablishes access using   established identification and authentication procedures.
#. Conceal, via the device lock, information previously visible on the   display with a publicly viewable image.

**DISCUSSION**

Device locks are temporary actions taken to prevent access to the system
when users depart from the immediate vicinity of the system but do not
want to log out because of the temporary nature of their absences.
Device locks can be implemented at the operating system or application
level. User-initiated device locking is behavior- or policy-based and
requires users to take physical action to initiate the device lock.
Device locks are not an acceptable substitute for logging out of the
system, such as when organizations require users to log out at the end
of workdays. Pattern-hiding displays can include static or dynamic
images, such as patterns used with screen savers, photographic images,
solid colors, a clock, a battery life indicator, or a blank screen with
the caveat that controlled unclassified information is not displayed.

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
| The SNAC configuration includes a terminal locking utility called vlock, which   |
| allows users to lock their terminal sessions by either calling it with the       |
| 'vlock' command. Users must resubmit their login credentials to unlock the       |
| screen. After 900 seconds of inactivity, the NILRT TMUX shell is configured to   |
| automatically lock the console. Note that vlock cannot obscure terminal history  |
| in remote SSH clients; organization clients should be configured to not retain   |
| history.                                                                         |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-11--session-termination:

---------------------------
3.1.11. Session Termination
---------------------------

Terminate a user session automatically after [*Assignment:
organization-defined conditions or trigger events*].

**DISCUSSION**

This requirement addresses the termination of user-initiated logical
sessions in contrast to the termination of network connections that are
associated with communications sessions (i.e., disconnecting from the
network) in 3.13.9. A logical session is initiated whenever a user (or
process acting on behalf of a user) accesses a system. Such sessions can
be terminated (and terminate user access) without terminating network
sessions. Session termination terminates all processes associated with a
user's logical session except those processes that are specifically
created by the user (i.e., session owner) to continue after the session
is terminated. Conditions or trigger events that require automatic
session termination can include organization-defined periods of user
inactivity, time-of-day restrictions on system use, and targeted
responses to certain types of incidents.

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
| Interactive user sessions are automatically terminated after 600 seconds of      |
| inactivity, via the TMOUT environment variable. Users are required to re-enter   |
| their credentials to regain access to a login session. This value is adjustable  |
| by modifying the '/etc/ profile.d/tmout.conf' file.                              |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-12--remote-access:

---------------------
3.1.12. Remote Access
---------------------

#. Establish, authorize, and document usage restrictions,   configurations, and connections allowed for each type of permitted   remote access.
#. Monitor and control remote access methods.
#. Route remote access to the system through managed access control   points.
#. Authorize remote execution of privileged commands and remote access   to security-relevant information.
#. Implement cryptographic mechanisms to protect the confidentiality   of remote access sessions.

**DISCUSSION**

Remote access to the system represents a significant potential
vulnerability that can be exploited by adversaries. Monitoring and
controlling remote access methods allows organizations to detect attacks
and help ensure compliance with remote access policies. This occurs by
auditing the connection activities of remote users on a variety of
systems, including servers, notebook computers, workstations, smart
phones, and tablets. Routing remote access through managed access
control points enhances explicit control over such connections. It also
reduces the susceptibility to unauthorized access to the system which
could result in the unauthorized disclosure of CUI.

Restricting the execution of privileged commands and access to
security-relevant information via remote access reduces the exposure of
the organization and its susceptibility to threats by adversaries. A
privileged command is a human-initiated command executed on a system
that involves the control, monitoring, or administration of the system,
including security functions and security-relevant information.
Security-relevant information is information that can potentially impact
the operation of security functions or the provision of security
services in a manner that could result in failure to enforce the system
security policy or maintain isolation of code and data. Privileged
commands give individuals the ability to execute sensitive,
security-critical, or security-relevant system functions. Controlling
access from remote locations helps to ensure that unauthorized
individuals are not able to execute such commands with the potential to
do serious or catastrophic damage to the system.

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
| The NILRT+SNAC configuration does not support device configuration or            |
| communication through extra-organizational networks.                             |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| System owners are directed to only use NILRT systems on networks which are       |
| logically segregated from external networks by dedicated network hardware.       |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-13--withdrawn--incorporated-into-3-1-12-:

--------------------------------------------
3.1.13. Withdrawn: Incorporated into 3.1.12.
--------------------------------------------

.. raw:: latex

    \newpage


.. _withdrawn-incorporated-into-3.1.12.-1:


.. _3-1-14--withdrawn--incorporated-into-3-1-12-:

--------------------------------------------
3.1.14. Withdrawn: Incorporated into 3.1.12.
--------------------------------------------

.. raw:: latex

    \newpage


.. _withdrawn-incorporated-into-3.1.12.-2:


.. _3-1-15--withdrawn--incorporated-into-3-1-12-:

--------------------------------------------
3.1.15. Withdrawn: Incorporated into 3.1.12.
--------------------------------------------

.. raw:: latex

    \newpage



.. _3-1-16--wireless-access:

-----------------------
3.1.16. Wireless Access
-----------------------

#. Establish configuration requirements, connection requirements, and   implementation guidance for wireless access to the system.
#. Authorize wireless access to the system prior to allowing such   connections.
#. Protect wireless access to the system using authentication and   encryption.
#. Disable, when not intended for use, wireless networking   capabilities embedded within the system prior to issuance and   deployment.

**DISCUSSION**

Establishing usage restrictions, configuration requirements, and
connection requirements for wireless access to the system provides
criteria for organizations to support wireless access authorization
decisions. These restrictions and requirements help to reduce the
susceptibility to unauthorized system access through wireless
technologies. Wireless networks use authentication protocols that
provide credential protection and mutual authentication. Organizations
authenticate individuals and devices to protect wireless access to the
system. Special attention is given to the wide variety of devices that
are part of the Internet of Things with potential wireless access to the
system. Wireless networking capabilities that are embedded within system
components represent a significant potential vulnerability that can be
exploited by adversaries. Disabling wireless capabilities when not
needed for essential organizational missions or functions can reduce
susceptibility to threats by adversaries involving wireless
technologies.

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
| The NILRT+SNAC configuration does not support wireless interfaces. System owners |
| are directed not to attach wireless network adapters to a NILRT system as a part |
| of their design, nor to wirelessly bridge network communications to or from the  |
| NILRT system.                                                                    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-17--withdrawn--incorporated-into-3-1-16-:

--------------------------------------------
3.1.17. Withdrawn: Incorporated into 3.1.16.
--------------------------------------------

.. raw:: latex

    \newpage



.. _3-1-18--access-control-for-mobile-devices:

-----------------------------------------
3.1.18. Access Control for Mobile Devices
-----------------------------------------

#. Establish configuration requirements, connection requirements, and   implementation guidance for organization-controlled mobile devices.
#. Authorize the connection of mobile devices to the system.
#. Implement [*Selection: full-device encryption; container-based   encryption*] to protect the confidentiality of CUI on mobile devices.

**DISCUSSION**

A mobile device is a computing device that has a small form factor such
that it can easily be carried by a single individual; is designed to
operate without a physical connection; possesses local, non-removable or
removable data storage; and includes a self-contained power source.
Mobile device functionality may also include voice communication
capabilities, on-board sensors that allow the device to capture
information, and/or built-in features for synchronizing local data with
remote locations. Examples include smart phones and tablets. Mobile
devices are typically associated with a single individual. The
processing, storage, and transmission capability of mobile devices may
be comparable to or a subset of notebook/desktop systems, depending on
the nature and intended purpose of the device. The protection and
control of mobile devices is behavior- or policy-based and requires
users to take physical action to protect and control such devices when
outside of controlled areas. Controlled areas are spaces for which the
organization provides physical or procedural controls to meet the
requirements established for protecting CUI.

Due to the large variety of mobile devices with different
characteristics and capabilities, organizational restrictions may vary
for the different classes or types of such devices. Usage restrictions
and specific implementation guidance for mobile devices include
configuration management, device identification and authentication,
implementation of mandatory protective software, scanning devices for
malicious code, updating virus protection software, scanning for
critical software updates and patches, conducting primary operating
system (and possibly other resident software) integrity checks, and
disabling unnecessary hardware.

Organizations can employ full-device encryption or container-based
encryption to protect the confidentiality of CUI on mobile devices and
computing platforms. Container-based encryption provides a fine-grained
approach to the encryption of data and information, including encrypting
selected data structures such as files, records, or fields.

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
| The NILRT+SNAC configuration does not support connection to mobile devices.      |
| System owners are directed to enforce policies against connecting to a NILRT     |
| system from a mobile device.                                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-19--withdrawn--incorporated-into-3-1-18--451:

------------------------------------------------
3.1.19. Withdrawn: Incorporated into 3.1.18. 451
------------------------------------------------

.. raw:: latex

    \newpage



.. _3-1-20--use-of-external-systems:

-------------------------------
3.1.20. Use of External Systems
-------------------------------

a. [*Selection (one or more): Establish* [*Assignment:
organization-defined terms and conditions*]\ *; Identify* [*Assignment:
organization-defined controls asserted to be implemented on external
systems*]], consistent with the trust relationships established with
other organizations owning, operating, and/or maintaining external
systems, allowing authorized individuals to:

#. Access the system from external systems; and
#. Process, store, or transmit CUI using external systems; or

b. Prohibit the use of [*Assignment: organizationally-defined types of
external systems*].

**DISCUSSION**

External systems are systems that are used by but are not part of the
organizational system and for which the organization has no direct
control over the implementation of required controls or the assessment
of control effectiveness. External systems include personally owned
systems, system components, or devices; privately owned computing and
communication devices in commercial or public facilities; systems owned
or controlled by nonfederal organizations; and systems managed by
contractors. Organizations have the option to prohibit the use of any
type of external system or specified types of external systems, (e.g.,
prohibit the use of any external system that is not organizationally
owned or prohibit the use of personally owned systems).

Authorized individuals include organizational personnel, contractors, or
other individuals with authorized access to the organizational system
and over whom organizations have the authority to impose specific rules
of behavior regarding system access. Restrictions that organizations
impose on authorized individuals need not be uniform, as the
restrictions may vary depending on the trust relationships between
organizations.

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
| The NILRT+SNAC configuration does not support communications with                |
| extra-organizational devices. System Owners are directed to enforce policies     |
| against connecting to NILRT systems using personal devices and connecting        |
| personal storage devices to NILRT systems.                                       |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-21--external-systems---limits-and-restrictions-on-authorized-use:

--------------------------------------------------------------------
3.1.21. External Systems - Limits and Restrictions on Authorized Use
--------------------------------------------------------------------

#. Permit authorized individuals to use an external system to access the
system or to process, store, or transmit CUI only after:

   #. Implemented controls on the external system as specified in the organization’s security policies and security plans are verified; or
   #. Approved system connection or processing agreements with the organizational entity hosting the external system are retained.

#. Restrict the use of organization-controlled portable storage devices
   by authorized individuals on external systems as follows: [*Assignment:
   organization-defined usage restrictions*].

**DISCUSSION**

Limiting authorized use recognizes circumstances in which individuals
who use external systems may need to access the organizational system.
Organizations need assurance that the external systems contain the
necessary controls so as not to compromise, damage, or otherwise harm
the system. Verification that the required controls have been
implemented can be achieved through independent assessments,
attestations, or other means, depending on the confidence level required
by the organization. Limits on the use of organization-controlled
portable storage devices in external systems include restrictions on how
the devices may be used and under what conditions.

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
| The NILRT+SNAC configuration does not support communications with                |
| extra-organizational devices. System Owners are directed to enforce policies     |
| against connecting to NILRT systems using personal devices and connecting        |
| personal storage devices to NILRT systems                                        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-1-22--publicly-accessible-content:

-----------------------------------
3.1.22. Publicly Accessible Content
-----------------------------------

#. Train authorized individuals to ensure that publicly accessible information does not contain CUI.
#. Review the content on publicly accessible systems for CUI [*Assignment: organization-defined frequency*]
   and remove such information, if discovered.

**DISCUSSION**

In accordance with applicable laws, Executive Orders, directives,
policies, regulations, standards, and guidelines, the public is not
authorized to have access to nonpublic information, including CUI.

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
| NI LinuxRT does not publish CUI data by default. Integrating organizations       |
| should develop their own policies and training for handling publicly-accessible  |
| CUI data.                                                                        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

