
.. _3-4--configuration-management:

=============================
3.4. Configuration Management
=============================


.. _3-4-1--baseline-configuration:

-----------------------------
3.4.1. Baseline Configuration
-----------------------------

#. Develop, document, and maintain under configuration control, a
   current baseline configuration of the system.
#. Review and update the baseline configuration of the system
   [*Assignment: organization-defined frequency*] and when system
   components are installed or upgraded.

**DISCUSSION**

Baseline configurations for systems and system components include
aspects of connectivity, operation, and communications. Baseline
configurations are documented, formally reviewed, and agreed-upon
specifications for systems or configuration items within those systems.
Baseline configurations serve as a basis for future builds, releases, or
changes to systems and include security control implementations,
information about system components, operational procedures, network
topology, and the logical placement of components in the system
architecture. Maintaining baseline configurations requires creating new
baselines as organizational systems change over time. Baseline
configurations of systems reflect the current enterprise architecture.

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
| The NILRT Base System Image plus the SNAC Configuration Tool defines the initial |
| system state.                                                                    |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| Application and driver configuration is built into IPKs using LabVIEW            |
| Application Builder. System owners can define a script to install these IPKs.    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-2--configuration-settings:

-----------------------------
3.4.2. Configuration Settings
-----------------------------

#. Establish, document, and implement configuration settings for the   system that reflect the most restrictive mode
   consistent with   operational requirements using [*Assignment: organization-defined   common secure configurations*].
#. Identify, document, and approve any deviations from established   configuration settings.
#. Monitor and control changes to the configuration settings in   accordance with organizational policies and procedures.

**DISCUSSION**

Configuration settings are the set of parameters that can be changed in
hardware, software, or firmware components of the system that affect the
security posture or functionality of the system. Security-related
configuration settings can be defined for computing systems (e.g.,
servers, workstations), input and output devices (e.g., scanners,
copiers, printers), network components (e.g., firewalls, routers,
gateways, voice and data switches, wireless access points, network
appliances, sensors), operating systems, middleware, and applications.

Security parameters are those parameters that impact the security state
of systems, including the parameters required to satisfy other security
requirements. Security parameters include registry settings; account,
file, and directory permission settings; and settings for functions,
ports, protocols, and remote connections. Organizations establish
organization-wide configuration settings and subsequently derive
specific configuration settings for systems. The established settings
become part of the systems configuration baseline.

Common secure configurations (also referred to as security configuration
checklists, lockdown and hardening guides, security reference guides,
and security technical implementation guides) provide recognized,
standardized, and established benchmarks that stipulate secure
configuration settings for specific information technology
platforms/products and instructions for configuring those system
components to meet operational requirements. Common secure
configurations can be developed by a variety of organizations, including
information technology product developers, manufacturers, vendors,
consortia, academia, industry, federal agencies, and other organizations
in the public and private sectors.

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
| NILRT + SNAC defines a configuration baseline. Organizations are free to apply   |
| their own configuration changes on top of SNAC, and define their own processes   |
| for managing those changes.                                                      |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-3--configuration-change-control:

-----------------------------------
3.4.3. Configuration Change Control
-----------------------------------

#. Determine the types of changes to the system that are   configuration-controlled.
#. Review proposed configuration-controlled changes to the system, and   approve or disapprove such changes with explicit consideration for   security impacts.
#. Implement and document approved configuration-controlled changes to   the system.
#. Monitor and review activities associated with   configuration-controlled changes to the system.

**DISCUSSION**

Configuration change control refers to tracking, reviewing, approving or
disapproving, and logging changes. Specifically, it involves the
systematic proposal, justification, implementation, testing, review, and
disposition of changes to systems, including system upgrades and
modifications. Configuration change control includes changes to baseline
configurations for system components and configuration items of systems,
changes to configuration settings for IT products (e.g., operating
systems, applications, firewalls, routers, mobile devices), unscheduled
and unauthorized changes, and changes to remediate vulnerabilities.

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
| Secure configuration management is responsibility of the system owner.           |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-4--impact-analyses:

----------------------
3.4.4. Impact Analyses
----------------------

#. Analyze the security impact of changes to the system prior to   implementation.
#. After system changes, verify that the impacted controls are   implemented correctly, operating as
   intended, and producing the   desired outcome with regard to meeting specified security   requirements.

