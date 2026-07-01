#Loops
#1. While Loop
i = 0
while i<=5:
    print(i)
    i +=1     #i++ does not exist in python, use i += 1

#2. For loop
for i in range(5): # range function generates the sequence and no counter or no increment
    print(i)

#range(start, stop, step) 
range(5)        # 0, 1, 2, 3, 4         — start defaults to 0
range(1, 6)     # 1, 2, 3, 4, 5         — start=1, stop=6 (stop is excluded)
range(0, 10, 2) # 0, 2, 4, 6, 8         — start=0, stop=10, step=2
range(10, 0, -1)# 10, 9, 8, ... 1       — counting backwards

hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for host in hosts:
    print(f"Pinging {host}")

# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(10):
    if i == 6:
        continue
    print(i)

# Loops for Real Automation Script while loop
attempts = 0

while True:  # infinte loop intentionally
    attempts +=1
    print(f"Attempting connection... try {attempts}")

    if attempts == 3:
        print("Max attempts reached. Stopping.")
        break # exits the infinite loop

# Loops for Real Automation Script: For loop

for attempt in range(3):
    print(f"Trying attempt {attempt + 1}")
    if attempt == 10:
        print("Connected")
        break
else:
    print("All attemps failed")  # only runs if break never happened

servers = ["server1", "server2", "server3"]
ports = [22, 80]

for server in servers:
    for port in ports:
        print(f"Checking {server} on port {port}")
