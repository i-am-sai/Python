import socket

# This is exactly what happens under the hood
# when you connect to any server

sock = socket.socket()
sock.connect(("192.168.1.1", 22))    # IP + Port together
# OS automatically assigns ephemeral port on your side