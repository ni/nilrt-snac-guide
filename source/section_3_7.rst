
.. _3-7--maintenance:

================
3.7. Maintenance
================


.. _3-7-1--withdrawn--recategorized-as-nco-:

---------------------------------------
3.7.1. Withdrawn: Recategorized as NCO.
---------------------------------------

.. raw:: latex

    \newpage



.. _3-7-2--withdrawn--incorporated-into-3-7-4-and-3-7-6-:

----------------------------------------------------
3.7.2. Withdrawn: Incorporated into 3.7.4 and 3.7.6.
----------------------------------------------------

.. raw:: latex

    \newpage



.. _3-7-3--withdrawn--incorporated-into-3-8-3-:

------------------------------------------
3.7.3. Withdrawn: Incorporated into 3.8.3.
------------------------------------------

.. raw:: latex

    \newpage



.. _3-7-4--maintenance-tools:

------------------------
3.7.4. Maintenance Tools
------------------------

#. Approve, control, and monitor the use of system maintenance tools.
#. Inspect maintenance tools and media containing diagnostic and test   programs for malicious code before the media and tools are used in the   system.
#. Prevent the removal of maintenance equipment containing CUI by:

   #. Verifying that there is no CUI on the equipment;
   #. Sanitizing or destroying the equipment; or
   #. Obtaining an exemption from [*Assignment: organization-defined      officials*] explicitly authorizing removal of the equipment from      the facility.

**DISCUSSION**

Approving, controlling, monitoring, and reviewing maintenance tools
address security-related issues associated with the tools that are used
for diagnostic and repair actions on the system. Maintenance tools can
include hardware and software diagnostic and test equipment as well as
packet sniffers. The tools may be pre-installed, brought in with
maintenance personnel on media, cloud-based, or downloaded from a
website. Diagnostic and test programs are potential vehicles for
transporting malicious code into the system, either intentionally or
unintentionally. Examples of media inspection include checking the
cryptographic hash or digital signatures of diagnostic and test programs
and/or media. If, upon inspection of media that contain maintenance
diagnostic and test programs, organizations determine that the media
contain malicious code, the incident is handled consistent with incident
handling policies and procedures.

A periodic review of system maintenance tools can result in the
withdrawal of approval for outdated, unsupported, irrelevant, or
no-longer-used tools. The hardware and software components that support
maintenance and are considered a part of the system (including software
implementing utilities such as "ping," "ls," "ipconfig," or hardware and
software that implement the monitoring port of an Ethernet switch) are
not addressed by maintenance tools.

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
| The system owner is responsible to develop and implement a maintenance plan that |
| protects data on the system.                                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-7-5--nonlocal-maintenance:

---------------------------
3.7.5. Nonlocal Maintenance
---------------------------

#. Approve and monitor nonlocal maintenance and diagnostic activities.
#. Implement multi-factor authentication and replay resistance in the   establishment of nonlocal maintenance and diagnostic sessions.
#. Terminate session and network connections when nonlocal maintenance   is completed.

**DISCUSSION**

Nonlocal maintenance and diagnostic activities are conducted by
individuals who communicate through either an external or internal
network. Local maintenance and diagnostic activities are carried out by
individuals who are physically present at the system location and not
communicating across a network connection. Authentication techniques
used to establish nonlocal maintenance and diagnostic sessions reflect
the requirements in 3.5.1.

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
| The system owner is responsible to develop and implement a maintenance plan that |
| protects data on the system.                                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage



.. _3-7-6--maintenance-personnel:

----------------------------
3.7.6. Maintenance Personnel
----------------------------

#. Establish a process for maintenance personnel authorization, and   maintain a list of authorized maintenance organizations or personnel.
#. Verify that non-escorted personnel who perform maintenance on the   system possess the required access authorizations.
#. Designate organizational personnel with required access   authorizations and technical competence to supervise the maintenance   activities of personnel who do not possess the required access   authorizations.

**DISCUSSION**

Maintenance personnel refers to individuals who perform hardware or
software maintenance on the system, while 3.10.1 addresses physical
access for individuals whose maintenance duties place them within the
physical protection perimeter of the system. Technical competence of
supervising individuals relates to the maintenance performed on the
system, while having required access authorizations refers to
maintenance on and near the system. Individuals not previously
identified as authorized maintenance personnel (e.g., manufacturers,
consultants, systems integrators, and vendors) may require privileged
access to the system, such as when they are required to conduct
maintenance with little or no notice. Organizations may choose to issue
temporary credentials to these individuals based on their risk
assessments. Temporary credentials may be for one-time use or for very
limited time periods.

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
| The system owner is responsible to develop and implement a maintenance plan that |
| protects data on the system.                                                     |
+----------------------------------------------------------------------------------+

.. raw:: latex

    \newpage

