from netmiko import ConnectHandler
import conf_diff
import time

# List of hosts or devices
hosts_list = ['sandbox-nxos-1.cisco.com']

# For loop to run through all the devices in the 'hosts_list'
for host in hosts_list:
    device = {
        "device_type": "cisco_nxos",
        "ip": host,
        "username": "admin",
        "password": "Admin_1234!",
        "port": "22",
    }

    # Creating a network connection with the device
    print(f"**** Connecting to {device['ip']} **** ...\n")
    net_connect = ConnectHandler(**device)

    # Sending 'show' command to the device to take first configuration snapshot before updating the device
    print(f"Connected to {device['ip']}, Sending commands ...\n")
    current_config = net_connect.send_command("show running-config")

    print(f"Saving pre-configuration change output for {device['ip']} ...\n")

    # Opening a file in write mode to save the configuration before the change
    with open(f"{device['ip']}_before_config.cfg", "w") as f:
        f.write(current_config)

    print(f"{device['ip']}_before_config.cfg has been saved ...\n")

    # List of configuration commands to the device
    print(f"Updating the configuration for {device['ip']}...\n")
    config_commands = ['interface Ethernet1/22-28',
                       'description testing python script',
                       'switchport mode trunk',
                       'switchport trunk allowed vlan 512,654,278'
                       ]

    # Sending above configuration commands to updathe the device configuration
    config_update = net_connect.send_config_set(config_commands)

    # Sleep for 2 sec before take another configuration snapshot
    time.sleep(2)

    # Sending 'show' command to the device again to take another configuration snapshot after the change
    print(f"Saving post-configuration change output for {device['ip']} ...\n")
    updated_config = net_connect.send_command("show running-config")

    # Opening a file in write mode to save the configuration after the change
    with open(f"{device['ip']}_after_config.cfg", "w") as f:
        f.write(updated_config)

    print(f"{device['ip']}_after_config.cfg has been saved ...\n")

    # Teardown the network connection with the device
    net_connect.disconnect()

    # To print the colourful output on the terminal
    config_diff = conf_diff.ConfDiff(f"{device['ip']}_before_config.cfg", f"{device['ip']}_after_config.cfg")
    print(config_diff.diff())

    # To generate a HTML output file
    html_diff = conf_diff.ConfDiff(f"{device['ip']}_before_config.cfg", f"{device['ip']}_after_config.cfg", "html_diff_output.html")
    html_diff.diff()
