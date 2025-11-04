import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))
s.listen(1)
print("TCP Server running...")
conn, addr = s.accept()
print("Connected by", addr)
data = conn.recv(1024).decode()
print("Received:", data)
conn.send(b"Hello from TCP Server")
conn.close()
