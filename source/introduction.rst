
.. _introduction:

============
Introduction
============


-----------------
Purpose and Scope
-----------------

This document provides a review of the security controls listed in NIST SP 800-171 Rev. 3 applied to the NI Linux RT software products from NI.
This document assumes a customer-operated NI Linux RT implementation.
The implementation may run on one of the following platforms:

* NI CompactRIO x64
* NI PXI

This document applies only to the operating system on the controllers in these platforms.
It does not discuss the process to secure individual hardware drivers or application software that might be used to interact with the supported platforms.
Contact your NI sales representative to inquire if there are cooperative secure configuration guides for your desired NI driver or Application Software.

Throughout this document, "NILRT" is used to refer to the NI Linux RT operating system.


------------
Organization
------------

The remainder of this document is organized as follows.

* **Chapter 2** provides a general overview of NI Linux RT and the cRIO and PXIe platforms.
* **Chapters 3 - 20** provide an enumeration of the total controls defined by NIST SP 800-171r3, and a summary of how the SNAC configuration satisfies the control, or what should be satisfied by implementing organizations.
* **Appendix 1** provides a detail description of the SNAC design, discusses application considerations, and provides instructions on how to deploy an NILRT cRIO/PXIe into the SNAC configuration.
* **Appendix 2** provides detail instructions of how to configure a Windows LabVIEW host to connect to a SNAC-configured NILRT device using the Wireguard VPN utility.
* **Appendix 3** provides an administrative guide to configuring the NILRT firewall daemon to suit your application.
* **Appendix 4** summarizes LabVIEW Real-Time feature support status in the SNAC configuration.
