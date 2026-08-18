# TCP connection — explicit, reliable
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM = TCP
sock.connect(("192.168.1.1", 22))    # 3-way handshake happens here

# UDP connection — fire and forget
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # SOCK_DGRAM = UDP
sock.sendto(data, ("8.8.8.8", 53))  # DNS query — no handshake