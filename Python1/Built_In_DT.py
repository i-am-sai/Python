#Imagine you're a network engineer. You have 10 servers to monitor. In Java you'd create an array with fixed size. 
# In Python — you use a List. Dynamic, flexible, powerful.

#Simple List
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Mixed Types: Python allows this and Java doesn't in arrays
infor = ["Server1", 8080, True, 3.5]

# Empty List - You'll add to it later
scan_results = []

print(hosts[2])  # indexing : 2 and -1 give same element from list
print(hosts[-1]) # last item (negative indexing, Java doesn't have this)
print(hosts[-2])    # "192.168.1.2" — second from last

# Slicing : [start:stop:step]
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
print(hosts[1:3])
print(hosts[0:2])
print(hosts[:3])
print(hosts[::2])

# Modify the lists
# Functions: append, insert, remove, pop, sort, reverse, len, in, enumerate  
hosts.append("192.168.1.6")
print(hosts)

#Add at specific position
hosts.insert(1, "10.0.0.1")
print(hosts)

# Remove by value
hosts.remove("10.0.0.1")
#hosts.remove(hosts[1])
print(hosts)

removed = hosts.pop(0)
print(removed)
print(hosts)

# Sort
hosts.sort()

# Reverse
hosts.reverse()

# Length
print(len(hosts))

print("10.0.0.1" in hosts)

# Looping over lists
for host in hosts:
    print(f"Scanning {host}")

#enumerate: Gives you both index and value simultaneously
for index, host in enumerate(hosts):
    print(f"Host {index +1}: {host}")

    # List  Comprehension
hosts = ["192.168.1.1", "10.0.0.1", "192.168.1.2", "172.16.0.1"]
filtered = [host for host in hosts if host.startswith("192")]
print(filtered)
# One line. Read it like English — "give me each host, for each host in hosts, if it starts with 192."


# Tuples
db_config = ("localhost", 5432, "postgres", "admin")
# config.append("additional")  # ERROR — tuples don't allow this
host, port, dbname, user = db_config #tuple unpacking: assigning multiple variables from a tuple in one line. Very clean, very Pythonic.
print(f"Connecting to {dbname} at {host}:{port} as {user}")


# Dictionaries and Sets
host_status = {
    "192.168.1.1": "Online",
    "192.168.1.2": "Offline",
    "192.168.1.3": "Online"
}

scan_results = {} # empty dictionary

# Direct access
print(host_status["192.168.1.2"])

print(host_status.get("192.168.1.1"))
print(host_status.get("192.168.1.9"))           # None — no crash

print(host_status.get("192.168.1.9", "unknown")) # "unknown" — default value

#Adding Updating Deleting:
scan_results["192.168.1.1"] = "online"
scan_results["192.168.1.1"] = "offline"

# Update existing
scan_results["192.168.1.2"] = "online"    # overwrites offline

# Delete a key
del scan_results["192.168.1.2"]

# Check if key exists
if "192.168.1.2" in scan_results:
    print("Host found in results")

# Nested Dictionary — Real World Structure
# This is where dictionaries get powerful. Values can themselve be dictionaries

network_inventory = {
   "192.168.1.1": {
       "hostname": "router_01",
       "ports": [22, 80, 443],
       "status": "online"
   },
   "192.168.1.2": {
       "hostname": "switch-01",
       "ports": [22, 161],
       "status": "offline"
   }
}

#accessing nested values
print(network_inventory["192.168.1.1"]["hostname"])
print(network_inventory["192.168.1.2"]["ports"])
print(network_inventory["192.168.1.1"]["status"])

# Loops over Dict
for host in host_status:
    print(host)

# Loop over value only
for status in host_status.values():
    print(status)

# Loop over both — most useful
for host, status in host_status.items():
    print(f"{host} is {status}")

# Useful Dict Methods
print(host_status.keys())  # all keys
print(host_status.values())    # all values
print(len(host_status))   # number of entries — 3

#Count how many are online
online_count = list(host_status.values()).count("Online")
print(f"Online hosts: {online_count}")

# Dictionary Comprehension — Same Concept as List Comprehension
online_host = {
    host: status for host, 
    status in host_status.items() if status == "Online"
    }
print(online_host)

# Sets: Duplicates are automatically removed
ports_scanned = {22, 80, 443, 22, 80, 22}
print(ports_scanned)

#Set Operations: Powerful for Network Analysis
server_a_ports = {22, 80, 443, 8080}
server_b_ports = {22, 443, 3306, 5432}

# Union — all ports across both servers
print(server_a_ports | server_b_ports)

# Intersection — ports open on BOTH servers
print(server_a_ports & server_b_ports)

# Difference — ports only on server A, not B
print(server_a_ports - server_b_ports)
print(server_b_ports - server_a_ports)