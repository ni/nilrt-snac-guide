
.. _appendix-4--labview-real-time-feature-support:

=============================================
Appendix 4: LabVIEW Real-Time Feature Support
=============================================

The following summarizes the current state of SNAC support for features
in LabVIEW RT and related NI software in the default firewall
configuration and a working WireGuard connection.

.. raw:: latex

    \scalefont{0.8}


.. tabularcolumns:: \Y{0.35}\Y{0.3}\Y{0.35}

+----------------------+-------------------+---------------------------+
| Feature              | Status            | Notes                     |
+======================+===================+===========================+
| LabVIEW RT protocol; | Supported         |                           |
| basic ADE support    |                   |                           |
+----------------------+-------------------+---------------------------+
| LabVIEW VI Server    | Supported         | Enabled by default for    |
|                      |                   | inbound only; see         |
|                      |                   | ni-labview-viserver       |
|                      |                   | service.                  |
+----------------------+-------------------+---------------------------+
| LabVIEW RT built     | Supported         |                           |
| applications, RTEXEs |                   |                           |
+----------------------+-------------------+---------------------------+
| DAQmx: application   | Supported         |                           |
| execution; I/O       |                   |                           |
| controls             |                   |                           |
+----------------------+-------------------+---------------------------+
| SystemLink           | Unsupported       | Untested, but AMQP and    |
|                      |                   | salt-master outbound      |
|                      |                   | traffic permitted         |
+----------------------+-------------------+---------------------------+
| SFTP/SSH VIs         | Partially         | By default, will not work |
| (incoming)           | disabled, can be  | across WireGuard (ssh is  |
|                      | enabled by user   | not enabled for the work  |
|                      |                   | zone)                     |
+----------------------+-------------------+---------------------------+
| SFTP/SSH VIs         | Disabled, can be  | ssh not enabled by        |
| (outgoing)           | enabled by user   | default for any outgoing  |
|                      |                   | policy                    |
+----------------------+-------------------+---------------------------+
| NI-RIO, bitfile on   | Unsupported       | Untested, but may work.   |
| disk or in VI        |                   |                           |
+----------------------+-------------------+---------------------------+
| NI-RIO Server        | Unsupported       | Untested and is not       |
|                      |                   | believed to work.         |
+----------------------+-------------------+---------------------------+
| MAX (general use)    | Unsupported       |                           |
+----------------------+-------------------+---------------------------+
| HWCU (general use)   | Supported         |                           |
+----------------------+-------------------+---------------------------+
| Network Shared       | Supported         | See note below.           |
| Variables            |                   |                           |
+----------------------+-------------------+---------------------------+
| Network Streams      | Supported         |                           |
+----------------------+-------------------+---------------------------+
| NI-RIO I/O Scan      | Unsupported       | Untested                  |
+----------------------+-------------------+---------------------------+
| NI System            | Supported         | With new SSH connection   |
| Configuration        |                   | type introduced in the    |
|                      |                   | 25.0 platform release.    |
+----------------------+-------------------+---------------------------+
| System Web Server;   | Disabled          | Uninstalled               |
| Web Based            |                   |                           |
| Configuration        |                   |                           |
+----------------------+-------------------+---------------------------+
| NIAuth               | Disabled          | Uninstalled               |
+----------------------+-------------------+---------------------------+
| LabVIEW Web Services | Disabled          | Required functionality    |
|                      |                   | uninstalled               |
+----------------------+-------------------+---------------------------+
| LabVIEW Remote       | Disabled          | Required functionality    |
| Panels; LabVIEW VI   |                   | uninstalled               |
| Snapshots            |                   |                           |
+----------------------+-------------------+---------------------------+
| LabVIEW Embedded UI  | Disabled          | Required functionality    |
|                      |                   | uninstalled               |
+----------------------+-------------------+---------------------------+

.. raw:: latex

    \scalefont{1.25}

.. _hosting-shared-variables-on-my-computer:

---------------------------------------
Hosting Shared Variables on My Computer
---------------------------------------

To access shared variables hosted on My Computer from your RT target,
update the My Computer alias to point to the WireGuard address. To do
this, specify a custom address on the My Computer item's `General page <https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/resource/framework/providers/lvdesktop-llb/prefpage-mycomputer.html>`__.
