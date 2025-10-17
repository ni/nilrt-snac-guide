
.. _appendix-1:

=======================================================
Appendix 1: The Secured, Network-Attached Configuration
=======================================================

This chapter describes the use of NI Linux RT (NILRT) in the Secured, Network-Attached Controller (SNAC) configuration.
SNAC is a domain-specific configuration for high-security environments, where compliance to NIST SP 800-171 or other NIST SP 800-53-derived security standards is required.

.. _design-constraints:

------------------
Design Constraints
------------------

When designing a deployment using the SNAC configuration, consider the
following support constraints.

**Supported Hardware Devices.** The SNAC configuration is verified to
work only on cRIO x64 and PXIe x64 devices, that support NILRT. The
sbRIO family of controllers is not included in the supported set.

**Supported NILRT System Images.** The SNAC configuration is supported
on the NILRT Base System Image 2025.3 and later.

**Device Configuration Utilities.** The SNAC configuration supports
device configuration via direct SSH connection or HWCU. Configuration
via NI MAX or SystemLink is not supported at this time.

**Supported Software Products.** The SNAC configuration supports the
deployment of the following NI software products.

-  LabVIEW Real-Time 2022-2025
-  NI-DAQmx
-  NI-DMM
-  NI-Scope
-  NI-DCPower
-  NI-Switch
-  NI-FGEN

**Runtime Software Installation.**
While in the SNAC configuration, software installation to the NILRT system is only permitted from:

#. the NI vendor `package feeds <https://download.ni.com/ni-linux-rt/feeds/>`__ (configured by default).
#. the `NI Linux Real-Time Offline Feed <https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000YGDsCAO>`__.
#. software sources that have been validated-by and which are controlled by the system Integrator.

**Connected Machines.** If your application design includes a
network-connected Windows or Linux system that receives data from the
NILRT device (via LabVIEW or otherwise), it must be configured with
a `Wireguard <https://www.wireguard.com/>`__ interface.

**Physical Security.** The SNAC configuration is not intended for use in
system designs which allow unauthorized users physical access the NILRT
system. Integrators are directed to design their application to limit
physical access to the NILRT device's IO to only permitted system
administrators and system maintainers.

**Safemode.** NILRT systems have the ability to boot into a temporary
"Safemode" of operation, where Base System Image and system software
configuration changes can be made. Because this boot configuration is
not secured to the same standards as SNAC, unprivileged users and system
administrators should never direct a NILRT device to reboot into
Safemode as a part of normal operations. System maintainers are still
expected to use Safemode to affect deployment of the NILRT Base System
Image, software installation, and system recovery operations.

**Graphical UI.**
Normal NILRT configurations support an optional graphical desktop interface based on the XFCE desktop environment.
This graphical UI is not intended for use in high-security environments and is disabled as a part of the SNAC configuration.
Integrators are directed to forbid system administrators from reinstalling or enabling the graphical UI.

**Application Web Server.** After applying the SNAC configuration, the
LabVIEW Application Web Server will cease to function.


.. _design-overview:

---------------
Design Overview
---------------

The NILRT SNAC configuration is a supported set of runtime configuration changes to the normal NILRT Base System Image ("Runmode").
This section describes the major differences between the factory NILRT configuration and NILRT+SNAC.


.. _access-control:

~~~~~~~~~~~~~~
Access Control
~~~~~~~~~~~~~~

The NILRT SNAC configuration substantially changes the system account
management framework from the default NILRT configuration. The legacy
credentials database that coordinates accounts between Safemode and
Runmode, and brokers authorization for some NI network services, is
de-installed and replaced with a PAM-based authentication scheme using
standard Linux tools. As a consequence of this reconfiguration:

-  System Administrators will find the NILRT system to be generally more
   similar to other Linux desktop distributions - aiding the design of
   custom authentication schemes based on common PAM tooling.

-  System credentials are no longer shared between Safemode and Runmode.
   The default login user for Safemode will remain ``admin``. Setting
   the ``admin`` account password while in Safemode will not transfer to
   Runmode.


.. _roles--users--and-groups:

~~~~~~~~~~~~~~~~~~~~~~~~
Roles, Users, and Groups
~~~~~~~~~~~~~~~~~~~~~~~~

The NILRT SNAC configuration recognizes that individuals accessing the
system can be broadly divided into one or more roles.

**System Integrators** are engineering organizations who design hardware
and software solutions using NI LinuxRT devices. Integrating
organizations may be the solutions end-user or an upstream vendor in
their own right.

**System Maintainers** are individuals who are responsible for
physically manipulating the NILRT device, deploying application
software, re-imaging the device, and performing remedial recovery
actions. Maintainers are expected to have constructive access privileges
to the system, and are directed to use the ``root`` login account when
performing system maintenance operations.

