import socket

u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
u.sendto(b"Hello from UDP Client", ('localhost', 12346))
data, addr = u.recvfrom(1024)
print("Received from server:", data.decode())
u.close()
