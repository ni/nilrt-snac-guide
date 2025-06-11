
.. _3-5--identification-and-authentication:

======================================
3.5. Identification and Authentication
======================================


.. _3-5-1--user-identification--authentication--and-re-authentication:

-----------------------------------------------------------------
3.5.1. User Identification, Authentication, and Re-Authentication
-----------------------------------------------------------------

#. Uniquely identify and authenticate system user, and associate that   unique identification with processes acting on behalf of those users.
#. Re-authenticate users when [*Assignment: organization-defined   circumstances or situations requiring re-authentication*].

**DISCUSSION**

System users include employees or individuals who have equivalent status
to employees. Typically, individual identifiers are the usernames
associated with the system accounts assigned to those individuals. Since
processes execute on behalf of groups and roles, organizations may
require the unique identification of individuals in group accounts or
accountability of individual activity. The unique identification and
authentication of users applies to all system accesses. Organizations
employ passwords, physical authenticators, biometrics or some
combination thereof, to authenticate user identities. Organizations may
require the re-authentication of individuals in certain situations,
including when roles, authenticators, or credentials change; when the
execution of privileged functions occurs; after a fixed time period; or
periodically.

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
| NI Linux RT runs software including LabVIEW RT on fixed system accounts and does |
| not support integration with external authentication solutions.                  |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-5-2--device-identification-and-authentication:

-----------------------------------------------
3.5.2. Device Identification and Authentication
-----------------------------------------------

Uniquely identify and authenticate [*Assignment: organization-defined
devices and/or types of devices*] before establishing a system or
network connection.

**DISCUSSION**

Devices that require unique device-to-device identification and
authentication are defined by type, device, or a combination of type and
device. Organization-defined device types include devices that are not
owned by the organization. Systems use shared known information (e.g.,
Media Access Control [MAC], Transmission Control Protocol/Internet
Protocol [TCP/IP] addresses) for device identification or organizational
authentication solutions (e.g., Institute of Electrical and Electronics
Engineers [IEEE] 802.1x and Extensible Authentication Protocol [EAP],
RADIUS server with EAP-Transport Layer Security [TLS] authentication,
Kerberos) to identify and authenticate devices on local and wide area
networks.

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
| NILRT supports 802.1X authentication on the network. Refer to the nilrt-docs     |
| `documentation <https://nilrt-docs.ni.com/eapol/eapol.html>`__ at                |
| *nilrt-docs.ni.com* for tutorials on how to configure an NILRT device to         |
| authenticate to an 802.1X-enabled network. The system owner can use this         |
| solution to identify and authenticate NILRT devices before establishing          |
| a network connection.                                                            |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-5-3--multi-factor-authentication:

----------------------------------
3.5.3. Multi-Factor Authentication
----------------------------------

Implement multi-factor authentication for access to system accounts.

**DISCUSSION**

Multi-factor authentication requires the use of two or more different
factors to achieve authentication. The authentication factors are
defined as follows: something you know (e.g., a personal identification
number [PIN]), something you have (e.g., a physical authenticator, such
as a cryptographic private key), or something you are (e.g., a
biometric). Multi-factor authentication solutions that feature physical
authenticators include hardware authenticators that provide time-based
or challenge-response outputs and smart cards. In addition to
authenticating users at the system level, organizations may also employ
authentication mechanisms at the application level to provide increased
information security.

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
| The SNAC configuration uses the PAM-based Linux authentication framework to      |
| authentication system access and enforce access control policies, but it does    |
| not include a Multi-factor Authentication schema by default. System owners are   |
| directed to consider PAM-compatible MFA implementations that may be appropriate  |
| for the system's operating environment, and to implement those solutions.        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-5-4--replay-resistant-authentication:

--------------------------------------
3.5.4. Replay-Resistant Authentication
--------------------------------------

Implement replay-resistant authentication mechanisms for access to
system accounts.

**DISCUSSION**

Authentication processes resist replay attacks if it is impractical to
successfully authenticate by recording or replaying previous
authentication messages. Replay-resistant techniques include protocols
that use nonces or challenges, such as time synchronous or
challenge-response one-time authenticators.

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
| NILRT does not provide protection from replay attacks. The system owner must     |
| provide protection from these attacks.                                           |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-5-5--identifier-management:

----------------------------
3.5.5. Identifier Management
----------------------------

#. Receive authorization from [*Assignment: organization-defined   personnel or roles*] to
   assign an individual, group, role, service, or   device identifier.
#. Select and assign an identifier that identifies an individual,   group, role, service, or device.
#. Prevent reuse of identifiers for [*Assignment: organization-defined   time period*].
#. Identify the status of each individual with the following   characteristic: [*Assignment: organization-defined characteristic*].

**DISCUSSION**

Identifiers are provided for users, processes acting on behalf of users,
and devices. Preventing the reuse of identifiers implies preventing the
assignment of previously used individual, group, role, service, or
device identifiers to different individuals, groups, roles, services, or
devices. Characteristics that identify the status of individuals include
contractors, foreign nationals, and non-organizational users.
Identifying the status of individuals by these characteristics provides
useful information about the people with whom organizational personnel
are communicating. For example, it might be useful for an employee to
know that one of the individuals on an email message is a contractor.

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
| Device identification controls are defined at the organization level;            |
| individualized users (when they exist) must be managed manually.                 |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-5-6--withdrawn-:

-----------------
3.5.6. Withdrawn.
-----------------

.. raw:: latex

    \newpage



.. _3-5-7--password-management:

--------------------------
3.5.7. Password Management
--------------------------

