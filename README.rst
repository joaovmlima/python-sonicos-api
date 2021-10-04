============
SonicOS API
============

************
About
************
This library provides functions to communicate with SonicWall's Firewall API, without the need to build the requests by hand.

It is built on firmware 6.5.4, compatibility with 7.0.0 should be fine but its yet to be tested.

| Currently only the HTTP Basic login method is supported.
| If you use HTTPS, it is secure enough ;)

See it on GitHub `here <https://github.com/joaovmlima/python-sonicos-api>`_.

*******
Usage
*******
| Install with:
| ``pip install sonicos-api`` or ``poetry add sonicos-api``

| Import with:
| ``from sonicos_api import sonicOS as snwl``

***********
Examples
***********
| ``snwl.fwLogin("https://192.168.1.1:3443", "admin", "password", False)``
| Logs into the firewall for executing the other functions.

| ``snwl.getCFSLists("192.168.1.1", False)``
| Returns all the Content Filter lists configured in the firewall at 192.168.1.1

******************
Supported Actions
******************
| Currently, this lib is focused on the CFS feature of the firewall, so there's a very limited number of functions to other features.
| I'm hoping to implement it along the way, feel free to help :)