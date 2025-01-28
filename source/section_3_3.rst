
.. _3-3--audit-and-accountability:

=============================
3.3. Audit and Accountability
=============================


.. _3-3-1--event-logging:

--------------------
3.3.1. Event Logging
--------------------

#. Specify the following event types for logging within the system:   [*Assignment: organization-defined event types*].
#. Review and update the event types selected for logging   [*Assignment: organization-defined frequency*].

**DISCUSSION**

An event is any observable occurrence in a system, which includes
unlawful or unauthorized system activity. Organizations identify event
types for which a logging functionality is needed as those events that
are significant and relevant to the security of systems and the
environments in which those systems operate to meet specific and ongoing
auditing needs. Event types can include password changes, failed logons
or failed accesses related to systems, administrative privilege usage,
or third-party credential usage. In determining event types that require
logging, organizations consider the system monitoring and auditing that
are appropriate for each of the 65 CUI security requirements. When
defining event types, organizations consider the logging necessary to
cover related events, such as the steps in distributed,
transaction-based processes (e.g., processes that are distributed across
multiple organizations) and actions that occur in service-oriented or
cloud-based architectures. Monitoring and auditing requirements can be
balanced with other system needs. For example, organizations may
determine that systems must have the capability to log every file
access, both successful and unsuccessful, but not activate that
capability except for specific circumstances due to the potential burden
on system performance. The event types that are logged by organizations
may change over time. Periodically reviewing and updating the set of
logged event types is necessary to ensure that the current set remains
necessary and sufficient.

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
| NI LinuxRT event logging is handled by syslog-ng. By default, syslog is setup to |
| harvest any log configuration files for other programs that introduce logging as |
| long as they install conf files to '/etc/syslog-ng.d/'.                          |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-2--audit-record-content:

---------------------------
3.3.2. Audit Record Content
---------------------------

Include the following content in audit records: what type of event
occurred; when and where the event occurred; source and outcome of the
event; identity of individuals, subjects, objects, or entities
associated with the event; and [*Assignment: organization-defined
additional information*].

**DISCUSSION**

Audit record content that may be necessary to support the auditing
function includes time stamps, source and destination addresses, user or
process identifiers, event descriptions, filenames, and the access
control or flow control rules that are invoked. Event outcomes can
include indicators of event success or failure and event-specific
results (e.g., the security state of the system after the event
occurred). Detailed information that organizations may consider in audit
records includes a full text recording of privileged commands or the
individual identities of group account users.

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
| The NILRT SNAC configuration uses the auditd kernel subsystem and auditd daemon  |
| to log important system events to the /var/log/audit log location.               |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-3--audit-record-generation:

------------------------------
3.3.3. Audit Record Generation
------------------------------

#. Provide an audit record generation capability for the event types   defined in 3.3.1a.
#. Generate audit records for the event types defined in 3.3.1a. that   include the audit record content defined in 3.3.2.
#. Retain audit records for [*Assignment: organization-defined time   period consistent with records retention policy, applicable contract   requirement, law, or regulation*].

**DISCUSSION**

Audit records can be generated at various levels of abstraction,
including at the packet level as information traverses the network.
Selecting the appropriate level of abstraction is a critical aspect of
an audit logging capability and can facilitate the identification of
root causes to problems. The ability to add information generated in
audit records is dependent on system functionality to configure the
audit record content. Organizations may consider additional information
in audit records including access control or flow control rules invoked
and individual identities of group account users. Organizations may also
consider limiting additional audit record information to only
information that is explicitly needed for audit requirements.

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
| The NILRT SNAC configuration uses the auditd kernel subsystem and auditd daemon  |
| to log important system events to the /var/log/audit log location. Audit logs    |
| are indefinitely retained.                                                       |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-4--response-to-audit-logging-process-failures:

-------------------------------------------------
3.3.4. Response to Audit Logging Process Failures
-------------------------------------------------

#. Alert [*Assignment: organization-defined personnel or roles*]   within [*Assignment: organization-defined time period*] in the event   of an audit logging process failure.
#. Take the following additional actions: [*Assignment:   organization-defined additional actions*].

**DISCUSSION**

Audit logging process failures include software and hardware errors,
failures in audit log capturing mechanisms, and reaching or exceeding
audit log storage capacity. Response actions include overwriting the
oldest audit records, shutting down the system, and stopping the
generation of audit records. Organizations may choose to define
additional actions for audit logging process failures based on the type
of failure, the location of the failure, the severity of the failure, or
a combination of such factors. When the audit logging process failure is
related to storage, the response is carried out for the audit log
storage repository (i.e., the distinct system component where the audit
logs are stored), the system on which the audit logs reside, the total
audit log storage capacity of the organization (i.e., all audit log
storage repositories combined), or all three. Organizations may decide
to take no additional actions after alerting designated roles or
personnel.

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
| System owners can configure auditd to send an email when there is a logging      |
| failure by setting 'action_mail_acct' in '/e tc/audit/auditd.conf' to a valid    |
| e-mail address and defining which alerts to send e-mails for in the audit.rules. |
| User must define the response policy to these alerts.                            |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-5--audit-record-review--analysis--and-reporting:

