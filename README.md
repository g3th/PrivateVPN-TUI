# PrivateVPN-TUI

Text user interface for Linux terminal, created to make connecting to a server easier.

Just pick a country, then a city and it will automatically connect, as long as PrivateVPN has been configured properly.

## Scrapes countries and cities directly from "https://privatevpn.com/serverlist"

--------------------------------------------------------------------------------------------------------------------------

### Requirements

Requires OpenVPN, i.e:

``` apt-get install openvpn ```

Requires Private VPN to be configured for a linux installation as root .i.e:

``` sudo -i ```

``` cd /home/user/Desktop/PrivateVPN ```

``` wget "https://privatevpn.com/client/install.sh" ```

``` ./install.sh ```

and edit path to your PrivateVPN folder.

--------------------------------------------------------------------------------------------------------------------------

Fixed:

01/06/22
fixed the (p) option in menu by adding a flag and nesting loop
fixed README requirements


