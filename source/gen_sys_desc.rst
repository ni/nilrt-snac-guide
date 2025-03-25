
.. _general-system-description:

==========================
General System Description
==========================


----------
CompactRIO
----------

.. figure:: media/image2.png
   :alt: A row of electronic devices Description automatically generated
   :width: 3in
   :height: 1.42847in

   A CompactRIO system

.. figure:: media/image3.png
   :width: 3in
   :height: 1.21597in

   cRIO Development Architecture

The *CompactRIO* ("cRIO") platform pairs a cRIO controller (an embedded PC) with 4-8 *C-Series* expansion slots in a small, ruggedized chassis.
Users control their C-Series devices either using NI's DAQmx API or by programming an onboard FPGA using LabVIEW FPGA.
CompactRIO embedded controllers run NI Linux RT.


----
PXIe
----

.. figure:: media/image4.png
   :alt: A white electronic device with buttons and switches Description automatically generated
   :width: 3in
   :height: 1.42917in

   A PXI system

.. figure:: media/image5.png
   :width: 3.15in
   :height: 1.28in

   PXI Development Architecture

The *PXI Express* ("PXIe" or "PXI") platform adapts the PCI Express bus for the needs of test and measurement applications using *CompactPCI Express* technology.
PXIe pairs a system controller (typically an embedded PC) with 2-18 PXIe slots in an active backplane.
The controller may run any compatible OS, including Windows, supported third-party Linux desktop distributions, or NI Linux RT.
This document only discusses the deployment of PXIe controllers with NI Linux RT.


------------------
NI Linux Real-Time
------------------

NI Linux Real-Time (NILRT) is an embedded, general-purpose operating system based on the Linux kernel and OpenEmbedded package distribution.
The system kernel is enhanced for better real-time scheduling performance in high-precision IO applications.
Both the kernel and distribution are specialized for use with NI compact RIO (cRIO) and PXIe devices.

Documentation for the generic use and administration of NILRT can be found at `ni.com <https://ni.com>`__ or on the `nilrt-docs <https://nilrt-docs.ni.com>`__ supplemental NILRT documentation site.
The source code for the open-source portions of the distribution and for the Linux kernel are available from the official NI github repositories `ni/nilrt <https://github.com/ni/nilrt>`__ and `ni/linux <https://github.com/ni/linux>`__ respectively.

Users develop their real-time applications on a network-connected host system, then deploy to the NI Linux RT controller.
Supported programming languages for real-time development include LabVIEW, C/C++, and Python3.
Applications may be deployed with or without network connectivity.

Alternatively, end users may program the device directly, using shell access UI.
They may also directly connect a keyboard and monitor, and login directly to the system TTY interface.


.. _security-overview:

-----------------
Security Overview
-----------------

The NI Linux RT team follows the NI Secure Development Lifecycle Process and Policies defined by the NI product security team.
The NI SDL is part of NI's Software Engineering Process required for all software development.
The process enforces policies recommended by the Open Web Application Security Project (OWASP).
The process includes:

-  Threat modeling
-  Automated security testing
-  Static analysis security testing
-  Software composition analysis
-  Dynamic analysis security testing
-  Vulnerability identification and documentation
-  Supply chain security