**DISCUSSION**

Organizational personnel with security responsibilities conduct impact
analyses which include reviewing security plans, policies, and
procedures to understand security controls; reviewing system design
documentation and operational procedures to understand control
implementation and how specific system changes might affect the
controls; reviewing with stakeholders, the impact of changes on supply
chain partners; and determining how potential changes to a system create
new risks and the ability of implemented controls to mitigate those
risks. Impact analyses also include risk assessments to understand the
impact of changes and to determine whether additional controls are
required.

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
| The system owner is responsible to create and utilize an impact analysis         |
| process.                                                                         |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-5--access-restrictions-for-change:

-------------------------------------
3.4.5. Access Restrictions for Change
-------------------------------------

Define, document, approve, and enforce physical and logical access
restrictions associated with changes to the system.

**DISCUSSION**

Changes to the hardware, software, or firmware components of systems or
the operational procedures related to the systems can have potentially
significant effects on the security of the systems. Therefore,
organizations permit only qualified and authorized individuals to access
systems for the purpose of initiating changes. Access restrictions
include physical and logical access controls, software libraries,
workflow automation, media libraries, abstract layers (i.e., changes
implemented into external interfaces rather than directly into systems),
and change windows (i.e., changes occur only during specified times).

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
| The system owner is responsible to ensure restrictions during system changes.    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-6--least-functionality:

--------------------------
3.4.6. Least Functionality
--------------------------

#. Configure the system to provide only mission-essential   capabilities.
#. Prohibit or restrict use of the following functions, ports,   protocols, software, and/or services: [*Assignment:
   organization-defined prohibited or restricted functions, system ports,   protocols, software, and/or services*].
#. Prevent program execution in accordance with [*Selection (one or more):* [*Assignment: organization-defined policies,
   rules of behavior, and/or access agreements regarding software program usage and restrictions*]; *rules authorizing
   the terms and conditions of software program usage*].

**DISCUSSION**

Systems can provide a variety of functions and services. Some functions
and services that are routinely provided by default may not be necessary
to support essential organizational missions, functions, or operations.
It may be convenient to provide multiple services from single system
components. However, doing so increases risk over limiting the services
provided by any one component. Where feasible, organizations limit
functionality to a single function per component.

Organizations review the functions and services provided by systems or
system components to determine which functions and services are
candidates for elimination. Organizations disable unused or unnecessary
physical and logical ports and protocols to prevent the unauthorized
connection of devices, the transfer of information, and tunneling.
Organizations can utilize network scanning tools, intrusion detection
and prevention systems, and end-point protections (e.g., firewalls and
host-based intrusion detection systems) to identify and prevent the use
of prohibited functions, ports, protocols, and services.

