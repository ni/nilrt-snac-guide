
.. _3-16--system-and-services-acquisition:

=====================================
3.16. System and Services Acquisition
=====================================


.. _3-16-1--security-engineering-principles:

---------------------------------------
3.16.1. Security Engineering Principles
---------------------------------------

Apply systems security engineering principles in the specification,
design, development, implementation, and modification of the system and
system components.

**DISCUSSION**

Organizations apply systems security engineering principles to new
development systems or systems undergoing major upgrades. For legacy
systems, organizations apply systems security engineering principles to
system upgrades and modifications to the extent feasible, given the
current state of hardware, software, and firmware components within
those systems. The application of systems security engineering concepts
and principles helps to develop trustworthy, secure, and resilient
systems and reduce the susceptibility of organizations to disruptions,
hazards, and threats. Examples include developing layered protections;
establishing security policies, architecture, and controls as the
foundation for design; incorporating security requirements into the
system development life cycle; delineating physical and logical security
boundaries; ensuring that developers are trained on how to build
trustworthy secure software; and performing threat modeling to identify
use cases, threat agents, attack vectors and patterns, design patterns,
and compensating controls needed to mitigate risk. Organizations that
apply security engineering concepts and principles can facilitate the
development of trustworthy, secure systems, system components, and
system services; reduce risk to acceptable levels; and make informed
risk-management decisions.

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
| NI has adopted a Secure Development Lifecycle for software development,          |
| including the development of NILRT. The NI SDL was developed with input from     |
| Micosoft's Security Development Lifecycle and NIST Secure Software Development   |
| Framework. The NI SDL leverages additional material from OWASP and SAFECode. The |
| NI SDL overlays NI's hardware and software engineering processes. It includes    |
| practices related to:                                                            |
+----------------------------------------------------------------------------------+
| - Security Training                                                              |
+----------------------------------------------------------------------------------+
| - Threat Modeling                                                                |
+----------------------------------------------------------------------------------+
| - Penetration Testing                                                            |
+----------------------------------------------------------------------------------+
| - Using Approved Tools                                                           |
+----------------------------------------------------------------------------------+
| - Automated Security Scanning Tools                                              |
+----------------------------------------------------------------------------------+
| - Incident Response                                                              |
+----------------------------------------------------------------------------------+
| - Secure Policies                                                                |
+----------------------------------------------------------------------------------+
| - Managing Third-Party Components                                                |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| These practices are applied to the development of NILRT.                         |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-16-2--unsupported-system-components:

-------------------------------------
3.16.2. Unsupported System Components
-------------------------------------

#. Replace system components when support for the components is no   longer available from the developer, vendor, or manufacturer; or
#. Provide options for alternative sources for continued support for   unsupported components.

**DISCUSSION**

Support for system components includes software patches, firmware
updates, replacement parts, and maintenance contracts. An example of
unsupported components includes when vendors no longer provide critical
software patches or product updates, which can result in an opportunity
for adversaries to exploit weaknesses in the installed components.
Exceptions to replacing unsupported system components include systems
that provide critical mission or business capabilities where newer
technologies are not available or where the systems are so isolated that
installing replacement components is not an option.

Alternative sources for support address the need to provide continued
support for system components that are no longer supported by the
original manufacturers, developers, or vendors when such components
remain essential to organizational mission and business functions. If
necessary, organizations can establish in-house support by developing
customized patches for critical software components or, alternatively,
obtain the services of external providers who provide ongoing support
for the designated unsupported components through contractual
relationships. Such contractual relationships can include open-source
software value-added vendors. The increased risk of using unsupported
system components can be mitigated, for example, by prohibiting the
connection of such components to public or uncontrolled networks or
implementing other forms of isolation.

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
| NILRT uses third-party components, including open source components. These       |
| components are managed and tracked. With each release of a NILRT component,      |
| developers review the list of components for support.                            |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| When a component is identified to be out of support, the development team        |
| creates a plan to replace the component or to take over support of that          |
| component directly. The plan is approved by NI managers prior to release.        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-16-3--external-system-services:

--------------------------------
3.16.3. External System Services
--------------------------------

#. Require the providers of external system services to comply with   organizational security requirements, and implement the following   controls: [*Assignment: organization-defined controls*].
#. Define and document organizational oversight and user roles and   responsibilities with regard to external system services.
#. Implement the following processes, methods, and techniques to   monitor control compliance by external service providers on an ongoing   basis: [*Assignment: organization-defined processes, methods, and   techniques*].

**DISCUSSION**

External system services are provided by an external provider, and in
most cases, the organization has no direct control over the
implementation of the required controls or the assessment of control
effectiveness. Organizations establish relationships with external
service providers in a variety of ways, including through business
partnerships, contracts, interagency agreements, lines of business
arrangements, licensing agreements, joint ventures, and supply chain
exchanges. The responsibility for managing risks from the use of
external system services remains with the organization charged with
protecting CUI. Service-level agreements define the expectations of
performance for the implemented controls, describe measurable outcomes,
and identify remedies, mitigations, and response requirements for
identified instances of noncompliance. Information from external service
providers regarding the specific functions, ports, protocols, and
services used in the provision of such services can be useful when the
need arises to understand the trade-offs involved in restricting certain
functions and services or blocking certain ports and protocols.

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
| NILRT devices are intended for on-premise use and NI provides no data services   |
| with the devices. The system owner owns the system and the data.                 |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