**System Administrators** are individuals responsible for the running
configuration and operation of the NILRT device. Administrators are
assigned individual accounts on the NILRT system, and enrolled in
the ``sudo`` group. As members of this group, they are permitted to perform
privileged operations via the sudo utility.

**System Auditors** are individuals responsible for collecting or
reviewing system logs. Auditors are assigned individual accounts on the
NILRT system, and enrolled in the ``adm`` group. As members of this group,
they are permitted write access to system logs and logging
configuration. Users should never be a member of both
the ``sudo`` and ``adm`` groups, as it would permit that user to both perform
privileged operations and remove audit records of their operations.

**System Users** are all other individuals who require limited access to
a NILRT system to perform their assigned tasks. These users are
generally unprivileged, and forbidden from being members of any of the
prior access groups.


.. _audit-and-accountability:

~~~~~~~~~~~~~~~~~~~~~~~~
Audit and Accountability
~~~~~~~~~~~~~~~~~~~~~~~~

Event and access logging is performed by several services in NI LinuxRT.
User processes log their actions by registering them with
the syslog-ng daemon. Kernel processes log actions
to dmesg (``/var/log/dmesg``) and to the audit subsystem (``/var/log/audit/``).
PAM authentication logs are written to (``/var/log/auth.log``).

For information about the default (non-SNAC) logging configuration on
NILRT, reference the
nilrt-docs `section <https://nilrt-docs.ni.com/troubleshooting/logs.html>`__ on
logging.

The default system logging configuration can be extended to meet mission requirements by appending configurations to the ``/etc/syslog-ng/syslog-ng.conf`` file.

The SNAC configuration enables *persistent log storage*.
Storing logs persistently may fill up the NILRT system's disk space, potentially halting other system operations.
Integrators are directed to periodically retrieve NILRT system logs, store them on another system, and then clean the logs on the NILRT system.

The additional hardware interrupts generated by storing system logs can have a measurable impact on a system's real-time performance characteristics - particularly on cRIO systems.
If your application has impressive real-time performance requirements, consider configuring syslog-ng to emit logs over the network using the `Configure Remote Logging <#configure-remote-logging>`__ section.


.. _physical-protection:

~~~~~~~~~~~~~~~~~~~
Physical Protection
~~~~~~~~~~~~~~~~~~~

When attackers gain physical access to a system, they can nearly always
construct root access. To mitigate against these risks, it is
important that Integrators design their deployments to control physical
access to the NILRT system. Limit personnel access to only System
Maintainers, for the purpose of changing system configuration. Construct
secure system enclosures to limit access to unused I/O ports and
peripherals on the system. And enforce organization policies limiting
the use of removable media to only authorized system maintenance
actions.

.. _system-and-communications-protection:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
System and Communications Protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Configuration.** NILRT system configuration operations are performed via two remote, encrypted paths and one local path.

#. (Remote) The NI HardWare Configuration Utility (HWCU) can be used for system maintenance and deployment of the NILRT Base System Image.
#. (Remote) The NILRT Base System Image supports Secure SHell (SSH) connections to its OpenSSH server instance, which can be used for subsequent manual configuration.
#. (Local) System users can connect the NILRT device to a graphical display and gain access to the system shell using a keyboard.

**Application.** System applications employ protection strategies that
are necessarily unique to their mission. For LabVIEW communications,
Integrators are recommended to use the provided Wireguard interface or
an equivalent Wireguard VPN of their own design. Non-LabVIEW
applications may use their own Wireguard interface, OpenVPN, or an
application-level encryption strategy of their own design.


.. _snac-configuration-instructions:

-------------------------------
SNAC Configuration Instructions
-------------------------------

System maintainers are directed to deploy and configure a NILRT system
in the SNAC configuration by performing the following actions. All
action should generally be performed by the System Maintainer, logged
into the NILRT shell as either ``admin`` (safemode) or ``root`` (runmode).


.. _install-necessary-configuration-software-to-the-host-machine:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Install necessary configuration software to the Host Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Choose a network-connected Windows or Linux desktop machine to use as the LabVIEW and configuration host.
#. Download and install the `NI Package Manager <https://www.ni.com/en/support/downloads/software-products/download.package-manager.html#322516>`__ (NIPM).
#. Run the NI Package Manager.

#. Install the latest "NI CompactRIO and Drivers" package. Be sure to include the optional components "NI Hardware Configuration Utility" (checked by default) and "NI Linux RT System Image" (not checked by default).

    .. figure:: media/image8.png
        :alt: A screenshot of a computer Description automatically generated
        :width: 3.5in
        :height: 1.57in


.. _connect-the-nilrt-device-to-the-internet:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connect the NILRT device to the internet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure NILRT as a SNAC device, some of the following steps require that the device be able to access the NILRT package feeds at *download.ni.com*.

