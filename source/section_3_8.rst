
.. _3-8--media-protection:

=====================
3.8. Media Protection
=====================


.. _3-8-1--media-storage:

--------------------
3.8.1. Media Storage
--------------------

Physically control and securely store digital and non-digital media
containing CUI until the media are destroyed or sanitized using approved
equipment, techniques, and procedures.

**DISCUSSION**

Digital media includes diskettes, flash drives, magnetic tapes, external
or removable solid state or magnetic drives, compact discs, and digital
versatile discs. Non-digital media includes paper and microfilm.
Physically controlling stored media includes conducting inventories,
establishing procedures to allow individuals to check out and return
media to libraries, and maintaining accountability for stored media.
Secure storage includes a locked drawer, desk, or cabinet or a
controlled media library. Controlled areas provide physical and
procedural controls to meet the requirements established for protecting
information and systems.

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
| NILRT runs on devices with local memory. Letters of Volatility are available     |
| from NI for these devices including clearing information for these memory        |
| locations. The system owner is responsible to sanitize data from these devices.  |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| NILRT devices have USB ports. It is the responsibility of the system owner to    |
| manage access to these ports, either physically or logically.                    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-8-2--media-access:

-------------------
3.8.2. Media Access
-------------------

Restrict access to CUI on digital and non-digital media to [*Assignment:
organization-defined personnel or roles*].

**DISCUSSION**

Access to CUI on system media can be restricted by physically
controlling such media, which includes conducting inventories, ensuring
that procedures are in place to allow individuals to check out and
return media to the media library, and maintaining accountability for
stored media.

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
| NILRT devices have USB ports. It is the responsibility of the system owner to    |
| manage access to these ports, either physically or logically.                    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-8-3--media-sanitization:

-------------------------
3.8.3. Media Sanitization
-------------------------

Sanitize system media containing CUI prior to maintenance, disposal,
release out of organizational control, or release for reuse.

**DISCUSSION**

Media sanitization applies to all digital and non-digital system media
subject to disposal or reuse, whether or not the media is considered
removable. Examples include digital media in scanners, copiers,
printers, notebook computers, workstations, mobile devices, network
components, and non-digital media. The sanitization process removes CUI
from system media such that the information cannot be retrieved or
reconstructed. Sanitization techniques (e.g., clearing, purging,
cryptographically erasing, and destroying) prevent the disclosure of
information to unauthorized individuals when such media is reused or
released for disposal. Organizations determine the appropriate
sanitization methods with the recognition that destruction is sometimes
necessary when other methods cannot be applied to media that require
sanitization. NARA policies control the sanitization process for CUI.

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
| NILRT runs on devices with local memory. Letters of Volatility are available     |
| from NI for these devices including clearing information for these memory        |
| locations. The system owner is responsible to sanitize data from these devices.  |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| NI LOVs are located here: https://ni.com/ letters-of-volatility                  |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-8-4--media-marking:

--------------------
3.8.4. Media Marking
--------------------

#. Mark system media containing CUI indicating distribution   limitations, handling caveats, and security markings.
#. Exempt [*Assignment: organization-defined types of system media   containing CUI*] from marking if the media remain within [*Assignment:   organization-defined controlled areas*].

**DISCUSSION**

Security marking refers to the application or use of human-readable
security attributes. Security labeling refers to the use of security
attributes for internal system data structures. Digital media includes
diskettes, magnetic tapes, external or removable solid state or magnetic
drives, flash drives, compact discs, and digital versatile discs.
Non-digital media includes paper and microfilm. CUI is defined by NARA
along with appropriate safeguarding and dissemination requirements for
such information.

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
| It is the responsibility of the system owner to create a plan for marking and    |
| managing media near the system.                                                  |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-8-5--media-transport:

----------------------
3.8.5. Media Transport
----------------------

#. Protect, control, and maintain accountability for system media   containing CUI and during transport outside of controlled areas.
#. Implement cryptographic mechanisms to prevent the unauthorized   disclosure of CUI stored on digital media during transport.

**DISCUSSION**

System media includes digital and non-digital media. Digital media
includes flash drives, diskettes, magnetic tapes, external or removable
solid state or magnetic drives, compact discs, and digital versatile
discs. Non-digital media includes microfilm and paper. Controlled areas
are spaces for which organizations provide physical or procedural
controls to meet the requirements established for protecting information
and systems. Controls to protect media during transport include
cryptography and locked containers. Cryptographic mechanisms can provide
confidentiality protections, depending on the mechanisms implemented.
Activities associated with media transport include releasing media for
transport, ensuring that media enters the appropriate transport
processes, and the actual transport. Authorized transport and courier
personnel may include individuals external to the organization.
Maintaining accountability of system media during transport includes
restricting transport activities to authorized personnel and tracking or
obtaining records of transport activities as the media moves through the
transportation system to prevent and detect loss, destruction, or
tampering.

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
| It is the responsibility of the system owner to create a plan for the transport  |
| of data from the system.                                                         |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-8-6--withdrawn--incorporated-into-3-8-5-:

------------------------------------------
3.8.6. Withdrawn: Incorporated into 3.8.5.
------------------------------------------

.. raw:: latex

    \newpage



.. _3-8-7--media-use:

----------------
3.8.7. Media Use
----------------

#. [*Selection: Restrict; Prohibit*] the use of [*Assignment:   organization-defined removable system media*].
#. Prohibit the use of portable storage devices when such devices have   no identifiable owner.

**DISCUSSION**

In contrast to requirement 3.8.1, which restricts user access to media,
this requirement restricts the use of certain types of media on systems,
such as restricting or prohibiting the use of flash drives or external
hard drives. Organizations can employ technical and nontechnical
controls (e.g., policies, procedures, and rules of behavior) to control
the use of system media. For example, organizations may control the use
of portable storage devices by using physical cages on workstations to
prohibit access to external ports or disabling or removing the ability
to insert, read, or write to devices.

Organizations may limit the use of portable storage devices to only
approved devices, including devices provided by the organization,
devices provided by other approved organizations, and devices that are
not personally owned. Finally, organizations may control the use of
portable storage devices based on the type of device - prohibiting the
use of writeable, portable devices -and implement this restriction by
disabling or removing the capability to write to such devices. Requiring
identifiable owners (e.g., individuals, organizations, or projects) for
portable storage devices reduces the risk of using such technologies by
allowing organizations to assign responsibility and accountability for
addressing known vulnerabilities in the devices (e.g., insertion of
malicious code).

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
| It is the responsibility of the system owner to create a plan for managing media |
| used with the system.                                                            |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-8-8--withdrawn--incorporated-into-3-8-7-:

------------------------------------------
3.8.8. Withdrawn: Incorporated into 3.8.7.
------------------------------------------

.. raw:: latex

    \newpage



.. _3-8-9--system-backup---cryptographic-protection:

-----------------------------------------------
3.8.9. System Backup - Cryptographic Protection
-----------------------------------------------

Implement cryptographic mechanisms to prevent the unauthorized
disclosure of CUI at backup storage locations.

**DISCUSSION**

Organizations can employ cryptographic mechanisms or alternative
physical controls to protect the confidentiality of backup information
at designated storage locations. Backed-up information that contains CUI
may include system-level information and user-level information.
System-level information includes system-state information, operating
system software, application software, and licenses. User-level
information includes information other than system-level information.

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
| NILRT systems do not backup data to additional storage locations. The system     |
| owner is responsible to set up any backup storage and to ensure proper           |
| encryption in those storage locations.                                           |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

