
.. _appendix-2--connect-the-labview-host-and-nilrt-system-using-wireguard:

=====================================================================
Appendix 2: Connect the LabVIEW Host and NILRT System Using WireGuard
=====================================================================

If you wish to use LabVIEW to run applications on your NILRT system, you
will need to connect each LV host machine to the device's WireGuard
network. The WireGuard interface on the NILRT system has been partially
configured by the nilrt-snac configuration tool. Before proceeding,
ensure that WireGuard is installed on the Windows host; it may be
downloaded from https://www.wireguard.com/install/.

The commands in the following instructions make use of the following
pseudocode variables, which you should replace before entry.

.. raw:: latex

    \scalefont{0.66666666}


.. tabularcolumns:: \Y{0.27}\Y{0.25}\Y{0.3}\Y{0.18}

+---------------------------+----------------------+-------------------------------+---------------+
| Variable                  | Description          | To compute…                   |Sample Value   |
+===========================+======================+===============================+===============+
|``${windows_private_key}`` | Private              | Open WireGuard,               |               |
|                           | key of Windows host  | select **Add Tunnel»Create    | YJ0NxsWisQ…   |
|                           |                      | New Tunnel…**, and record     |               |
|                           |                      | the value of **PrivateKey**   |               |
+---------------------------+----------------------+-------------------------------+---------------+
| ``${windows_public_key}`` | Public key           | Record the value of "Public   |               |
|                           | of Windows host      | key" in the **Create new      | OF9sbmVqTs…   |
|                           |                      | tunnel** dialog above         |               |
+---------------------------+----------------------+-------------------------------+---------------+
|                           | IPv4 address of      | ``ipconfig``                  | 10.0.2.1      |
|``${windows_ipv4_address}``| Windows host through |                               |               |
|                           | which RT target is   |                               |               |
|                           | accessible           |                               |               |
+---------------------------+----------------------+-------------------------------+---------------+
| ``${device_private_key}`` | Private              | ``wg show wglv0 private-key`` |               |
|                           | key of RT target     |                               | SJvSIy5Epo…   |
+---------------------------+----------------------+-------------------------------+---------------+
| ``${device_public_key}``  | Public key           | ``wg show wglv0``             |               |
|                           | of RT target         |                               | wGleQMHB6b…   |
+---------------------------+----------------------+-------------------------------+---------------+
|``${device_ipv4_address}`` | IPv4 address of RT   | ``ip addr``                   | 10.0.2.2      |
|                           | target on local      |                               |               |
|                           | network              |                               |               |
+---------------------------+----------------------+-------------------------------+---------------+
| ``${windows_wg_address}`` | IPv6 address of      | Choose from IPv4 private      | 192.168.94.1  |
|                           | Windows host on      | network ranges, avoiding      |               |
|                           | VPN                  | networks in use               |               |
+---------------------------+----------------------+-------------------------------+---------------+
| ``${device_wg_address}``  | IPv6 address of RT   | Same                          | 192.168.94.2  |
|                           | target on            |                               |               |
|                           | VPN                  |                               |               |
+---------------------------+----------------------+-------------------------------+---------------+

.. raw:: latex

    \scalefont{1.5}

.. _key-setup:

^^^^^^^^^
Key setup
^^^^^^^^^

You must possess the public and private keys of both devices
(``${windows_private_key}``, ``${windows_public_key}``, ``${device_private_key}``,
and ``${device_public_key}``) before proceeding. To obtain
``${device_private_key}`` and ``${device_public_key}``, log into your NILRT
target and run

.. code-block:: bash

    wg show wglv0 # public key
    wg show wglv0 private-key # private key

To obtain ``${windows_private_key}`` and ``${windows_public_key}``, open the
WireGuard application and click **Add Tunnel»Add empty tunnel…**. The
public and private keys will be displayed. Keep this dialog open --- it
will be added to below.


.. _nilrt-target-instructions:

^^^^^^^^^^^^^^^^^^^^^^^^^
NILRT target instructions
^^^^^^^^^^^^^^^^^^^^^^^^^

#.  Log into the NILRT system over SSH. Add the windows host as a peer to
    your device:

    .. code-block:: bash

        wg set \
            wglv0 peer ${windows_public_key} \
            endpoint ${windows_ipv4_address}:51820 \
            allowed-ips ${windows_wg_address}/24

#.  Save your configuration to make it persist across reboots.

    .. code-block:: bash

        wg-quick save wglv0


.. _windows-host-instructions:

^^^^^^^^^^^^^^^^^^^^^^^^^
Windows host instructions
^^^^^^^^^^^^^^^^^^^^^^^^^

1.  In the **Create new tunnel** dialog, append additional lines after
    PrivateKey such that the configuration file consists of the
    following. Note that all key values in this configuration are
    case-sensitive.

    .. code-block:: ini

        [Interface]
        PrivateKey = ${windows_private_key}
        Address = ${windows_wg_address}/24
        ListenPort = 51820
        [Peer]
        PublicKey = ${device_public_key}
        AllowedIPs = ${device_wg_address}/24
        Endpoint = ${device_ipv4_address}:51820

    Give the tunnel an appropriate name (e.g. wglv0) and save the tunnel
    configuration.

#.  Add a firewall rule that permits incoming network traffic to the
    Wireguard tunnel listening port. This can be accomplished from a
    command line with Administrator permissions:

    .. code-block:: powershell

        netsh advfirewall `
            firewall add rule `
                name=nilrt-wireguard `
                dir=inaction=allow `
                protocol=ANY `
                localip=${device_wg_address}/24 `
                profile=any

#.  In the WireGuard application, click the **Activate** button on your
    tunnel's information panel.

Once the Windows-side WireGuard tunnel is activated, you should begin to see network traffic reported on the tunnel's status panel. Thereafter, you can connect to the device in LabVIEW using its Wireguard IP address (``${windows_wg_address}``, e.g. 172.16.1.1). Additional NILRT devices can be attached to the host by performing similar steps but changing each new device to a new address on the e.g. 172.16.1.0/24 address space.