#. Enforce the following password composition and complexity rules:   [*Assignment: organization-defined composition and complexity rules*].
#. Allow user selection of long passwords and passphrases, including   spaces and all printable characters.
#. Verify, when users create or update passwords, that the passwords   are not found on the list of | commonly-used, expected, or compromised passwords.
#. Transmit passwords only over cryptographically-protected channels.
#. Store passwords using an approved salted key derivation function,   preferably using a keyed hash.
#. Select a new password immediately upon account recovery.
#. Allow the use of a temporary password for system logons with an   immediate change to a permanent password.

**DISCUSSION**

Password-based authentication applies to passwords used in single-factor
or multi-factor authentication. Long passwords or passphrases are
preferable over shorter passwords. Enforced composition rules provide
marginal security benefits while decreasing usability. However,
organizations may choose to establish certain rules for password
generation (e.g., minimum character length) under certain circumstances
and can enforce this requirement. For example, account recovery can
occur when a password is forgotten. Cryptographically protected
passwords include salted one-way cryptographic hashes of passwords. The
list of commonly used, compromised, or expected passwords includes
passwords obtained from previous breach corpuses, dictionary words, and
repetitive or sequential characters. The list includes context-specific
words, such as the name of the service, username, and derivatives
thereof. Changing temporary passwords to permanent passwords immediately
after system logon ensures that the necessary strength of the
authentication mechanism is implemented at the earliest opportunity and
reduces the susceptibility to authenticator compromises.

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
| The NILRT+SNAC configuration uses the PAM pwquality module to enforce password   |
| quality limitations. The PWQuality configuration is defined and configurable via |
| the '/etc/sec urity/pwquality.conf' file. Passwords are also checked against a   |
| dictionary of common words, and agains the cracklib compromised password         |
| database. Password quality limitations are not enforced for the 'root' account.  |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| Passwords are stored internally in a hashed form, controlled by PAM.             |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| System administrators can reset user passwords using the 'passwd' utility and    |
| set the password lifetime to expire immediately, forcing users to enter a new    |
| password after logging in with a temporary password.                             |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage


.. _withdrawn.-1:


.. _3-5-8--withdrawn-:

-----------------
3.5.8. Withdrawn.
-----------------

.. raw:: latex

    \newpage



.. _3-5-9--withdrawn--incorporated-into-3-5-7-:

------------------------------------------
3.5.9. Withdrawn: Incorporated into 3.5.7.
------------------------------------------

.. raw:: latex

    \newpage


.. _withdrawn-incorporated-into-3.5.7.-1:


.. _3-5-10--withdrawn--incorporated-into-3-5-7-:

-------------------------------------------
3.5.10. Withdrawn: Incorporated into 3.5.7.
-------------------------------------------

.. raw:: latex

    \newpage



.. _3-5-11--authentication-feedback:

-------------------------------
3.5.11. Authentication Feedback
-------------------------------

Obscure feedback of authentication information.

**DISCUSSION**

The feedback from systems does not provide information that would allow
unauthorized individuals to compromise authentication mechanisms. For
example, for desktop or notebook computers with relatively large
monitors, the threat may be significant (often referred to as shoulder
surfing). For mobile devices with small displays, this threat may be
less significant and is balanced against the increased likelihood of
input errors due to small keyboards. Therefore, the means for obscuring
the authenticator feedback is selected accordingly. Obscuring
authenticator feedback includes displaying asterisks when users type
passwords into input devices or displaying feedback for a limited time
before fully obscuring it.

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
| All password handling tools installed with NILRT + SNAC obscure passwords during |
| entry.                                                                           |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-5-12--authenticator-management:

--------------------------------
3.5.12. Authenticator Management
--------------------------------

#. Establish initial authenticator content for any authenticators   issued by the organization.
#. Verify the identity of the individual, group, role, service, or   device receiving the authenticator as part of the initial   authenticator distribution.
#. Establish and implement administrative procedures for initial   authenticator distribution, for lost, compromised, or damaged   authenticators, and for revoking authenticators.
#. Protect authenticator content from unauthorized disclosure and   modification.
#. Change default authenticators prior to first use.
#. Change or refresh authenticators [*Assignment: organization-defined   time period by authenticator type*] or when [*Assignment:   organization-defined events*].
#. Change authenticators for group or role accounts when membership to   those accounts change.

**DISCUSSION**

Authenticators include passwords, cryptographic devices, biometrics,
certificates, one-time password devices, and ID badges. The initial
authenticator content is the actual content of the authenticator (e.g.,
the initial password). In contrast, requirements for authenticator
content contain specific characteristics. Authenticator management is
supported by organization-defined settings and restrictions for various
authenticator characteristics (e.g., password complexity and composition
rules, validation time window for time synchronous one-time tokens, and
the number of allowed rejections during the verification stage of
biometric authentication).

The requirement to protect individual authenticators may be implemented
by 3.15.3 for authenticators in the possession of individuals and by
3.1.1, 3.1.2, 3.1.5, and 3.13.8 for authenticators stored in
organizational systems. This includes passwords stored in hashed or
encrypted formats or files that contain encrypted or hashed passwords
accessible with administrator privileges. Actions can be taken to
safeguard authenticators, including maintaining possession of
authenticators, not sharing authenticators with others, and immediately
reporting lost, stolen, or compromised authenticators. Developers may
deliver system components with factory default authentication
credentials to allow for initial installation and configuration. Default
authentication credentials are often well-known, easily discoverable,
and present a significant risk. Authenticator management includes
issuing and revoking authenticators for temporary access when no longer
needed.

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
| PAM natively supports password expiration and first-login password expiration;   |
| the remaining controls are organization-centric.                                 |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

