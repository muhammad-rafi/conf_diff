[![license](https://img.shields.io/github/license/abatilo/actions-poetry.svg)](https://github.com/muhammad-rafi/conf_diff/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/conf_diff.svg)](https://pypi.org/project/conf-diff/) 
[![Build Status](https://github.com/muhammad-rafi/conf_diff/actions/workflows/main.yml/badge.svg)](https://github.com/muhammad-rafi/conf_diff/actions)

# Introduction

This module is built to provide you the configuration comparison between two configuration files and generates configuration differences either on the terminal or create a HTML output file based on the parameter provided to the module.

Note: This module is built on the top of the Python built-in difflib module but modified to show you the colourful output and customised HTML template.

## Features

* Shows the configuration differences on the terminal window with colourful output.
* Generate a HTML output file as a comparison report.

## Installation

Install this module from PyPI:

```sh

pip install conf-diff

```

## Usage:

### Prerequisite
As this module compares the configuration difference between two config file, so we need to have two configuration files should be present in the same directory where you are running the script from or specify the absolute path for the configuration files. e.g. `"/Users/rafi/sandbox-nxos-1.cisco.com_before_config.cfg"` and `"/Users/rafi/sandbox-nxos-1.cisco.com_after_config.cfg"`

You may use either .cfg or .txt file extensions.

In the below example, I am using two output files of 'show running-config ntp' from the Cisco NXOS always-on sandbox, assuming that, `sbx-nxos-mgmt.cisco.com_ntp_before.cfg` was taken before the change and `sbx-nxos-mgmt.cisco.com_ntp_after.cfg` after the change, and we want to see the configuration diffrence between them. You may name the filenames as you like or add the timestamp.

Import the `conf_diff` module in your python script and instantiate a class object with both config output files as arguments.

```python

import conf_diff

# Instantiate a class object 'config_change'
config_change = conf_diff.ConfDiff("sbx-nxos-mgmt.cisco.com_ntp_before.cfg", "sbx-nxos-mgmt.cisco.com_ntp_after.cfg")

# Display the output of the configuration difference on the terminal 
print(config_change.diff())

```

This will display the colourful configuration difference on the terminal. 

![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/cli_output.png)

To generate a html output file, add third argument as the expected output file name. e.g. `"sbx-nxos-mgmt.cisco.com_html_output.html"`

```python

 # Instantiate a class object 'html_diff'
html_diff = conf_diff.ConfDiff("sbx-nxos-mgmt.cisco.com_ntp_before.cfg", "sbx-nxos-mgmt.cisco.com_ntp_after.cfg", "sbx-nxos-mgmt.cisco.com_html_output.html")

# Generates a `sbx-nxos-mgmt.cisco.com_html_output.html` in your current directory unless expected absolute path is specified.
html_diff.diff()

```
This will generates a `sbx-nxos-mgmt.cisco.com_html_output.html` in your current directory unless expected absolute path is specified.

See the screenshot below for the `sbx-nxos-mgmt.cisco.com_html_output.html`

![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/html_output_file.png)

### Example
In this example, I am running a script with well known 'netmiko' library and taking a backup of running config before and after the change. Then compare the configuration difference between these config files. See the [example](https://github.com/muhammad-rafi/conf_diff/tree/main/examples) directory. 


```python

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

```

## Issues
Please raise an issue or pull request if you find something wrong with this module.

## Authors
[Muhammad Rafi](https://github.com/muhammad-rafi)

## License
The source code is released under the MIT License.