When deploying a system on an isolated network, the `Offline Feeds Installer <https://www.ni.com/en/support/downloads/software-products/download.ni-linux-real-time-offline-installation-support.html>`__ utility can be used to setup a bespoke feed server on a Windows host on the same isolated network.


.. _deploy-the-latest-firmware-and-nilrt-base-system-image-to-the-nilrt-system:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Deploy the latest Firmware and NILRT Base System Image to the NILRT system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the host system:

#.  Run HWCU. Connect to the NILRT system.

    #. Open the 'Edit' menu and select 'Add Hardware'.
    #. Add your hardware by discovery, hostname, or ipv4 address.

#.  Select your device in the drop-down menu.
#.  Update the device's Firmware (Safemode) image.

    #. In the 'Configuration' pane » Firmware management, click 'Update firmware...'.
    #. Select a firmware image versioned "25.3" or later.
    #. Click 'Update'.

#.  Format the device (erase existing Runmode).

    #. In the 'Configuration' pane » 'Advanced', click 'Format disk'.
    #. Click 'Format'.

#.  Install the latest NILRT Base System Image.

    #. In the 'Configuration' pane, click 'Manage software...'.
    #. When prompted, choose a Linux RT System Image versioned "2025 Q2" and click 'OK'.

#.  Set the ``admin`` account password. 

    #. When prompted enter a new administrator password.
    #. This password will be used by System Maintainers when the device is booted into Safemode, and is not related to the ``root`` user account you will configure later.

#.  Install software

    #. When prompted, select the programming environment and click 'Next'.
    #. When prompted to install software packages, de-select "NI-VISA" and click 'Review changes'.
    #. When prompted, click 'Continue'.


.. _using-ssh--log-in-to-the-nilrt-device-:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using SSH, log in to the NILRT device.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Use an SSH client of your choice to connect to the NILRT device's hostname.
#. Log in using the ``admin`` account and the password you previously configured. e.g. ``ssh://admin@$hostname``
#. All following steps are performed on the NILRT device, using the SSH shell.


.. _snac-configuration-file:

~~~~~~~~~~~~~~~~~~~~~~~~~
SNAC Configuration File
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``nilrt-snac`` tool reads its settings from ``/etc/snac/snac.conf``.
Edit this file as the ``admin`` user (``root`` if already in SNAC mode) to control which configuration 
modules are applied during ``configure`` and which checks are executed during ``verify``.

Modules
^^^^^^^

The configuration file contains a ``[modules]`` section where each module is configured individually using the form:

``<module_name> = enabled|disabled``

Behavior:

- ``enabled`` — the module will be processed by ``nilrt-snac configure`` and checked by ``nilrt-snac verify``.
- ``disabled`` — the module will be skipped by both commands.
- If the ``[modules]`` section is omitted or left empty, all modules are processed.
- Any module not explicitly set to ``disabled`` is treated as ``enabled`` by default.

Examples
^^^^^^^^

Enable common modules and disable GUI/Web Server:

.. code-block:: ini

    [modules]
    access-control = enabled
    audit          = enabled
    logging        = enabled
    sudo           = enabled
    ssh            = enabled
    gui            = disabled
    app-webserver  = disabled

Disable a single module and leave the rest at defaults (enabled):

.. code-block:: ini

    [modules]
    gui = disabled

After editing ``/etc/snac/snac.conf``, re-run the tool to apply or check the selected modules:

.. code-block:: bash

    nilrt-snac configure
    nilrt-snac verify

.. list-table:: Available SNAC Modules
   :header-rows: 1

   * - **Module Name**
     - **Description**
   * - ntp
     - NTP time synchronization
   * - opkg
     - OPKG package manager
   * - wireguard
     - WireGuard VPN
   * - cryptsetup
     - Disk encryption (cryptsetup)
   * - niauth
     - NIAuth authentication modules
   * - wifi
     - WiFi support
   * - faillock
     - PAM faillock for login security
   * - graphical
     - Graphical UI components
   * - console
     - Console access
   * - sysapi
     - NI SysAPI SSH CLI
   * - tmux
     - tmux session manager
   * - pwquality
     - Password quality enforcement
   * - ssh
     - SSH server settings
   * - sudo
     - Sudoers security
   * - firewall
     - System firewall
   * - auditd
     - Auditd system auditing
   * - syslog
     - syslog-ng logging
   * - usbguard
     - USBGuard device control (verification only)

.. _run-the-nilrt-snac-configuration-tool:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Run the nilrt-snac configuration tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#.  Install the configuration tool using opkg.

    .. code-block:: bash

        opkg install nilrt-snac

