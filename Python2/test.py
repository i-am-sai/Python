
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

# Difference — ports only on server B, not A
print(server_b_ports - server_a_ports)