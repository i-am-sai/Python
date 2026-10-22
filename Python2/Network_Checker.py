
# 1. Network Checker: Conditionals
# 2. Network port scanner simulation: Loops
# 3. Network host manager: Lists_Tuples
# 4. Network Inventory Manager: dictionaries_sets


# 1. Network Checker: Conditionals

host = input("Enter hostname: ")
port = int(input("Enter port number: "))

is_valid_port = port >= 1 and port <= 65535
is_known_port = port == 22 or port == 80 or port == 443

if not is_valid_port:
    print("In Valid Port Number")
elif is_known_port and port == 22:
    print(f"Connecting to {host} on port {port} - SSH Connection")
elif is_known_port and port == 80:
    print(f"Connecting to {host} on port {port} - HTTP Connection")
elif is_known_port and port == 443:
    print(f"Connecting to {host} on port {port} - HTTPS Connection")
else:
    print(f"Connecting to {host} on port {port} - Custom port")



# --------------------------------

# 2. Network port scanner simulation: Loops
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
ports = [22, 80, 443, 8080]
max_attempts = 3

# Task 1: Scan all hosts and ports
print("=== Port Scan Started ===")
for host in hosts:
    for port in ports:
        print(f"Scanning {host} : {port}")

# Task 2: Retry logic with while loop
print("\n=== Connection Retry Logic ===")
attempts = 0
while True:
    attempts +=1
    print(f"Attempt {attempts} - trying to connect...")
    if attempts == max_attempts:
        print("Max attempts reached.")
        break

# Task 3 - print only even ports using continue
print("\n=== Even Ports Only ===")
for port in range(20, 450, 1):
    if port%2 != 0:
        continue
    if port > 100:
        break
    print(f"Even port: {port}")

# --------------------------------

# Lists_Tuples
# 3. Network host manager

# Your host inventory: Lists
hosts = ["192.168.1.1", "192.168.1.2", "10.0.0.1", "192.168.1.3", "172.16.0.1"]

# Fixed server config so Tuple
server_config = ("admin", 22, "production")
username, port, environment = server_config

print(f"=== {environment.upper()} Environment ====")
print(f"User: {username} | Port: {port}\n")

# Show all hosts with index
print("All hosts")
for index, host in enumerate(hosts):
    print(f" {index + 1}: {host}")

# Filter only 192.168 hosts using list comprehension
lan_hosts = [host for host in hosts if host.startswith("192.168")]
print(f"\nLAN Hosts Only: {lan_hosts}")

hosts.append("192.168.1.4")
print(f"\nAfter adding new host: {hosts}")

hosts.remove("172.16.0.1")
print(f"After removing 10.0.0.1: {hosts}")

priority_hosts = hosts[:3]
print(f"{priority_hosts}")

#Check if host exists before scanning
target = "172.16.0.1"
if target in hosts:
    print(f"\n{target} is in inventory - safe to scan")
else:
    print(f"\n{target} not found - skipping")

# --------------------------------
# 4. Network Inventory Manager: dictionaries_sets

inventory = {
    "192.168.1.1": {
        "hostname": "router-01",
        "ports": [20, 80, 443],
        "status": "online"
    },
    "192.168.1.2": {
        "hostname": "switch-01",
        "ports": [22, 161],
        "status": "offline"
    },
    "192.168.1.3": {
        "hostname": "server-01",
        "ports": [22, 443, 8080],
        "status": "online"
    }
}

#Print Full Inventory
print(" === NETWORK INVENTORY === ")
for ip, details in inventory.items():
    print(f"\nIP: {ip}")
    print(f" Hostname: {details['hostname']}")
    print(f" Status : {details['status']}")
    print(f" Ports : {details['ports']}")

# Filter only online hosts
print("\n=== Online Hosts ===")
online = {ip: d for ip, d in inventory.items() if d["status"] == "online"}
for ip, details in online.items():
    print(f"{details['hostname']} ({ip})")

# Collect all unique ports across all hosts using set
all_ports = [] #empty list
for details in inventory.values():
    all_ports.extend(details["ports"])

unique_ports = set(all_ports)
print(f"\n=== Unique Open Ports Across Network ===")
print(f"  {sorted(unique_ports)}")

inventory["10.0.0.1"] = {
    "hostname": "firewall-01",
    "ports": [22, 443],
    "status": "online"
}

print(f"\nAdded firewall-01. Total devices: {len(inventory)}")

# Safe lookup
target = "10.0.0.1"
result = inventory.get(target, "Not found in inventory")
print(f"\nLookup {target}: {result}")