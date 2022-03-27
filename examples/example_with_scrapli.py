from scrapli.driver.core import NXOSDriver
import conf_diff
import time

device = {
    "host": "sbx-nxos-mgmt.cisco.com",
    "auth_username": "admin",
    "auth_password": "Admin_1234!",
    "auth_strict_key": False
}

# # Scrapli connection via open() menthod
# cli = NXOSDriver(**device)
# cli.open()

# cli_cmd = cli.send_command("show running-config")
# runnig_config = cli_cmd.result

# Scrapli connection via "with open" menthod
with NXOSDriver(**device) as conn:
    response = conn.send_command("show running-config ntp")
    runnig_config = response.result

with open(f"{device['host']}_ntp_before.cfg", "w") as f:
    f.write(runnig_config)


with NXOSDriver(**device) as conn:
    conn.send_configs(["ntp server 10.10.10.1 use-vrf default key 123",
                       "ntp server 10.10.10.2 use-vrf default key 456",
                       "ntp server 10.10.10.3 use-vrf default key 789",
                       "ntp server 192.0.2.1 use-vrf default",
                       "ntp server 192.0.2.2 use-vrf default"
                       ])

time.sleep(5)

with NXOSDriver(**device) as conn:
    response = conn.send_command("show running-config ntp")
    updated_config = response.result

with open(f"{device['host']}_ntp_after.cfg", "w") as f:
    f.write(updated_config)

cli_diff = conf_diff.ConfDiff(f"{device['host']}_ntp_before.cfg", f"{device['host']}_ntp_after.cfg")
html_diff = conf_diff.ConfDiff(f"{device['host']}_ntp_before.cfg", f"{device['host']}_ntp_after.cfg", f"{device['host']}_html_output.html")

# print output on the terminal
print(cli_diff.diff())

# Generate html output file
html_diff.diff()
