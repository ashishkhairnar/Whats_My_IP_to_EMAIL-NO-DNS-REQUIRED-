Send your current home IP to your EMAIL (**NO Dynamic DNS or Business ISP Plan need**)

Simply spin your Raspberry-Pi for this.

Script sends email if there is change in IP. You can run script using Cron job every hour or 4 hours (as most of DHCP leases are for 8 hours)

**Cron:**

0 1 * * * /usr/bin/python /home/whats_my_ip_script.py
