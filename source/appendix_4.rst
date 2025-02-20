
.. _appendix-4--labview-real-time-feature-support:

=============================================
Appendix 4: LabVIEW Real-Time Feature Support
=============================================

The following summarizes the current state of SNAC support for features
in LabVIEW RT and related NI software in the default firewall
configuration and a working WireGuard connection.

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
| SFTP/SSH VIs,        | Partially         | By default, will not work |
| incoming             | disabled, can be  | across WireGuard (ssh is  |
|                      | enabled by user   | not enabled for the work  |
|                      |                   | zone)                     |
+----------------------+-------------------+---------------------------+
| SFTP/SSH VIs,        | Disabled, can be  | ssh not enabled by        |
| outgoing             | enabled by user   | default for any outgoing  |
|                      |                   | policy                    |
+----------------------+-------------------+---------------------------+
| NI-RIO, bitfile on   | Unsupported       | Untested, but may work.   |
| disk or in VI        |                   |                           |
+----------------------+-------------------+---------------------------+
| NI-RIO Server        | Unsupported       | Untested and is not       |
|                      |                   | believed to work.         |
+----------------------+-------------------+---------------------------+
| MAX (general use)    | Supported         |                           |
+----------------------+-------------------+---------------------------+
| HWCU (general use)   | Supported         |                           |
+----------------------+-------------------+---------------------------+
| Network Shared       | Supported         |                           |
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
| Web Interface        |                   |                           |
| Framework (WIF)      |                   |                           |
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

