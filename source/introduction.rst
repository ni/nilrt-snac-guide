
.. _introduction:

============
Introduction
============


-----------------
Purpose and Scope
-----------------

NIST SP 800-171 is a publication from the National Institute of Standards and Technology (NIST) that provides a set of security requirements for protecting Controlled Unclassified Information (CUI) in non-federal systems and organizations.
Its recommendations are the basis for several other cybersecurity standards sets, including the Cybersecurity Maturity Model Certification (CMMC) and the Defense Federal Acquisition Regulation Supplement (DFARS).

This document provides a review of the security controls listed in NIST SP 800-171 Rev. 3, and how they can be satisfied by an NI LinuxRT (NILRT) system configured with the Secured, Network-Attached Controller (SNAC) configuration described in :ref:`appendix-1`.


-----
Scope
-----

This document applies only to the operating system on the controllers in these platforms.
It does not discuss the process to secure individual hardware drivers or application software that might be used to interact with the supported platforms.
Contact your NI sales representative to inquire if there are cooperative secure configuration guides for your desired NI driver or Application Software.

The SNAC configuration can generally be applied to NI Hardware platforms which support NILRT and which use Intel x86_64 processors.
For a list of supported platforms, refer to the :ref:`appendix-1-supported-hardware` section of Appendix 1.


------------
Organization
------------

The remainder of this document is organized as follows.

* **Chapter 2** provides a general overview of NI Linux RT and the CompactRIO and PXIe platforms.
* **Chapters 3 - 20** provide an enumeration of the total controls defined by NIST SP 800-171r3, and a summary of how the SNAC configuration satisfies the control, or what should be satisfied by implementing organizations.
* **Appendix 1** provides a detailed description of the SNAC design, discusses application considerations, and provides instructions on how to deploy a NILRT CompactRIO/PXIe system into the SNAC configuration.
* **Appendix 2** provides detailed instructions on how to configure a Windows LabVIEW host to connect to a SNAC-configured NILRT device using the Wireguard VPN utility.
* **Appendix 3** provides an administrative guide to configuring the NILRT firewall daemon to suit your application.
* **Appendix 4** summarizes LabVIEW Real-Time feature support status in the SNAC configuration.
* **Appendix 5** provides instructions for additional security and system tools including USBGuard and ClamAV installation and configuration in the SNAC configuration.
