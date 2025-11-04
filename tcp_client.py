import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))
s.send(b"Hello from TCP Client")
data = s.recv(1024).decode()
print("Received from server:", data)
s.close()
