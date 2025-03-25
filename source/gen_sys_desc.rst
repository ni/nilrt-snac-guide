
.. _general-system-description:

==========================
General System Description
==========================

This section includes a general description of NI Linux RT.


.. _system-function-or-purpose:

--------------------------
System Function or purpose
--------------------------

NI Linux RT software is deployed on Operational Technology (OT) systems
for control, monitoring, and measurement systems, including the
CompactRIO and PXI Express instrumentation platforms.

.. figure:: media/image2.png
   :alt: A row of electronic devices Description automatically generated
   :width: 3in
   :height: 1.42847in

   A CompactRIO system

.. figure:: media/image3.png
   :width: 3in
   :height: 1.21597in

   cRIO Development architecture

The *CompactRIO* ("cRIO") platform pairs a cRIO controller (an
embedded PC) with 4-8 *C-Series* expansion slots in a small, ruggedized
chassis. Users control their C-Series devices either using NI's DAQmx
API or by programming an onboard FPGA using LabVIEW FPGA. CompactRIO
embedded controllers run NI Linux RT.

..
   _Need a new page so the following paragraph does not float to above the related figures
   _Use figure instead of image sp that the caption is displayed

.. raw:: latex

    \newpage

.. figure:: media/image4.png
   :alt: A white electronic device with buttons and switches Description automatically generated
   :width: 3in
   :height: 1.42917in

   A PXI system

.. figure:: media/image5.png
   :width: 3.15in
   :height: 1.28in

   PXI Development architecture

The *PXI Express* ("PXIe" or "PXI") platform adapts the PCI
Express bus for the needs of test and measurement applications using
*CompactPCI Express* technology. PXIe pairs a system controller
(typically an embedded PC) with 2-18 PXIe slots in an active backplane.
The controller may run any compatible OS, including Windows, supported
third-party Linux desktop distributions, or NI Linux RT.

NI Linux Real-Time ("NI Linux RT") is an embedded Linux distribution for
real-time application development across NI's embedded controllers.
Users develop their real-time applications on a network-connnected host
system, then deploy to the NI Linux RT controller. Supported programming
languages for real-time development include LabVIEW and C/C++; embedded
programming in Python is also supported. Applications may be deployed
with or without network connectivity.

Alternatively, end users may program the device directly, using shell
access and embedded UI. They may also directly connect with a keyboard,
mouse and monitor, by launching a shortcut to the terminal.

For the purposes of this document, NI Linux RT is restricted to the
Operating System running on these devices.


.. _security-overview:

-----------------
Security Overview
-----------------

The NI Linux RT team follows the NI Secure Development Lifecycle Process
and Policies defined by the NI product security team. The NI SDL is part
of NI's Software Engineering Process required for all software
development. The process enforces policies recommended by the Open Web
Application Security Project (OWASP). The process includes:

-  Threat modeling

-  Automated security testing

-  Static analysis security testing

-  Software composition analysis

-  Dynamic analysis security testing

-  Vulnerability identification and documentation

-  Supply chain security
