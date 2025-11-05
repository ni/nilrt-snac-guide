
.. _3-14--system-and-information-integrity:

======================================
3.14. System and Information Integrity
======================================


.. _3-14-1--flaw-remediation:

------------------------
3.14.1. Flaw Remediation
------------------------

#. Identify, report, and correct system flaws.
#. Test software and firmware updates related to flaw remediation for   effectiveness and potential side effects before installation.
#. Install security-relevant software and firmware updates within   [*Assignment: organization-defined time period*] of the release of the   updates.

**DISCUSSION**

Organizations identify systems that are affected by announced software
and firmware flaws, including potential vulnerabilities that result from
those flaws, and report this information to designated personnel with
information security responsibilities. Security-relevant updates include
patches, service packs, hot fixes, and anti-virus signatures.
Organizations address the flaws discovered during security assessments,
continuous monitoring, incident response activities, and system error
handling. Organizations can take advantage of available resources, such
as the Common Weakness Enumeration (CWE) or Common Vulnerabilities and
Exposures (CVE) databases, in remediating the flaws discovered in
organizational systems. Organization-defined time periods for updating
security-relevant software and firmware may vary based on a variety of
factors, including the criticality of the update (i.e., severity of the
vulnerability related to the discovered flaw). Some types of flaw
remediation may require more testing than other types of remediation.

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
| System owners can report any system flaws related to NILRT to NI by emailing     |
| security@ni.com.                                                                 |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| NI tests NILRT prior to release to customers. System owners are responsible to   |
| test updates to NILRT components on the deployed system prior to installation of |
| updates, as some local configuration settings may have unintended effects.       |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| NI announces security updates and publishes updates to ni.com/security. The      |
| system owner is encouraged to enroll in the security notification system at that |
| site. The system owner is responsible to evaluate and install security updates   |
| in a timely manner.                                                              |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-14-2--malicious-code-protection:

---------------------------------
3.14.2. Malicious Code Protection
---------------------------------

#. Implement malicious code protection mechanisms at designated   locations within the system to detect and eradicate malicious code.
#. Update malicious code protection mechanisms as new releases are   available in accordance with organizational configuration management   policy and procedures.

**DISCUSSION**

Malicious code insertions occur through the exploitation of system
vulnerabilities. Periodic scans of the system and real-time scans of
files from external sources as files are downloaded, opened, or executed
can detect malicious code. Malicious code can be inserted into the
system in a variety of ways, including by electronic mail, the world
wide web, and portable storage devices. Malicious code includes viruses,
worms, Trojan horses, and spyware. Malicious code can be encoded in
various formats, contained in compressed or hidden files, or hidden in
files using techniques such as steganography. In addition to the above
technologies, pervasive configuration management, comprehensive software
integrity controls, and anti-exploitation software may be effective in
preventing the execution of unauthorized code. Malicious code may be
present in commercial off-the-shelf software as well as custom-built
software and could include logic bombs, backdoors, and other types of
attacks that could affect organizational mission and business functions.

In situations where malicious code cannot be detected by detection
methods or technologies, organizations rely on other types of controls -
including secure coding practices, configuration management and control,
trusted procurement processes, and monitoring practices - to ensure that
software does not perform functions other than the functions intended.
Organizations may determine that different actions are warranted in
response to the detection of malicious code. For example, organizations
can define actions in response to malicious code detection during scans,
the detection of malicious downloads, or the detection of maliciousness
when attempting to open or execute files.

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
| NILRT provides ClamAV as the malicious code scanning solution. It is the         |
| responsibility of the system owner to configure and use ClamAV to scan for       |
| malicious code.                                                                  |
| For details on configuring and using ClamAV, refer to the                        |
| :ref:`Appendix 5 <appendix-5>`                                                   |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-14-3--security-alerts--advisories--and-directives:

---------------------------------------------------
3.14.3. Security Alerts, Advisories, and Directives
---------------------------------------------------

#. Receive security alerts, advisories, and directives from external   organizations.
#. Generate internal security alerts, advisories, and directives, as   necessary.

**DISCUSSION**

