ReadME

This is a simple DNS project.
The client requests the IP address from a host name from the RS server, and returns the ip address.
If RS server fails to find the IP address it returns to the client the TS server instead.
The client then sends the requested host name to the TS server. The TS server returns the ip address or returns "ERROR: Host not found" if the hostname is not found.

Instructions to run the servers and client:
Run using python 3.

Must run RSserver.py first, then run TSserver.py.
Change the host name of the NS flag in PROJIDNSRS.txt to whatever host TSserver.py is running on.
Change the name of the host of the Client.py to the name of the host of where RSserver.py is running on.