Restricting the use of nonessential software (programs) includes
restricting the roles allowed to approve program execution, prohibiting
auto-execute, and restricting the number of program instances executed
at the same time. Bluetooth, File Transfer Protocol (FTP), and
peer-to-peer networking are examples of protocols that organizations
consider eliminating, restricting, or disabling.

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
| NILRT + SNAC defines the minimal set of services necessary for system operation  |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| NI publishes a list of ports used by its drivers and protocols ("`Configuring    |
| Software and Hardware Firewalls to Support NI Products <https://ww               |
| w.ni.com/en/support/security/configuring-software-and-hardware-                  |
| firewalls-to-support-national-.html>`__"), system owners can configure the       |
| system firewall to let through the ports/traffic needed for specific             |
| applications.                                                                    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-7--withdrawn--incorporated-into-3-4-6-:

------------------------------------------
3.4.7. Withdrawn: Incorporated into 3.4.6.
------------------------------------------

.. raw:: latex

    \newpage



.. _3-4-8--authorized-software---allow-by-exception:

-----------------------------------------------
3.4.8. Authorized Software - Allow by Exception
-----------------------------------------------

#. Identify software programs authorized to execute on the system.
#. Implement a deny-all, allow-by-exception policy to allow the   execution of authorized software programs on the system.
#. Review and update the list of authorized software programs   [*Assignment: organization-defined frequency*].

**DISCUSSION**

If provided with the necessary privileges, users can install software in
organizational systems. To maintain control over the software installed,
organizations identify permitted and prohibited actions regarding
software installation. Permitted software installations include updates
and security patches to existing software and downloading new
applications from organization-approved "app stores." Prohibited
software installations include software with unknown or suspect
pedigrees or software that organizations consider potentially malicious.
The policies selected for governing user-installed software are
organization-developed or provided by some external entity. Policy
enforcement methods can include procedural methods and automated
methods.

Authorized software programs can be limited to specific versions or from
a specific source. To facilitate a comprehensive authorized software
process and increase the strength of protection against attacks that
bypass application-level authorized software, software programs may be
decomposed into and monitored at different levels of detail. These
levels include applications, application programming interfaces,
application modules, scripts, system processes, system services, kernel
functions, registries, drivers, and dynamic link libraries.
Organizations consider verifying the integrity of authorized software
programs using digital signatures, cryptographic checksums, or hash
functions. The verification of authorized software can occur either
prior to execution or at system startup.

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
| NI Linux RT only allows package installation by superusers. Package              |
| installations are restricted to the NILRT feed, but additional packages can be   |
| installed by the user by building code packages within the NILRT environment.    |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-9--withdrawn--addressed-by-3-1-5--3-1-6--3-1-7--3-4-8--3-12-3:

-----------------------------------------------------------------
3.4.9. Withdrawn: Addressed by 3.1.5, 3.1.6, 3.1.7, 3.4.8, 3.12.3
-----------------------------------------------------------------

.. raw:: latex

    \newpage



.. _3-4-10--system-component-inventory:

----------------------------------
3.4.10. System Component Inventory
----------------------------------

#. Develop and document an inventory of system components.
#. Review and update the system component inventory [*Assignment:   organization-defined frequency*]
   and as part of component   installations, removals, and system updates.

**DISCUSSION**

System components are discrete, identifiable information technology
assets that include hardware, software, and firmware. Organizations may
choose to implement centralized system component inventories that
include components from all organizational systems. In such situations,
organizations ensure that the inventories include system-specific
information required for component accountability. The information
necessary for effective accountability of system components includes the
system name, software owners, software version numbers, hardware
inventory specifications, software license information, and for
networked components, the machine names and network addresses across all
implemented protocols (e.g., IPv4, IPv6). Inventory specifications
include the date of receipt, cost, model, serial number, manufacturer,
supplier information, component type, and physical location.

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
| NI System Configuration can be used as a data source for inventory of NI         |
| hardware.                                                                        |
+----------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------+
| SBOMs are available from security@ni.com and, in combination with package        |
| management, can provide inventory information for software.                      |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-11--information-location:

----------------------------
3.4.11. Information Location
----------------------------

#. Identify and document the location within the system where CUI is   processed and stored.
#. Identify and document the users who have access to the system where   CUI is processed and stored.
#. Document changes to the location where CUI is processed and stored.

**DISCUSSION**

Information location addresses the need to understand the specific
system components where CUI is being processed and stored and the users
who have access to CUI so that appropriate protection mechanisms can be
provided including information flow controls, access controls, and
information management.

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
| NILRT does not provide software or hardware features for constraining the        |
| location of CUI to any finer granularity than the controller as a whole.         |
| System-wide management of information location is conducted at the discretion of |
| the system owner.                                                                |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-4-12--system-and-component-configuration-for-high-risk-areas:

--------------------------------------------------------------
3.4.12. System and Component Configuration for High-Risk Areas
--------------------------------------------------------------

#. Issue [*Assignment: organization-defined system*] with   [*Assignment: organization-defined system configurations*]
   to individuals traveling to locations that the organization deems to be   of significant risk.
#. Apply the following controls to the system when the individuals   return from travel: [*Assignment: organization-defined controls*].

**DISCUSSION**

When it is known that systems or system components will be in high-risk
areas external to the organization, additional controls may be
implemented to counter the increased threat. For example, organizations
can take actions for notebook computers used by individuals departing on
and returning from travel. Actions include determining the locations
that are of concern, defining the required configurations for the
components, ensuring that components are configured as intended before
travel is initiated, and applying controls to the components after
travel is completed. Specially configured notebook computers include
computers with sanitized hard drives, limited applications, and more
stringent configuration settings. Controls applied to mobile devices
upon return from travel include examining the mobile device for signs of
physical tampering and purging and reimaging disk drives.

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
| The system owner is responsible to secure the system when it is transported to   |
| high-risk areas.                                                                 |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