#.  Run the nilrt-snac tool.

    .. code-block:: bash

        nilrt-snac configure

    .. note::

        All output is logged to ``/var/log/snac/`` with the filename in the form of
        ``configure-<timestamp>.log`` or ``verify-<timestamp>.log``.

#.  Reboot the system. Note that after rebooting the system, serial
    console will be disabled. SSH is the preferred mechanism to continue
    administrating the system.

    .. code-block:: bash

        reboot

#.  Reconnect to the NILRT device in HWCU.

    #. Click 'Reconnect' or select your device in the drop-down menu.
    #. When prompted, login as ``root`` with no password.
    #. This confirms the host system is able to still communicate with the NILRT device.

#.  Login as ``root`` with no password. ``root`` is the new super-user account that replaces ``admin``.

#.  Change the ``root`` account password.

    .. code-block:: bash

        passwd root


.. _configure-privileged-operations-via-sudo:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configure Privileged Operations via Sudo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NILRT Base System Image includes the sudo utility: a service to
temporarily escalate user privileges. In the SNAC configuration, system
administrators should be given unprivileged user accounts and the
ability to execute privileged functions using sudo.

Add system administrators' user account is added to the group with
the ``usermod`` command.

    .. code-block:: bash

        usermod -a -G sudo $user

By default, a log of all sudo commands will be written
to ``/var/log/auth.log``.


.. _configure-remote-logging:

~~~~~~~~~~~~~~~~~~~~~~~~
Configure Remote Logging
~~~~~~~~~~~~~~~~~~~~~~~~

1.  On the remote server, configure the ``/etc/syslog-ng/syslog-ng.conf`` file. For example, the configuration file may look like this:

    .. code-block:: linuxconfig

        @version: 4.2
        @include "scl.conf"

        ########################
        # Sources
        ########################
        source s_net { tcp(); udp(ip(0.0.0.0) port(514)); };

        ########################
        # Destinations
        ########################
        # First some standard logfile
        #
        destination d_syslog { file("/var/log/remotelogs/syslog"); };

        ########################
        # Log paths
        ########################
        # All messages send to a remote site
        #
        log { source(s_net); destination(d_syslog); };

    Where any IP address is able to send logs to the remote server, and the logs will be stored in the ``/var/log/remotelogs/syslog`` file.

#.  On the target, configure the ``/etc/syslog-ng/syslog-ng.conf`` file.  For example, the configuration file may look like this: 

    .. code-block:: linuxconfig

        @version: 4.6

        source s_local {
            system();
            internal();
        };

        destination d_remote {
            syslog("<Remote IP Address>" transport("udp") port(514));
        };

        log {
            source(s_local);
            destination(d_remote);
        };

    Where the remote server's IP address is set as the destination for the target's system logs.

#.  Restart syslog-ng on both the target and remote server.

    .. code-block:: bash

        /etc/init.d/syslog restart

    For more information on configuring syslog-ng, refer to the `Syslog-ng Github <https://github.com/syslog-ng/syslog-ng>`_.



.. _optional-snac-configuration-instructions:

----------------------------------------
Optional SNAC Configuration Instructions
----------------------------------------

The following instructions outline additional configuration steps that may be performed at the discretion of the system maintainers. 
These steps are not mandatory but can enhance the functionality or performance of the NILRT system. 
System maintainers should evaluate their specific needs and decide whether to implement these configurations.

.. _non-runtime-partition-encryption:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Non-Runtime Partition Encryption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System maintainers should consider encrypting partitions on designs that store controlled data on 
removable devices or non-runtime partitions to protect sensitive information.

#.  Install the `cryptsetup` tool using `opkg`.

    .. code-block:: bash

        opkg install cryptsetup

#.  Create a non-runtime partition (if needed) using the following commmands:

    .. code-block:: bash

        dd if=/dev/zero of=/tmp/test_partition bs=1M count=32
        mkdir /mnt/test_partition

    Note: Replace `/tmp/test_partition` with the desired file path and size for your partition.

#.  Encrypt the partition.

    .. code-block:: bash

        cryptsetup luksFormat /tmp/test_partition

    Note: You will be prompted to enter a secure passphrase.

#.  Open the encrypted partition.

    .. code-block:: bash
    
        cryptsetup luksOpen /tmp/test_partition test_partition

#.  Format the encrypted partition.

    .. code-block:: bash
    
        mkfs.ext4 /dev/mapper/test_partition_crypt

#.  Mount the encrypted partition.

    .. code-block:: bash

        mount /dev/mapper/test_partition_crypt /mnt/test_partition

After mounting the encrypted partition, you can use it just like any other filesystem.
For additional encryption options or configurations using `cryptsetup`, refer to the `Cryptsetup Documentation <https://www.man7.org/linux/man-pages/man8/cryptsetup.8.html>`_.
Please be aware that root partition encryption is not supported.