---------------------------------------------------
3.3.5. Audit Record Review, Analysis, and Reporting
---------------------------------------------------

#. Review and analyze system audit records [*Assignment:   organization-defined frequency*] for indications and potential impact   of inappropriate or unusual activity.
#. Report findings to [*Assignment: organization-defined personnel or   roles*].
#. Analyze and correlate audit records across different repositories   to gain organization-wide situational awareness.

**DISCUSSION**

Audit record review, analysis, and reporting covers information
security-related logging performed by organizations and can include
logging that results from the monitoring of account usage, remote
access, wireless connectivity, configuration settings, the use of
maintenance tools and non-local maintenance, system component inventory,
mobile device connection, physical access, temperature and humidity,
equipment delivery and removal, communications at system interfaces, and
the use of mobile code. Findings can be reported to organizational
entities that include the incident response team, help desk, and
security or privacy offices. If organizations are prohibited from
reviewing and analyzing audit records or unable to conduct such
activities, the review or analysis may be carried out by other
organizations granted such authority. The scope, frequency, and/or depth
of the audit record review, analysis, and reporting may be adjusted to
meet organizational needs based on new information received. Correlating
audit record review, analysis, and reporting processes helps to ensure
that they do not operate independently but rather collectively create a
more complete view of events. Regarding the assessment of a given
system, the requirement is agnostic as to whether this correlation is
applied at the system level or at the organization level across all
systems.

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
| The system owner is responsible to set up a process to review audit log records. |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-6--audit-record-reduction-and-report-generation:

---------------------------------------------------
3.3.6. Audit Record Reduction and Report Generation
---------------------------------------------------

#. Implement an audit record reduction and report generation   capability that supports on-demand audit record review, analysis,   reporting requirements, and after-the-fact investigations of   incidents.
#. Preserve the original content and time ordering of audit records.

**DISCUSSION**

Audit record reduction is a process that manipulates collected audit
information and organizes it in a summary format that is more meaningful
to analysts. Audit record reduction and report generation capabilities
do not always come from the same system or organizational entities that
conduct auditing activities. An audit record reduction capability can
include, for example, modern data mining techniques with advanced data
filters to identify anomalous behavior in audit records. The report
generation capability provided by the system can help generate
customizable reports. The time ordering of audit records can be a
significant issue if the granularity of the time stamp in the record is
insufficient.

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
| The system owner is responsible to set up audit record reduction tooling to      |
| review audit log records.                                                        |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-7--time-stamps:

------------------
3.3.7. Time Stamps
------------------

#. Use internal system clocks to generate time stamps for audit   records.
#. Record time stamps for audit records that meet [*Assignment:   organization-defined granularity of time measurement*] and that:

   #. Use Coordinated Universal Time (UTC);
   #. Have a fixed local time offset from UTC; or
   #. Include the local time offset as part of the time stamp.

**DISCUSSION**

Time stamps generated by the system include the date and time. Time is
commonly expressed in Coordinated Universal Time (UTC) - a modern
continuation of Greenwich Mean Time (GMT) -or local time with an offset
from UTC. The granularity of time measurements refers to the degree of
synchronization between system clocks and reference clocks (e.g., clocks
synchronizing within hundreds of milliseconds or tens of milliseconds).
Organizations may define different time granularities for different
system components. Time service can be critical to other security
capabilities, such as access control, and identification and
authentication, depending on the nature of the mechanisms used to
support those capabilities.

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
| Syslog is configured to use UTC from the system hardware clock.                  |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-8--protection-of-audit-information:

--------------------------------------
3.3.8. Protection of Audit Information
--------------------------------------

Protect audit information and audit logging tools from unauthorized
access, modification, and deletion.

**DISCUSSION**

Audit information includes information needed to successfully audit
system activity, such as audit records, audit log settings, audit
reports, and personally identifiable information. Audit logging tools
are programs and devices used to conduct system audit and logging
activities. The protection of audit information focuses on technical
protection and limits the ability to access and execute audit logging
tools to authorized individuals. The physical protection of audit
information is addressed by media and physical protection controls.

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
| The NILRT SNAC configuration restricts write access to system logs to System     |
| Maintainers (via the \`root\` account), and System Auditors via membership in    |
| the \`adm\` group.                                                               |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-3-9--withdrawn--incorporated-into-03-03-08:

--------------------------------------------
3.3.9. Withdrawn: Incorporated into 03.03.08
--------------------------------------------

.. raw:: latex

    \newpage

