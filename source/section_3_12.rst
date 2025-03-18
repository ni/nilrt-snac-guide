
.. _3-12--security-assessment-and-monitoring:

========================================
3.12. Security Assessment and Monitoring
========================================


.. _3-12-1--control-assessments:

---------------------------
3.12.1. Control Assessments
---------------------------

Assess the controls in the system and its environment of operation
[*Assignment: organization-defined frequency*] to determine the extent
to which the controls are implemented correctly, operating as intended,
and producing the desired outcome with respect to meeting specified
security requirements.

**DISCUSSION**

Organizations assess security controls in the system and the environment
in which that system operates as part of the system development life
cycle. Security controls are the safeguards that organizations implement
to satisfy security requirements. By assessing implemented security
controls, organizations determine whether the necessary safeguards are
in place and operating as intended. Security control assessments
identify weaknesses and deficiencies early in the system life cycle,
provide essential information needed to make risk-based decisions, and
ensure compliance to vulnerability mitigation procedures. Assessments
are conducted on the implemented controls as documented in system
security plans.

Security assessment reports document assessment results in sufficient
detail as deemed necessary by organizations to determine the accuracy
and completeness of the reports and whether the security controls are
implemented correctly, operating as intended, and producing the desired
outcome with respect to meeting security requirements. Security
assessment results are provided to the individuals or roles appropriate
for the types of assessments being conducted.

Organizations ensure that assessment results are current, relevant to
the determination of control effectiveness, and obtained with the
appropriate level of assessor independence. Organizations can choose to
use other types of assessment activities, such as vulnerability scanning
and system monitoring, to maintain the security posture of the system
during the system life cycle.

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
| The system owner is responsible to perform a security review based on the        |
| company's security policies.                                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-12-2--plan-of-action-and-milestones:

-------------------------------------
3.12.2. Plan of Action and Milestones
-------------------------------------

#. Develop a plan of action and milestones for the system:

   #. To document the planned remediation actions to correct      weaknesses or deficiencies noted during control assessments; and
   #. To reduce or eliminate known vulnerabilities in the system.

#. Update the existing plan of action and milestones [*Assignment:
   organization-defined frequency*] based on the findings from control
   assessments, independent audits or reviews, and continuous monitoring
   activities.

**DISCUSSION**

Plans of action and milestones (POAMs) are important documents in
organizational security programs. Organizations use POAMs to describe
how unimplemented security requirements and security controls will be
met and how planned mitigations will be implemented. Organizations can
document system security plans and POAMs as separate or combined
documents and in any chosen format. Federal agencies may consider system
security plans and POAMs as inputs to risk-based decisions on whether to
process, store, or transmit CUI on a system hosted by a nonfederal
organization.

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
| The system owner is responsible to create a POAM for the system based on the     |
| security assessment.                                                             |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-12-3--continuous-monitoring:

-----------------------------
3.12.3. Continuous Monitoring
-----------------------------

Develop and implement a system-level continuous monitoring strategy that
includes ongoing monitoring and assessment of control effectiveness.

**DISCUSSION**

Continuous monitoring at the system level facilitates ongoing awareness
of the system security posture to support organizational risk management
decisions. The terms *continuous* and *ongoing* imply that organizations
assess and monitor their controls and risks at a frequency sufficient to
support risk-based decisions. Different types of controls may require
different monitoring frequencies. When monitoring the effectiveness of
multiple controls that have been grouped into capabilities, a root cause
analysis may be needed to determine the specific control that has
failed.

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
| The system owner is responsible to establish and manage a continuous monitoring  |
| process for the system.                                                          |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-12-4--withdrawn--incorporated-into-3-15-2-:

--------------------------------------------
3.12.4. Withdrawn: Incorporated into 3.15.2.
--------------------------------------------

.. raw:: latex

    \newpage


.. _3-12-5--information-exchange:

----------------------------------
3.12.5. Information Exchange
----------------------------------

#. Approve and manage the exchange of CUI between the system and other   systems using [Selection (one or more): interconnection security   agreements; information exchange security agreements; memoranda of   understanding or agreement; service-level agreements; user agreements;   non-disclosure agreements; other types of agreements].
#. Document interface characteristics, security requirements, and   responsibilities for each system as part of the exchange agreements.
#. Review and update the exchange agreements [Assignment:   organization-defined frequency].

**DISCUSSION**

Information exchange applies to information exchanges between two or
more systems, both internal and external to the organization.
Organizations consider the risks related to new or increased threats
that may be introduced when systems exchange information with other
systems that may have different security requirements or policies. The
types of agreements selected are based on factors such as the
relationship between the organizations exchanging information (e.g.,
government to government, business to business, government to business,
government or business, or government or business to individual) and the
level of access to the organizational system by users of the other
system. The types of agreements can include information exchange
security agreements, interconnection security agreements, memoranda of
understanding or agreement, service-level agreements, or other types of
agreements. Organizations may incorporate agreement information into
formal contracts, especially for information exchanges established
between federal agencies and nonfederal organizations (e.g., service
providers, contractors, system developers, and system integrators). The
types of information contained in exchange agreements include the
interface characteristics, security requirements, controls, and
responsibilities for each system.

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
| NILRT collects data from networked test systems and stores data in locations as  |
| configured by the system owner. The system owner is responsible to review the    |
| system components and determine the appropriate security agreement for each      |
| component.                                                                       |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