There are many publicly available sources of system security alerts and
advisories. For example, the Department of Homeland Security's
Cybersecurity and Infrastructure Security Agency (CISA) generates
security alerts and advisories to maintain situational awareness across
the Federal Government and in nonfederal organizations. Software
vendors, subscription services, and industry Information Sharing and
Analysis Centers (ISACs) may also provide security alerts and
advisories. Compliance with security directives is essential due to the
critical nature of many of these directives and the potential immediate
adverse effects on organizational operations and assets, individuals,
other organizations, and the Nation should the directives not be
implemented in a timely manner. Examples of response actions include
notifying relevant external organizations, such as external mission and
business partners, supply chain partners, service providers, and peer or
supporting organizations.

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
| NI monitors major security alert systems and reacts to relevant alerts.          |
| Notifications that are relevant to NILRT will be published through the security  |
| update system.                                                                   |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| NI announces security updates and publishes updates to ni.com/security. The      |
| system owner is responsible to enroll in the security notification system at     |
| that site and to enroll in public notification systems for monitoring.           |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-14-4--withdrawn--incorporated-into-3-14-2:

-------------------------------------------
3.14.4. Withdrawn: Incorporated into 3.14.2
-------------------------------------------

.. raw:: latex

    \newpage



.. _3-14-5--withdrawn--addressed-by-3-14-2-:

---------------------------------------
3.14.5. Withdrawn: Addressed by 3.14.2.
---------------------------------------

.. raw:: latex

    \newpage



.. _3-14-6--system-monitoring:

-------------------------
3.14.6. System Monitoring
-------------------------

#. Monitor the system, including inbound and outbound communications
   traffic, to detect:

   #. Attacks and indicators of potential attacks;
   #. Unusual or unauthorized activities or conditions; and
   #. Unauthorized connections.

#. Identify unauthorized use of the system.

**DISCUSSION**

System monitoring involves external and internal monitoring. External
monitoring includes the observation of events that occur at the system
boundary, while internal monitoring includes the observation of events
that occur within the system. Organizations can monitor the system, for
example, by observing audit record activities in real time or by
observing other system aspects, such as access patterns, characteristics
of access, and other actions. The monitoring objectives may guide
determination of the events.

A system monitoring capability is achieved through a variety of tools
and techniques (e.g., audit record monitoring software, intrusion
detection systems, intrusion prevention systems, malicious code
protection software, scanning tools, network monitoring software).
Strategic locations for monitoring devices include selected perimeter
locations and near server farms that support critical applications with
such devices being employed at managed system interfaces. The
granularity of monitoring the information collected is based on
organizational monitoring objectives and the capability of the system to
support such objectives.

System monitoring is an integral part of continuous monitoring and
incident response programs. The output from system monitoring serves as
input to continuous monitoring and incident response programs. A network
connection is any connection with a device that communicates through a
network (e.g., local area network, internet). A remote connection is any
connection with a device that communicates through an external network
(e.g., the internet). Local, network, and remote connections can be
either wired or wireless.

Unusual or unauthorized activities or conditions related to inbound and
outbound communications traffic include internal traffic that indicates
the presence of malicious code in the system or propagating among system
components, the unauthorized export of information, or signaling to
external systems. Evidence of malicious code is used to identify a
potentially compromised system. System monitoring requirements,
including the need for types of system monitoring, may be referenced in
other requirements.

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
| System monitoring should happen at the system level and is the responsibility of |
| the system owner.                                                                |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-14-7--withdrawn--incorporated-into-3-14-6-:

--------------------------------------------
3.14.7. Withdrawn: Incorporated into 3.14.6.
--------------------------------------------

.. raw:: latex

    \newpage



.. _3-14-8--information-management-and-retention:

--------------------------------------------
3.14.8. Information Management and Retention
--------------------------------------------

Manage and retain CUI within the system and CUI output from the system
in accordance with applicable laws, Executive Orders, directives,
regulations, policies, standards, guidelines, and operational
requirements.

**DISCUSSION**

Federal agencies consider data retention requirements for nonfederal
organizations. Retaining CUI on nonfederal systems after contracts or
agreements have concluded increases the attack surface for those systems
and the risk of the information being compromised. NARA provides federal
policy and guidance on records retention and schedules.

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
| The system owner is responsible for understanding and cooperating with           |
| applicable regulations concerning CUI data retention.                            |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

