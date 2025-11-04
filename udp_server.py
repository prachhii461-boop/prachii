import socket

u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
u.bind(('localhost', 12346))
print("UDP Server running...")
data, addr = u.recvfrom(1024)
print("Received:", data.decode())
u.sendto(b"Hello from UDP Server", addr)
u.close()
