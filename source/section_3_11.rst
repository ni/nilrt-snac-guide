
.. _3-11--risk-assessment:

=====================
3.11. Risk Assessment
=====================

.. _risk-assessment-1:


.. _3-11-1--risk-assessment:

-----------------------
3.11.1. Risk Assessment
-----------------------

#. Assess the risk (including supply chain risk) of unauthorized   disclosure resulting from the processing, storage, or transmission of   CUI.
#. Update risk assessments (including supply chain risk) [*Assignment:   organization-defined frequency*].

**DISCUSSION**

Clearly defined system boundaries are a prerequisite for effective risk
assessments. Risk assessments consider threats, vulnerabilities,
likelihood, and impact to organizational operations and assets based on
the operation and use of the system. Risk assessments also consider risk
from external parties (e.g., service providers, contractors operating
systems on behalf of the organization, individuals accessing systems,
outsourcing entities). Risk assessments, either formal or informal, can
be conducted at the organization level, the mission or business process
level, or the system level and at any phase in the system development
life cycle.

Risk assessments include supply chain-related risks associated with
suppliers or contractors and the system, system component, or system
service that they provide. Supply chain events that affect risk include
disruption, the use of defective components, the insertion of
counterfeits, theft, malicious development practices, improper delivery
practices, and the insertion of malicious code. These events can have a
significant impact on the system and its information and, therefore, can
also adversely impact organizations. The supply chain events may be
unintentional or malicious and can occur at any point in the system life
cycle.

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
| The system owner is responsible to assess the risk associated with each device   |
| and component in the system.                                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-11-2--vulnerability-monitoring-and-scanning:

---------------------------------------------
3.11.2. Vulnerability Monitoring and Scanning
---------------------------------------------

#. Monitor and scan for vulnerabilities in the system [*Assignment:   organization-defined frequency*] and when new vulnerabilities   affecting the system are identified.
#. Remediate vulnerabilities [*Assignment: organization-defined   response times*] in accordance with an organizational assessment of   risk.
#. Update vulnerabilities to be scanned [*Assignment:   organization-defined frequency*].
#. Implement privileged access authorization to the system for   vulnerability scanning activities.

**DISCUSSION**

Organizations determine the required vulnerability scanning for system
components (including hardware, software, firmware, and applications)
and ensure that potential sources of vulnerabilities (e.g., networked
printers, scanners, and copiers) are not overlooked. The vulnerabilities
to be scanned are readily updated as new vulnerabilities are discovered
and announced and new scanning methods are developed. This process
ensures that potential vulnerabilities in the system are identified and
addressed as quickly as possible.

Vulnerability analyses for custom software may require additional
approaches, such as static analysis, dynamic analysis, binary analysis,
or a hybrid of the three approaches. Organizations can employ these
analysis approaches in source code reviews and in a variety of tools
(e.g., static analysis tools, web-based application scanners, binary
analyzers). Vulnerability scanning includes scanning for patch levels;
scanning for functions, ports, protocols, and services that should not
be accessible to users or devices; and scanning for improperly
configured or incorrectly operating information flow control mechanisms.

To facilitate interoperability, organizations consider using products
that are Security Content Automated Protocol (SCAP)-validated, as well
as scanning tools that express vulnerabilities in the Common
Vulnerabilities and Exposures (CVE) naming convention and that employ
the Open Vulnerability Assessment Language (OVAL) to determine the
presence of system vulnerabilities. Sources for vulnerability
information include the Common Weakness Enumeration (CWE) listing and
the National Vulnerability Database (NVD).

Security assessments, such as red team exercises, provide additional
sources of potential vulnerabilities for which to scan. Organizations
also consider using scanning tools that express vulnerability impact by
the Common Vulnerability Scoring System (CVSS). In certain situations,
the nature of the vulnerability scanning may be more intrusive, or the
system component that is the subject of the scanning may contain highly
sensitive information. Privileged access authorization to selected
system components facilitates thorough vulnerability scanning and
protects the sensitive nature of such scanning.

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
| The system owner is responsible to perform vulnerability scan on the deployed    |
| system, as vulnerabilities depend on the full system configuration.              |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| NI performs regular vulnerability scans of products prior to release to the      |
| customer.                                                                        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-11-3--withdrawn--incorporated-into-3-11-2-:

--------------------------------------------
3.11.3. Withdrawn: Incorporated into 3.11.2.
--------------------------------------------

.. raw:: latex

    \newpage



.. _3-11-4--risk-response:

---------------------
3.11.4. Risk Response
---------------------

Respond to findings from security assessments, monitoring, and audits.

**DISCUSSION**

Organizations have many options for responding to risk, including
mitigating risk by implementing new controls or strengthening existing
controls, accepting risk with appropriate justification or rationale,
sharing or transferring risk, or avoiding risk. The organizational risk
management strategy and risk tolerance influence risk response decisions
and actions. This requirement addresses the need to determine an
appropriate response to risk before generating a plan of action and
milestones entry. For example, the response may be to accept risk or
reject risk, or it may be possible to mitigate the risk immediately so
that a plan of action and milestones entry is not needed. However, if
the risk response is to mitigate the risk, and the mitigation cannot be
completed immediately, a plan of action and milestones entry is
generated.

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
| The system owner is responsible to respond to system issues discovered on the    |
| system.                                                                          |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| If a vulnerability is discovered related to the NILRT system, report the issue   |
| to security@ni.com.                                                              |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

